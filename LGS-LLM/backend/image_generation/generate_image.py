"""
Image generation module for LGS exam illustrations.
Provides functions to generate images using Chroma or Z-Image services.
"""

import os
from dotenv import load_dotenv
import requests
import base64
from datetime import datetime
from typing import Optional

from .image_prompts import ChromaPromptEngine, ZimagePromptEngine

# Load .env from current directory (if present)
load_dotenv()


# ============================================================================
# HIGH-LEVEL FUNCTIONS - Use these for exam question image generation
# ============================================================================

def generate_image_chroma(
    unit: str,
    image_prompt: str,
    seed: int = 42,
    steps: int = 40,
    guidance_scale: float = 3.0,
) -> bytes:
    """
    Generate an image for exam questions using Chroma service with prompt engineering.
    
    Automatically uses the ChromaPromptEngine to create structured prompts
    based on the unit and LLM-generated image description.
    
    Args:
        unit: The exam unit/topic (e.g., "Friendship", "Teen Life", "Adventures")
        image_prompt: Raw image description from LLM (2-4 sentences)
        seed: Random seed for reproducibility (default: 42)
        steps: Number of diffusion steps (default: 40)
        guidance_scale: Guidance scale for quality (default: 3.0)
    
    Returns:
        Image data as bytes
        
    Raises:
        RuntimeError: If image generation fails
    """
    print(f"[DEBUG IG] INIT: generate_image_chroma(unit={unit})")
    
    # Generate structured prompts using ChromaPromptEngine
    prompts = ChromaPromptEngine.generate_prompts(unit, image_prompt)
    
    positive_prompt = prompts['positive_prompt']
    negative_prompt = prompts['negative_prompt']
    
    # Make API call with the generated prompts
    url = os.getenv("CHROMA_APP_URL")
    if not url:
        raise RuntimeError("CHROMA_APP_URL environment variable is not set!")
    
    if url.endswith('/generate'):
        url = url[: -len('/generate')]
    url = url.rstrip('/')
    
    payload = {
        'prompt': positive_prompt,
        'negative_prompt': negative_prompt,
        'num_images_per_prompt': 1,
        'steps': steps,
        'guidance_scale': guidance_scale,
        'seed': seed,
    }
    
    try:
        print(f"[DEBUG IG] CALL: Chroma /generate (steps={steps})")
        response = requests.post(f"{url}/generate", json=payload, timeout=60*5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] Chroma API request failed: {type(e).__name__}: {e}")
        raise RuntimeError(f"Request to Chroma app failed: {e}")
    
    # Process response
    data = response.json()
    img_b64 = data.get('image') or data.get('image_base64')
    if img_b64 is None:
        print(f"[ERROR] No image data in response")
        raise RuntimeError(f"Unexpected response from Chroma app: {data}")
    
    img_bytes = base64.b64decode(img_b64)
    print(f"[DEBUG IG] RESULT: Chroma image generated ({len(img_bytes)} bytes)")
    return img_bytes


def generate_image_zimage(
    unit: str,
    image_prompt: str,
    seed: int = 42,
    width: int = 1024,
    height: int = 1024,
    steps: int = 9,
    guidance_scale: float = 0.0,
) -> bytes:
    """
    Generate an image for exam questions using Z-Image service with prompt engineering.
    
    Automatically uses the ZimagePromptEngine to create structured prompts
    based on the unit and LLM-generated image description.
    
    Args:
        unit: The exam unit/topic (e.g., "Friendship", "Teen Life", "Adventures")
        image_prompt: Raw image description from LLM (2-4 sentences)
        seed: Random seed for reproducibility (default: 42)
        width: Image width in pixels (default: 1024)
        height: Image height in pixels (default: 1024)
        steps: Number of diffusion steps (default: 9)
        guidance_scale: Guidance scale for quality (default: 0.0)
    
    Returns:
        Image data as bytes
        
    Raises:
        RuntimeError: If image generation fails
    """
    print(f"[DEBUG IG] INIT: generate_image_zimage(unit={unit})")
    
    # Generate structured prompt using ZimagePromptEngine
    final_prompt = ZimagePromptEngine.generate(unit, image_prompt)
    
    # Make API call with the generated prompt
    url = os.getenv("ZIMAGE_APP_URL")
    if not url:
        raise RuntimeError("ZIMAGE_APP_URL environment variable is not set!")
    
    if url.endswith('/generate'):
        url = url[: -len('/generate')]
    url = url.rstrip('/')
    
    payload = {
        'prompt': final_prompt,
        'width': width,
        'height': height,
        'steps': steps,
        'guidance_scale': guidance_scale,
        'seed': seed,
    }
    
    try:
        print(f"[DEBUG IG] CALL: Z-Image /generate (width={width}, height={height}, steps={steps})")
        response = requests.post(f"{url}/generate", json=payload, timeout=60*5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] Z-Image API request failed: {type(e).__name__}: {e}")
        raise RuntimeError(f"Request to Z-Image app failed: {e}")
    
    # Process response
    data = response.json()
    img_b64 = data.get('image') or data.get('image_base64')
    if img_b64 is None:
        print(f"[ERROR] No image data in response")
        raise RuntimeError(f"Unexpected response from Z-Image app: {data}")
    
    img_bytes = base64.b64decode(img_b64)
    print(f"[DEBUG IG] RESULT: Z-Image generated ({len(img_bytes)} bytes)")
    return img_bytes
