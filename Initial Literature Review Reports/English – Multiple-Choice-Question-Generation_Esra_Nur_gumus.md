First Literature Review Journal

Researcher: Esra Nur Gümüş Date: November 9, 2025
Proposed Subject Area: English – Multiple-Choice Question Generation (LGS Style)

### **Executive Synthesis and Recommendation**

**Paragraph 1: Topic and Problem**
Our project focuses on **generating multiple-choice questions (MCQs) for the LGS English course that are similar to past exam questions**. Research indicates that the primary challenges in automatic question generation include **data scarcity**, **distractor quality**, and **suitability for the exam level**. For instance, although Li et al. (2020) attempted to reduce data costs with zero-shot methods, adaptation to LGS-like language and level remained limited. Similarly, Das et al.'s (2021) survey highlights the lack of pedagogical metadata in existing datasets and the absence of suitable labeling for the middle school level. These two sources reveal that data and level alignment issues are critical in automatic question generation.

---

**Paragraph 2: Comparative Analysis**
Four sources offer different but complementary approaches to the problem of LGS-like question generation. Li et al. (2020) focus on **rapid prototyping with zero-shot pre-trained models**, while Zhang et al. (2020) present **hybrid methods to improve distractor quality**; both emphasize the critical components that determine question quality (question stem and distractors). Rao & Saha (2023), on the other hand, offer directly applicable solutions at the middle school level through a **textbook-based pipeline**; Das et al. (2021) provide a **literature review and dataset guide**, indicating which data and evaluation methods are appropriate. A common theme across all studies is the risk of **lack of human evaluation and pedagogical suitability in automatic MCQ generation**. The differences lie in their methods: Li et al. and Rao & Saha are more model/pipeline-oriented, while Zhang et al. and Das et al. are more data and quality control-oriented.

---

**Paragraph 3: Recommendation for LGS-LLM**
In light of these four articles, our project appears highly applicable for LGS English question generation. The **primary opportunity** is the possibility of rapid prototyping and middle school-level question generation using the **textbook-based pipeline and zero-shot models** presented by Rao & Saha (2023) and Li et al. (2020). The **primary risk**, as shown by Li et al. (2020) and Zhang et al. (2020), is that **distractor quality and level alignment require additional filtering and human validation specifically for LGS**. The proposed approach: first generate prototype questions with Li et al.'s zero-shot or Rao & Saha's pipeline, then optimize distractors with a Zhang-style distractor module, and finally add human-in-the-loop pedagogical evaluation guided by Das et al. This method will enable both rapid and high-quality generation of LGS-style English questions.
                                                                                                                                                                       2. Annotated Bibliography and Analysis
                                                                                                                                                             ## Item 1: AGenT Zero: Zero-shot Automatic Multiple-Choice Question Generation for Skill Assessments

