## EXECUTIVE SUMMARY FOR PHASE 1

**(To: Project Stakeholders)**

This document is the official control log and synthesis report for Phase 1: Initial Literature Review.

- **Objective:** To have all 15 team members research 2 sources to help define the project's scope and technical direction.
- **Methodology:** A `REPORTS_CHECK.md` log (this file) was used to track individual submissions, adherence to project protocols (coordination, naming), and academic integrity (citation validity).
- **Performance:**
  - **Submissions:** 12 out of 15 members (80%) submitted a report. 3 members (25%) failed to correctly submit.
  - **Validity:** Of the 12 submissions, 2 contained "Citation Check: NO" (unverifiable sources). This leaves **10 valid and usable reports**.
  - 
- **Key Research Findings (From Valid Reports):**
  1.  **Strategic Validation (RAG):** The research (e.g., Soner Eski, Art 2) provides strong evidence that our RAG-based approach (using lecture books) is superior to prompt-only methods.
  2.  **Strategic Validation (QA):** The research (e.g., Muhammed Göymen, Art 1; Burak Erden, Art 2) confirms that automatic evaluation is unreliable. Our plan to use a "Human-in-the-Loop" (teacher-in-the-loop) QA team is the correct methodology.
  3.  **Core Technical Challenge Identified:** The 7 valid reports unanimously identify that generating the question stem is easy. The core, unresolved challenge in all AQG systems is the generation of high-quality, plausible **distractors** (wrong answers).
- **Conclusion:** Phase 1 was a partial success. The valid reports have successfully defined our project's technical path and primary bottleneck. However, the log also revealed critical issues in team compliance and submission, which are being addressed before proceeding to Phase 2.

## Individual Performance & Grading Log

For clarity, team members are grouped by performance category.

#### Category 1: Valid & High-Value Submissions

These members successfully completed the task, adhered to academic standards, and provided the actionable intelligence summarized above. Their reports are the foundation for Phase 2.

- `Esra Gümüş` (OK)
- `Emirhan Dursun` (OK)
- `Soner Eski` (OK)
- `Muhammed Göymen` (OK)
- `Burak Can Kahraman` (OK)
- `Burak Erden` (OK)
- `Ömer Efe Gürbüz` (OK)
- `Gökhan Çağaptay` (OK)
- `Mehmet Fatih Şık` (OK)
- `Elif Eslem Özkan` (OK)

#### Category 2: Invalid Submissions (Requires Correction)

These members submitted work, but it failed a critical academic integrity check. The citations provided were not findable (`Citation Check: NO`). As such, their research is currently unusable and requires immediate correction and resubmission.

- `Serhat Çelik` (Invalid Citations)

#### Category 3: Non-Submissions / Critical Failure

These members failed to produce a usable report for Phase 1.


- `Metin Cansız` (Submission: NO)
- `Ramazan Tunç` (Submission: NO)
- `Doğukan Enes` (Submission: NO)

---

## Correction of Mistakes

Failed members can correct their report and reach out to me(Ali Bulut). This way their name can be removed form the lists above.
Though I'll not make a individual report analysis for non-submitting members.

# LGS-LLM: Review Control Log

# 1. Researcher: `Esra Gümüş` **Submission:** OK

...

# 1. **Researcher:** `Esra Gümüş` **Submission:** OK

**Report File:** `Create English – Multiple-Choice-Question-Generation_Esra_Nur_gumus.md`
**Date of Review:** `10.11.2025`

---

## 1.1. Compliance & Documentation Hygiene

This section verifies that the process was followed. This is a non-trivial check; a failure here indicates a breakdown in communication or attention to detail that must be corrected.

| **1. Coordination: Filled 'Topic Claim List' (on Trello) :** YES
| **2. Naming: File name is correct (`[Topic]_[Name]_Review.md`) :** NO, too long, prefer without space
| **3. Placement: File is in `Initial Literature Review Reports/` :** YES
| **4. Structure: Followed main template sections (1, 2, Art1, Art2) :** YES, there are 4 articles(positive), Markdown is bad on item 1.
| **5. Hygiene: Removed instructional sections (Header, Appendix, Credit) :** YES

