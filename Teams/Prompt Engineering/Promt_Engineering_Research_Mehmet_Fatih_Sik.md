# LGS Odaklı Araştırma Görevi

**Hazırlayan:** Mehmet Fatih Şık

# Article #1 – [Distractor Generation]

* **Tür:** Distractor Generation (Çeldirici Üretimi)
* **Tam Referans:** Bitew, S. K., Deleu, J., Develder, C., & Demeester, T. (2023). *Distractor generation for multiple-choice questions with predictive prompting and large language models.* Proceedings of the GAIED Workshop.
* **Link / DOI:** https://ugentt2k.github.io/papers/2023/bitew2023rkde.pdf

* **Hedef Seviye:** Dil Öğrenimi (Language Learning) / Ortaokul – Lise
* **Soru Türü:** Boşluk Doldurma (Cloze Test), Kelime ve Gramer Soruları.

### Kullanılan Yöntem / Model:
* **Modeller:** ChatGPT (GPT-3.5 tabanlı).
* **Stratejiler:** **Predictive Prompting (Tahmine Dayalı İstemleme)** vs. Standard Prompting.
    * *Standart Yöntem:* Modele "Bana bu soru için 3 yanlış şık üret" demek.
    * *Predictive Yöntem (Önerilen):* Modele cevabı göstermeden, "Bu boşluğa gelebilecek en olası 10 kelimeyi sırala" demek ve doğru cevap haricindeki diğer yüksek olasılıklı kelimeleri çeldirici olarak seçmek.

### Veri Seti / Domain:
* **Domain:** İngilizce Dil Sınavları (Standart Cloze Test Veri Setleri: CLOTH, RACE).

### Çalışmanın Katkısı:
* **Mantıksal Tutarlılık Sorunu Çözümü:** Çalışma, standart prompting yönteminin (doğrudan "çeldirici yaz" demenin) genellikle metinle alakasız veya çok bariz yanlış şıklar ürettiğini tespit etmiştir.
* **İnsan Hatasını Simüle Etme:** "Predictive Prompting" yöntemi, modelin metni bir öğrenci gibi okuyup boşluğu tahmin etmesini sağlar. Modelin "yanlış ama olası" tahminleri, aslında öğrencilerin de düşebileceği en mantıklı tuzaklardır. Bu yöntemle üretilen şıkların, standart yönteme göre çok daha "makul" (plausible) olduğu kanıtlanmıştır.
* **Bağlam Farkındalığı:** Çeldiricilerin sadece kelime türü olarak (örneğin hepsi fiil) değil, anlamsal bağlam (context) olarak da metne uyumlu olmasını garanti altına alır.

### LGS’ye Benzerlik:
* **Benzerlik (Cloze Test Yapısı):** LGS İngilizce sınavının yaklaşık %40-50'si "Boşluğa hangisi gelmelidir?" (Choose the best option to complete the sentence) yapısındadır. Bu makale doğrudan bu soru tipine odaklanır.
* **Benzerlik (Çeldirici Kalitesi):** LGS'de A şıkkı (Doğru) ile B şıkkı (Çeldirici) arasındaki fark, genellikle gramer hatası değil, bağlam hatasıdır. Makale, "metne gramer olarak uyan ama anlamca uymayan" o ince çizgideki şıkları üretmek için mükemmel bir rehberdir.

### Uygulanabilir Fikirler:
* **Tersine Mühendislik Prompt Stratejisi:** Projede çeldirici üretirken modele "Bana çeldirici yaz" dememeliyiz. Bunun yerine şu akışı izlemeliyiz:
    1.  **Adım:** Modele soruyu ve boşluğu ver (Doğru cevabı verme).
    2.  **Adım:** "Bu boşluğa gelebilecek en mantıklı 5 kelimeyi tahmin et" de.
    3.  **Adım:** Bu listeden, bizim belirlediğimiz "Doğru Cevap"ı çıkar.
    4.  **Sonuç:** Geriye kalan 4 kelime, senin en kaliteli, en kafa karıştırıcı çeldiricilerindir.
