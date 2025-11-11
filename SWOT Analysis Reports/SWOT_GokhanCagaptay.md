## SWOT Analysis: LGS English Question Generator

**Researcher:** Gökhan Çağaptay
**Date:** November 11, 2025

### Project Scope (Reminder)

This analysis **must** be based on the following project plan, which we decided upon as a team:

- **Project Goal:** Generate LGS English exam questions.
- **Core Method:** Advanced Prompt Engineering.
- **Knowledge Base:** Grounding the LLM with official LGS English lecture books **and** a corpus of previous official exam questions.
- **Key Feature:** Generating _both_ text-based questions and the prompts for corresponding images (for visual questions).
- **Strategic Decision:** We are _not_ using finetuning. Our success will be determined by our prompt quality and knowledge-base integration (RAG).

---

### 1. Strengths (Internal, Positive)

- **Speed and Flexibility (No Finetuning):** "No finetuning" stratejimiz, en büyük gücümüzdür. Bize muazzam bir geliştirme hızı ve esneklik sağlar. Bizi pahalı ve yavaş bir eğitim sürecinden kurtarır. En yeni SOTA (State-of-the-Art) modeli (GPT-4o, Llama 3, Claude 4 vb.) anında sistemimize entegre edebilir ve hangisinin en iyi sonucu verdiğini test edebiliriz.
- **High Accuracy and Relevance (RAG):** RAG yaklaşımını (MEB ders kitapları ve eski sınav soruları) kullanma kararımız, modelin "hayal görmesini" (hallucination) engeller. Üretilen her soru, doğrudan müfredat materyaline veya gerçek bir sınav sorusunun yapısına "topraklanmış" (grounded) olacaktır. Bu, müfredat uyumu (curriculum alignment) için en güçlü garantimizdir.
- **Focused Scope (English-Only):** İlk fazdaki (Fen Bilimleri) incelememin gösterdiği gibi, en büyük zorluklardan biri karmaşık görsel/mantıksal (deney düzeneği, grafik) sorulardır. Proje kapsamını "LGS İngilizce" ile sınırlamak, bu karmaşıklığı azaltır ve bizi daha yönetilebilir, metin ağırlıklı bir alana odaklar.
- **Evaluation Power (Large Team):** 15 kişilik büyük bir ekip, RAG için veri setini (kitapları/soruları vektörize etmek) hızlıca hazırlayabilir. Daha da önemlisi, üretilen soruları değerlendirmek (insan-değerlendirmesi / human-in-the-loop) için muazzam bir paralel iş gücümüz var.

---

### 2. Weaknesses (Internal, Negative)

- **Prompt Brittleness (No Finetuning):** "No finetuning" kararı, tüm yükü "Prompt Engineering" üzerine bindirir. LGS İngilizce'nin kendine has "tonunu", "stilini" veya "zorluk seviyesini" sadece prompt ile yakalamakta zorlanabiliriz. Prompt'larımız aşırı karmaşık, yönetilemez ve kırılgan hale gelebilir.
- **Scope Creep (Image Prompts):** Kapsama "görsel sorular için prompt üretme" özelliğini dahil etmek, bence bir zayıflıktır. Bu, benim Fen Bilimleri incelememde de belirttiğim "görsel" sorunudur. Metin üretimi (NLP) ile görsel üretimi için prompt tasarlamak (Computer Vision / Multimodality) farklı uzmanlıklar gerektirir. Bu, ekibin odağını dağıtır ve sahip olmadığımız becerilere ihtiyaç duyabilir.
- **Coordination Overhead (Large Team):** 15 kişilik bir ekip, en büyük zayıflığımız da olabilir. Aynı işin mükerrer yapılması, iletişim kopuklukları ve kalitede tutarsızlık yaşama riskimiz çok yüksek.
- **RAG Failure Point (Retrieval):** RAG sistemimizin kalitesi, "Retriever" (Getirici) modülünün kalitesine bağlıdır. Eğer RAG, LLM'e kitaptan alakasız bir bölümü veya yanlış bir eski soruyu "bağlam" olarak getirirse, LLM bu alakasız bağlama dayanarak "kendinden emin bir şekilde yanlış" bir soru üretecektir.

---

### 3. Opportunities (External, Positive)