---

## 1.2. Academic & Content Analysis

This section evaluates the _content_ of the report. This is where the value for the project is extracted.

### Article 1:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** This study aims to generate high-quality multiple-choice questions (MCQs) without a fine-tuning dataset (zero-shot)

In experimental results, AGenT Zero performed better in three out of four metrics compared to T5-based paraphrase methods

- **Reviewer Synthesis (Utility to LGS-LLM):** Similar to our methodolgy.

### Article 2:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** The article presents a hybrid method aiming to generate three adequate distractors for a given question-answer pair. It combines rule-based NLP, WordNet, embedding similarities, and edit-distance techniques, achieving high accuracy with human evaluation.
  Distractor generation is a critical component of MCQ quality
- **Reviewer Synthesis (Utility to LGS-LLM):** Distraction generation. Very Important for our case.

### Article 3:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** This paper presents a survey of automatic question generation and assessment strategies from textual and pictorial learning resources.

The survey presents a comprehensive picture of the field and brings to the forefront the identified data/labeling deficiency for LGS.

- **Reviewer Synthesis (Utility to LGS-LLM):** Survey, Pictorial learning might be interesting

### Article 4:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** This paper presents an end-to-end pipeline for automatic MCQ generation from middle school textbooks:

preprocessing → sentence/key selection → question formulation → distractor generation → difficulty assessment.

Tested on NCERT middle school textbooks, results evaluated by human experts are included in the article.
"The Textbook → MCQ pipeline is the closest real-world approach for LGS-like exams at the middle school level."

- **Reviewer Synthesis (Utility to LGS-LLM):** Same target group. Research is super valuable for our case.

---

# 2. **Researcher:** `Emirhan Sevimli` **Submission:** OK

**Report File:** `IELTS-QuestionGeneration_EmirhanSevimli_Review.md`
**Date of Review:** `10.11.2025`

---

## 2.1. Compliance & Documentation Hygiene

This section verifies that the process was followed. This is a non-trivial check; a failure here indicates a breakdown in communication or attention to detail that must be corrected.

| **1. Coordination: Filled 'Topic Claim List' (on Trello) :** YES
| **2. Naming: File name is correct (`[Topic]_[Name]_Review.md`) :** YES, too long, prefer without space
| **3. Placement: File is in `Initial Literature Review Reports/` :** YES
| **4. Structure: Followed main template sections (1, 2, Art1, Art2) :** YES
| **5. Hygiene: Removed instructional sections (Header, Appendix, Credit) :** YES

---

## 2.2. Academic & Content Analysis

This section evaluates the _content_ of the report. This is where the value for the project is extracted.

### Article 1:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** Analysis of sample essays. Categorization of topics. Thematic map of IELTS essay prompts.
  IELTS question themes are highly structured. This offers a good opportunity for building an AI system capable of generating new questions based on topic frequencies.

- **Reviewer Synthesis (Utility to LGS-LLM):** Mapping of essay prompts.Topic is about IELTS. Usable when we talk about works in other exams.

### Article 2:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** The author analyzed essays from multiple learner corpora and developed NLP-based models to predict proficiency levels.
  It also suggests that even without deep model training, feature-based approaches yield useful results—important for teams with limited computational resources.
- **Reviewer Synthesis (Utility to LGS-LLM):** Analysis and development. Useful to cite when talking about our limited computational resources.

---

# 3. **Researcher:** `Soner Eski` **Submission:** OK

**Report File:** `LGS English–Math Question Generation_SonerEski_Review.md`
**Date of Review:** `11.11.2025`

---

## 3.1. Compliance & Documentation Hygiene

This section verifies that the process was followed. This is a non-trivial check; a failure here indicates a breakdown in communication or attention to detail that must be corrected.

| **1. Coordination: Filled 'Topic Claim List' (on Trello) :** YES
| **2. Naming: File name is correct (`[Topic]_[Name]_Review.md`) :** YES, too long, prefer without space
| **3. Placement: File is in `Initial Literature Review Reports/` :** YES
| **4. Structure: Followed main template sections (1, 2, Art1, Art2) :** YES
| **5. Hygiene: Removed instructional sections (Header, Appendix, Credit) :** YES

