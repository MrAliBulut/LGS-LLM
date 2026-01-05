import json
import prompts
import asyncio
import random
import os
from groq import Groq
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Groq API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in .env file.")

client = Groq(api_key=GROQ_API_KEY)

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://cluster0.mongodb.net/")
DB_NAME = "lgs_database"
COLLECTION_NAME = "english_questions"

mongo_client = AsyncIOMotorClient(MONGO_URI)
db = mongo_client[DB_NAME]
collection = db[COLLECTION_NAME]

# Cache for all questions grouped by topic
_questions_cache = None


def load_vocab(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # readlines() gets each line, strip() removes spaces/newlines
        words = [line.strip() for line in f if line.strip()]
    return ", ".join(words)

def load_schema(file_path):
    with open(file_path, "r") as f:
        schema_data = json.load(f)
    return schema_data


async def fetch_all_questions_from_db():
    """Fetch ALL questions from MongoDB collection"""
    try:
        # Fetch all questions
        cursor = collection.find({})
        all_questions = []
        
        async for doc in cursor:
            # Format the question
            raw_options = doc.get("options") or doc.get("choices") or []
            
            # Format options
            if isinstance(raw_options, dict):
                options = {k: v for k, v in raw_options.items()}
            else:
                options = raw_options
            
            question = {
                "question_text": doc.get("question_text", doc.get("text", "")),
                "options": options,
                "correct_option": doc.get("correct_option", "A"),
                "topic": doc.get("topic", "General")
            }
            all_questions.append(question)
        
        print(f"[DEBUG] RESULT: Fetched {len(all_questions)} questions from DB")
        return all_questions

    except Exception as e:
        print(f"[ERROR] Failed to fetch questions: {e}")
        return []


def group_questions_by_topic(questions):
    """Group questions by topic into separate lists"""
    grouped = {}
    for question in questions:
        topic = question["topic"]
        if topic not in grouped:
            grouped[topic] = []
        grouped[topic].append(question)
    
    print(f"[DEBUG] RESULT: Grouped {len(grouped)} topics")
    
    return grouped


async def get_grouped_questions():
    """Get or fetch grouped questions (with caching)"""
    global _questions_cache
    
    if _questions_cache is None:
        all_questions = await fetch_all_questions_from_db()
        _questions_cache = group_questions_by_topic(all_questions)
    
    return _questions_cache


async def load_examples_from_db(topic):
    """Get ALL example questions for a topic from the grouped cache"""
    try:
        grouped = await get_grouped_questions()
        
        if topic not in grouped:
            print(f"[WARNING] No questions found for topic '{topic}'")
            return []
        
        examples = grouped[topic]
        print(f"[DEBUG] RESULT: Loaded {len(examples)} examples for '{topic}'")
        return examples
    
    except Exception as e:
        print(f"[ERROR] Failed to load examples for topic '{topic}': {e}")
        return []


async def generate_unit_data(unit):
    """Generate unit data with vocab and examples from database"""
    unit_data = {
        "unit_name": unit,
        "glossary": [load_vocab(f"vocab/{unit}_vocab.txt")],
        "examples": await load_examples_from_db(unit)
    }
    return unit_data


async def generate_question_for_unit(unit, visual=False):
    """Generate a question for the given unit using LLM"""
    unit_data = await generate_unit_data(unit)
     
    if visual:
        injection_prompt = prompts.VISUAL_QUESTION_TEMPLATE.format(**unit_data)
    else:
        injection_prompt = prompts.TEXT_QUESTION_TEMPLATE.format(**unit_data)

    response = client.chat.completions.create(
         model="llama-3.3-70b-versatile",
         messages=[
             {"role": "system", "content": prompts.MASTER_SCHEMA},
             {"role": "user", "content": injection_prompt}
         ],
         response_format={"type": "json_object"}
    )   
    
    # Parse the JSON response from LLM
    try:
        generated_question = json.loads(response.choices[0].message.content)
        return generated_question
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to parse LLM response as JSON: {e}")
        print(f"Raw response: {response.choices[0].message.content}")
        return None


# Main execution
if __name__ == "__main__":
    result = asyncio.run(generate_question_for_unit("In The Kitchen", visual=False))
    print(result)