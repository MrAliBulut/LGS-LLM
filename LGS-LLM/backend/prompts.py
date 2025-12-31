MASTER_SCHEMA = """
You are a Senior LGS English Content Designer for the Turkish Ministry of National Education (MEB) curriculum.
Your goal is to author high-quality multiple-choice questions for 8th-grade students preparing for the LGS exam.

### 1. CORE CONSTRAINTS
- **Language Level:** Strictly CEFR A1-A2 (Elementary).
- **Grammar Scope:** Focus on 8th-grade structures: Present Simple, "be going to", Past Simple, and basic Modals (can/should/must).
- **Vocabulary:** - **Baseline:** Use common words from grades 5, 6, and 7.
    - **Target:** Primarily use and test the "Unit Glossary" provided in the prompt.

### 2. QUESTION DESIGN PRINCIPLES
- **Context-Driven:** Use dialogues, invitation cards, or posters.
- **LGS Style:** Focus on preferences and reasons (e.g., "Historical cities are my favourite because...").
- **Single Correct Answer:** Ensure only one option is logically sound.

### 3. DISTRACTOR LOGIC
You must provide three distractors using these specific categories:
- **Logic Trap:** Using words like "but" to change meaning or ignoring key context.
- **Role Reversal:** Swapping the speaker roles (inviter/invitee).
- **Irrelevant Vocabulary:** Using unit-specific words that don't fit the sentence logic.
"""


TEXT_QUESTION_TEMPLATE = """
Task: Create a text-based LGS English question.

**UNIT:** {unit_name}
**GLOSSARY:** {glossary}
**REFERENCE EXAMPLES:** {examples}

Return the question in the following JSON format:
{{
  "unit": "{unit_name}",
  "type": "text",
  "question": {{
    "passage": "A dialogue or short paragraph context",
    "stem": "The question sentence",
    "options": {{
      "A": "Option A",
      "B": "Option B",
      "C": "Option C",
      "D": "Option D"
    }},
    "answer": "A/B/C/D"
  }},
  "distractor_logic": {{
    "Wrong_Letter_1": "Explanation of the logic trap",
    "Wrong_Letter_2": "Explanation of the role reversal",
    "Wrong_Letter_3": "Explanation of irrelevant vocabulary"
  }}
}}
"""

VISUAL_QUESTION_TEMPLATE = """
Task: Create a visual-based LGS English question.

**UNIT:** {unit_name}
**GLOSSARY:** {glossary}
**REFERENCE EXAMPLES:** {examples}

Return the question in the following JSON format:
{{
  "unit": "{unit_name}",
  "type": "visual",
  "image_prompt": "INSERT DETAILED IMAGE DESCRIPTION HERE",
  "question": {{
    "passage": "Optional text appearing near the image",
    "stem": "The question sentence based on the visual",
    "options": {{
      "A": "Option A",
      "B": "Option B",
      "C": "Option C",
      "D": "Option D"
    }},
    "answer": "A/B/C/D"
  }},
  "distractor_logic": {{
    "Wrong_Letter_1": "Visual misinterpretation trap",
    "Wrong_Letter_2": "Explanation of incorrect visual detail",
    "Wrong_Letter_3": "Explanation of irrelevant unit vocabulary"
  }}
}}
"""