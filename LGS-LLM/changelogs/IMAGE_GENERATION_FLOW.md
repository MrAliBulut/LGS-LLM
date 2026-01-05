# Image Generation Flow Architecture

## Sequential Flow

```python
# Step 1: Wait for LLM to generate the question
generated_question = await generate_question_for_unit(topic, visual=is_visual)

# At this point, generated_question contains:
# {
#   "stem": "Which activity...",
#   "options": {"a": "reading", "b": "playing", ...},
#   "answer": "a",
#   "image_prompt": "A girl reading a book at home...",  ← HERE
#   ...
# }

# Step 2: Check if it's a visual question
if is_visual:
    # Step 3: Extract the image_prompt from the LLM response
    image_prompt = generated_question.get('image_prompt')
    
    # Step 4: Send the image_prompt to generate the image
    image_url = await generate_image_from_prompt(image_prompt)
    
    # Step 5: Add the generated image to the question
    generated_question["imageUrl"] = image_url
else:
    generated_question["imageUrl"] = None

# Step 6: Send complete question JSON to frontend via NDJSON stream
yield encoder.encode(generated_question) + "\n"
```

## Flow Diagram

```
┌─────────────────────────────────────────┐
│ 1. LLM Generates Question               │
│    (with image_prompt if visual=True)   │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 2. Check: is_visual?                    │
└──────────┬────────────────────┬─────────┘
           │                    │
        YES│                    │NO
           ↓                    ↓
    ┌────────────────┐   ┌──────────────┐
    │ 3. Extract     │   │ imageUrl=None│
    │ image_prompt   │   │              │
    │ from question  │   └──────┬───────┘
    └────────┬───────┘          │
             ↓                  │
    ┌─────────────────────┐     │
    │ 4. Call generate_   │     │
    │ image_from_prompt   │     │
    │ (image_prompt)      │     │
    └────────┬────────────┘     │
             ↓                  │
    ┌─────────────────────┐     │
    │ 5. Get image bytes  │     │
    │ Convert to base64   │     │
    │ data URI            │     │
    └────────┬────────────┘     │
             ↓                  │
    ┌─────────────────────┐     │
    │ 6. Add imageUrl to  │     │
    │ question JSON       │     │
    └────────┬────────────┘     │
             │                  │
             └────────┬─────────┘
                      ↓
         ┌─────────────────────────┐
         │ 7. Send Question JSON   │
         │ via NDJSON stream to    │
         │ Frontend                │
         └─────────────────────────┘
```

## Process Summary

1. ✅ Wait for LLM question generation to complete
2. ✅ Extract `image_prompt` from the generated question
3. ✅ If `is_visual=true`, send that `image_prompt` to `generate_image_from_prompt()`
4. ✅ Get back the image (as base64 data URI or placeholder)
5. ✅ Add it as `imageUrl` to the question
6. ✅ Send the complete question to frontend

## Frontend Image Expectations

The frontend expects each visual question to have:

```javascript
{
  "id": "q1",
  "hasImage": true,
  "imageUrl": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...",
  "stem": "Question text...",
  "options": { "a": "...", "b": "...", "c": "...", "d": "..." },
  "answer": "a",
  "topic": "Friendship",
  ...
}
```

- **imageUrl**: Base64 data URI (`data:image/png;base64,...`) or placeholder URL (`/placeholder.svg`)
- **hasImage**: Boolean flag indicating if question has an image
- Uses Next.js `<Image>` component for rendering
- Shows loading spinner while image loads

## Backend Image Generation Function

```python
async def generate_image_from_prompt(image_prompt: str) -> str:
    """
    Generate an image from a text prompt using Chroma service.
    
    Returns:
        Base64 data URI of the generated image, or placeholder URL as fallback
    """
    try:
        # Generate image using Chroma service with custom prompt
        img_bytes = generate_image_chroma(prompt=image_prompt)
        
        # Convert to base64 data URI
        img_b64 = base64.b64encode(img_bytes).decode('utf-8')
        data_uri = f"data:image/png;base64,{img_b64}"
        
        print(f"[IMAGE GENERATION] Successfully generated image from prompt")
        return data_uri
    
    except Exception as e:
        # Fallback to placeholder on error
        print(f"[IMAGE GENERATION] Failed to generate image: {e}")
        print(f"[IMAGE GENERATION] Returning placeholder as fallback")
        placeholder_url = "/placeholder.svg"
        return placeholder_url
```

## Key Features

✓ **Sequential Processing** - LLM generates question first, then image is generated  
✓ **No File I/O** - Images are embedded as base64 in JSON  
✓ **Streaming** - Images start loading before all questions are generated  
✓ **Error Handling** - Automatic fallback to placeholder if image generation fails  
✓ **Frontend Compatible** - Next.js Image component handles data URIs natively  
✓ **Efficient** - Single HTTP request returns all questions with images
