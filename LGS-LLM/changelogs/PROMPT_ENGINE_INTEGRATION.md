# Prompt Engine Integration - Architecture Overview

## Summary
Refactored the image generation system to use comprehensive prompt engineering engines (`ChromaPromptEngine` and `ZimagePromptEngine`) for creating structured, educationally-optimized prompts.

---

## Architecture Changes

### Before
```
LLM Image Prompt (raw)
         ↓
generate_image_chroma(prompt=raw_prompt)
         ↓
API Call → Image Bytes
```

### After
```
Unit Name + LLM Image Prompt (raw)
         ↓
[ChromaPromptEngine | ZimagePromptEngine].generate()
         ↓
Structured Prompt (with style guide + unit schema)
         ↓
generate_image_for_exam_chroma/zimage()
         ↓
generate_image_chroma/zimage(prompt=structured_prompt)
         ↓
API Call → Image Bytes
```

---

## New Functions

### 1. `generate_image_for_exam_chroma(unit, image_prompt, seed, steps, guidance_scale)` 
**High-level function for exam questions**
- Takes: unit name + raw LLM prompt (2-4 sentences)
- Uses: `ChromaPromptEngine.generate_prompts(unit, image_prompt)`
- Returns: Image bytes
- Benefits: Automatic prompt engineering, consistent visual style

Example:
```python
img_bytes = generate_image_for_exam_chroma(
    unit="Friendship",
    image_prompt="Two students are sitting on a bench and reading magazines together."
)
```

### 2. `generate_image_for_exam_zimage(unit, image_prompt, seed, width, height, steps, guidance_scale)`
**High-level function for exam questions**
- Takes: unit name + raw LLM prompt (2-4 sentences)
- Uses: `ZimagePromptEngine.generate(unit, image_prompt)`
- Returns: Image bytes
- Benefits: Automatic prompt engineering, consistent visual style

Example:
```python
img_bytes = generate_image_for_exam_zimage(
    unit="In the Kitchen",
    image_prompt="A student is peeling a large potato with a knife."
)
```

### 3. `generate_image_chroma(prompt, negative_prompt, seed, steps, guidance_scale)`
**Low-level function for direct API control**
- Takes: Fully constructed prompt strings
- Returns: Image bytes
- Use when: You've already engineered the prompt

### 4. `generate_image_zimage(prompt, seed, width, height, steps, guidance_scale)`
**Low-level function for direct API control**
- Takes: Fully constructed prompt string
- Returns: Image bytes
- Use when: You've already engineered the prompt

---

## Flow in generate_exam.py

### Updated `generate_image_from_prompt()`
```python
async def generate_image_from_prompt(
    image_prompt: str,
    unit: str,
    model_type: str = None,
    **model_kwargs
) -> str:
    # Get model from env (IMAGE_GENERATION_MODEL)
    # Routes to appropriate high-level function based on model_type
    # Returns base64 data URI
```

### Usage in question_stream()
```python
image_url = await generate_image_from_prompt(
    image_prompt=image_prompt,  # From LLM
    unit=topic,                 # Current exam unit
    seed=42
)
```

---

## Prompt Engineering Details

### ChromaPromptEngine
**Components:**
- `STYLE_POSITIVE`: Master style settings (flat vector, pastel colors, exam-safe)
- `STYLE_NEGATIVE`: Global negative constraints (no text, realistic photos, etc.)
- `UNIT_CONFIG`: Unit-specific purposes, results, and negative tags

**Output:** Positive + Negative prompt pair

Example output:
```
POSITIVE:
"Role: Educational illustration for LGS English exam. 
Style: Clean flat vector illustration, soft pastel colors...
Purpose: Show social interactions and friendship...
Image: <LLM-generated-scene>
Constraints: No text, no symbols."

NEGATIVE:
"text, letters, numbers, labels, signs, brand logos...
fighting, aggressive faces, crowded scenes..."
```

### ZimagePromptEngine
**Components:**
- `MASTER_PREFIX`: Exam-safe textbook aesthetic
- `UNIT_SCHEMAS`: Unit-specific visual guidelines
- `MASTER_SUFFIX`: Composition rules (uncluttered, centered)
- `NEGATIVE_PROMPT`: Comprehensive exam safety guardrails

**Output:** Single unified prompt with embedded guardrails

Example output:
```
"Educational illustration for the Turkish LGS English exam.
Style: Clean flat vector illustration...
Focus on social interactions...
<LLM-generated-scene>
The composition must be uncluttered with a minimalist background...
Strictly avoid: text, letters, words, numbers, labels..."
```

---

## Configuration

Add to `.env`:
```env
# Image generation model to use
IMAGE_GENERATION_MODEL=chroma  # or "zimage"

# API endpoints
CHROMA_APP_URL=http://localhost:7860
ZIMAGE_APP_URL=http://localhost:7861
```

---

## Benefits of This Approach

✅ **Separation of Concerns**: Prompt engineering logic separate from API calls  
✅ **Consistency**: Same style guidelines applied to all images  
✅ **Maintainability**: Change global rules in one place  
✅ **Flexibility**: Easy to adjust prompts for different exam types  
✅ **Safety**: Built-in guardrails for exam-appropriate content  
✅ **Extensibility**: Easy to add new units or modify schemas  
✅ **Debugging**: Clear logging shows generated prompts at each stage

---

## Debug Logging

Enable by running backend, look for `[DEBUG IG]` prefix:
```
[DEBUG IG] generate_image_for_exam_chroma() called
[DEBUG IG] Unit: Friendship
[DEBUG IG] Raw image prompt length: 145 chars
[DEBUG IG] Generating structured prompts with ChromaPromptEngine...
[DEBUG IG] Generated positive prompt length: 892 chars
[DEBUG IG] Generated negative prompt length: 234 chars
[DEBUG IG] Calling generate_image_chroma(prompt=...)
[DEBUG IG] Base64 image string length: 524288 chars
[DEBUG IG] Decoded image bytes: 262144 bytes
[IMAGE GENERATION] ✓ Successfully generated image from chroma model
```

---

## Migration Checklist

- ✅ Created `ChromaPromptEngine` and `ZimagePromptEngine` in `image_prompts.py`
- ✅ Created high-level functions in `generate_image.py`
- ✅ Updated `generate_image_from_prompt()` to accept unit parameter
- ✅ Updated call sites in `generate_exam.py` to pass unit name
- ✅ Added comprehensive DEBUG logging
- ✅ Tested imports (all passing)

---

## Testing

```bash
# Test imports
python -c "import generate_exam; print('✓ OK')"

# Run backend
python generate_exam.py

# Test endpoint
curl -X POST http://localhost:8000/generate-exam \
  -H "Content-Type: application/json" \
  -d '{"distribution": {"Friendship": 2}, "visualCount": 1}'
```

---

## Next Steps

1. **Integration Testing**: Run end-to-end with actual image APIs
2. **Quality Assessment**: Review generated images for consistency
3. **Prompt Tuning**: Adjust unit schemas based on image quality
4. **Performance**: Monitor API response times with new prompts
5. **Documentation**: Update user guides for configuration options
