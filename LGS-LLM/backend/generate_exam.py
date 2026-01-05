import os
import json
import asyncio
import random
import base64
import copy
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from question_generator import generate_question_for_unit
from image_generation.generate_image import generate_image_chroma, generate_image_zimage
from session_logger import create_session, get_session, close_session
from image_generation.image_prompts import ChromaPromptEngine, ZimagePromptEngine

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


async def generate_image_from_prompt(
    image_prompt: str,
    unit: str,
    model_type: str = None,
    question_id: str = None,
    **model_kwargs
) -> str:
    """
    Generate an image for an exam question using the specified image generation model.
    
    Args:
        image_prompt: Raw image description from LLM (2-4 sentences)
        unit: The exam unit/topic (e.g., "Friendship", "Teen Life", "Adventures")
        model_type: Type of image generation model ("chroma" or "zimage").
                    If None, uses IMAGE_GENERATION_MODEL from environment.
        question_id: Question ID for logging
        **model_kwargs: Additional model-specific parameters
                       For chroma: seed, steps, guidance_scale
                       For zimage: width, height, seed, steps, guidance_scale
        
    Returns:
        Base64 data URI of the generated image, or placeholder URL as fallback
    """
    # Use environment variable if model_type not provided
    if model_type is None:
        model_type = os.getenv("IMAGE_GENERATION_MODEL", "chroma")
    
    print(f"[DEBUG IG] INIT: generate_image_from_prompt(unit={unit}, model={model_type})")
    
    try:
        img_bytes = None
        engineered_prompt = {}
        
        if model_type.lower() == "chroma":
            # Extract chroma-specific parameters
            seed = model_kwargs.get("seed", 42)
            steps = model_kwargs.get("steps", 40)
            guidance_scale = model_kwargs.get("guidance_scale", 3.0)
            
            # Generate engineered prompts for logging
            prompts = ChromaPromptEngine.generate_prompts(unit, image_prompt)
            engineered_prompt = {
                "positive_prompt": prompts['positive_prompt'],
                "negative_prompt": prompts['negative_prompt']
            }
            
            img_bytes = generate_image_chroma(
                unit=unit,
                image_prompt=image_prompt,
                seed=seed,
                steps=steps,
                guidance_scale=guidance_scale
            )
        
        elif model_type.lower() == "zimage":
            # Extract zimage-specific parameters
            width = model_kwargs.get("width", 1024)
            height = model_kwargs.get("height", 1024)
            seed = model_kwargs.get("seed", 42)
            steps = model_kwargs.get("steps", 9)
            guidance_scale = model_kwargs.get("guidance_scale", 0.0)
            
            # Generate engineered prompt for logging
            final_prompt = ZimagePromptEngine.generate(unit, image_prompt)
            engineered_prompt = {"final_prompt": final_prompt}
            
            img_bytes = generate_image_zimage(
                unit=unit,
                image_prompt=image_prompt,
                width=width,
                height=height,
                seed=seed,
                steps=steps,
                guidance_scale=guidance_scale
            )
        
        else:
            raise ValueError(f"Unknown model type: {model_type}. Supported types: 'chroma', 'zimage'")
        
        if img_bytes is None:
            raise RuntimeError(f"Image generation returned no bytes from {model_type}")
        
        # Convert to base64 data URI
        img_b64 = base64.b64encode(img_bytes).decode('utf-8')
        data_uri = f"data:image/png;base64,{img_b64}"
        
        # Log image generation if session logger exists
        session = get_session()
        if session and question_id:
            session.log_image_generation(
                question_id=question_id,
                model_type=model_type,
                llm_image_prompt=image_prompt,
                engineered_prompt=engineered_prompt,
                image_size_bytes=len(img_bytes)
            )
        
        print(f"[DEBUG IG] RESULT: Image generated ({len(img_bytes)} bytes)")
        return data_uri
    
    except Exception as e:
        # Fallback to placeholder on error
        error_msg = f"{type(e).__name__}: {e}"
        print(f"[ERROR] Image generation failed: {error_msg}")
        import traceback
        traceback.print_exc()
        
        # Log error to session
        session = get_session()
        if session and question_id:
            session.log_error("image_generation", type(e).__name__, str(e), {"question_id": question_id, "unit": unit})
        
        placeholder_url = "/placeholder.svg"
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
        
        print(f"[DEBUG] INIT: /generate-exam (topics={len(distribution)}, visual={visual_count})")
        
        # Create session logger with timestamp-based file
        session = create_session(distribution, visual_count)
        
        # Randomly distribute visual questions across topics
        visual_distribution = {}
        remaining_visual = visual_count
        topics_list = list(distribution.keys())
        
        if visual_count > 0 and topics_list:
            # Create a pool of topics that can accommodate visual questions
            # Shuffle to randomize assignment
            topics_pool = []
            for topic in topics_list:
                max_visual = distribution[topic]
                # Add topic to pool for each question slot it can accommodate
                topics_pool.extend([topic] * max_visual)
            
            # Shuffle the pool
            random.shuffle(topics_pool)
            
            # Assign visual questions from the shuffled pool
            for i in range(min(visual_count, len(topics_pool))):
                topic = topics_pool[i]
                visual_distribution[topic] = visual_distribution.get(topic, 0) + 1
            
            # If we couldn't distribute all visual questions (not enough slots), 
            # log a warning
            if visual_count > len(topics_pool):
                warning_msg = f"Requested {visual_count} visual but only {len(topics_pool)} slots available"
                print(f"[WARNING] {warning_msg}")
                session.log_error("visual_distribution", "InsufficientSlots", warning_msg)
        
        # For each topic, randomly select which questions should be visual
        visual_indices = {}
        for topic, visual_count_for_topic in visual_distribution.items():
            topic_count = distribution[topic]
            all_indices = list(range(topic_count))
            visual_indices[topic] = set(random.sample(all_indices, min(visual_count_for_topic, topic_count)))
        
        # Log distribution logic
        session.log_distribution_logic(visual_distribution, visual_indices)
        
        async def question_stream():
            encoder = json.JSONEncoder()
            question_index = 1
            total_questions = sum(distribution.values())
            questions_sent = 0
            images_generated = 0
            
            # Build a list of all questions to generate
            # Format: [(topic, q_num, is_visual), ...]
            all_questions = []
            for topic, count in distribution.items():
                if count <= 0:
                    continue
                for q_num in range(count):
                    is_visual = q_num in visual_indices.get(topic, set())
                    all_questions.append((topic, q_num, is_visual))
            
            # PRIORITIZE: Sort so text questions come first, visual questions last
            # This ensures text questions are generated and streamed before visual ones
            all_questions.sort(key=lambda x: x[2])  # False (text) = 0, True (visual) = 1
            
            print(f"[DEBUG] Generation order: {sum(1 for q in all_questions if not q[2])} text first, then {sum(1 for q in all_questions if q[2])} visual")
            
            # Generate questions in prioritized order
            for topic, q_num, is_visual in all_questions:
                try:
                    q_id = f"q{question_index}"
                    
                    # Call the LLM generator for this topic
                    generated_question = await generate_question_for_unit(topic, visual=is_visual)
                    
                    if not generated_question:
                        error_msg = f"Failed to generate question {q_num + 1} for {topic}"
                        print(f"[WARNING] {error_msg}")
                        session.log_error("question_generation", "GenerationFailed", error_msg, {"topic": topic, "q_num": q_num})
                        continue
                    
                    # Log the question generation (BEFORE adding imageUrl)
                    # Log a deep copy to avoid capturing imageUrl later
                    session.log_question(
                        question_id=q_id,
                        topic=topic,
                        question_type="visual" if is_visual else "text",
                        llm_response=copy.deepcopy(generated_question)
                    )
                    
                    # Generate image if this is a visual question
                    if is_visual:
                        image_prompt = generated_question.get('image_prompt', 'N/A')
                        print(f"[DEBUG IG] CALL: Image generation for {q_id}")
                        image_url = await generate_image_from_prompt(
                            image_prompt=image_prompt,
                            unit=topic,
                            question_id=q_id,
                            seed=42
                        )
                        generated_question['imageUrl'] = image_url
                        images_generated += 1
                    else:
                        generated_question['imageUrl'] = None
                    
                    # Add metadata for frontend
                    generated_question["id"] = q_id
                    generated_question["topic"] = topic
                    generated_question["hasImage"] = is_visual
                    question_index += 1
                    questions_sent += 1
                    
                    print(f"[DEBUG] CALL: Stream {q_id} for {topic} ({'visual' if is_visual else 'text'})")
                    yield encoder.encode(generated_question) + "\n"
                    
                    # Add small delay between questions
                    await asyncio.sleep(0.5)
                
                except Exception as e:
                    error_msg = f"Failed to generate question {q_num + 1} for {topic}: {e}"
                    print(f"[ERROR] {error_msg}")
                    import traceback
                    traceback.print_exc()
                    session.log_error("question_generation", type(e).__name__, str(e), {"topic": topic, "q_num": q_num})
                    continue
            
            # Log session completion
            session.log_completion(questions_sent, images_generated)
            print(f"[DEBUG] RESULT: Generated {questions_sent} questions, {images_generated} images")
        
        return StreamingResponse(question_stream(), media_type="application/x-ndjson")
    
    except Exception as e:
        error_msg = str(e)
        print(f"[ERROR] {error_msg}")
        import traceback
        traceback.print_exc()
        
        # Log error to session
        session = get_session()
        if session:
            session.log_error("endpoint", type(e).__name__, error_msg)
        
        return {"error": error_msg}
        traceback.print_exc()
        return {"error": str(e)}


def format_options(options):
    """Helper to ensure options are in ["A) Text", "B) Text"] format"""
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
