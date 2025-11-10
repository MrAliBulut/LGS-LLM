SWOT Analysis: LGS English Question Generator
Researcher: Elif Eslem Özkan
Date: November 11, 2025

**1. Strengths (Internal, Positive)**
* **S1: Optimal Language Alignment:** LLMs perform best in English, the target language. This inherently minimizes the risk of grammatical errors, linguistic nuance loss, and contextual ambiguity often seen in lower-resource languages.
* **S2: High-Quality RAG Corpus:** Utilizing official LGS lecture books and previous exam questions provides a clean, pedagogically validated, and highly relevant knowledge base for RAG. This is a massive strength over using general web data.
* **S3: Methodological Efficiency (Prompt Engineering over Finetuning):** Choosing Prompt Engineering avoids the high computational cost, time consumption, and expertise required for finetuning. This allows for rapid iteration and pivoting, which is ideal for a short-term project.
* **S4: Large Team Size & Diverse Skill Potential:** A 15-person team provides a robust workforce for the tedious but necessary tasks of data preprocessing, RAG implementation, and the comprehensive human QA required to validate both text and image output.

**2. Weaknesses (Internal, Negative)**
* **W1: High Dependency on Prompt Quality (W/O Finetuning):** Since we are not using finetuning, success hinges entirely on the quality and complexity of our Prompt Engineering. If the prompts fail to capture LGS's subtle logic/structure (as required by Liu et al., 2024), the project fails.
* **W2: Inconsistent Distractor Quality:** Based on the literature (Zhai et al., 2023), generating truly plausible, yet incorrect, options (distractors) is the most challenging NLP task. Our internal process must be extremely meticulous here, which consumes significant time.
* **W3: Risk of Unfocused Effort due to Image Feature:** The complexity of managing two distinct outputs (textual question vs. image prompt generation) may dilute focus. The team might struggle to allocate resources effectively between core text generation and the complex image prompt subsystem.
* **W4: Coordination and Communication Overhead:** A 15-person team inherently suffers from high coordination overhead. Without rigid documentation and clear task boundaries, there is a risk of duplicated work or communication breakdowns, especially across different sub-teams.

**3. Opportunities (External, Positive)**
* **O1: Advancements in Image Prompting Capabilities:** Rapid improvements in multimodal LLMs (like newer versions of DALL-E, Imagen) offer an opportunity to generate high-quality, relevant images directly from textual instructions, enhancing our key feature (visual questions).
* **O2: Structured Nature of English Exams:** The LGS English syllabus and question types (vocabulary, grammar rules) are highly structured and predictable, making them ideal targets for RAG and rule-based Prompt Engineering.
* **O3: Open-Source RAG Ecosystem Maturity:** The availability of mature, open-source RAG libraries (LangChain, LlamaIndex) minimizes our development time for the knowledge base integration, allowing us to focus our efforts on prompt logic.
* **O4: Strong Stakeholder Engagement:** Successfully producing a practical, high-quality content generator (unlike a pure research paper) presents a powerful opportunity to impress our teacher and potentially secure high marks.

**4. Threats (External, Negative)**
* **T1: API Cost and Unreliability:** Reliance on proprietary LLM APIs (for text and image generation) presents a significant cost threat, potentially making the final product unsustainable. API unreliability (downtime, censorship, rate limits) threatens development speed.
* **T2: Image Generation IP/Copyright Issues:** The images produced by commercial generators may have unclear licensing terms for educational content, posing a legal risk if the product were to be commercialized.
* **T3: Subtlety of LGS Logic:** The core challenge of LGS questions is often not the English language itself, but the **human-level logic leap** required to interpret the context. No prompt, however advanced, can guarantee the LLM will master this nuanced logical inference every time.
* **T4: Data Staleness:** If the LGS English curriculum or exam format undergoes a sudden, major shift before the project's completion, our entire RAG corpus (lecture books/old exams) could instantly become obsolete, requiring a major overhaul.

**5. Personal Strategic Recommendation**
My analysis indicates that the project’s greatest inherent advantage lies in **S3 (Efficiency of Prompt Engineering)** combined with **S2 (High-Quality RAG Corpus)**. However, the most significant risk is the combination of **W3 (Unfocused Image Effort)** and **W2 (Distractor Quality)**. I recommend a strategic prioritization of effort: we should immediately form a small, dedicated **"Image Time-Box" sub-team** of 2-3 people. This team should be given a hard deadline (e.g., 10 days) to prove the viability and reliability of image prompt generation (O1). If the image output fails to meet the required quality standard within that box, the feature should be deprioritized or dropped entirely, allowing the main team to focus 100% on perfecting **text-based question generation and the critical distractor quality (W2)**. The high dependency on prompt quality (W1) demands that a core team focus exclusively on developing and iterating structural LGS prompts.