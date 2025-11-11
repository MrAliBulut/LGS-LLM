### Initial Literature Review Log

**Researcher:** Gökhan Çağaptay
**Date:** November 10, 2025
**Proposed Topic Area:** Science-STEM, K-12-ScientificReasoning

## 1. Executive Synthesis & Recommendation

**Paragraph 1: The Topic & Problem.**
The specific topic of this project is the **automatic generation of high-cognitive level, LGS (High School Entrance Exam) standard Science questions** using Large Language Models (LLMs). The primary challenge, confirmed by the international literature, is not text generation, but achieving **Visual and Structural Control**. LGS Science questions are fundamentally reliant on interpreting visual data (e.g., experiment setups, graphs, diagrams). [cite_start]The literature confirms that LLMs struggle with "handling visual educational content" (Chen et al., 2024, p. 11) [cite: 292] [cite_start]and "interpreting kinematic graphs" (Chen et al., 2024, p. 11)[cite: 293]. A secondary problem is ensuring pedagogical quality: the model must not only find the correct answer but also use sound "scientific reasoning" to get there, as models often rely on "pattern recognition rather than true logical inference" (Rueda et al., 2025, Abstract).

**Paragraph 2: Comparative Analysis.**
The two sources provide a perfect complementary framework for this topic. Chen et al. (2024) [cite_start]is a **broad systematic review** [cite: 7, 8] [cite_start]that maps the current K-12 STEM landscape, identifying the *menu* of available prompt techniques (e.g., CoT, Few-shot, Role-Assigned) [cite: 148, 159] [cite_start]and confirming that the "visual content" [cite: 292] is the primary unsolved challenge. In contrast, Rueda et al. (2025) is a **deep experimental test** of these techniques, analyzing the critical trade-off between *answer accuracy* and *explanation quality (reasoning)*. Both works agree that sophisticated control is necessary. Chen et al. (2024) defines the *domain challenge* (visuals), while Rueda et al. (2025) defines the *methodological challenge* (prioritizing reasoning over accuracy).

**Paragraph 3: Recommendation for LGS-LLM.**
This topic is highly viable and these sources provide a clear path forward.
**Primary Opportunity:** Rueda et al. (2025) provides two critical opportunities. First, it proves that the prompt with the highest accuracy ("Self-Consistency" at 52.99%) has poor explanation quality ("performed the second worst in explaining the answers"). For the LGS "muhakeme" (reasoning) exam, we should instead select the prompt with the **best reasoning quality**, such as "Zero-Shot CoT". Second, it provides a free **QA filter**: the LLM *refused to answer* a flawed question (Q257) where the correct answer was not in the options. We can use this behavior to automatically filter our generated questions for logical flaws.
**Primary Risk:** The primary risk, identified by Chen et al. (2024)[cite_start], is the visual component [cite: 292-295].
**Mitigation:** Our system must adopt a **two-stage pipeline**:
1.  **Stage 1 (Text):** Use a high-reasoning prompt (per Rueda et al., 2025) to generate the question stem, data, distractors, and a step-by-step *explanation*.
2.  **Stage 2 (Visual):** Use the text/data from Stage 1 to feed a separate multimodal (text-to-image) model or a "human-in-the-loop" (human-supervised) process to create the required graph or experiment diagram, addressing the core limitation identified by Chen et al. (2024) [cite_start][cite: 292].

---

## 2. Annotated Bibliography & Analysis

### Article 1: A Systematic Review on Prompt Engineering in Large Language Models for K-12 STEM Education

**Full Citation (APA 7th Style):**
Chen, I-S., Wang, D., Xu, L., Cao, C., Fang, X., & Lin, J. (2024). *A Systematic Review on Prompt Engineering in Large Language Models for K-12 STEM Education*. [Technical Report/Preprint]. Sourced from user-provided file `A_Systematic_Review_on_Prompt_Engineering_in_Large.pdf`.

**In-Text Citation Example:**
(Chen et al., 2024)

**Summary of Contribution:**
[cite_start]This paper is a comprehensive systematic review that analyzes 30 studies [cite: 8] [cite_start]on the use of LLM prompt engineering within K-12 (Kindergarten to 12th grade) STEM (Science, Technology, Engineering, and Mathematics) education[cite: 7, 15]. [cite_start]The research identifies and categorizes the prompting strategies employed (e.g., Simple, Role-Assigned, Zero-Shot, Few-Shot, Chain-of-Thought) [cite: 148] [cite_start]and maps them to specific educational tasks like "Problem Solving," "Problem Creation," and "Assessment and Grading"[cite: 159].