**Full Citation (APA 7):**
Li, X., Chen, Y., & Liu, Q. (2020). *AGenT Zero: Zero-shot automatic multiple-choice question generation for skill assessments*. *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020)*, 3456–3465. [https://doi.org/10.18653/v1/2020.acl-main.315](https://doi.org/10.18653/v1/2020.acl-main.315)

**In-text Citation Example:**
(Li, Chen, & Liu, 2020) or **Li et al. (2020)**

**Contribution Summary:**
This study aims to generate high-quality multiple-choice questions (MCQs) without a fine-tuning dataset (zero-shot). The pipeline uses pre-trained models to generate question stems, correct answers, and distractors; the goal is to minimize data collection costs. In experiments, AGenT Zero demonstrates superiority in fluency and semantic similarity compared to other pre-trained methods.

**Key Findings and Quotes:**

* “Our pipeline, which we call AGenT Zero, consists of only pre-trained models and requires no fine-tuning, minimizing data acquisition costs for question generation.” (Li et al., 2020, p. 1)
* “AGenT Zero successfully outperforms other pre-trained methods in fluency and semantic similarity.” (Li et al., 2020, p. 1)
* In experimental results, AGenT Zero performed better in three out of four metrics compared to T5-based paraphrase methods (Li et al., 2020, p. 5).

**Personal Analysis and Relationship with LGS-LLM:**

* Zero-shot strategies provide a practical and strong starting point in situations where data collection costs are high.
* Limitations: Additional fine-tuning or prompt engineering will be required to adapt to the LGS-Turkish language level and terminology; distractor quality must be controlled.
* Contribution to our project: Suitable for rapid prototyping and initial examples of LGS-like questions. Output filters should be used to control level and vocabulary.

---

## Item 2: Generating Adequate Distractors for Multiple-Choice Questions

**Full Citation (APA 7):**
Zhang, Y., Yuan, T., & Wang, S. (2020). *Generating adequate distractors for multiple-choice questions using semantic similarity and word embeddings*. *Proceedings of the 12th International Conference on Educational Data Mining (EDM 2020)*, 412–423.

**In-text Citation Example:**
(Zhang, Yuan, & Wang, 2020) or **Zhang et al. (2020)**

**Contribution Summary:**
The article presents a hybrid method aiming to generate three adequate distractors for a given question-answer pair. It combines rule-based NLP, WordNet, embedding similarities, and edit-distance techniques, achieving high accuracy with human evaluation.

**Key Findings and Quotes:**

* “We use the US SAT practice reading tests ... each MCQ has at least one adequate distractor and 84% of MCQs have three adequate distractors.” (Zhang et al., 2020, p. 1)
* “An adequate distractor must satisfy: (1) incorrect answer; (2) grammatically correct and consistent with the article; (3) semantically related to the correct answer; and (4) provide distraction so that the correct answer could be identified only with some understanding of the underlying article.” (Zhang et al., 2020, p. 1)
* The article reports achieving high success by applying different strategies based on types (numerical, named entity, general noun/phrase) (Zhang et al., 2020, pp. 2–4).

**Personal Analysis and Relationship with LGS-LLM:**

* Distractor generation is a critical component of MCQ quality; this hybrid approach is practical and powerful.
* Limitations: The study was tested with SAT-level data; adaptation to the LGS-middle school level may be required.
* Contribution to our project: Zhang's methods can be directly used for distractor quality; a pipeline combining retrieval + rule filter + LLM-paraphrase can be established.

---

## Item 3: Automatic Question Generation and Answer Assessment: A Survey

**Full Citation (APA 7):**
Das, B., Majumder, M., Phadikar, S., Sekh, A. A., et al. (2021). *Automatic question generation and answer assessment: a survey*. *Research and Practice in Technology Enhanced Learning, 16*, Article 5. [https://doi.org/10.1186/s41039-021-00151-1](https://doi.org/10.1186/s41039-021-00151-1)

**In-text Citation Example:**
(Das, Majumder, Phadikar, & Sekh, 2021) or **Das et al. (2021)**

**Contribution Summary:**
This is a comprehensive review study; it summarizes automatic question generation and answer assessment methods, used datasets, and open problems. It covers objective and subjective question types, visual and auditory modalities; gaps in the literature and future research directions are discussed.

**Key Findings and Quotes:**

* “This paper presents a survey of automatic question generation and assessment strategies from textual and pictorial learning resources.” (Das et al., 2021, p. 1)
* Limitations of existing datasets for educational assessment purposes and the lack of pedagogical metadata are highlighted (Das et al., 2021, pp. 4–6).
* “Limited research works found in the literature that focused on subjective question generation ...” (Das et al., 2021, p. 5)

**Personal Analysis and Relationship with LGS-LLM:**

* The survey presents a comprehensive picture of the field and brings to the forefront the identified data/labeling deficiency for LGS.
* Limitations: Does not propose new methods; provides systematic information on datasets and evaluation criteria.
* Contribution to our project: Datasets like RACE, CK-12, LearningQ can be used as a starting point; LGS-specific labeling (topic, learning outcome, difficulty) can be added; human evaluation and pedagogical rubric are needed.

---

## Item 4: Generation of Multiple-Choice Questions From Textbook Contents of School-Level Subjects

**Full Citation (APA 7):**
Rao, D. R. C. H., & Saha, S. K. (2023). *Generation of multiple-choice questions from textbook contents of school-level subjects*. *IEEE Transactions on Learning Technologies, 16*(1), 40–52. [https://doi.org/10.1109/TLT.2022.3224232](https://doi.org/10.1109/TLT.2022.3224232)

**In-text Citation Example:**
(Rao & Saha, 2023)

**Contribution Summary:**
This paper presents an end-to-end pipeline for automatic MCQ generation from middle school textbooks: preprocessing → sentence/key selection → question formulation → distractor generation → difficulty assessment. Tested on NCERT middle school textbooks, results evaluated by human experts are included in the article.

**Key Findings and Quotes:**

* “The proposed pipeline … is partially subject-independent and is evaluated using NCERT India textbooks for three subjects; experimental results demonstrate that generated questions could be useful in real examination.” (Rao & Saha, 2023; summary source)
* Four main modules (preprocessing, sentence selection, key selection, distractor generation) produce practically usable questions (Rao & Saha, 2023; summary).

**Personal Analysis and Relationship with LGS-LLM:**

* The Textbook → MCQ pipeline is the closest real-world approach for LGS-like exams at the middle school level.
* Limitations: NCERT textbooks are in the Indian context; for LGS-Turkey, alignment with MEB (Ministry of National Education) learning outcome lists, terminology, and language level is required. Full text access is limited; detailed parameters are missing.
* Contribution to our project: Adapting the pipeline with MEB-sourced preprocessing and key-selection is ideal for LGS-like questions.
