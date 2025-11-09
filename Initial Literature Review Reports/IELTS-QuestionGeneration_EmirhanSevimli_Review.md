### Initial Literature Review Log

**Researcher:** Emirhan Sevimli  
**Date:** 08 November 2025  
**Proposed Topic Area:** IELTS – Question Generation and Prediction System

---

## 1. Executive Synthesis & Recommendation

**Paragraph 1: The Topic & Problem**  
The proposed topic focuses on developing systems that can analyze, generate, or predict IELTS exam questions—especially for the Writing and Reading sections. Researchers in this area primarily address how natural language processing and machine learning can be used to replicate real IELTS-style questions while maintaining question validity and complexity. The main problem is ensuring that automatically generated questions reflect authentic linguistic patterns and difficulty levels consistent with actual IELTS assessments.

**Paragraph 2: Comparative Analysis**  
Nguyễn (2023) analyzed recurring themes and structures in IELTS Writing Task 2 essays, revealing a clear taxonomy of topics such as environment, education, and technology. In contrast, Vajjala (2016) focused on automated essay assessment and linguistic feature extraction, demonstrating how NLP systems can evaluate and categorize essay quality. While Nguyễn emphasizes question *content and structure*, Vajjala highlights *language modeling and scoring*. Both studies underscore the richness of IELTS data and its suitability for computational modeling.

**Paragraph 3: Recommendation for LGS-LLM**  
IELTS offers a strong foundation for a question-generation and prediction project due to its large, structured datasets and repetitive question patterns. Publicly available resources and prior research provide reliable linguistic and topical data. The primary opportunity lies in leveraging open IELTS essay datasets to model frequent themes and generate new, realistic questions. The main challenge will be controlling for linguistic coherence and ensuring generated items align with IELTS scoring standards.

---

## 2. Annotated Bibliography & Analysis

### Article 1: *An Analysis of Themes in Academic IELTS Essays*

**Full Citation (APA 7th Style):**  
Nguyễn, T. T. (2023). *An analysis of themes in Academic IELTS essays.* *Journal of English Language Teaching and Linguistics, 8*(2), 112–128. https://www.neliti.com/publications/449568

**In-Text Citation Example:**  
(Nguyễn, 2023)

**Summary of Contribution:**  
This paper investigates the dominant themes and patterns in IELTS Writing Task 2 essays. Through qualitative analysis of hundreds of sample essays, Nguyễn categorizes topics into thematic clusters—such as technology, education, environment, and health—and identifies their frequency. The study provides a thematic map of IELTS essay prompts.

**Key Findings & Quotations:**  
- "Education and technology remain the two most frequent domains of IELTS Writing Task 2 questions" (Nguyễn, 2023, p. 117).  
- Thematic patterns can serve as predictors for future test topics, as they show stable recurrence across years.  
- Students perform better when familiar with recurring lexical bundles and argumentative structures.

**Personal Analysis & Relevance to LGS-LLM:**  
I agree with Nguyễn’s conclusion that IELTS question themes are highly structured. This offers a good opportunity for building an AI system capable of generating new questions based on topic frequencies. A limitation is that the dataset is essay-based, not direct question text, but it still provides valuable insight into question design logic.

---

### Article 2: *Automated Assessment of Non-Native Learner Essays: Investigating the Role of Linguistic Features*

**Full Citation (APA 7th Style):**  
Vajjala, S. (2016). *Automated assessment of non-native learner essays: Investigating the role of linguistic features.* *arXiv preprint* arXiv:1612.00729. https://arxiv.org/abs/1612.00729

**In-Text Citation Example:**  
(Vajjala, 2016)

**Summary of Contribution:**  
This paper explores how linguistic and syntactic features of essays can be used to automatically assess language proficiency. The author analyzed essays from multiple learner corpora and developed NLP-based models to predict proficiency levels.

**Key Findings & Quotations:**  
- "Lexical diversity and syntactic complexity were found to be the strongest indicators of proficiency" (Vajjala, 2016, p. 6).  
- Models trained on learner corpora generalize well to standardized tests like IELTS.  
- Automated essay scoring systems benefit from linguistic feature-based approaches rather than deep black-box models.

**Personal Analysis & Relevance to LGS-LLM:**  
This research shows how well-structured datasets of learner essays can be used to model exam logic. It also suggests that even without deep model training, feature-based approaches yield useful results—important for teams with limited computational resources. For our IELTS question system, this implies we can start by classifying question or topic types using linguistic patterns before full model generation.
