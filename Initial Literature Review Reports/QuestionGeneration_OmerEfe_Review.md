
### Initial Literature Review Log

**Researcher:** Ömer Efe Peltek 
**Date:** 09/11/2025  
**Proposed Topic Area:**  Question Generation for LGS Exams

---

## 1. Executive Synthesis & Recommendation

**Paragraph 1 – The Topic & Problem:**  
This literature review examines the use of Large Language Models (LLMs) for generating exam-style questions, focusing specifically on their potential for LGS English exams in Türkiye. The core challenge in this field is enabling models to produce **pedagogically valid**, **contextually appropriate**, and **grammar-accurate** questions that match official exam standards. Researchers are trying to bridge the gap between **free-form language generation** and **curriculum-aligned assessment** design, ensuring that automatically generated questions maintain validity and difficulty balance similar to those crafted by human teachers.

**Paragraph 2 – Comparative Analysis:**  
The first study (Akyön et al., 2022) approaches the problem through *automated question generation (QG)* from Turkish texts using mT5, focusing on linguistic structure and context extraction. In contrast, the second paper (Zeinalipour et al., 2024) explores *quiz generation* using large instruction-tuned LLMs (like GPT-4 and Llama-2), focusing on educational domain adaptation. While both agree on the efficiency and scalability of LLM-based QG, Akyön et al. emphasize **syntactic coherence** and **semantic alignment**, whereas Zeinalipour et al. highlight **prompt engineering** and **evaluation of question quality**. Together, they show that hybrid approaches—leveraging both dataset-driven and instruction-tuned strategies—yield the most reliable educational questions.

**Paragraph 3 – Recommendation for LGS-LLM:**  
For the **LGS-LLM** project, these studies confirm strong feasibility. The **first paper** offers a linguistic foundation for adapting Turkish-English mixed content, while the **second** demonstrates how large-scale LLMs can generate diverse, high-quality quiz items with minimal data. The main opportunity lies in adapting LLMs with **LGS-specific datasets** and clear question templates (reading comprehension, vocabulary, grammar). However, the main risk is **over-generalization**—models might produce grammatically correct but pedagogically invalid questions. Overall, this topic is highly viable for our project, especially with a supervised fine-tuning or reinforcement learning step to enforce LGS exam structure.

---

## 2. Annotated Bibliography & Analysis

---

### Article 1: *Automated Question Generation and Question Answering from Turkish Texts*

**Full Citation (APA 7th Style):**  
Akyön, F., Dağ, H., & Keleş, A. (2022). Automated question generation and question answering from Turkish texts. *Turkish Journal of Electrical Engineering & Computer Sciences, 30*(5), 2051–2065. https://journals.tubitak.gov.tr/elektrik/vol30/iss5/17/

**In-Text Citation Example:**  
(Akyön, Dağ, & Keleş, 2022)

**Summary of Contribution:**  
This study explores an automated system for generating and answering questions in Turkish using the multilingual T5 (mT5) model. The researchers trained and evaluated their model on Turkish reading comprehension datasets. The system automatically creates question–answer pairs, enabling data augmentation for educational applications and AI-driven assessments.

**Key Findings & Quotations:**  
- “The proposed model successfully generates syntactically coherent questions that align with Turkish grammar rules” (Akyön et al., 2022, p. 2058).  
- “mT5 demonstrated superior performance compared to traditional template-based question generation methods” (Akyön et al., 2022, p. 2062).  
- “The model can contribute to the creation of Turkish educational resources where manual question writing is costly” (Akyön et al., 2022, p. 2063).

**Personal Analysis & Relevance to LGS-LLM:**  
This paper is directly relevant because it provides a **Turkish-language foundation** for question generation models. Although it does not focus specifically on LGS or English subjects, the mT5 framework could be fine-tuned with bilingual data (Turkish–English) to create LGS-style English reading comprehension questions. A limitation is the **lack of pedagogical validation**; questions are evaluated mainly for grammar and fluency, not for exam difficulty levels. Still, this approach offers a strong baseline for our project’s data preprocessing and QG pipeline.

---

### Article 2: *Automating Turkish Educational Quiz Generation Using Large Language Models*

**Full Citation (APA 7th Style):**  
Zeinalipour, M., & Alper, B. (2024). Automating Turkish educational quiz generation using large language models. *arXiv preprint* arXiv:2406.03397. https://arxiv.org/abs/2406.03397

**In-Text Citation Example:**  
(Zeinalipour & Alper, 2024)

**Summary of Contribution:**  
This recent work introduces the “Turkish-Quiz-Instruct” dataset and examines how LLMs like GPT-4, Llama-2, and Mistral can automatically generate Turkish quiz questions. The authors test multiple prompt structures and scoring criteria, focusing on educational alignment, factual accuracy, and question diversity. Their results indicate that fine-tuned LLMs outperform both rule-based and smaller transformer models in generating meaningful assessment questions.

**Key Findings & Quotations:**  
- “Instruction-tuned models exhibit significant improvement in generating educationally relevant quiz questions” (Zeinalipour & Alper, 2024, p. 4).  
- “GPT-4 and Llama-2 achieve the highest coherence and relevance scores when evaluated by human teachers” (Zeinalipour & Alper, 2024, p. 6).  
- “Our dataset establishes a foundation for large-scale, automated Turkish quiz generation for education systems” (Zeinalipour & Alper, 2024, p. 8).

**Personal Analysis & Relevance to LGS-LLM:**  
This study directly supports the LGS-LLM project’s goals. It validates that **LLM-based question generation** can achieve educational quality close to teacher-written items. Moreover, the use of instruction-tuned prompts and teacher evaluation aligns perfectly with the structured LGS exam format. The paper’s limitation is that it primarily evaluates **general knowledge quizzes**, not language-learning tasks. However, adapting its methodology—especially prompt design and evaluation framework—could enable an English-focused LGS question generator that aligns with curriculum outcomes and CEFR levels.

---
