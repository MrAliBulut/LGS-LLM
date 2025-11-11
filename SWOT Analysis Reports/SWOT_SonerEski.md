## SWOT Analysis: LGS English Question Generator

**Researcher:** Soner Eşki  
**Date:** November 11, 2025

---

### 1. Strengths (Internal, Positive)

* **Structured Domain:** Compared to subjects like math or science, LGS English has more clearly defined vocabulary lists, clear grammar structures, and recurring question patterns (e.g., dialogue completion, picture matching). This structured nature makes it easier for the AI to learn patterns and produce successful outputs.

* **High Added Value with Low Development Cost**  
Thanks to the prompt engineering approach, effective results can be obtained without requiring high computational power or long model training processes. This makes the production process cost-efficient from a budget perspective.

* **Comprehensive Question Types**  
Producing not only text-based questions but also visual/picture-based questions brings the model much closer to the real LGS format and leads to more realistic outputs that better match the actual student experience.

* **User-Centered and Feedback-Driven Design** 
The project can be continuously improved in terms of question quality and user experience by regularly collecting and analyzing feedback from teachers and students. A user-friendly and simple interface makes it easier for teachers to generate and review questions, while also providing an interactive environment where students can experience the questions and share feedback. This holistic approach makes the technology accessible to everyone and ensures that the system continuously evolves based on real user experiences.  

---

### 2. Weaknesses (Internal, Negative)

* **Superficial Similarity of Questions and Lack of Pedagogical Depth**  
The model can successfully imitate the formal properties of past LGS questions (such as question structure, length, and word choice), but these questions may not always reflect the cognitive depth and thinking skills required in real exam questions. For example, the model might generate a question like “Which activity do students like most?”, whereas what is expected in LGS would be something like “According to the chart, which activity do students spend the most time on after school?”, which requires students to interpret a chart and draw conclusions. This difference can cause the questions to look similar to LGS on the surface, but fail to adequately measure students’ skills in analysis, inference, and understanding context.

* **Inconsistent Quality Control**  
Working with a large team of 15 people makes it difficult to establish a common standard for what “quality” means. One team member might approve a question as “perfect LGS level”, while another might flag it as “too easy” or “not aligned with the curriculum”. Managing such a crowded quality control process within limited time and still building a consistent item pool is a serious weakness.

* **Dataset Bias (Past Exam Questions vs. Textbooks)**  
The most valuable data you have are the “past exam questions”, but they are limited in number. The largest volume of data comes from “textbooks”. Due to this imbalance, the LLM may tend to generate questions closer to textbook exercise style rather than the style and difficulty level of LGS itself. This can prevent the generated questions from truly capturing the “real exam” feeling.

* **Inconsistency and Alignment Challenges in the Visual Model**  
The visual generation model used in the project does not directly understand an instruction like “generate an image suitable for the LGS format” because it operates separately from the LLM. For the visual to fully match the question text produced by the model (for example, “a child who looks sad but is waving”), the LLM has to describe this scene in a detailed and accurate way. However, current visual models may struggle to consistently produce didactic, simple, and explanatory visuals that match the LGS style. This can lead to quality discrepancies in the question–image pairing and reduce the overall reliability of the system.  

---

### 3. Opportunities (External, Positive)

* **Topic-Based Scalability and Gradual Rollout**  
The project will initially focus on a specific topic area within the English curriculum. Once the model is successfully validated, the same structure can be easily adapted to other units and themes (for example, “The Environment”, “Hobbies and Skills”, “Technology Addictions”). This step-by-step expansion approach helps the system mature gradually, increases content diversity, and allows the model’s performance in different units to be measured systematically.

* **Rapidly Evolving LLM Ecosystem and Easy Integration**  
New-generation language models (such as GPT-5, Claude, Gemini, Mistral) are offering higher accuracy at increasingly lower cost. These developments make it possible to keep the project’s technical infrastructure up to date without frequent full retraining. In addition, the growing number of open-source APIs and plugins makes it easier to integrate the system into different platforms.

* **Consistency and Structural Advantages of the LGS Format**  
The LGS English exam has remained structurally quite consistent over the years. This provides a strong pattern for the model to learn from. The recurring structure of question types allows the model to reliably learn certain patterns, which in turn makes it easier for the RAG system to work in a targeted manner.

* **Maturity of Open-Source RAG Tools**  
Recently, open-source libraries developed in the RAG (Retrieval-Augmented Generation) space (such as LangChain, LlamaIndex, Haystack) have become more stable and easier to use. This enables data management, retrieval, and verification processes in the project to be carried out with less technical effort. As a result, the team can focus more on pedagogical content instead of spending most of its time on infrastructure.  

---

### 4. Threats (External, Negative)

* **Quality and Consistency Issues in Visual Content Generation**  
The visual models used may not always produce didactic, simple, and pedagogically appropriate images. Stock-photo-like or highly aesthetic images may not fit the clear and instructional visual style expected in LGS. This can cause quality inconsistencies in multimodal (text + image) questions and lead to a decrease in user trust.

* **Bias Risk in AI Models**  
LLMs and visual models can unintentionally carry over biases present in their training data. This creates a risk of generating examples that may be culturally or linguistically inappropriate. Especially content that does not match students’ age or cultural context can cause both pedagogical and ethical problems.

* **Excessive Similarity (Overfitting and Question Repetition Risk)**  
Because the RAG system relies heavily on past LGS questions, the model may end up memorizing superficial patterns instead of learning the underlying learning outcomes of the exam. This can lead the model to produce content that is formally similar to past questions rather than truly original items. If the LLM repeatedly generates the same kinds of patterns, the diversity of the item pool will decrease, causing students to get used to only certain types of questions and gradually weakening the validity of measurement.

* **Scalability and Resource Constraints During Pilot Phase**  
The system may perform very well on small datasets; however, as the question pool grows and multi-unit tests begin to be generated, computation time, storage requirements, and API usage costs can rapidly increase. This can make it difficult for the system to maintain the same efficiency in large-scale applications. External factors—such as server costs, cloud infrastructure limits, or API quotas—can become significant threats that restrict large-scale deployment of the project.  

---

### 5. Personal Strategic Recommendation

Based on my analysis, the strongest side of the project is that LGS English has a very predictable and systematic exam structure. This makes it easier for both the RAG system and the LLM to learn meaningful patterns. On top of that, the low-cost and fast prompt-engineering approach gives us the advantage of building strong prototypes in a relatively short time. On the other hand, the size of the team and inconsistencies in quality control are points that need careful attention. Different perspectives are valuable, but without clear criteria for approving questions (for example “similarity to LGS”, “curriculum alignment”, “visual coherence”), it will be hard to maintain a common quality standard.  

For this reason, I recommend starting with a small but clearly defined English unit. Our first goal in that unit should be to get as close as possible to “real LGS quality” in both text-based and visual questions. Visual question generation should definitely remain part of the project; however, at this stage it would be helpful to form a small sub-team that specifically monitors how the LLM and the visual model work together and whether the images match the LGS style (simple, clear, and instructional). If this team regularly reviews the generated visuals from a pedagogical perspective and provides continuous feedback, the system will evolve in a much more consistent and high-quality way.
