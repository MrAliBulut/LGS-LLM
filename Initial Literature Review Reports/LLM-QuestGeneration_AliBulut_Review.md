### Initial Literature Review Log

**Researcher:** Ali Bulut
**Date:** 09/11/2025
**Proposed Topic Area:** LLM Question Generation

## 1\. Executive Synthesis & Recommendation

[This section is completed **last**, after analyzing both articles below.]

This review provides a critical strategic choice for the **LGS-LLM** project. The two articles present directly opposing, yet successful, methodologies for LLM-based exam generation.

1.  **Article 1 (Degiovanni & Cabot, 2025)** argues for using **general, open-source models** (like Llama) with **advanced prompt engineering** (specifically `Context_plus_Answer`). They provide evidence that this approach _outperforms_ specialized, fine-tuned models. This is the "low-cost, high-leverage" path.
2.  **Article 2 (Tiratatri et al., 2025)** argues for a **structured, fine-tuning approach** (using custom GPT-4o on authentic IELTS data). They present a complete system architecture ("NOAH") built with a formal SDLC and LLMOps framework. This is the "high-investment, high-control" path.

**Comparative Analysis:**
Degiovanni & Cabot (2025) focus on the _generation component_ (the prompt) and find that fine-tuning is brittle and less effective than superior prompting. Tiratatri et al. (2025) focus on the _entire system_, where fine-tuning is just one component, and argue that it's necessary for domain-specific accuracy (like IELTS/LGS).

Both articles agree on two critical points:

- The system must be built to handle **specific metadata** (difficulty, skill type, etc.), not just raw text.
- The generated output requires a **robust validation/assessment module**.

**Recommendation for LGS-LLM:**
The LGS-LLM project should adopt a **hybrid approach**, leveraging the key insights from both papers.

1.  **Adopt the Architecture of Article 2:** We must adopt the formal SDLC and LLMOps framework from Tiratatri et al. (2025). LGS is a high-stakes exam, and "ad-hoc" development will fail. We must build a system with modular, version-controlled pipelines for generation, assessment, and feedback.
2.  **Adopt the Generation Strategy of Article 1:** For the core generation module, we should follow Degiovanni & Cabot (2025). We will **prioritize prompt engineering (like `Context_plus_Answer`)** with a general-purpose model (e.g., Llama, GPT-4o). This avoids the high cost of fine-tuning and allows us to iterate on prompts, which is faster.
3.  **Address the "Distractor" Problem:** Both papers identify generation quality as a risk. Degiovanni & Cabot (2025) explicitly name **distractor generation** as the primary failure mode (25% match rate). The "Assessment Module" from Tiratatri et al. (2025) must be adapted to solve this. **Recommendation:** Our first "assessor" agent must be a **Distractor Quality Validator**.

In summary: We will build the robust, "NOAH"-like system architecture (Article 2) but power it with the flexible, prompt-driven generation core from Article 1.

## 2\. Analysis of Individual Articles

---

### Article 1: Towards Reliable LLM-based Exam Generation: Lessons Learned and Open Challenges in an Industrial Project

**Full Citation (APA 7th Style):**
Degiovanni, R., & Cabot, J. Towards Reliable LLM-based Exam Generation.

**In-Text Citation Example:**
(Degiovanni & Cabot, 2025)

**Summary of Contribution:**
This paper (Degiovanni & Cabot, 2025) empirically compares 16 LLMs (e.g., GPT, Llama) against 5 specialized, fine-tuned models for generating multiple-choice questions. It finds that general-purpose LLMs, when prompted effectively, outperform the specialized models. The study concludes that prompt engineering is a more effective strategy than fine-tuning for this task.

**Key Findings & Quotations:**

- **Prompting Beats Fine-Tuning:** The study's primary finding is that a specific prompting strategy (`Context_plus_Answer`) "is significantly more effective" than general prompts (Degiovanni & Cabot, 2025, p. 3). This approach, which provides the answer within the prompt, "produces up to 4 times more questions that exactly matches with the ground truth" (Degiovanni & Cabot, 2025, p. 4).
- **Distractor Quality is the Main Failure Point:** While LLMs could generate valid questions and answers, they failed at creating high-quality distractors. The authors report that "only the 25% of the generated distractors, on average, matches with the ones in the ground truth" (Degiovanni & Cabot, 2025, p. 4).

**Objective Analysis & Relevance to LGS-LLM:**

