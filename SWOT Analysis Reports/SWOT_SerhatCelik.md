# SWOT Analysis: LGS English Question Generator  
**Researcher:** Serhat Celik  
**Date:** November 11, 2025  

---

## 1. Strengths (Internal, Positive)

- The team includes both software and language experts, improving the technical and linguistic accuracy of the project.  
- Using Prompt Engineering instead of fine-tuning allows for faster experimentation and flexibility.  
- The RAG (Retrieval-Augmented Generation) method enables direct use of official LGS sources, increasing content reliability.  
- Focusing only on English ensures that the model’s attention and dataset remain specialized and consistent.  
- The plan to generate image-based questions gives the project a unique and innovative edge.

---

## 2. Weaknesses (Internal, Negative)

- Prompt Engineering can produce inconsistent results compared to fine-tuned models.  
- The visual question generation module requires additional technical knowledge and API integrations, which could increase workload.  
- Building and curating a large knowledge base is time-consuming; poor data selection can lead to inaccuracies.  
- Coordination within a large team may be difficult, leading to redundant or conflicting work.  
- Manual human validation during testing can slow down the development process.

---

## 3. Opportunities (External, Positive)

- LLM-based question generation is an emerging trend in educational technology; this project is entering at an early and advantageous stage.  
- Open-source RAG and vector database tools (e.g., FAISS, LlamaIndex, LangChain) make development easier and more modular.  
- The Ministry of Education’s shift toward digital learning materials could increase institutional interest in such tools.  
- Visual-enhanced English questions can provide direct pedagogical value for teachers and students.  
- The project can later be adapted for other subjects (e.g., Science or Mathematics), creating a scalable foundation.

---

## 4. Threats (External, Negative)

- Changes in LLM API pricing or access policies could threaten long-term sustainability.  
- Image-generation models (e.g., DALL·E, Stable Diffusion) may produce low-quality or inappropriate outputs.  
- If the LGS exam format changes significantly, the generated question style may become outdated.  
- Dependence on third-party APIs and open-source frameworks increases systemic vulnerability.  
- Copyright or ethical restrictions in educational content may limit usable materials.

---

## 5. Personal Strategic Recommendation

Based on this analysis, the greatest strength is our ability to integrate official resources via RAG, ensuring accurate question generation. However, the main weakness lies in the complexity of the image-generation module.  
I recommend splitting the team into two groups: one focusing on text-based question generation, the other on visual integration.  
If stable progress on the image module isn’t achieved within two weeks, the first release should focus solely on text-based questions. This will maintain both quality and delivery speed.

---