---

## 3.2. Academic & Content Analysis

This section evaluates the _content_ of the report. This is where the value for the project is extracted.

### Article 1:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** a system that uses ChatGPT to generate English reading comprehension exercises for Chinese middle school students.
  The results show that ChatGPT’s passages are in many respects comparable to, or even better than, human-written passages. However, the multiple-choice questions still need improvement, especially in terms of the quality of the distractors.

- **Reviewer Synthesis (Utility to LGS-LLM):** Similar target group different base language. Useful to cite when talking about other country works.

### Article 2:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** This paper develops four different GPT-4o-based methods for generating mathematics questions aligned with the Malaysian secondary school curriculum.
  The generated questions are evaluated with semantic similarity analyses that measure how closely they match the official learning objectives, and with an additional validation step (RAG-QA) that checks whether the questions can actually be answered using the curriculum materials.
  The results show that RAG-based methods perform much better than prompt-only methods in terms of both curriculum alignment and content correctness.
- **Reviewer Synthesis (Utility to LGS-LLM):** Very valuable for the project. Similar target group different base language. Similar method RAG. A lot to learn from this.

---

## 3.3. Reviewer's Note

- **Overall Topic Viability:** Both are focused on same target group but on different base languages. Very valuable works for our project.

# 4. **Researcher:** `Muhammed Göymen` **Submission:** OK

**Report File:** `LGS-AQG_MuhammedGoymen_Review.md`
**Date of Review:** `11.11.2025`

---

## 4.1. Compliance & Documentation Hygiene

This section verifies that the process was followed. This is a non-trivial check; a failure here indicates a breakdown in communication or attention to detail that must be corrected.

| **1. Coordination: Filled 'Topic Claim List' (on Trello) :** YES
| **2. Naming: File name is correct (`[Topic]_[Name]_Review.md`) :** YES
| **3. Placement: File is in `Initial Literature Review Reports/` :** YES
| **4. Structure: Followed main template sections (1, 2, Art1, Art2) :** YES , needs improvement with md structure.
| **5. Hygiene: Removed instructional sections (Header, Appendix, Credit) :** YES

---

## 4.2. Academic & Content Analysis

This section evaluates the _content_ of the report. This is where the value for the project is extracted.

### Article 1:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** survey 37 papers on automatic question generation (AQG) published between 2013 and 2018 to map how systems are evaluated
  Diverse and non-standardized evaluation practices in AQG make it difficult to compare systems across studies
  For LGS-style question generation, this survey is a strong warning against relying solely on automatic metrics.

- **Reviewer Synthesis (Utility to LGS-LLM):** Explains how it's hard to do a survey because there are no common framework. Also criticizes about the evaluation metrics. Useful for us on evaluation phase

### Article 2:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** This survey reviews techniques for automatic question generation and automated answer assessment, spanning rule-based, template-driven, semantic, and neural approaches, and links them to self-learning and self-assessment paradigms

Incorporating answer assessment allows iterative refinement: generated question -> model simulates student answers -> calibration of difficulty and discrimination -> accept or revise. For Turkish LGS contexts, building a concept map / skill taxonomy and attaching it to generation prompts can constrain semantic drift and ensure syllabus alignment.

- **Reviewer Synthesis (Utility to LGS-LLM):** Very valuable for the project. Similar target group different base language. Similar method RAG. A lot to learn from this.

---

## 4.3. Reviewer's Note

- **Overall Topic Viability:** Second article is strange, it talks about incorporating answer to refine iteratively.
  Might not work well with our case but its a good research.

# 5. **Researcher:** `Burak Can Kahraman` **Submission:** OK

**Report File:** `LGS-LLM_Mathematics – Word Problems (LGS) & Turkish – Reading Comprehension_Review_BurakCanKahraman.md`
**Date of Review:** `11.11.2025`

---

## 5.1. Compliance & Documentation Hygiene