- **Rapidly Evolving SOTA Models:** "No finetuning" stratejimiz, teknoloji dünyasındaki en büyük fırsatı yakalamamızı sağlar: GPT-5, Llama 4 veya Claude 4 gibi yeni ve daha güçlü bir model çıktığı gün, bu modeli anında sistemimize entegre edebilir ve kalitemizi ücretsiz olarak artırabiliriz.
- **Rapidly Evolving RAG Frameworks:** RAG, şu an yapay zekadaki en sıcak konu. LangChain, LlamaIndex gibi açık kaynaklı kütüphaneler her gün daha da güçleniyor. Bu, bizim RAG sistemimizi kurma maliyetimizi ve karmaşıklığımızı azaltan dışsal bir fırsattır.
- **Predictable Exam Structure:** LGS İngilizce, standart bir sınavdır. Bu, soru tiplerinin (örn. "diyaloğu tamamla", "resme göre hangisi doğrudur", "ana fikir nedir") tekrarlı ve tahmin edilebilir olduğu anlamına gelir. Bu yapı, her bir soru tipi için özel "prompt şablonları" oluşturmamıza ve otomasyonu kolaylaştırmamıza olanak tanır.
- **Evolving Image Models:** "Görsel prompt" özelliğimiz için, DALL-E 3, Midjourney v7 gibi metinden-görsele modellerin kalitesi hızla artmaktadır. Bu, ürettiğimiz prompt'ların LGS kalitesinde görsellere (örn. bir davetiye kartı, bir tablo) dönüşme şansını artırır.

---

### 4. Threats (External, Negative)

- **The Distractor Bottleneck:** İlk fazdaki literatür taramamızda (özellikle Elif Eslem'in ve Ali Bulut'un raporları) belirlenen en büyük tehdit budur. RAG sistemi bize **doğru cevabı** bulmamızda yardım eder, ancak LGS sorularının kalitesini belirleyen **"inandırıcı ama yanlış çeldiricileri"** (plausible distractors) üretmekte bize yardımcı olmaz. LLM'in çeldirici üretme performansı, projemizin başarısındaki en büyük dışsal tehdittir.
- **API Dependency (Cost & Reliability):** Tüm projemiz OpenAI, Google veya Anthropic gibi bir API sağlayıcısına bağlı. Eğer bu servisler zam yaparsa, kesintiye uğrarsa veya "eğitim" içeriği için ani sansür (content filter) politikaları uygularsa, sistemimiz çalışmaz hale gelebilir.
- **Source Material Quality:** RAG sistemimiz, MEB ders kitaplarının kalitesine rehin düşmüştür. Eğer ders kitapları belirsiz, kötü yazılmış veya hatalar içeriyorsa, RAG sistemimiz bu hataları "doğru" kabul edecek ve LLM'imiz bu hataları temel alan sorular üretecektir.
- **Domain Shift (Exam Format Change):** Kontrolümüz dışındaki bir tehdit de MEB'in LGS İngilizce sınav formatını aniden değiştirmesidir. Eğer format değişirse, "eski sınav sorularından" oluşan RAG veritabanımız bir anda anlamsız veya yanıltıcı hale gelebilir.

---

### 5. Personal Strategic Recommendation

SWOT analizim, planımızın **hız (Strengths)** ve **maliyet (Strengths)** açısından güçlü, ancak **kalite kontrol (Threats)** ve **odak (Weaknesses)** açısından riskli olduğunu göstermektedir. "Çeldirici kalitesi" en büyük tehdit, "görsel prompt" hedefi ise en büyük odak dağıtıcı zayıflıktır.

Tavsiyem, bu riskleri yönetmek için **ekibi derhal uzmanlaşmış "Pod" (alt-ekip) yapılarına bölmektir:**

1.  **Pod 1 - RAG & Altyapı:** Bu ekip, sadece MEB kitaplarını ve eski LGS sorularını RAG sistemine (LlamaIndex/LangChain) yüklemekten sorumlu olmalıdır.
2.  **Pod 2 - Soru Kökü (Question Stem):** Bu ekip, RAG'ı kullanarak *sadece* soru kökünü ve *doğru cevabı* üreten prompt'lar üzerine odaklanmalıdır.
3.  **Pod 3 - Çeldirici (Distractor):** Bu ekip, en büyük tehdidimizle savaşmalıdır. Pod 2'nin çıktısını (soru kökü + doğru cevap) alıp, *sadece* "inandırıcı ama yanlış" çeldiriciler üreten prompt'lar tasarlamalıdır.

İkinci tavsiyem, zayıf yönümüz olan "görsel prompt üretme" özelliğini **"de-prioritize" (ikincil öncelik) olarak etiketlemektir.** Pod 2 ve 3, metin tabanlı soru/cevap/çeldirici üretimini mükemmelleştirene kadar bu özelliğe *hiçbir* kaynak ayrılmamalıdır.