* **Filtreleme Mekanizması:** Makale, üretilen tahminlerin bazılarının eş anlamlı (yani aslında doğru cevap olabilecek) kelimeler olabileceği uyarısında bulunur. Bu nedenle prompta *"Tahminlerin, doğru cevabın eş anlamlısı olmamalı, anlamı değiştirmeli"* kısıtlaması eklenmelidir.

### Notlar:
* **Maliyet/Performans Dengesi:** Bu yöntemle çeldirici üretmek, standart yönteme göre biraz daha fazla token harcayabilir (çünkü modele analiz yaptırıyoruz), ancak LGS gibi eleyici sınavlarda çeldirici kalitesi her şeydir. Kalitesiz 1000 soru yerine, bu yöntemle üretilmiş kaliteli 100 soru çok daha değerlidir.
* **LLM Doğası:** LLM'ler aslında "bir sonraki kelimeyi tahmin eden" (Next Token Prediction) makinelerdir. Bu makale, LLM'in doğasına en uygun görevi vererek (tahmin etmesini isteyerek) ondan en yüksek verimi almanın yolunu gösteriyor.



# Article #2 – [Reading Comprehension]

* **Type:** Question Generation (Reading Comprehension)
* **Full Reference:** Hämäläinen, M., & Tavakoli, P. (2024). Automatic Generation and Evaluation of Reading Comprehension Test Items with Large Language Models. arXiv preprint arXiv:2404.07720.
* **Link / DOI:** https://arxiv.org/abs/2404.07720

* **Target Level:** K-12 / EFL (English as a Foreign Language)
* **Question Type:** Reading Comprehension (Paragraph-based), Multiple-choice questions.

### Method / Model Used:
* **Models:** GPT-4 (Closed-source) vs. Llama 2 (Open-source).
* **Strategies:** Zero-shot Prompting (Instruction only) vs. Few-shot Prompting. Additionally, the study introduces an "Automated Evaluation" pipeline where the LLM acts as a judge for the questions it generates.

### Dataset / Domain:
* **Domain:** English reading passages specifically curated for language proficiency testing.

### Contribution of the Study:
* **Model Performance Comparison:** The study provides a clear benchmark: GPT-4 is capable of generating near-human quality questions using only **Zero-shot** prompting (just instructions). In contrast, open-source models like Llama 2 fail with Zero-shot and strictly require **Few-shot** examples to understand the format.
* **LLM-as-a-Judge:** It demonstrates that LLMs can be used not only to *generate* content but also to *evaluate* it. The study successfully used LLMs to rate the generated questions on criteria like "grammatical correctness," "answer clarity," and "distractor plausibility."
* **EFL Context:** It specifically addresses the needs of English learners, ensuring that questions test comprehension rather than obscure general knowledge.

### Similarity to LGS:
* **Similarity (Format):** The "Text + Question Root + 4 Options" format discussed in the paper is identical to the core LGS Reading section structure.
* **Similarity (Target Audience):** The study focuses on "EFL" (English as a Foreign Language). This matches the LGS demographic perfectly (Turkish students learning English), meaning the findings on difficulty adjustment and vocabulary usage are directly transferable.

### Actionable Ideas:
* **Dynamic Prompting Strategy:** We should adjust our prompt strategy based on the model we choose.
    * *If using GPT-4/DeepSeek-V3:* We can rely on detailed instructions (Zero-shot/One-shot) to save token costs.
    * *If using a smaller/cheaper model:* We **must** inject 3-5 high-quality examples (Few-shot) via RAG, otherwise, the output format will break.
* **Automated QA Layer:** We can implement the "LLM-as-Judge" method described in the paper. After generating a question, we can trigger a second, cheaper prompt: *"You are a critic. Look at this generated question. Is the correct answer clearly supported by the text? Are the distractors logical? Rate it 1-5."* This automates the first layer of Quality Assurance.

### Notes:
* **Zero-Shot Efficiency:** The finding that GPT-4 works well with Zero-shot is great news for the budget. It means we don't always have to load heavy examples into the context window for every single request, provided we write very clear system instructions.
* **The "Hallucination" Check:** The paper warns that even good models sometimes generate questions whose answers are *not* in the text (external knowledge). The "Automated QA" step mentioned above is crucial to catch these before they reach the human editors.