This section verifies that the process was followed. This is a non-trivial check; a failure here indicates a breakdown in communication or attention to detail that must be corrected.

| **1. Coordination: Filled 'Topic Claim List' (on Trello) :** YES
| **2. Naming: File name is correct (`[Topic]_[Name]_Review.md`) :** YES, too long, prefer without space
| **3. Placement: File is in `Initial Literature Review Reports/` :** YES
| **4. Structure: Followed main template sections (1, 2, Art1, Art2) :** YES
| **5. Hygiene: Removed instructional sections (Header, Appendix, Credit) :** YES

---

## 5.2. Academic & Content Analysis

This section evaluates the _content_ of the report. This is where the value for the project is extracted.

### Article 1:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** compiles a dataset of German multiple‑choice reading‑comprehension (MCRC) items and introduces a human+automatic evaluation protocol built around text informativity—defined as answerability with passage minus guessability without passage.
  Human‑authored, Llama‑2, and GPT‑4 items are compared. GPT‑4 performs strongly both as generator and automatic evaluator, though some generated items remain susceptible to passage‑independent answering.

GPT‑4 aligns well with human ratings as an automatic evaluator; Llama‑2 requires more careful thresholding and prompt control.

- **Reviewer Synthesis (Utility to LGS-LLM):** Evaluation protocol can be useful. Information about the models are very valuable

### Article 2:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** The authors present an end‑to‑end MWP generation framework

- **Reviewer Synthesis (Utility to LGS-LLM):** Using llm to check solvability is a good idea

---

## 5.3. Reviewer's Note

- **Overall Topic Viability:** Very useful topics in regards of evaluation.

---

# 6. **Researcher:** `Burak Erden` **Submission:** OK

**Report File:** `LGS-QuestionGeneration_BurakErden_Review.md`
**Date of Review:** `11.11.2025`

---

## 6.1. Compliance & Documentation Hygiene

This section verifies that the process was followed. This is a non-trivial check; a failure here indicates a breakdown in communication or attention to detail that must be corrected.

| **1. Coordination: Filled 'Topic Claim List' (on Trello) :** YES
| **2. Naming: File name is correct (`[Topic]_[Name]_Review.md`) :** YES
| **3. Placement: File is in `Initial Literature Review Reports/` :** YES
| **4. Structure: Followed main template sections (1, 2, Art1, Art2) :** YES, addition 3 and 4
| **5. Hygiene: Removed instructional sections (Header, Appendix, Credit) :** YES

---

## 6.2. Academic & Content Analysis

This section evaluates the _content_ of the report. This is where the value for the project is extracted.

### Article 1:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** eğitim metinlerinden otomatik olarak çoktan seçmeli sorular üreten QGen adlı modüler bir sistem sunmaktadır. Sistem, soru üretimi (T5 / InstructGPT), cevap çıkarımı (RoBERTa / InstructGPT) ve distractor üretimi için hibrit yöntemler kullanır.

T5 modelleri dilsel akıcılık açısından güçlü sonuçlar vermiştir.

Cevap çıkarımında EM ≈ 0.64 ve F1 ≈ 0.84 skorları elde edilmiştir; bu değerler makul ve uygulanabilir seviyededir.
Distractor üretiminde hibrit yaklaşım (sense2vec + LLM) ~%58 kabul edilebilir kalite sağlamıştır.

- **Reviewer Synthesis (Utility to LGS-LLM):** We can learn from QGen system

### Article 2:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** Bu çalışma, ChatGPT gibi büyük dil modellerinin doğrudan kullanılmasından ziyade, dikkatle tasarlanmış prompt şablonları ve öğretmen-in-the-loop doğrulama süreçlerinin, soru üretim kalitesini artırdığını göstermektedir.

öğretmen kontrollü geri bildirim döngüsü

- **Reviewer Synthesis (Utility to LGS-LLM):** Super valuable and in line with our project.

---

## 6.3. Reviewer's Note

- **Overall Topic Viability:** Great sources for our project. we will check this sources again for sure.

# 7. **Researcher:** `Ömer Efe Peltek` **Submission:** OK

