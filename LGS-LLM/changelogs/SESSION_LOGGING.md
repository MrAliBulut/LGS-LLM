# Session Logging System

## Overview

Each exam generation session now creates a dedicated log file with timestamp-based naming. Sessions are initiated when the `/generate-exam` endpoint receives a distribution request.

## Log File Structure

**Location**: `logs/` directory  
**Naming**: `YYYY-MM-DD_HH-MM-SS-mmm.json` (date, time, milliseconds)

## Log Contents

Each session log is a JSON file with the following structure:

```json
{
  "timestamp": "2026-01-01T12:34:56.789123",
  "distribution": {
    "topics_requested": {
      "Friendship": 2,
      "Teen Life": 2,
      ...
    },
    "total_questions": 10,
    "visual_count_requested": 4
  },
  "distribution_logic": {
    "visual_distribution": {
      "Friendship": 1,
      "Teen Life": 1,
      ...
    },
    "visual_indices": {
      "Friendship": [0],
      "Teen Life": [1],
      ...
    }
  },
  "questions": [
    {
      "id": "q1",
      "topic": "Friendship",
      "type": "visual",
      "llm_response": {
        "question_text": "...",
        "options": {...},
        "correct_option": "A",
        "image_prompt": "..."
      }
    },
    ...
  ],
  "images": [
    {
      "question_id": "q1",
      "model": "chroma",
      "llm_prompt": "A sunny day at the park with friends playing",
      "engineered_prompt": {
        "positive_prompt": "...",
        "negative_prompt": "..."
      },
      "image_size_bytes": 45678
    },
    {
      "question_id": "q2",
      "model": "zimage",
      "llm_prompt": "A teenage student studying hard at a desk",
      "engineered_prompt": {
        "final_prompt": "..."
      },
      "image_size_bytes": 52341
    }
  ],
  "errors": [
    {
      "timestamp": "2026-01-01T12:34:57.123456",
      "location": "image_generation",
      "type": "RuntimeError",
      "message": "CHROMA_APP_URL environment variable is not set!",
      "context": {
        "question_id": "q1",
        "unit": "Friendship"
      }
    }
  ],
  "completion": {
    "timestamp": "2026-01-01T12:35:12.456789",
    "total_questions_sent": 10,
    "total_images_generated": 4,
    "total_errors": 0
  }
}
```

## What Gets Logged

### 1. Distribution Information
- Topics requested with count per topic
- Total questions requested
- Visual questions requested
- Final visual distribution across topics
- Which question indices are visual per topic

### 2. Question Generation
- Question ID (q1, q2, etc.)
- Topic
- Type (visual or text)
- Complete LLM JSON response including:
  - question_text
  - options
  - correct_option
  - image_prompt (if visual)

### 3. Image Generation
- Question ID this image belongs to
- Model used (chroma or zimage)
- Original LLM image prompt
- Engineered prompt from prompt engine:
  - **Chroma**: positive_prompt, negative_prompt
  - **Z-Image**: final_prompt
- Image size in bytes

### 4. Errors
- Timestamp when error occurred
- Location (question_generation, image_generation, visual_distribution, endpoint)
- Error type (RuntimeError, JSONDecodeError, etc.)
- Error message
- Context (topic, question_id, etc.)

### 5. Session Completion
- Completion timestamp
- Total questions successfully sent
- Total images successfully generated
- Total errors encountered

## Usage in Code

### Creating a Session

```python
from session_logger import create_session, get_session

# When endpoint receives distribution
session = create_session(distribution, visual_count)
```

### Logging Distribution Logic

```python
session.log_distribution_logic(visual_distribution, visual_indices)
```

### Logging Questions

```python
session.log_question(
    question_id="q1",
    topic="Friendship",
    question_type="visual",
    llm_response={
        "question_text": "...",
        "options": {...},
        "image_prompt": "..."
    }
)
```

### Logging Images

```python
session.log_image_generation(
    question_id="q1",
    model_type="chroma",
    llm_image_prompt="Raw prompt from LLM",
    engineered_prompt={
        "positive_prompt": "...",
        "negative_prompt": "..."
    },
    image_size_bytes=45678
)
```

### Logging Errors

```python
session.log_error(
    error_location="image_generation",
    error_type="RuntimeError",
    error_message="CHROMA_APP_URL not set",
    context={"question_id": "q1"}
)
```

### Session Completion

```python
session.log_completion(
    total_questions_sent=10,
    total_images_generated=4
)
```

## Benefits

1. **Complete Audit Trail**: Every session has a detailed record
2. **Debugging**: See exactly what prompts were used and what was generated
3. **Analysis**: Compare different sessions, analyze prompt effectiveness
4. **Error Tracking**: All errors captured with full context
5. **Performance**: Track image generation size and model performance
6. **Distribution Testing**: Verify visual distribution logic worked correctly

## Example Analysis

With these logs, you can:
- Verify visual distribution is random and fair
- See which prompts generated problematic images
- Identify patterns in question generation failures
- Compare performance between chroma and zimage models
- Analyze LLM response quality
- Track system reliability over time
