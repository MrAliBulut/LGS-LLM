import os
import json
import asyncio
import random
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from question_generator import generate_question_for_unit

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def generate_image_from_prompt(image_prompt: str) -> str:
    """
    Generate an image from a text prompt using the image generation system.
    
    Args:
        image_prompt: Text description of the image to generate
        
    Returns:
        URL of the generated image (or placeholder)
        
    Future: This function will integrate with the image generation API
    """
    print(f"[IMAGE GENERATION] Processing prompt: {image_prompt[:100]}...")
    
    # TODO: Integrate with image generation API here
    # For now, return placeholder URL
    # In the future, this will return the actual generated image URL
    placeholder_url = "/placeholder.svg"
    
    print(f"[IMAGE GENERATION] Returning placeholder: {placeholder_url}")
    return placeholder_url


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": "LGS Exam Generator"}


@app.post("/generate-exam")
async def generate_exam_with_llm(request: Request):
    """Generate exam questions using LLM based on distribution"""
    try:
        body = await request.json()
        distribution = body.get("distribution", {})
        visual_count = body.get("visualCount", 0)
        
        print(f"[DEBUG] Received distribution: {distribution}")
        print(f"[DEBUG] Visual count: {visual_count}")
        
        # Randomly distribute visual questions across topics
        visual_distribution = {}
        remaining_visual = visual_count
        topics_list = list(distribution.keys())
        
        if visual_count > 0 and topics_list:
            # Randomly assign visual questions to topics
            for topic in topics_list:
                if remaining_visual <= 0:
                    break
                max_visual_for_topic = distribution[topic]
                visual_for_topic = random.randint(0, min(max_visual_for_topic, remaining_visual))
                if visual_for_topic > 0:
                    visual_distribution[topic] = visual_for_topic
                    remaining_visual -= visual_for_topic
            
            print(f"[DEBUG] Visual distribution: {visual_distribution}")
        
        # For each topic, randomly select which questions should be visual
        visual_indices = {}
        for topic, visual_count_for_topic in visual_distribution.items():
            topic_count = distribution[topic]
            all_indices = list(range(topic_count))
            visual_indices[topic] = set(random.sample(all_indices, min(visual_count_for_topic, topic_count)))
        
        print(f"[DEBUG] Visual indices per topic: {visual_indices}")
        
        async def question_stream():
            encoder = json.JSONEncoder()
            question_index = 1
            total_questions = sum(distribution.values())
            
            print(f"[DEBUG] Starting to generate {total_questions} questions via LLM")
            
            # Generate questions for each topic in distribution
            for topic, count in distribution.items():
                if count <= 0:
                    continue
                
                print(f"[DEBUG] Generating {count} question(s) for topic: {topic}")
                
                # Generate 'count' questions for this topic
                for q_num in range(count):
                    try:
                        # Check if this question should be visual
                        is_visual = q_num in visual_indices.get(topic, set())
                        
                        # Call the LLM generator for this topic
                        generated_question = await generate_question_for_unit(topic, visual=is_visual)
                        
                        if not generated_question:
                            print(f"[WARNING] Failed to generate question {q_num + 1} for {topic}")
                            continue
                        
                        # Print image prompt if this is a visual question
                        if is_visual:
                            image_prompt = generated_question.get('image_prompt', 'N/A')
                            print(f"[DEBUG] Image prompt for q{question_index}: {image_prompt}")
                            
                            # Generate image from prompt (currently returns placeholder)
                            image_url = await generate_image_from_prompt(image_prompt)
                            generated_question["imageUrl"] = image_url
                        else:
                            generated_question["imageUrl"] = None
                        
                        # Add metadata for frontend
                        generated_question["id"] = f"q{question_index}"
                        generated_question["topic"] = topic
                        generated_question["hasImage"] = is_visual
                        question_index += 1
                        
                        print(f"[DEBUG] Sending generated question {generated_question['id']} ({q_num + 1}/{count}) for topic: {topic}" + (" [VISUAL]" if is_visual else ""))
                        yield encoder.encode(generated_question) + "\n"
                        
                        # Add small delay between questions
                        await asyncio.sleep(0.5)
                    
                    except Exception as e:
                        print(f"[ERROR] Failed to generate question {q_num + 1} for {topic}: {e}")
                        import traceback
                        traceback.print_exc()
                        continue
            
            print(f"[DEBUG] Finished generating all {question_index - 1} questions")
        
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
