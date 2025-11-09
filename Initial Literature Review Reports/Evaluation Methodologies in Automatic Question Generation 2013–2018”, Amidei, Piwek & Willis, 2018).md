# 🧑‍🔬 Second Literature Review Log

**Researcher:** Muhammed Göymen  
**Date:** November 9, 2025  
**Proposed Topic Area:** *Evaluation Methodologies in Automatic Question Generation 2013–2018”, Amidei, Piwek & Willis, 2018)*  

# 📘 Paper Summary

## 🎯 Purpose
The study aims to systematically analyze **37 research papers on Automatic Question Generation (AQG)** published between 2013 and 2018, focusing on the **evaluation methodologies** used in the field.  
It highlights the **need for a standardized evaluation framework** to ensure comparability and reliability among AQG systems.

---

## 📈 Key Findings
- AQG research has increased rapidly in recent years, **but evaluation methods have not advanced at the same pace.**  
- Due to the use of **diverse methodologies** (human-based, automatic, and task-based), it is difficult to compare system quality consistently.  
- This **lack of standardization** prevents objective performance measurement across AQG systems.

---

## 🧪 Evaluation Types
The paper categorizes evaluation approaches into two main types:

### **Intrinsic Evaluation**
- Directly evaluates the system’s output (e.g., grammar, fluency, semantic correctness).  
- Relies on **human judgment** or **automatic metrics** (BLEU, METEOR, ROUGE, etc.).  
- **83%** of the reviewed studies use this type of evaluation.  

### **Extrinsic Evaluation**
- Measures how well the system performs a specific **external task** (e.g., contribution to a QA system).  
- This approach is **rarely used (around 6%)**.

---

## ⚙️ Automatic Evaluation Metrics
The most commonly used metrics include:
- **BLEU** (most frequent)  
- **METEOR**  
- **ROUGE**, **Precision**, **Recall**, **F1-score**, **Accuracy**

> However, these metrics show **weak correlation with human judgments.**  
> There is a lack of systematic studies analyzing the relationship between human evaluation and automatic metrics.

---

## 🧍‍♀️ Human Evaluation
- Most studies use **Likert-scale evaluations** (e.g., 1–5 ratings).  
- Commonly assessed dimensions: **grammatical correctness, meaning, fluency, naturalness, appropriateness, and diversity.**  
- Over **50%** of papers **did not report inter-annotator agreement (IAA)**.  
- Among those that did, **high agreement (κ ≥ 0.8)** was observed in only **23%** of cases.

---

## 💬 Discussion and Conclusions
- Despite progress in AQG systems, **no standard evaluation framework** currently exists.  
- **Automatic metrics** should be viewed as **diagnostic tools** rather than true measures of quality.  
- The field needs **shared datasets** and **standardized human evaluation protocols.**  
- The authors propose a **shared evaluation platform** to help researchers compare systems and share consistent results.

---

## 🔍 Overall Conclusion
The study concludes that in the AQG field:
- **Methodological diversity is high**,  
- **Consistency is low**, and  
- **Common standards are missing.**

> The authors recommend revisiting shared tasks such as **QG-STEC (Question Generation Shared Task Evaluation Challenge)** and developing a **unified evaluation framework** for future research.

---

## 🔗 Reference Information
**Source:** Amidei, J., Piwek, P., & Willis, A. (2018).  
*“Evaluation Methodologies in Automatic Question Generation 2013–2018.”*  
*Proceedings of the 11th International Natural Language Generation Conference (INLG 2018), pp. 307–317.*  

📄 [Read the full paper on ACL Anthology](https://aclanthology.org/W18-6537/)