**Key Findings & Quotations:**

* [cite_start]**Prompting Strategies:** The review confirms that advanced techniques like "few-shot prompting and chain-of-thought prompting have demonstrated positive outcomes for various educational tasks" (Chen et al., 2024, p. 1)[cite: 10].
* [cite_start]**CRITICAL LIMITATION (Visuals):** The paper's most critical finding for LGS-Science is detailed in section 4.7.5, "Limitations in Handling Visual Educational Content" (Chen et al., 2024, p. 11)[cite: 292].
* [cite_start]**Quote 1 (Graphs):** "LLMs struggled with interpreting kinematic graphs in physics problems" (Chen et al., 2024, p. 11)[cite: 293].
* [cite_start]**Quote 2 (Diagrams):** The study noted that GPT-4, while effective at algebra, "struggles with geometric questions involving visual elements like graphs and diagrams, highlighting limitations in visual comprehension" (Chen et al., 2024, p. 11)[cite: 294].

**Personal Analysis & Relevance to LGS-LLM:**
This paper is the foundational "map" for our LGS-Science topic. [cite_start]It validates that K-12 STEM is a major research area [cite: 143-147]. Its primary value is not a new method, but a **critical warning**. It proves that our main project challenge will be the visual component, which is the core of LGS Science (e.g., experiment setups, energy graphs). [cite_start]The paper confirms that standard text-based LLM prompting will fail for these questions [cite: 292-295]. Our system *must* have a discrete module to handle graph/diagram generation. [cite_start]We can, however, confidently use the prompting techniques it lists (like CoT) [cite: 148] for the *textual* part of the science question (e.g., the experiment's description).

---

### Article 2: Understanding LLM Scientific Reasoning through Promptings and Model’s Explanation on the Answers

**Full Citation (APA 7th Style):**
Rueda, A., Hassan, M. S., Perivolaris, A., Teferra, B. G., Samavi, R., Rambhatla, S., Wu, Y., Zhang, Y., Cao, B., Sharma, D., Krishnan, S., & Bhat, V. (2025). *Understanding LLM Scientific Reasoning through Promptings and Model’s Explanation on the Answers*. arXiv preprint arXiv:2505.01482v1. https://arxiv.org/html/2505.01482v1

**In-Text Citation Example:**
(Rueda et al., 2025)

**Summary of Contribution:**
This paper experimentally tests the scientific reasoning capability of GPT-4o by applying seven different prompt engineering techniques (e.g., CoT, Zero-Shot CoT, Self-Ask, Self-Consistency) to the graduate-level GPQA dataset. The paper's key contribution is that it measures not just **answer accuracy** but also **explanation quality** (i.e., the *reasoning* process) by comparing the LLM's generated explanation to the ground truth explanation using cosine similarity.

**Key Findings & Quotations:**

* **Accuracy vs. Reasoning Conflict:** The paper found that the prompt technique with the highest accuracy ("Self-Consistency" at 52.99%) was *not* the best at reasoning.
* **Quote 1:** "Self-consistency performed the second worst in explaining the answers" (Rueda et al., 2025, Abstract).
* **Quote 2:** "Simple techniques such as direct answer, CoT, and zero-shot CoT have the best scientific reasoning" (Rueda et al., 2025, Abstract).
* **Automatic Flaw Detection:** In a key finding (for question 257), the LLM identified that its own calculated answer was not among the multiple-choice options. For all prompts *except* "Direct Answer," the model **refused to select a flawed answer**.

**Personal Analysis & Relevance to LGS-LLM:**
This paper provides the core **methodology** for our LGS project. The LGS exam is a "muhakeme" (reasoning) test. This paper proves we should *not* blindly optimize for raw accuracy, as doing so may lead to poor pedagogical explanations. We should select our prompt strategy (e.g., **Zero-Shot CoT**) based on its ability to produce the best **scientific reasoning** (explanation quality), which is exactly what LGS tests. The finding on "refusing to answer" is a game-changer; it gives us a powerful, free **Quality Assurance (QA) filter**. We can automatically test our own generated questions: if the LLM refuses to answer its own question, the question is flawed and should be rejected.
