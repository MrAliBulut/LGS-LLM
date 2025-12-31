import os
import json
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Connection String
# Replace with your actual username and password or set environment variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://burak:Burak123.@cluster0.xue2b.mongodb.net/")
DB_NAME = "lgs_database"
COLLECTION_NAME = "english_questions"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

async def fetch_all_questions_from_db():
    """Fetch ALL questions from MongoDB collection"""
    try:
        # Fetch all questions
        cursor = collection.find({})
        all_questions = []
        
        async for doc in cursor:
            # Map MongoDB document to the schema expected by the UI
            raw_options = doc.get("options") or doc.get("choices") or []
            
            # If options are flattened like optionA, optionB, etc.
            if not raw_options and "optionA" in doc:
                raw_options = [doc.get("optionA"), doc.get("optionB"), doc.get("optionC"), doc.get("optionD")]
                
            question = {
                "id": str(doc.get("_id")),
                "year": doc.get("year"),
                "question_number": doc.get("question_number"),
                "topic": doc.get("topic", "Genel"),
                "question": doc.get("question_text", doc.get("text", doc.get("question", ""))),
                "options": format_options(raw_options),
                "correctAnswer": doc.get("correct_option", "A"),
                "source": doc.get("source", "Unknown"),
                "created_at": str(doc.get("created_at", "Unknown"))
            }
            all_questions.append(question)
        
        print(f"[DEBUG] Total questions fetched from database: {len(all_questions)}")
        return all_questions

    except Exception as e:
        print(f"[ERROR] Failed to fetch questions: {e}")
        import traceback
        traceback.print_exc()
        return []


def group_questions_by_topic(questions):
    """Group questions by topic into separate lists"""
    grouped = {}
    for question in questions:
        topic = question["topic"]
        if topic not in grouped:
            grouped[topic] = []
        grouped[topic].append(question)
    
    print(f"[DEBUG] Grouped questions by topic:")
    for topic, q_list in sorted(grouped.items()):
        print(f"  - {topic}: {len(q_list)} questions")
    
    return grouped


def select_questions_for_distribution(grouped_questions, distribution):
    """
    Select questions from topic groups based on distribution requirements.
    Returns a list of tuples (topic, questions_list) in order.
    """
    selected = []
    
    for topic, count in distribution.items():
        if count <= 0:
            continue
        
        # Topic name should match database exactly (no mapping needed)
        if topic not in grouped_questions:
            continue
        
        available_questions = grouped_questions[topic]
        
        if len(available_questions) < count:
            selected_qs = available_questions
        else:
            # Randomly select 'count' questions from the topic
            import random
            selected_qs = random.sample(available_questions, count)
        
        selected.append((topic, selected_qs))
    
    return selected


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": "LGS Exam Generator"}


@app.post("/generate-exam")
async def fetch_questions_stream(request: Request):
    """Stream questions to frontend based on distribution"""
    try:
        body = await request.json()
        distribution = body.get("distribution", {})
        visual_count = body.get("visualCount", 0)
        
        print(f"[DEBUG] Received distribution: {distribution}")
        
        # Fetch all questions once
        all_questions = await fetch_all_questions_from_db()
        if not all_questions:
            print("[ERROR] No questions available in database!")
            return {"error": "No questions available"}
        
        # Group by topic
        grouped = group_questions_by_topic(all_questions)
        
        # Select questions for distribution
        selected = select_questions_for_distribution(grouped, distribution)
        
        print(f"[DEBUG] Selected questions for distribution:")
        for topic, topic_questions in selected:
            print(f"  - {topic}: {len(topic_questions)} questions")
        
        total_selected = sum(len(q_list) for _, q_list in selected)
        print(f"[DEBUG] Total questions selected: {total_selected}")
        
        async def question_stream():
            encoder = json.JSONEncoder()
            question_index = 1
            visual_questions_assigned = 0
            total_to_send = sum(len(q_list) for _, q_list in selected)
            
            print(f"[DEBUG] Starting to stream {total_to_send} questions to frontend")
            
            # Stream selected questions in order
            for topic, topic_questions in selected:
                for question in topic_questions:
                    # Add visual flag
                    has_image = visual_questions_assigned < visual_count
                    if has_image:
                        visual_questions_assigned += 1
                        question["hasImage"] = True
                        question["imageUrl"] = f"/placeholder.svg?query={topic}"
                    else:
                        question["hasImage"] = False
                        question["imageUrl"] = None
                    
                    # Add ID for ordering (q1, q2, q3, etc.)
                    question["id"] = f"q{question_index}"
                    question_index += 1
                    
                    print(f"[DEBUG] Sending question {question['id']} for topic: {topic}")
                    yield encoder.encode(question) + "\n"
                    
                    # Add delay for visual questions
                    if has_image:
                        await asyncio.sleep(2)
                    else:
                        await asyncio.sleep(0.5)
            
            print(f"[DEBUG] Finished streaming all {total_to_send} questions")
        
        return StreamingResponse(question_stream(), media_type="application/x-ndjson")
    
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
        return {"error": str(e)}

def format_options(options):
    # Helper to ensure options are in ["A) Text", "B) Text"] format
    formatted = []
    
    # Handle dictionary format {"a": "...", "b": "..."}
    if isinstance(options, dict):
        for key in ['a', 'b', 'c', 'd']:
            val = options.get(key) or options.get(key.upper())
            if val:
                formatted.append(f"{key.upper()}) {val}")
        return formatted

    if isinstance(options, list):
        for i, opt in enumerate(options):
            if isinstance(opt, str):
                prefix = f"{chr(65+i)}) "
                if not opt.startswith(prefix):
                    formatted.append(f"{prefix}{opt}")
                else:
                    formatted.append(opt)
            elif isinstance(opt, dict):
                # Handle case where options are objects {label: "A", text: "..."}
                label = opt.get("label", chr(65+i))
                text = opt.get("text", "")
                formatted.append(f"{label}) {text}")
    return formatted

if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server...")
    print(f"Server running at http://localhost:8000")
    print(f"API Documentation: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
