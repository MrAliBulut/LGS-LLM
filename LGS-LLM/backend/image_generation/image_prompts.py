class ChromaPromptEngine:
    # 1. MASTER STYLE SETTINGS (Consistency across all images)
    STYLE_POSITIVE = (
        "Role: Educational illustration for LGS English exam. "
        "Style: Clean flat vector illustration, soft pastel colors, "
        "clear outlines, child-friendly, exam-safe, minimalist details. "
        "Environment: Bright, neutral background, realistic proportions. "
    )

    STYLE_NEGATIVE = (
        "text, letters, numbers, labels, signs, brand logos, watermarks, "
        "realistic photography, 3D render, dark colors, exaggerated style, "
        "fantasy elements, blur, low quality, messy lines, cluttered composition, "
    )

    # 2. UNIT SCHEMAS
    # Each unit contains a specific Purpose, Result, and Unit-Specific Negative tags.
    UNIT_CONFIG = {
        "Friendship": {
            "positive": "Purpose: Show social interactions and friendship. Result: Students identify positive social behaviors. Image: {image_prompt}",
            "negative": "fighting, aggressive faces, crowded scenes"
        },
        "Teen Life": {
            "positive": "Purpose: Show daily teen interests and routines. Result: Students match activities with teen life. Image: {image_prompt}",
            "negative": "clocks, time labels, school names"
        },
        "In the Kitchen": {
            "positive": "Purpose: To show cooking processes and kitchen tools. Result: Students identify cooking verbs and ingredients. Image: {image_prompt}",
            "negative": "food labels, brand names on appliances, spice jar text"
        },
        "On the Phone": {
            "positive": "Purpose: To illustrate phone conversations and communication. Result: Students recognize calling/messaging contexts. Image: {image_prompt}",
            "negative": "text on screen, interface icons with words, speech bubbles"
        },
        "The Internet": {
            "positive": "Purpose: To represent online activities and safety. Result: Students identify digital habits. Image: {image_prompt}",
            "negative": "URL addresses, search bar text, browser window words"
        },
        "Adventures": {
            "positive": "Purpose: To show extreme sports and outdoor activities. Result: Students identify adventure vocabulary. Image: {image_prompt}",
            "negative": "scoreboards, complex equipment labels, advertisements"
        },
        "Tourism": {
            "positive": "Purpose: To illustrate travel, holidays, and landmarks. Result: Students identify locations and sightseeing. Image: {image_prompt}",
            "negative": "city names, signboards, map text, street names"
        },
        "Chores": {
            "positive": "Purpose: To show household responsibilities. Result: Students recognize domestic tasks. Image: {image_prompt}",
            "negative": "cleaning product labels, brand logos on vacuum"
        },
        "Science": {
            "positive": "Purpose: To show scientific exploration and lab work. Result: Students identify science-related nouns. Image: {image_prompt}",
            "negative": "chemical formulas, periodic table text, book titles"
        },
        "Natural Forces": {
            "positive": "Purpose: To show weather events and natural disasters. Result: Students identify environmental forces. Image: {image_prompt}",
            "negative": "news headlines, temperature numbers, emoji icons"
        }
    }

    @classmethod
    def generate_prompts(cls, unit: str, llama_image_prompt: str):
        """
        Creates a structured Positive and Negative prompt for the Chroma model.
        """
        # Get unit configuration or use a default
        config = cls.UNIT_CONFIG.get(unit, {
            "positive": "Purpose: Educational support. Result: Visual clarity. Image: {image_prompt}",
            "negative": "Don't write any text or letters."
        })

        # Construct Positive Prompt
        # Combines Style + Unit Purpose + LLM Description + Constraints
        unit_positive = config["positive"].format(image_prompt=llama_image_prompt)
        final_positive = f"{cls.STYLE_POSITIVE}{unit_positive} Constraints: No text, no symbols."

        # Construct Negative Prompt
        # Combines Master Negatives + Unit Specific Negatives
        final_negative = f"{cls.STYLE_NEGATIVE}{config['negative']}"

        return {
            "positive_prompt": final_positive,
            "negative_prompt": final_negative
        }
        
        