**Report File:** `QuestionGeneration_OmerEfe_Review.md`
**Date of Review:** `11.11.2025`

---

## 7.1. Compliance & Documentation Hygiene

This section verifies that the process was followed. This is a non-trivial check; a failure here indicates a breakdown in communication or attention to detail that must be corrected.

| **1. Coordination: Filled 'Topic Claim List' (on Trello) :** NO
| **2. Naming: File name is correct (`[Topic]_[Name]_Review.md`) :** YES
| **3. Placement: File is in `Initial Literature Review Reports/` :** YES
| **4. Structure: Followed main template sections (1, 2, Art1, Art2) :** YES
| **5. Hygiene: Removed instructional sections (Header, Appendix, Credit) :** YES

---

## 7.2. Academic & Content Analysis

This section evaluates the _content_ of the report. This is where the value for the project is extracted.

### Article 1:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** This study explores an automated system for generating and answering questions in Turkish using the multilingual T5 (mT5) model.

mT5 demonstrated superior performance compared to traditional template-based question generation methods

- **Reviewer Synthesis (Utility to LGS-LLM):** Valuable info about T5 model.

### Article 2:

- **Citation Check (Full):** OK
- **Reviewer Synthesis (What is this paper about?):** This recent work introduces the “Turkish-Quiz-Instruct” dataset and examines how LLMs like GPT-4, Llama-2, and Mistral can automatically generate Turkish quiz questions.

Their results indicate that fine-tuned LLMs outperform both rule-based and smaller transformer models in generating meaningful assessment questions.

- **Reviewer Synthesis (Utility to LGS-LLM):** Seems outdated with the phrase fine tuned LLMS outperform. More recent studies show otherwise

---

## 7.3. Reviewer's Note

- **Overall Topic Viability:** Info about T5 model.

# 8. **Researcher:** `Gökhan Çağaptay` ### **Submission:** NO - Empty file.

**Report File:** `Science-STEM_GokhanCagaptay_Review.md`
**Date of Review:** `11.11.2025`

---

## 8.1. Compliance & Documentation Hygiene

This section verifies that the process was followed. This is a non-trivial check; a failure here indicates a breakdown in communication or attention to detail that must be corrected.

| **1. Coordination: Filled 'Topic Claim List' (on Trello) :**
| **2. Naming: File name is correct (`[Topic]_[Name]_Review.md`) :**
| **3. Placement: File is in `Initial Literature Review Reports/` :**
| **4. Structure: Followed main template sections (1, 2, Art1, Art2) :**
| **5. Hygiene: Removed instructional sections (Header, Appendix, Credit) :**

---

## 8.2. Academic & Content Analysis

This section evaluates the _content_ of the report. This is where the value for the project is extracted.
The research identifies and categorizes the prompting strategies employed (e.g., Simple, Role-Assigned, Zero-Shot, Few-Shot, Chain-of-Thought)

### Article 1:

- **Citation Check (Full):** YES
- **Reviewer Synthesis (What is this paper about?):** This paper is a comprehensive systematic review that analyzes 30 studies

- **Reviewer Synthesis (Utility to LGS-LLM):** Important for our prompting strategies.

### Article 2:

- **Citation Check (Full):** YES
- **Reviewer Synthesis (What is this paper about?):** This paper experimentally tests the scientific reasoning capability of GPT-4o by applying seven different prompt engineering techniques (e.g., CoT, Zero-Shot CoT, Self-Ask, Self-Consistency) to the graduate-level GPQA dataset.

The paper's key contribution is that it measures not just _answer accuracy_ but also _explanation quality_ (i.e., the reasoning process) by comparing the LLM's generated explanation to the ground truth explanation using cosine similarity.

- **Reviewer Synthesis (Utility to LGS-LLM):** Both of the sources are quite important for our research especially in prompt engineering

---

## 8.3. Reviewer's Note

- **Overall Topic Viability:**

# 9. **Researcher:** `Serhat Çelik` **Submission:** OK

**Report File:** `SocialStudies-ReadingComprehension_SerhatCelik_Review.md`
**Date of Review:** `11.11.2025`

