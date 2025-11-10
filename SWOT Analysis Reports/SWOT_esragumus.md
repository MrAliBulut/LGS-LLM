## SWOT Analysis: LGS English Question Generator

**Researcher:** Esra Nur Gümüş
**Date:** November 10, 2025

---

### 1. Strengths (Internal, Positive)

* **Team Competence:** The success of our project largely depends on the proficiency of the team members in NLP and English language education. The team is skilled in coding, NLP, English, and data processing, which facilitates rapid prototyping. **Inspired by Literature:** Das et al. (2021) emphasizes that human evaluation and methodological knowledge are critical in automated question generation; this enhances the value of our team's expertise.
* **Prompt Engineering:** The most powerful tool enabling quick project prototyping is well-designed prompts. Utilizing prompt engineering instead of fine-tuning allows for rapid prototype production and low data dependency (inspired by Li et al., 2020). Zero-shot and few-shot strategies are ideal for initially coping with data scarcity.
* **Focused Subject Area:** The project's sole focus on English allows the model to deeply learn a specific domain, increasing pedagogical accuracy. **Inspired by Literature:** Drawing from Rao & Saha (2023), pipelines based on middle school textbooks have strong potential for adaptation to the exam level.
* **Existing Data Resources:** One of the project's biggest advantages is the readily available LGS questions and textbooks. Previous LGS questions and textbooks form a ready foundation for RAG integration. **Inspired by Literature:** Das et al. (2021) and Rao & Saha (2023) show that pedagogical metadata and correct source selection are critical to AQG success.
* **Distractor and Question Quality:** The pedagogical accuracy of the distractors in our project is an opportunity to enhance the quality of the questions. **Inspired by Literature:** Based on Zhang et al. (2020), the possibility of using hybrid distractor generation strategies can improve question quality. This specifically helps to ensure pedagogical alignment for LGS-like questions.
* **Multimodal Plan:** The project's focus on generating both text and visual questions will increase the richness and variety of the outcomes. **Inspired by Literature:** The textbook→MCQ pipeline in Rao & Saha's (2023) work supports the practical applicability of a multimodal approach.

---

### 2. Weaknesses (Internal, Negative)

* **Prompt Engineering Only:** Solely prompt-based methods may cause some questions to not align with the LGS level. Distractor or pedagogical accuracy control is limited; some questions may not meet the LGS standard. **Inspired by Literature:** While Li et al. (2020) highlights the flexibility of zero-shot approaches, it notes limitations in adapting to LGS-Turkish exam language and level nuances.
* **Visual Generation Experience:** The lack of sufficient team experience in generating visual questions poses a risk in terms of production time and quality. **Inspired by Literature:** Rao & Saha (2023) suggests visual and multimodal pipelines but notes that time and labor costs may be high for inexperienced teams.
* **Necessity of Human Review:** The reliability of model outputs depends on human validation, a process that requires extra labor. **Inspired by Literature:** Das et al. (2021) emphasizes that automated production metrics alone cannot guarantee pedagogical accuracy; human-in-the-loop is critical.
* **Language and Level Alignment:** The model may not automatically align with the LGS English level (A2/B1) and the nuances of the exam language. **Inspired by Literature:** Rao & Saha (2023) and Das et al. (2021) stress the importance of ensuring level alignment with data based on textbooks.
* **Distractor Alignment:** Lack of control in the prompt-only approach can lead to the formation of incorrect or overly easy options (distractors). **Inspired by Literature:** Zhang et al. (2020) suggests multi-step control for distractor generation; this weakness is critical for the project.

---

### 3. Opportunities (External, Positive)

* **Open-Source Tools:** Existing LLM APIs and RAG libraries offer opportunities that technically strengthen the project. **Inspired by Literature:** Li et al. (2020) and Zhang et al. (2020) show that combinations of existing tools and models increase productivity.
* **Predictable Exam Format:** The regular structure of LGS English questions makes it easier for the model to generate exam-compliant questions. **Inspired by Literature:** Rao & Saha (2023) notes that middle school textbook-based pipelines ensure regular content and learning objective alignment.
* **Pedagogical Added Value:** The generated questions can be directly utilized as a practical tool for teachers and students. **Inspired by Literature:** Das et al. (2021) highlights the importance of pedagogical suitability and the use of metadata.
* **New Technological Trends:** Rapid developments in the fields of NLP and LLMs present new methods as opportunities to improve production quality. **Inspired by Literature:** Li et al. (2020) demonstrates the advantages of zero-shot/few-shot strategies.
* **Hybrid Distractor Approach:** Generating distractors in a hybrid manner can create pedagogically safe and effective options for LGS-like questions (Zhang et al., 2020).

---

### 4. Threats (External, Negative)

* **LLM Limitations:** One of the most critical threats to the project is the potential failure of LLM APIs to generate pedagogically sufficient and reliable results. **Inspired by Literature:** Li et al. (2020) emphasizes that such models can generate erroneous or irrelevant questions even in zero-shot/few-shot scenarios.
* **Visual Module Risk:** Generating visual questions may create unexpected difficulties in the project; incorrect or unclear visuals could lead to extra labor and time loss. **Inspired by Literature:** Rao & Saha (2023) points out that production time may be prolonged for inexperienced teams working with visual pipelines.
* **Copyright and Data Dependency:** The textbooks and previous exam questions to be used may be copyrighted; restrictions on data access or legal risks may arise. **Inspired by Literature:** Rao & Saha (2023) stresses that the use of copyrighted sources can complicate data integration.
* **Human Factor:** The absence of team members with critical skills ("bus factor") can directly affect the project timeline and output quality. **Inspired by Literature:** Das et al. (2021) emphasizes that the human-in-the-loop mechanism is central to project success; team loss poses a serious risk.
* **Time and Resource Constraints:** Complex modules (visual generation, distractor generation, alignment) may not be completed within the project timeline, jeopardizing the project's core objectives. **Inspired by Literature:** Rao & Saha (2023) notes that resource and time management are critical in multimodal pipelines.
* **Prompt and Distractor Alignment:** Uncontrolled prompt and distractor strategies can lead to questions being pedagogically inappropriate and misaligned with the exam. **Inspired by Literature:** Li et al. (2020) and Zhang et al. (2020) show that this risk is particularly decisive in automated MCQ generation.

---

### 5. Personal Strategic Recommendation

This SWOT analysis indicates that the project's strengths lie in team competence, prompt engineering, and existing data resources. **Inspired by Literature:**

* **Li et al. (2020)** $\rightarrow$ Zero-shot strategies are advantageous for the start.
* **Zhang et al. (2020)** $\rightarrow$ Hybrid distractor control module is critical.
* **Das et al. (2021)** $\rightarrow$ Human-in-the-loop and use of pedagogical metadata are mandatory.
* **Rao & Saha (2023)** $\rightarrow$ Textbook-based pipeline is the closest approach for LGS alignment.

**My Recommendation:**

1.  **Prioritize** text-based MCQ generation, adding visual questions in the second phase, allowing the prototype to progress quickly and under control.
2.  Utilize **Zhang et al.-style hybrid control mechanisms** for distractor and pedagogical alignment, and **human-in-the-loop evaluation** must be included.
3.  Ensure model alignment with the exam level by integrating **RAG** and using **existing textbooks**; add **output filters** according to the LGS English level.
4.  Set a **time limit** for the visual generation module: If the prototype is not functional within **2 weeks**, focus should shift solely to the text module.

This strategy maximizes strengths while minimizing weaknesses and threats, thereby increasing project success.
