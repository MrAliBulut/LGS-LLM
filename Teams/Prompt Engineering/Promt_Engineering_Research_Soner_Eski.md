# LGS Odaklı Araştırma Görevi

**Hazırlayan:** Soner Eski

# Article #1 – [QG]

* **Type:** Question Generation
* **Full Reference:** Chen, I. S., Wang, D., Xu, L., Cao, C., Fang, X., & Lin, J. (2024). A Systematic Review on Prompt Engineering in Large Language Models for K-12 STEM Education. arXiv preprint arXiv:2410.11123.
* **Link / DOI:** https://arxiv.org/pdf/2410.11123

* **Target Level:** K-12
* **Question Type:** Multiple-choice questions, Open-ended questions.

### Method / Model Used:
* **Models:** GPT (GPT-3, GPT-3.5, GPT-4), LLaMA-2.
* **Strategies:** Prompt Engineering techniques: Simple Prompting, Zero-shot, Few-shot, Chain-of-Thought (CoT), RAG (Retrieval-Augmented Generation).

### Dataset / Domain:
* **Domain:** K-12 STEM Education

### Contribution of the Study:
* **Classification of Prompt Strategies:** By reviewing 30 different empirical studies, the work demonstrates with evidence which techniques—Zero-shot (providing no examples), Few-shot (providing few examples), and Chain-of-Thought—are more efficient in which situations (question generation vs. question answering) in education-oriented content generation.
* **Importance of Persona Adoption:** It emphasizes that when LLMs are asked to behave like a teacher or exam preparer (Persona adoption), the quality of generated educational materials increases. This serves as the academic basis for the "You are a MoNE expert" prompt pattern in the project.
* **Hallucination and Accuracy:** It analyzes the risks of "hallucination" (fabrication) in LLMs, especially in logical constructs and visual interpretation, and provides tips on how prompts should be structured to reduce this.

### Similarity to LGS:
* **Similarity (Logical Inference):** Although the article is STEM-focused, LGS English questions require not just vocabulary knowledge but also "Inference" skills. The Chain-of-Thought (CoT) technique praised in the article is directly applicable for correctly constructing questions that require logic and negative roots (such as *"Which of the following cannot be said according to this dialogue?"*) in English questions (specifically for generating logical distractors).

* **Similarity (Visually Supported Questions):** A large portion of LGS English questions includes visuals (table, graph, poster reading). The article clearly reveals the weakness of text-based models in visual generation and interpretation. This situation is the academic proof of why we need an "Image R&D" team and a separate image generation model in our project. It confirms that as a prompt engineer, we should choose the strategy of "having the model write a description" of the visual instead of "having the model interpret" the visual.

* **Difference:** While the article focuses on numerical/analytical problem solving, our project focuses on linguistic nuances and vocabulary level (A2-B1). Therefore, instead of the mathematical verification methods in the article, we will need to add "Grammar constraints" (linguistic verification constraints).

### Actionable Ideas:
* **"Reasoning-First" Prompt Structure:** Based on the article's strong evidence for Chain-of-Thought (CoT), we should structure our prompts to force the model to *think* before it *writes*.
    * *Direct Application:* "First, analyze the provided text. Second, explain why Option A is the correct answer. Third, explain why B, C, and D are plausible but incorrect distractors. Finally, output the JSON."

* **MoNE Expert Persona:** The study confirms that Persona Adoption significantly improves quality in K-12 settings. We must standardize the system prompt to: *"You are a senior question writer for the Turkish Ministry of National Education (MoNE), specializing in LGS English exams for A2-B1 level students."* This specific persona will help the model mimic the "official" tone of the exam.

* **Text-Based Visual Descriptions:** Since the review highlights the failure of LLMs in directly handling complex visual data in STEM, we must strictly separate the visual task.
    * *Direct Application:* The prompt must explicitly state: *"Do not attempt to generate an image. Instead, provide a detailed, static prompt description (e.g., 'A vector illustration of a boy playing chess') that a separate image model can understand."*

### Notes:
* **Logic Transfer:** Even though the paper focuses on STEM, the logic applies perfectly to our English "Inference" questions. If Chain-of-Thought (CoT) helps solve a math equation step-by-step, it will definitely help the model figure out tricky questions like *"Which title fits best?"* by forcing it to think through the options logically before answering.
* **Quality Over Quantity:** The study suggests that for Few-Shot prompting, *quality* beats *quantity* every time. This is a major heads-up for the **Dataset Team**: the "Example Questions" in the database need to be top-tier. Pulling a bad or irrelevant example via RAG is actually worse than having no example at all—it just confuses the model.



# Article #2 – [QG]

