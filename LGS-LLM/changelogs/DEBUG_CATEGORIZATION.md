# Debug Print Categorization

## Overview
All debug prints in the backend have been simplified and categorized using a consistent `[DEBUG]` header system.

## Categories

### 1. **[DEBUG]** - General Operations (Main flow)
- **INIT**: Function initialization and start
  ```python
  print(f"[DEBUG] INIT: /generate-exam (topics={len(distribution)}, visual={visual_count})")
  print(f"[DEBUG] INIT: Fetched {len(all_questions)} questions from DB")
  ```

- **CALL**: API calls or function invocations
  ```python
  print(f"[DEBUG] CALL: Stream q{question['id']} ({topic})")
  ```

- **RESULT**: Final outcomes or summaries
  ```python
  print(f"[DEBUG] RESULT: Generated {question_index - 1} questions")
  print(f"[DEBUG] RESULT: Grouped {len(grouped)} topics")
  ```

### 2. **[DEBUG IG]** - Image Generation Pipeline
- **INIT**: Image generation start
  ```python
  print(f"[DEBUG IG] INIT: generate_image_from_prompt(unit={unit}, model={model_type})")
  print(f"[DEBUG IG] INIT: generate_image_chroma(unit={unit})")
  ```

- **CALL**: API calls to image services
  ```python
  print(f"[DEBUG IG] CALL: Image generation for q{question_index}")
  print(f"[DEBUG IG] CALL: Chroma /generate (steps={steps})")
  ```

- **RESULT**: Image generation completion
  ```python
  print(f"[DEBUG IG] RESULT: Image generated ({len(img_bytes)} bytes)")
  print(f"[DEBUG IG] RESULT: Chroma image generated ({len(img_bytes)} bytes)")
  ```

### 3. **[WARNING]** - Potential Issues
```python
print(f"[WARNING] Requested {visual_count} visual but only {len(topics_pool)} slots available")
print(f"[WARNING] Failed to generate question {q_num + 1} for {topic}")
```

### 4. **[ERROR]** - Critical Failures
```python
print(f"[ERROR] Image generation failed: {type(e).__name__}: {e}")
print(f"[ERROR] Failed to fetch questions: {e}")
```

## Files Updated

### generate_exam.py
- **INIT**: `/generate-exam` endpoint start with topic count and visual count
- **CALL**: Image generation calls, streaming calls
- **RESULT**: Total questions generated
- **WARNING**: Visual distribution issues
- **ERROR**: Question generation failures

### question_generator.py
- **RESULT**: Database fetch counts, grouped topics count
- **WARNING**: Missing topics
- **ERROR**: Database and loading errors

### backup.py
- **INIT**: `/generate-exam` endpoint start
- **RESULT**: Selection counts, streaming completion
- **CALL**: Streaming operations
- **WARNING/ERROR**: Failures and exceptions

### image_generation/generate_image.py
- **INIT**: Function start (chroma/zimage)
- **CALL**: API calls to Chroma/Z-Image services
- **RESULT**: Image bytes generated
- **ERROR**: Generation failures with fallback

## Benefits

1. **Cleaner Output**: Removed verbose intermediate logging
2. **Better Tracking**: Category headers make it easy to follow flow
3. **Consistency**: All debug prints follow same pattern
4. **Reduced Noise**: Only essential checkpoints logged
5. **Easy Filtering**: Can search for `[DEBUG]`, `[DEBUG IG]`, `[WARNING]`, `[ERROR]`

## Summary

- **[DEBUG]** for main backend flow
- **[DEBUG IG]** for image generation specifically
- **[WARNING]** for potential issues
- **[ERROR]** for failures with stack traces
