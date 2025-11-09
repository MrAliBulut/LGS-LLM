### Initial Literature Review Log

**Researcher:** Burak Can KAHRAMAN
**Date:** 9 November 2025  
**Proposed Topic Area:** Mathematics – Word Problems (LGS) & Turkish – Reading Comprehension (Multiple Choice)

## 1. Executive Synthesis & Recommendation

**The Topic & Problem.** This review focuses on two sub‑areas highly relevant to LGS‑style item generation: (a) multiple‑choice reading‑comprehension items grounded in a given passage; and (b) elementary‑level mathematics word‑problem (MWP) generation. Across both strands, the literature highlights the central bottleneck: human‑authored items are costly and slow to produce at scale, while LLM‑generated items require systematic quality controls to ensure passage‑dependence (for RC), curricular alignment and solvability (for MWPs) (Säuberli & Clematide, 2024; Ariyarathne et al., 2025).

**Comparative Analysis.** The reading‑comprehension study proposes an evaluation protocol that quantifies *text informativity* as the difference between answerability (with passage) and guessability (without passage). Using this, the authors compare human‑authored items with Llama‑2 and GPT‑4 generations and show that GPT‑4 is a strong generator and also a reliable automatic rater, although some generated items remain too guessable. The math study, in contrast, is an end‑to‑end MWP generation pipeline: open‑source LLM selection, QLoRA fine‑tuning, preference‑based alignment (DPO/KTO/CPO), decoding‑time diversity controls, and a secondary‑LLM *solvability checker* that filters unsound problems. Both agree that raw LLM output needs targeted post‑processing for assessment‑quality items (Säuberli & Clematide, 2024; Ariyarathne et al., 2025).

**Recommendation for LGS‑LLM.** Based solely on these sources, two actionable directions stand out. (1) For Turkish paragraph items, adopt the *informativity*‑driven evaluation loop (human+LLM hybrid): screen out items that are answerable even without the passage, and iterate prompts until informativity is above a threshold. (2) For math word problems, implement a *generate → solvability‑check → regenerate* pipeline with explicit unit/realism/adequacy rules. **Primary opportunity:** a clear evaluation protocol (RC) and a practical quality‑assurance pipeline (MWP). **Primary risk:** persistent guessability in RC and curriculum/grade mismatch in MWPs unless we add LGS‑specific constraints and content policies.

---

## 2. Annotated Bibliography & Analysis

### Article 1: Automatic Generation and Evaluation of Reading Comprehension Test Items with Large Language Models

**Full Citation (APA 7th Style):**  
Säuberli, A., & Clematide, S. (2024). Automatic generation and evaluation of reading comprehension test items with large language models. In *Proceedings of the 3rd Workshop on Tools and Resources for People with REAding DIfficulties (READI 2024)* (pp. 22–37). European Language Resources Association (ELRA).

**In‑Text Citation Example:**  
(Säuberli & Clematide, 2024)

**Summary of Contribution:**  
The paper compiles a dataset of German multiple‑choice reading‑comprehension (MCRC) items and introduces a human+automatic evaluation protocol built around *text informativity*—defined as answerability with passage minus guessability without passage. Human‑authored, Llama‑2, and GPT‑4 items are compared. GPT‑4 performs strongly both as generator and automatic evaluator, though some generated items remain susceptible to passage‑independent answering.

**Key Findings & Quotations:**  
- *Text informativity* provides a practical, reference‑free signal of passage‑dependence for RC items.  
- GPT‑4 aligns well with human ratings as an automatic evaluator; Llama‑2 requires more careful thresholding and prompt control.  
- Typical quality issues include weak distractors, ambiguous wording, and items solvable by world knowledge rather than the passage itself.

**Personal Analysis & Relevance to LGS‑LLM:**  
- I agree with the core claim that informativity is a robust proxy for measuring whether an item truly tests reading.  
- Limitations: the dataset and experiments are in German; transfer to Turkish/LGS requires adaptation of passage genres, distractor design patterns, and difficulty scaling.  
- For LGS‑LLM: implement a two‑mode checker (with‑passage vs. no‑passage) and reject items whose informativity falls below a target threshold; combine with style guides for Turkish passages and distractors.

---

### Article 2: Elementary Math Word Problem Generation using Large Language Models

**Full Citation (APA 7th Style):**  
Ariyarathne, N., Bandara, H., Heshan, Y., Gamage, O., Ranathunga, S., Nayanajith, D., Sivapalan, Y., Lihinikaduarachchi, G., Vihidun, T., Chandirakumar, M., Premakumar, S., & Gathsara, S. (2025). Elementary math word problem generation using large language models. *arXiv preprint* arXiv:2506.05950. https://doi.org/10.48550/arXiv.2506.05950

**In‑Text Citation Example:**  
(Ariyarathne et al., 2025)

**Summary of Contribution:**  
The authors present an end‑to‑end MWP generation framework: selection of an open‑source base model, QLoRA fine‑tuning, preference‑based alignment (DPO/KTO/CPO), decoding‑time diversity controls, and a secondary‑LLM *solvability checker* to filter unsound problems. Human+LLM evaluation is used to analyze error types (e.g., missing data, unrealistic scenarios, wrong units), and a new dataset is released.

**Key Findings & Quotations:**  
- Decoding controls and alignment improve variety and reduce repetitive patterns while maintaining correctness.  
- A secondary‑LLM *solvability* filter removes a large fraction of unsound items (unsolvable or unrealistic), materially improving quality.  
- Despite gains, strict grade/topic adherence remains challenging and benefits from explicit constraints and human feedback.

**Personal Analysis & Relevance to LGS‑LLM:**  
- The generation+solvability loop is directly actionable for LGS math.  
- Limitations: curriculum alignment and culturally appropriate contexts must be enforced; otherwise items may be solvable yet misaligned with LGS targets.  
- For LGS‑LLM: add unit‑checking, realism constraints, and topic/grade classifiers; maintain a rejection taxonomy (e.g., wrong units, missing data, unrealistic outcomes) to drive regeneration prompts.