---

## 9.1. Compliance & Documentation Hygiene

This section verifies that the process was followed. This is a non-trivial check; a failure here indicates a breakdown in communication or attention to detail that must be corrected.

| **1. Coordination: Filled 'Topic Claim List' (on Trello) :** NO
| **2. Naming: File name is correct (`[Topic]_[Name]_Review.md`) :** YES, too long
| **3. Placement: File is in `Initial Literature Review Reports/` :** YES
| **4. Structure: Followed main template sections (1, 2, Art1, Art2) :** YES
| **5. Hygiene: Removed instructional sections (Header, Appendix, Credit) :** YES

---

## 9.2. Academic & Content Analysis

This section evaluates the _content_ of the report. This is where the value for the project is extracted.

### Article 1:

- **Citation Check (Full):** NO
- **Reviewer Synthesis (What is this paper about?):** examines how question design strategies can improve reading comprehension in Social Studies courses

The language used in question stems determines the student’s cognitive engagement level

- **Reviewer Synthesis (Utility to LGS-LLM):** Study is reliant on human insight

### Article 2:

- **Citation Check (Full):** NO
- **Reviewer Synthesis (What is this paper about?):** This study assesses GPT-4 and similar models on reasoning tasks involving historical events and temporal causality.

While LLMs demonstrate factual recall, they struggle with reasoning over temporal causality in historical narratives

- **Reviewer Synthesis (Utility to LGS-LLM):** Seems outdated

---

## 9.3. Reviewer's Note

- **Overall Topic Viability:** Both papers seems unusable in our research. Also citations are done with confidence but I wasn't able to find the sources.

# 10. **Researcher:** `Elif Eslem Özkan` **Submission:** OK

**Report File:** `Turkish-SözelMantık_ElifEslem_Review.md`
**Date of Review:** `11.11.2025`

---

## 10.1. Compliance & Documentation Hygiene

This section verifies that the process was followed. This is a non-trivial check; a failure here indicates a breakdown in communication or attention to detail that must be corrected.

| **1. Coordination: Filled 'Topic Claim List' (on Trello) :** YES
| **2. Naming: File name is correct (`[Topic]_[Name]_Review.md`) :** YES, too long
| **3. Placement: File is in `Initial Literature Review Reports/` :** YES
| **4. Structure: Followed main template sections (1, 2, Art1, Art2) :** YES
| **5. Hygiene: Removed instructional sections (Header, Appendix, Credit) :** YES

---

## 10.2. Academic & Content Analysis

This section evaluates the _content_ of the report. This is where the value for the project is extracted.

### Article 1:

- **Citation Check (Full):** NO
- **Reviewer Synthesis (What is this paper about?):** This research proposes a method for generating questions where the complexity and topic are tightly controlled using "structure-aware keywords."
  The study validates that explicitly defining the desired reasoning structure (e.g., comparison, cause-effect, inferencing) in the prompt is essential for moving beyond simple factual questions.

This paper provides the technical mechanism for creating "new-generation" LGS questions.

- **Reviewer Synthesis (Utility to LGS-LLM):** Important for promp generation

### Article 2:

- **Citation Check (Full):** NO
- **Reviewer Synthesis (What is this paper about?):** This comprehensive survey meticulously reviews the state-of-the-art techniques used to automatically generate distractors (incorrect options) for multiple-choice questions using Natural Language Processing (NLP).

The authors categorize existing methods

While question stem generation is mature, the core bottleneck of Automated Question Generation (AQG) systems remains the creation of high-quality, plausible distractors"

- **Reviewer Synthesis (Utility to LGS-LLM):** Veery important for creation of distractors

---

## 10.3. Reviewer's Note

- **Overall Topic Viability:** Both papers are valuable for our question generation.

# 11. **Researcher:** `Mehmet Fatih Şık` **Submission:** NO

# 12. **Researcher:** `Metin Cansız` **Submission:** NO

# 13. **Researcher:** `Ramazan Tunç` **Submission:** NO

# 14. **Researcher:** `Doğukan Enes` **Submission:** NO