- **Study Limitations:** The analysis is based on the SciQ (science) dataset (Degiovanni & Cabot, 2025). Its applicability to the complex reasoning required for LGS-level math and Turkish-language comprehension is not guaranteed.
- **Project Strategy:** The findings (Degiovanni & Cabot, 2025) strongly suggest the LGS-LLM project should prioritize **prompt engineering** and **model selection** (e.g., Llama, DeepSeek) over investing in custom fine-tuning, which performed worse.
- **Core Feature Requirement:** The `Context_plus_Answer` prompt strategy (Degiovanni & Cabot, 2025) should be implemented. The system's UI should allow a user to select the "correct answer" from the text _before_ generation.
- **Critical Risk Identified:** The 25% match rate for distractors (Degiovanni & Cabot, 2025) identifies the project's single greatest risk. LGS questions are defined by their high-quality "çeldiriciler" (distractors). The model's output for distractors cannot be trusted and will require a separate, robust validation process, as noted in the "open challenges" (Degiovanni & Cabot, 2025, p. 5).
- **Metadata Requirement:** The authors note that "the textual context might not be sufficient" and "Specific contextual information of the target audience... and the expected difficulty" is needed (Degiovanni & Cabot, 2025, p. 1, 5). For LGS, this means all prompts must include structured metadata (e.g., curriculum unit, difficulty target).

---

### Article 2: Designing an LLM-Based IELTS Question Generator, Assessment, and Personalized Training System: Architecture and Research Agenda

**Full Citation (APA 7th Style):**
Tiratatri, T., Sukittivarapunt, K., Sarasinpitak, T., & Pyae, A. (2025, May). _Designing an LLM-Based IELTS Question Generator, Assessment, and Personalized Training System: Architecture and Research Agenda_. [Conference Paper]. 2025 22nd International Conference on Electrical Engineering/Electronics, Computer, Telecommunications and Information Technology (ECTI-CON). DOI:10.1109/ECTI-CON64996.2025.11101665

**In-Text Citation Example:**
(Tiratatri et al., 2025)

**Summary of Contribution:**
This paper (Tiratatri et al., 2025) introduces "NOAH," a complete, full-stack system for generating IELTS exam questions and providing personalized training. Unlike generic AI tutors, NOAH is built on a formal Software Development Life Cycle (SDLC) and LLMOps framework. The architecture features custom fine-tuned GPT-4o models (trained on authentic IELTS materials), "prompt-chained" question generation, and separate modules for assessment, mock testing, and even audio/visual synthesis for speaking and listening tasks.

**Key Findings & Quotations:**

- **System Architecture is Paramount:** The paper's primary contribution is its formal architecture. It advocates for "a structured SDLC and LLMOps framework" to manage the complexity of an exam-generation system (Tiratatri et al., 2025, Abstract).
- **Fine-Tuning for Domain Accuracy:** In direct contrast to Article 1, this paper's premise is that "custom fine-tuned GPT-4o models trained on authentic IELTS materials" are necessary to provide "skill-specific, exam-aligned feedback" (Tiratatri et al., 2025, Abstract).
- **Modular "Pipelines":** The "NOAH" system is built on "modular skill pipelines" (Tiratatri et al., 2025, Abstract). This means generation, assessment, and feedback are separate, version-controlled components, which is a best practice for production-grade AI.

**Objective Analysis & Relevance to LGS-LLM:**

- **Project Management Model:** The LGS-LLM project is a high-stakes, production-focused system, just like the "NOAH" project (Tiratatri et al., 2025). Therefore, we should **immediately adopt their core recommendation:** all development must follow a formal **SDLC and LLMOps framework**. This is a non-negotiable requirement for ensuring reliability, maintainability, and version control of our prompts and models.
- **System Architecture:** The modular design of NOAH (Generation, Assessment, Mock Testing) (Tiratatri et al., 2025) is the correct blueprint for the LGS-LLM. We should structure our system similarly.
- **Validation Module:** The concept of an "Assessment" module (Tiratatri et al., 2025) is the solution to the "distractor" problem identified in Article 1. We must build an independent "LGS-LLM-Assessor" module that validates the quality and difficulty of generated questions, especially their distractors.
- **Counter-Point on Fine-Tuning:** This paper (Tiratatri et al., 2025) makes a case for fine-tuning, which Article 1 (Degiovanni & Cabot, 2025) refutes. As a project strategy, fine-tuning adds significant cost and complexity. We should only consider it _if_ the prompt-engineering approach from Article 1 fails to produce LGS-specific, domain-accurate results. This paper (Tiratatri et al., 2025) provides the "Plan B" if our initial strategy fails.
