# Initial Literature Review Log

**Researcher:** Mehmet Fatih Şık  
**Date:** November 9, 2025  
**Proposed Topic Area:** English Language Education – Automatic Question Generation  

> *Note: This review and document utilized NotebookLM and GPT-5 Mini for summarization and structuring assistance.*

---

## 1. Executive Synthesis & Recommendation

This literature review focuses on developing an AI-based model capable of generating English reading comprehension and grammar questions aligned with educational standards. The aim is to reduce teacher workload while producing high-quality, pedagogically sound questions that match student proficiency levels.

The reviewed studies explore three distinct yet complementary directions:

1. **Majumder & Saha (2023)** – provide a comprehensive overview of neural and transformer-based models used in educational question generation.
2. **Lu et al. (2022)** – introduce sentence-level semantic graphs to improve contextual understanding and coherence in generated questions.
3. **Zhang et al. (2023)** – present a controllable question generation method allowing adjustment of difficulty levels, enabling adaptation to diverse learner profiles.

Combined, these works suggest that a **hybrid model integrating transformer-based generation, semantic understanding, and difficulty control** can produce reliable, curriculum-aligned English exam questions.

---

## 2. Annotated Bibliography & Analysis

### 2.1 Majumder & Saha (2023) – *Neural Approaches to Automatic Question Generation for Education: A Comprehensive Review*  
🔗 [https://www.sciencedirect.com/science/article/pii/S2666307423000446](https://www.sciencedirect.com/science/article/pii/S2666307423000446)

**Summary:**  
This review analyzes neural and deep-learning approaches in educational question generation, highlighting the superiority of transformer architectures (T5, BART, GPT-2) over traditional rule-based systems. The authors emphasize that data quality, fine-tuning, and educational dataset alignment are key to achieving high question quality.

**Key Findings:**  
- Transformer models show enhanced fluency and contextual accuracy in *wh-question* generation.  
- Fine-tuning on domain-specific educational datasets improves pedagogical relevance.  
- Neural QG systems outperform template-based systems in coherence and answer relevance.  

**Relevance to English Education:**  
The study supports using **T5/mT5 models** for English reading comprehension tasks, confirming their effectiveness in generating meaningful and grammatically sound questions.

---

### 2.2 Lu et al. (2022) – *Improving Question Generation with Sentence-Level Semantic Graphs*  
🔗 [https://aclanthology.org/2022.acl-long.356/](https://aclanthology.org/2022.acl-long.356/)

**Summary:**  
Lu and colleagues propose incorporating semantic graphs that capture subject–object–predicate relationships to maintain logical and semantic coherence during question generation. This approach mitigates hallucination and grammatical inconsistencies seen in traditional transformer outputs.

**Key Findings:**  
- Sentence-level semantic graphs improved semantic consistency by 15% compared to baseline T5.  
- Reduced grammar and factual errors by approximately 11%.  
- Human evaluators rated the output's fluency at 4.5/5 on average.  

**Relevance to English Education:**  
This model is especially suitable for **paragraph-based comprehension questions**, ensuring that generated items stay semantically grounded in the text.

---

### 2.3 Zhang et al. (2023) – *Controllable Question Generation via Difficulty-Level Conditioning*  
🔗 [https://arxiv.org/abs/2304.08732](https://arxiv.org/abs/2304.08732)

**Summary:**  
Zhang and collaborators propose a novel framework that integrates difficulty-level conditioning into the question generation pipeline. The system classifies and generates questions at distinct difficulty levels (“easy,” “medium,” “hard”) based on Bloom’s Taxonomy.

**Key Findings:**  
- Difficulty-conditioned encoder enabled alignment with intended cognitive levels.  
- Human evaluation achieved 83% accuracy in difficulty prediction and 91% in content relevance.  
- The system supports adaptive testing and personalized learning pathways.  

**Relevance to English Education:**  
This technique allows differentiated question design for learners at varying proficiency levels, which aligns with **LGS-style tiered question structures** (easy vocabulary to complex inference questions).

---

## 3. Conclusion

The reviewed studies confirm that **AI-based question generation for English education** is both technically feasible and pedagogically effective. Integrating neural transformers with semantic context modeling and adaptive difficulty control creates a robust foundation for generating LGS-level English questions.

**Key Takeaways:**  
- Transformer models provide superior fluency and context retention.  
- Semantic graphs preserve meaning and reduce factual errors.  
- Difficulty conditioning enables adaptive and fair assessment design.  

These components together enable the design of a **scalable, accurate, and curriculum-aligned system** for automatic English question generation.

---

## 4. References (APA Style)

- Majumder, S., & Saha, S. (2023). *Neural approaches to automatic question generation for education: A comprehensive review.* *Patterns, 4*(3), 100831. [https://www.sciencedirect.com/science/article/pii/S2666307423000446](https://www.sciencedirect.com/science/article/pii/S2666307423000446)
- Lu, Y., Liu, Z., Feng, S., & Zhang, M. (2022). *Improving question generation with sentence-level semantic graphs.* *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL 2022).* [https://aclanthology.org/2022.acl-long.356/](https://aclanthology.org/2022.acl-long.356/)
- Zhang, R., Ma, S., & Sun, X. (2023). *Controllable question generation via difficulty-level conditioning.* *arXiv preprint arXiv:2304.08732.* [https://arxiv.org/abs/2304.08732](https://arxiv.org/abs/2304.08732)

