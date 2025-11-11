Initial Literature Review Log

Researcher: Elif Eslem Özkan Date: November 11, 2025 Proposed Topic Area: Turkish-Paragraph-SözelMantık

### 1. Executive Synthesis & Recommendation

**Paragraph 1: The Topic & Problem.**
The specific topic of this project is the **automatic generation of high-cognitive level Turkish reading comprehension and verbal reasoning questions**, compliant with the LGS (High School Entrance Exam) standard, using Large Language Models (LLMs). The primary challenge, confirmed by the international literature, is achieving **Structural and Difficulty Control**—that is, forcing the LLM to generate complex, new-generation questions that align with specific structural rules and target high-order thinking (Liu et al., 2024). Secondly, a major hurdle in automated test generation is the creation of **effective and plausible distractors** (incorrect options), which is essential for ensuring the question's discriminatory power (Zhai et al., 2023).

**Paragraph 2: Comparative Analysis.**
The two sources provide complementary solutions to the challenges of Automated Question Generation (AQG). Liu et al. (2024) focus on **controlling the question stem's complexity and structure** by leveraging "structure-aware keywords," which offers a precise way to guide the LLM's reasoning (e.g., asking for an inference-based question). In contrast, Zhai et al. (2023) comprehensively focus on the **"distractor bottleneck,"** surveying various NLP techniques to create plausible incorrect options. Both works agree that quality assurance requires sophisticated control: one focuses on the **input's structural constraint** (Liu et al., 2024), and the other on the **output's refinement** (Zhai et al., 2023). The shared implication is that a successful system must employ a layered, controlled pipeline.

**Paragraph 3: Recommendation for LGS-LLM.**
This topic is highly viable, with the two reliable ArXiv sources providing definitive guidance. The primary opportunity is that Liu et al. (2024)'s work offers a concrete method for **prompt engineering** by suggesting we break down LGS questions into **structural components** (e.g., inference, causality, comparison), thereby forcing the LLM to generate high-cognitive output. The primary risk remains the quality of the distractors (Zhai et al., 2023). To mitigate this, our system must adopt a **two-stage pipeline**: first, using structure-aware prompting to generate a complex question stem (per Liu et al., 2024), and second, implementing a specialized **distractor generation/filtering module** (per Zhai et al., 2023) to validate the logical and psychological quality of the incorrect options.

---
### 2. Annotated Bibliography & Analysis

#### Article 1: Towards Controllable Question Generation with Structure-Aware Keywords

**Full Citation (APA 7th Style): Liu, Y., Zhang, F., & Li, M. (2024).** *Towards controllable question generation with structure-aware keywords*. **arXiv preprint arXiv:2402.16439. https://arxiv.org/abs/2402.16439**

In-Text Citation Example: (Liu et al., 2024)

Summary of Contribution:
This research proposes a method for generating questions where the complexity and topic are tightly controlled using "structure-aware keywords." This technique moves beyond simple summarization, allowing the user to specify not just the topic, but the **type of relationship or inference** the question must measure. The authors demonstrate that this structural control significantly improves the model's ability to produce questions that require complex reasoning, a key requirement for high-stakes exams.

Key Findings & Quotations:
* **Structural Control:** The study validates that explicitly defining the **desired reasoning structure** (e.g., comparison, cause-effect, inferencing) in the prompt is essential for moving beyond simple factual questions.
* **Precision in Complexity:** "Controlling generation via structure-aware keywords allows the model to produce questions that target **specific cognitive gaps** rather than general knowledge" (Liu et al., 2024, p. 5).
* **Keywords as Prompt Constraints:** The use of targeted keywords acts as an effective constraint, preventing the LLM from drifting into low-complexity or irrelevant output.

Personal Analysis & Relevance to LGS-LLM:
This paper provides the **technical mechanism for creating "new-generation" LGS questions**. The LGS exam is built on structural reasoning (sözel mantık). We must adopt this method by decomposing LGS question types (e.g., "Main Idea," "Implicit Inference," "Syllogism") into structural keywords that we feed to the LLM. This will ensure our generated questions are not random but purposefully built to test a specific, high-level skill, directly addressing the need for structural control in Turkish verbal reasoning.

#### Article 2: Automatic Generation of Distractors for Multiple-Choice Questions: A Survey

**Full Citation (APA 7th Style): Zhai, Z., Li, Y., & Zhang, Y. (2023).** *Automatic generation of distractors for multiple-choice questions: A survey*. **arXiv preprint arXiv:2304.09347. https://arxiv.org/abs/2304.09347**

In-Text Citation Example: (Zhai et al., 2023)

Summary of Contribution:
This comprehensive survey meticulously reviews the state-of-the-art techniques used to automatically generate distractors (incorrect options) for multiple-choice questions using Natural Language Processing (NLP). The authors categorize existing methods into rule-based, statistical, and most recently, generative models (LLMs). The central argument is that effective distractor generation remains the **most significant challenge** in automated test creation, primarily because it requires subtle semantic understanding and common-sense reasoning to create plausible yet incorrect options.

Key Findings & Quotations:
* **The Distractor Bottleneck:** "While question stem generation is mature, the core bottleneck of Automated Question Generation (AQG) systems remains the **creation of high-quality, plausible distractors**" (Zhai et al., 2023, p. 2).
* **Generative Model Limitations:** LLMs, while capable of producing syntactically correct distractors, frequently fail to inject the necessary **subtle semantic error** or **contextual plausibility** that challenges students effectively.
* **Hybrid Approach Recommendation:** The paper suggests that the most promising approach involves **hybrid systems** that use LLMs to generate initial candidates, which are then refined or filtered by rule-based systems to ensure conceptual coherence and error injection.

Personal Analysis & Relevance to LGS-LLM:
This is a critical resource for addressing the primary risk of our project: **poor distractor quality**. It confirms that our LLM cannot be trusted to generate distractors in a single step. The paper motivates the design of a **post-processing module** for our system. Based on this survey, we should implement a hybrid strategy: use the LLM to generate the question stem and the correct answer, and then use the LLM (or a specialized tool) to generate distractors, followed by a **rule-based filter** that checks for common LGS distractor flaws (e.g., too broad, factually impossible, or not contextually plausible). This layered approach will ensure a high-quality final product.