* **Type:** Reading Test Item Design
* **Full Reference:** Sakulwichitsintu, K. (2024). Evaluating GPT-4 Turbo's Ability to Design English Reading Test Items for Language Learners. ResearchGate.
* **Link:** https://www.researchgate.net/publication/393172024_Evaluating_GPT-4_Turbos_Ability_to_Design_English_Reading_Test_Items_for_Language_Learners

* **Target Level:** Language Learners (EFL/ESL)
* **Question Type:** Reading Comprehension, Multiple-choice Questions.

### Method / Model Used:
* **Models:** GPT-4 Turbo.
* **Strategies:** Automatic Item Generation (AIG), CEFR Level Adaptation, Human-AI Comparative Evaluation.

### Dataset / Domain:
* **Domain:** English Language Teaching (ELT) and Assessment.

### Contribution of the Study:
* **GPT-4 Turbo Performance Analysis:** Unlike previous models, the study examines GPT-4 Turbo's competence in creating reading passages and generating related questions. It demonstrates how advanced the model's skills in context retention and instruction following are in test preparation.
* **Language Level Alignment:** It analyzes how suitable the texts and questions generated by the model are for the target audience's (Language Learners) language proficiency level (in terms of vocabulary and grammar structure).
* **Item Quality and Consistency:** It evaluates the compliance of AI-generated questions with assessment standards (clarity of the correct answer, quality of distractors) and compares them with questions prepared by human experts.

### Similarity to LGS:
* **Similarity (Paragraph Questions):** It is a direct guide for "Reading Comprehension" questions, which are the most important part of the LGS English exam. The article covers not only asking questions but also **constructing the text (passage)** where that question will be asked, which is the joint working area of the "Prompt Engineering" and "Dataset" teams in the LGS project.

* **Similarity (Target Audience - EFL):** The fact that the article is "Language Learners" oriented is of critical importance for our project. Since questions are prepared for those learning English subsequently, not for native speakers; it provides technical data on how the model can be adapted to A2-B1 level constraints (simple sentence structures, specific vocabulary lists) in LGS.

* **Difference/Application:** While the article focuses on general English proficiency, LGS has a strict adherence to the MoNE curriculum (unit-based outcomes). Therefore, when using the methods in the article, we will need to add extra constraints to our prompts such as "Use only Unit 1 vocabulary".

### Actionable Ideas:
* **Strict CEFR Constraints:** The study highlights that generic prompts often lead to vocabulary that is too difficult for the target level. We must implement a "Negative Constraint" mechanism in our prompts to control the difficulty.
    * *Direct Application:* "Use **only** A2/B1 level vocabulary. Do **not** use complex passive voice structures. If a word is not in the provided 'Unit Vocabulary List', do not use it in the question root or options."

* **Passage-First Generation Strategy:** Instead of asking for the passage and question simultaneously, we should split the prompt into two distinct phases (Sequential Prompting) to ensure the text is coherent before a question is derived from it.
    * *Direct Application:* *Phase 1:* "Generate a 50-70 word reading passage about 'Teen Life' suitable for 8th-grade EFL students." -> *Phase 2:* "Using the passage above, create a multiple-choice question focusing on 'Stating Preferences'."

* **Distractor Plausibility Check:** To avoid the common AI issue of nonsensical distractors mentioned in the study, we should ask the model to verify its own options against the passage.
    * *Direct Application:* "Ensure that the incorrect options (distractors) are mentioned in the text or related to the topic, but are factually incorrect according to the passage's specific context."



# Article #3 – [Distractor Generation]

* **Type:** Distractor Generation
* **Full Reference:** Wei, Y., Zhang, H., Zan, D., et al. (2024). From Easy to Hard: A Dual-Curriculum Learning Framework for Distractor Generation. Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).
* **Link:** https://aclanthology.org/2024.acl-long.432/

* **Target Level:** General Education (Adaptable to K-12 Exams)
* **Question Type:** Multiple-choice Questions (Focusing only on option generation).

### Method / Model Used:
* **Models:** T5, BART (Seq2Seq Models).
* **Strategies:** Dual-Curriculum Learning, Answer-aware Generation, Hard Negative Sampling.

### Dataset / Domain:
* **Domain:** Standard exam datasets like RACE (Reading Comprehension Dataset from Examinations) and SciQ.

### Contribution of the Study:
* **Curriculum Learning (From Easy to Hard):** It argues that existing models are inefficient when trying to process all data at once when generating distractors. Instead, it proves that the model should first learn "easy" distractors and then "hard" (confusing) distractors.
* **Distractor Quality:** It emphasizes that a good distractor needs to be not only grammatically correct but also relevant to the text yet definitely wrong. The study optimizes the production of high-quality options that are very similar to the correct answer but wrong using the "Hard Negative Sampling" method.
* **Dual Framework:** It proposes a structure at both the data level (ordering examples from easy to hard) and the model level (combining answer selection and option generation tasks) to increase the logical consistency of the options.

