### Initial Literature Review Log

Researcher: Muhammed Göymen  
Date: November 9, 2025  
Proposed Topic Area: LGS-AQG

1. Executive Synthesis & Recommendation

Paragraph 1: The Topic & Problem. This review focuses on LGS-style automatic question generation (AQG) and reliable evaluation. The core problem is that while models can generate syntactically valid items, ensuring pedagogical quality (curriculum alignment, cognitive level, discrimination, fairness) and establishing trustworthy evaluation procedures remains difficult. Literature shows fragmented metric practices and broad surveys calling for integrated frameworks that couple generation with automatic and human assessment loops.

Paragraph 2: Comparative Analysis. Amidei et al. (2018) survey 37 AQG papers (2013–2018) and reveal heterogeneous intrinsic (BLEU/METEOR/ROUGE) and extrinsic evaluations with under-specified human studies, limiting cross-system comparability. Das et al. (2021) provide a broader survey spanning automatic question generation plus answer assessment, categorizing methods (surface, semantic, template, deep learning) and emphasizing feedback, self-learning, and assessment integration. Both agree current automatic metrics poorly capture educational usefulness; Amidei et al. stress standardization, while Das et al. extend scope to full pipeline (question + answer judging) and highlight opportunities in adaptive/self-assessment contexts.

Paragraph 3: Recommendation for LGS-LLM. The topic is viable: we can deliver value by defining a focused LGS evaluation framework combining (a) a curated, educator-validated mini benchmark set, (b) a rubric (clarity, syllabus tag, Bloom level, distractor plausibility, linguistic correctness), (c) lightweight psychometric proxies (difficulty estimation by model perplexity or student performance simulation), and (d) answer assessment integration for automatic filtering. Opportunity: surveys supply taxonomy and gaps—standardization + integration. Risk: Achieving reliable human agreement and psychometric validity may exceed initial timeframe. Mitigation: start with small pilot (50 questions across subjects) and iterative refinement; produce a reproducible evaluation protocol and open dataset artifact.

2. Annotated Bibliography & Analysis

Article 1: Evaluation methodologies in Automatic Question Generation 2013–2018

Full Citation (APA 7th Style): Amidei, J., Piwek, P., & Willis, A. (2018). Evaluation methodologies in Automatic Question Generation 2013–2018. In Proceedings of the 11th International Conference on Natural Language Generation (pp. 307–317). Association for Computational Linguistics. https://doi.org/10.18653/v1/W18-6537

In-Text Citation Example: (Amidei et al., 2018)

Summary of Contribution: The authors survey 37 papers on automatic question generation (AQG) published between 2013 and 2018 to map how systems are evaluated. They find that system development has outpaced the maturation of evaluation methodology. Both intrinsic (e.g., n-gram overlap metrics) and extrinsic (task-based) evaluations are used, but practices are highly heterogeneous, limiting comparability. The paper argues for a common framework and stronger links between automatic metrics and human judgment.

Key Findings & Quotations:
- Diverse and non-standardized evaluation practices in AQG make it difficult to compare systems across studies; a common framework is needed for reliable benchmarking (Amidei et al., 2018).
- Heavy reliance on automatic n-gram metrics (e.g., BLEU, METEOR) persists despite mixed evidence about their validity for question quality and pedagogical usefulness; human evaluation protocols are often under-specified (Amidei et al., 2018).
- Better designed human studies and clearer reporting (criteria, raters, agreement, and tasks) are recommended to align evaluations with end-use goals (Amidei et al., 2018).

Personal Analysis & Relevance to LGS-LLM: For LGS-style question generation, this survey is a strong warning against relying solely on automatic metrics. We should define a concise rubric (clarity, syllabus alignment, cognitive level, distractor plausibility) and report rater agreement, alongside any automatic metric. A small, shared evaluation set with educator-validated gold questions would help us compare model variants fairly, and task-based checks (e.g., difficulty calibration, item discrimination) can connect to exam-quality goals.

Article 2: Automatic question generation and answer assessment: a survey

Full Citation (APA 7th Style): Das, B., Majumder, M., Phadikar, S., & Ahmed, S. A. (2021). Automatic question generation and answer assessment: A survey. Research and Practice in Technology Enhanced Learning, 16, Article XX. https://doi.org/10.1186/s41039-021-00151-1

In-Text Citation Example: (Das et al., 2021)

Summary of Contribution: This survey reviews techniques for automatic question generation and automated answer assessment, spanning rule-based, template-driven, semantic, and neural approaches, and links them to self-learning and self-assessment paradigms. It catalogs feature extraction, semantic role labeling, deep models (e.g., seq2seq, transformer-based), and evaluation criteria, emphasizing integration with educational feedback loops.

Key Findings & Quotations:
- The paper stresses coupling question generation with answer assessment to support self-learning and self-assessment, moving beyond isolated generation quality (Das et al., 2021).
- It highlights educational assessment dimensions (e.g., difficulty, relevance, learner feedback) as essential evaluation signals often absent from purely NLP-centric AQG studies (Das et al., 2021).
- Neural models expand coverage and fluency but require controlled mechanisms (curriculum tags, concept maps) to avoid off-syllabus or ambiguous questions (Das et al., 2021).

Personal Analysis & Relevance to LGS-LLM: This broader pipeline perspective suggests our system should not only generate questions but also auto-assess candidate answers (e.g., distractor validation, grading short constructed responses) to prune low-quality items and estimate difficulty. Incorporating answer assessment allows iterative refinement: generated question -> model simulates student answers -> calibration of difficulty and discrimination -> accept or revise. For Turkish LGS contexts, building a concept map / skill taxonomy and attaching it to generation prompts can constrain semantic drift and ensure syllabus alignment.