class ZimagePromptEngine:
    # 1. THE MASTER SCHEMA
    # This acts as the "wrapper" for every prompt to maintain visual unity.
    MASTER_PREFIX = (
        "Educational illustration for the Turkish LGS English exam. Don't write any text or letters.  "
        "Style: Clean flat vector illustration, professional textbook aesthetic, "
        "soft pastel colors, simple shapes, neutral lighting. "
    )

    MASTER_SUFFIX = (
        " The composition must be uncluttered with a minimalist background and "
        "wide margins. The subject should be centered and easily recognizable "
        "by middle school students."
    )

    # The ultimate guardrail for exam safety.
    NEGATIVE_PROMPT = (
        "Strictly avoid: text, letters, words, numbers, labels, signage, "
        "brand logos, watermarks, speech bubbles, realistic photography, "
        "3D rendering, heavy shadows, cluttered details, symbols, or emojis."
    )

    # 2. UNIT-SPECIFIC SCHEMAS
    # Each unit provides a specific 'lens' for the image_prompt.
    UNIT_SCHEMAS = {
        "Friendship": (
            "Focus on social interactions, positive facial expressions, "
            "and body language. {image_prompt} Ensure characters look "
            "like middle school students."
        ),
        "Teen Life": (
            "Focus on daily hobbies, school activities, and common teen "
            "interests. {image_prompt} Use a modern, relatable school-age vibe."
        ),
        "In the Kitchen": (
            "Focus on cooking tools, kitchen utensils, and clear action verbs "
            "like chopping, stirring, or boiling. {image_prompt} The food "
            "items must be distinct and identifiable."
        ),
        "On the Phone": (
            "Focus on communication gestures, holding devices, and polite "
            "interactions. {image_prompt} Smartphone screens must be blank "
            "with no text or icons."
        ),
        "The Internet": (
            "Focus on digital devices, computer monitors, and social media "
            "concepts. {image_prompt} Use symbolic representations for "
            "connectivity without using any letters."
        ),
        "Adventures": (
            "Focus on outdoor settings, extreme sports equipment, and "
            "nature. {image_prompt} Emphasize safety gear like helmets "
            "and life jackets."
        ),
        "Tourism": (
            "Focus on sightseeing, landmarks, transportation, and "
            "vacation-related objects. {image_prompt} Architecture should "
            "be simple and iconic."
        ),
        "Chores": (
            "Focus on household cleaning tools, domestic tasks, and "
            "responsibility. {image_prompt} Show a clear contrast between "
            "messy and clean states if applicable."
        ),
        "Science": (
            "Focus on laboratory equipment, scientific inventions, and "
            "exploration. {image_prompt} Use iconic shapes like test tubes "
            "and microscopes."
        ),
        "Natural Forces": (
            "Focus on environmental elements, weather extremes, and "
            "the power of nature. {image_prompt} Use clear visual cues "
            "for temperature and wind."
        )
    }

    @classmethod
    def generate(cls, unit_name: str, llama_image_prompt: str) -> str:
        """
        Combines the Master Schema, Unit Schema, and the Llama-generated prompt.
        """
        # Fallback to a generic schema if unit is not found
        unit_template = cls.UNIT_SCHEMAS.get(
            unit_name, 
            "Focus on educational clarity. {image_prompt}"
        )
        
        # Insert the 3-4 sentence prompt from Llama into the unit template
        filled_unit_schema = unit_template.format(image_prompt=llama_image_prompt)
        
        # Construct the final prompt
        final_prompt = (
            f"{cls.MASTER_PREFIX} "
            f"{filled_unit_schema} "
            f"{cls.MASTER_SUFFIX} "
            f"Negative Prompt: {cls.NEGATIVE_PROMPT}"
        )
        
        return final_prompt

# --- BACKEND INTEGRATION EXAMPLE ---
if __name__ == "__main__":
    # 1. Received from LLM
    current_unit = "Adventures"
    llama_generated_scene = "A young girl wearing a life jacket is paddling a blue kayak on a calm river with mountains in the background."

    # 2. Generate for Chroma
    prompts = ChromaPromptEngine.generate_prompts(current_unit, llama_generated_scene)

    print("--- CHROMA POSITIVE PROMPT ---")
    print(prompts['positive_prompt'])
    print("\n--- CHROMA NEGATIVE PROMPT ---")
    print(prompts['negative_prompt'])
    
    # This simulates the data you get from llama-3.3-70b-versatile
    unit = "In the Kitchen"
    llama_output = "A student is peeling a large potato with a knife. A bowl of water is on the counter next to them."

    final_zimage_prompt = ZimagePromptEngine.generate(unit, llama_output)
    
    print(f"PROMPT FOR ZIMAGE:\n\n{final_zimage_prompt}")