### Similarity to LGS:
* **Similarity (Distractor Logic):** The most defining feature of LGS English questions is that the options are very close to each other (For example; the verb "invite" appears in the text, but if the student does not know the meaning of "refuse", they fall into the trap). This article provides the technical infrastructure of how to generate such "tricky" and "distinctive" options (Distractor Logic).
* **Similarity (Exam Data - RACE):** The fact that the study was tested on the RACE dataset, which is the academic equivalent of LGS, shows that the methods are directly applicable to the middle school/high school level in our project.
* **Difference/Application:** The article is a "model training" (Fine-tuning) method. We will use API (Prompting). However, the lesson we will learn from this article is: When providing "Few-Shot" examples in our prompt, we can improve quality by giving the model a simple option example first, then a hard option example (Easy-to-Hard Prompting).

### Actionable Ideas:
* **Defining "Hard Negative" in System Prompt:** We must explicitly define what makes a distractor "Hard" for the model to prevent it from just generating random words.
    * *Direct Application:* "Generate 'Hard Negative' distractors. These are options that contain keywords found in the passage (to trick the student) but are factually incorrect or answer a different question than the one asked."
* **Two-Step Distractor Generation:** Following the "Dual Framework" logic, we can ask the model to first generate 10 potential distractors, and then ask it to "Select the 3 most confusing/tricky ones" for the final question.

### Notes:
* **Distractor Relevance:** The study proves that the best distractors are "Answer-aware." This means the model shouldn't generate options in a vacuum; it must look at the correct answer and generate the "opposite" or "similar-looking but wrong" version of *that specific answer*.



# Article #4 – [Foundation Model / LLM]

* **Type:** LLM Technical Report
* **Full Reference:** DeepSeek-AI, et al. (2025). DeepSeek-V3 Technical Report. arXiv preprint arXiv:2501.03462.
* **Link:** https://arxiv.org/abs/2501.03462

* **Target Level:** General Purpose (Adaptable to any field including Education)
* **Question Type:** All Question Types (Open-ended, Multiple-choice, Coding, Logic).

### Method / Model Used:
* **Models:** DeepSeek-V3 (671 Billion Parameter Mixture-of-Experts Model).
* **Strategies:** Mixture-of-Experts (MoE), Multi-head Latent Attention (MLA), Auxiliary-loss-free Load Balancing, Multi-Token Prediction (MTP).

### Dataset / Domain:
* **Domain:** Multilingual general texts, predominantly Math and Coding data.

### Contribution of the Study:
* **Cost-Effective High Performance:** It proves that DeepSeek-V3 has much lower training and operating costs while performing on par with closed-source "top models" like GPT-4 and Claude 3.5 Sonnet. (Budget-friendly API alternative for your project).
* **MoE Architecture Innovation:** By using the "Mixture-of-Experts" (MoE) architecture instead of classic dense models, it activates only a small part of the model (37B parameters) for each token. This allows the model to respond very quickly.
* **Logical Reasoning Power:** The report highlights the model's superior success, especially in math and coding domains. This shows that the model's capability for logical reasoning chain construction is highly developed.

### Similarity to LGS:
* **Similarity (Model Alternative/Cost):** It is the third strongest candidate for the "Gemini Flash or GPT-4o?" debate discussed at the beginning of your project. DeepSeek-V3 offers a similar intelligence level while drastically reducing API costs compared to GPT-4o (almost 1/10th) when generating thousands of questions in the LGS project.

* **Similarity (Logical Consistency):** The "inference" and "dialogue completion" parts of LGS English questions require logic rather than just grammar. The high mathematical logic capability highlighted in the report ensures that the model constructs the distractors in English questions more consistently.

* **Difference/Application:** This is not a "Prompt Engineering" article, but a "Model Architecture" report. It doesn't tell us "write the prompt like this," but it gives the information that "if you use this model, you can produce complex logic questions cheaper and faster." It is the primary source to be evaluated by the project's "Back-end/Software" team for API integration.

### Actionable Ideas:
* **"Generate-Critique-Refine" Workflow:** Since the API cost is significantly lower than GPT-4o, we can afford a more expensive prompting strategy. Instead of asking for one question, we can implement a loop:
    * *Step 1:* "Generate 5 variations of this question."
    * *Step 2:* "Critique these 5 variations based on LGS criteria."
    * *Step 3:* "Select and output the single best one."
    This ensures higher quality without breaking the budget.
* **JSON Consistency:** The report highlights strong coding performance. For our project, this means the model will likely be very reliable at outputting the valid **JSON** format required by our backend software, reducing technical errors in the pipeline.
