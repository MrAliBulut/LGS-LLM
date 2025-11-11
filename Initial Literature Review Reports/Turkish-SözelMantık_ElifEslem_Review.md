Initial Literature Review Log

Researcher: Elif Eslem Özkan Date: November 11, 2025 Proposed Topic Area: Turkish-Paragraph-SözelMantık

### 1. Executive Synthesis & Recommendation

**Paragraph 1: The Topic & Problem.**
The specific topic of this project is the **automatic generation of high-cognitive level Turkish reading comprehension and verbal reasoning questions**, compliant with the LGS (High School Entrance Exam) standard, using Large Language Models (LLMs). The primary challenge, confirmed by the international literature, is achieving **Structural and Difficulty Control**—that is, forcing the LLM to generate complex, new-generation questions that align with specific structural rules and target high-order thinking (Li & Zhang, 2024). Secondly, a major hurdle in automated test generation is the creation of **effective and plausible distractors** (incorrect options), which is essential for ensuring the question's discriminatory power (Qiu et al., 2020).

**Paragraph 2: Comparative Analysis.**
The two sources provide complementary solutions to the challenges of Automated Question Generation (AQG). Li & Zhang (2024) focus on **controlling the question stem's complexity and structure** by leveraging a "planning-first" method, which offers a precise way to guide the LLM's reasoning (e.g., asking for an inference-based question) before the question is drafted. In contrast, Qiu et al. (2020) focus specifically on the practical implementation of **automatic distractor generation** for standard tests, confirming that quality requires sophisticated control mechanisms beyond simple model output. Both works agree that quality assurance requires sophisticated control: one focuses on the **input's structural constraint** (Li & Zhang, 2024), and the other on the **output's refinement and plausibility** (Qiu et al., 2020). The shared implication is that a successful system must employ a layered, controlled pipeline.

**Paragraph 3: Recommendation for LGS-LLM.**
This topic is highly viable, with these two reliable sources providing definitive guidance. The primary opportunity is that Li & Zhang (2024)'s work offers a concrete method for **prompt engineering** by suggesting we break down LGS questions into a **structural planning stage** (e.g., inference, causality, comparison), thereby forcing the LLM to generate high-cognitive output. The primary risk remains the quality of the distractors (Qiu etal., 2020). To mitigate this, our system must adopt a **two-stage pipeline**: first, using structured planning to generate a complex question stem (per Li & Zhang, 2024), and second, implementing a specialized **distractor generation/filtering module** (per Qiu et al., 2020) to validate the logical and psychological quality of the incorrect options.

---
### 2. Annotated Bibliography & Analysis

#### Article 1: Planning First, Question Second: An LLM-Guided Method for Controllable Question Generation

**Full Citation (APA 7th Style): Li, M., & Zhang, W. (2024).** *Planning first, question second: An LLM-guided method for controllable question generation*. **In** *Findings of the Association for Computational Linguistics: ACL 2024* **(pp. 4235–4251).** Association for Computational Linguistics. **https://aclanthology.org/2024.findings-acl.280/**

In-Text Citation Example: (Li & Zhang, 2024)

Summary of Contribution:
This research addresses the core challenge of Controllable Question Generation (CQG) by proposing a "Planning-First" method. Instead of immediately generating the question, the Large Language Model (LLM) is first forced to generate an internal **Plan** that defines the desired structural elements, topic focus, and reasoning path. This Plan then guides the final question generation, ensuring the output is not a simple factual question but one that requires specific, high-level cognitive skills.

Key Findings & Quotations:
* **Structural Control:** The study validates that explicitly defining the **desired reasoning structure** (the 'Plan') is essential for moving beyond simple factual questions and achieving high-level complexity.
* **Precision in Complexity:** "By forcing the LLM to commit to an intermediate planning stage, the model's output quality and controllability are significantly improved, reducing the frequency of irrelevant or simple questions" (Li & Zhang, 2024, p. 4240).
* **Planning as Prompt Constraint:** The use of a mandatory planning step acts as an effective constraint, preventing the LLM from drifting into low-complexity or irrelevant output.

Personal Analysis & Relevance to LGS-LLM:
This paper provides the **technical mechanism for creating "new-generation" LGS questions**. The LGS exam is built on structural reasoning (sözel mantık). We must adopt this Planning-First method by decomposing LGS question types (e.g., "Main Idea," "Implicit Inference," "Syllogism") into a planning template that we force the LLM to fill. This will ensure our generated questions are purposefully built to test a specific, high-level skill.

#### Article 2: Automatic distractor generation for multiple choice questions in standard tests

**Full Citation (APA 7th Style): Qiu, Z., Wu, X., & Fan, W. (2020).** *Automatic distractor generation for multiple choice questions in standard tests*. **arXiv preprint arXiv:2011.13100. https://arxiv.org/abs/2011.13100**

In-Text Citation Example: (Qiu et al., 2020)

Summary of Contribution:
This research focuses specifically on the challenges and techniques for generating plausible distractors (incorrect options) within the context of standardized testing environments. The authors explore methods that ensure the generated distractors are not only grammatically correct but also highly effective at testing the student's knowledge by being semantically close to the correct answer or reflecting common student errors. This work confirms that automated test creation's **core bottleneck** is indeed the quality and plausibility of incorrect options.

Key Findings & Quotations:
* **Plausibility Focus:** The study emphasizes generating distractors that are highly plausible or semantically similar to the correct answer, which is crucial for maximizing the question's discriminatory power in standardized tests.
* **Standardized Testing Relevance:** The research highlights the need for specialized models/pipelines to produce distractors that align with the specific error patterns expected in formal, high-stakes assessments like the LGS.
* **Hybrid Approach Confirmation:** The paper indirectly supports the necessity of a controlled, multi-stage process where initial generated options must be refined or filtered to ensure their effectiveness as true distractors.

Personal Analysis & Relevance to LGS-LLM:
This paper is highly relevant as it focuses specifically on **standardized testing**, which mirrors the LGS environment. It confirms the necessity of moving beyond simple generative LLMs for distractors and adopting a post-processing or hybrid module. This resource strongly supports our strategic decision to implement a dedicated QA module to check for **plausibility** and **common error patterns** in the automatically generated incorrect options.
