# LGS Odaklı Araştırma Görevi – Makale Dökümantasyonu

Bu dosya, seçilen **3 makale** için (2 × QG, 1 × Distractor) doldurulmuş şablonu içerir.

---

## Makale #1 – [QG]

### Transformer and Large Language Models for Automatic Multiple-Choice Question Generation: A Systematic Literature Review

| Alan                              | Bilgi |
|-----------------------------------|-------|
| Tür                               | QG |
| Tam Referans (APA’ya yakın)       | Awalurahman, H. W., Aji, R. F., & Budi, I. (2025). Transformer and Large Language Models for Automatic Multiple-Choice Question Generation: A Systematic Literature Review. *IEEE Access, 13*, 127100–127112. https://doi.org/10.1109/ACCESS.2025.3590423 |
| Link / DOI                        | https://doi.org/10.1109/ACCESS.2025.3590423 |
| Hedef Seviye                      | Çeşitli seviyeler (K12, üniversite vb.); makale, farklı çalışmaları toplayan bir **sistematik literatür taraması**, bu yüzden tek bir hedef seviye yok. |
| Soru Türü                         | **Çoktan seçmeli (MCQ)** – soru kökü + doğru cevap + distractor’lar. |
| Kullanılan Yöntem / Model        | Tek bir model önermiyor; **Transformer ve LLM tabanlı MCQ üretimi** yapan **28 çalışmayı** inceliyor. Bu çalışmalarda kullanılan T5, BERT-tabanlı modeller, GPT-tabanlı LLM’ler vb. için **fine-tuning** ve **prompt engineering** (zero-shot, few-shot, chain-of-thought, RAG) stratejilerini sınıflandırıyor. |
| Veri Seti / Domain               | Tekil bir veri seti yok; farklı alanlardan **otomatik MCQ üreten** modelleri inceleyen 28 çalışmanın sonuçlarını derliyor (dil öğrenimi, okuduğunu anlama, alan bilgisi sınavları vb.). |
| Çalışmanın Katkısı               | Transformer ve LLM tabanlı **otomatik çoktan seçmeli soru üretimi** alanındaki güncel literatürü sistematik olarak derliyor. Kullanılan model türleri, stratejiler (fine-tuning / prompt), veri kaynakları ve değerlendirme metrikleri için ayrıntılı bir **taksonomi** sunuyor; ayrıca LLM’lerin **distractor üretimi ve otomatik değerlendirmedeki** rolüne dair açık problemleri gösteriyor. |
| LGS’ye Benzerlik                 | Format olarak LGS ile birebir örtüşüyor: **metin / bilgi kaynağı → çoktan seçmeli soru + distractor**. Çalışmaların büyük kısmı İngilizce MCQ üretiyor; bu da **LGS İngilizce** testi için yöntemlerin doğrudan uyarlanabilmesini mümkün kılıyor. |
| Uygulanabilir Fikirler           | • Metrikler: Ürettiğimiz soruları değerlendirmek için sadece BLEU/ROUGE değil, "Item Writing Flaws" (Soru yazım hataları) gibi kural tabanlı değerlendirmeler kullanabiliriz. • Pipeline Yaklaşımı: LGS soruları için soruyu ve şıkları tek seferde (end-to-end) ürettirmek yerine, önce soruyu sonra çeldiricileri üreten "Step-Wise" (Adım adım) yaklaşımın daha kontrollü olabileceği fikri.• LGS sistemi için mimari tasarlarken, makaledeki **taksonomiyi** (Transformer fine-tuning tabanlı vs. LLM prompt tabanlı yaklaşımlar) **yol haritası** olarak kullanmak.<br>• LLM’leri hem **soru/distractor üretiminde**, hem de **otomatik kalite değerlendirmede** (farklı bir LLM hakem modeli ile) kullanma fikrini uygulamak.<br>• **Zero-shot, few-shot, chain-of-thought, RAG** gibi prompt stratejilerini LGS senaryolarında sistematik olarak karşılaştırmak. |
| Notlar                           | Bu makale “tek bir model”den çok, **senin kuracağın sistemi tasarlarken hangi model/strateji kombinasyonlarının mantıklı olduğuna** dair üst seviye rehberlik veriyor. Bu yüzden QG tarafında **temel başvuru makalesi** olarak kullanılabilir. |

---

## Makale #2 – [QG]

### Exploring prompt pattern for generative artificial intelligence in automatic question generation

| Alan                              | Bilgi |
|-----------------------------------|-------|
| Tür                               | QG |
| Tam Referans (APA’ya yakın)       | Wang, L., Song, R., Guo, W., & Yang, H. (2025). Exploring prompt pattern for generative artificial intelligence in automatic question generation. *Interactive Learning Environments, 33*(3), 2559–2584. https://doi.org/10.1080/10494820.2024.2412082 |
| Link / DOI                        | https://doi.org/10.1080/10494820.2024.2412082 |
| Hedef Seviye                      | **İlkokul (primary school)** seviyesi; Çin’deki **The Smart Education of China** platformundan indirilen **örnek ilkokul ders tasarımlarındaki** sorular ve metinler üzerine bir çalışma. |
| Soru Türü                         | Çeşitli **okuduğunu anlama / düşünme becerisi** soruları: bilgi geri çağırma, çıkarımsal, karşılaştırma/karşıtlık, değerlendirme, uygulama vb. Üretilen sorular ağırlıklı olarak **açık uçlu**, ancak **çoktan seçmeli formata dönüştürülebilir** (stem aynı, doğru cevap + distractor’lar sonradan eklenebilir). |
| Kullanılan Yöntem / Model        | LLM tabanlı **Automatic Question Generation (AQG)** çerçevesi. Ana katkı, öğretmenlerden toplanan **kolektif bilgi tabanı**na dayalı bir **“prompt pattern”** tasarlamak. LLM, bu pattern ve bilgi tabanı ile yönlendirilerek sorular üretiyor; model ismi üzerinden değil, **prompt tasarımı** üzerinden yenilik getiriyor. |
| Veri Seti / Domain               | Çin’deki **Smart Education of China** platformundan alınan **ilkokul ders tasarımları** içindeki öğretmen soruları. Bu soruların özellikleri çıkarılıp **11 soru türüne** (Bloom taksonomisi vb. teorilerle ilişkili) ayrılıyor ve bu çerçeve üzerinden prompt pattern tasarlanıyor. Domain: **ana dili Çince olan ilkokul öğrencileri için okuduğunu anlama**. |
| Çalışmanın Katkısı               | • Öğretmen bilgisinden türetilmiş bir **soru tipi taksonomisi + prompt pattern** ile çalışan AQG çerçevesi öneriyor.<br>• Prompt pattern + kolektif bilgi tabanının LLM ile birleştiğinde, öğretmen sorularına yakın kalitede sorular üretebildiğini, uzman değerlendirmeleri ve uygulama örnekleriyle gösteriyor.<br>• Sadece “LLM’ye metni ver, soru üret” değil, **tasarlanmış pedagojik pattern’lerle LLM’yi yönlendirme** fikrini temellendiriyor. |
| LGS’ye Benzerlik                 | • **K12 seviyesi** ve **reading comprehension** odaklı olması, LGS İngilizce’nin okuma bölümüyle **yapısal olarak çok benzer**.<br>• Soru türü sınıflandırması (literal / inferential / evaluative / application tarzı) LGS İngilizce sorularını tasarlarken birebir kullanılabilir.<br>• Metin ve sorular Çince olsa da, yöntem olarak **LGS İngilizce’ye direkt aktarılabilir** (fark, sadece dil ve içerik). |
| Uygulanabilir Fikirler           | • Öğretmen Bilgisi ile Prompt Zenginleştirme: Sistemimize "LGS Soru Yazarı Rolü" tanımlarken, sadece "zor soru sor" demek yerine; LGS'deki "Inference Question" (Çıkarım Sorusu) tanımını ve özelliklerini prompt içine "Context" olarak ekleyebiliriz. Örneğin: "Bu bir LGS çıkarım sorusudur, metinde açıkça yazmaz ama ipuçlarından anlaşılır" gibi tanımları prompta gömmek.   • LGS için öğretmenlerle birlikte bir **“soru tipi + bilişsel seviye + beceri”** taksonomisi çıkarıp, buna uygun **prompt pattern kütüphanesi** tasarlamak.<br>• Her pattern’e **sınıf seviyesi, beceri türü (reading / vocabulary / grammar), Bloom seviyesi, zorluk** gibi meta veriler ekleyip, sistemi bu pattern’lerle kontrol etmek.<br>• LLM’nin ürettiği soruları, tıpkı makaledeki gibi **uzman değerlendirmesi ve öğrenci performansı** ile geri besleyip pattern’leri iyileştirmek. |
| Notlar                           | Bu makaleyi, “**LLM’yi nasıl prompt’larsam pedagojik olarak kaliteli soru üretir?**” sorusuna cevap veren bir çerçeve gibi düşünebilirsin. LGS projesinde özellikle **prompt pattern tasarımı** için çekirdek referans olabilir. |

---

## Makale #3 – [Distractor]

### LLM-Based Automatic Generation of Multiple-Choice Questions With Meaningful Distractors

| Alan                              | Bilgi |
|-----------------------------------|-------|
| Tür                               | Distractor |
| Tam Referans (APA’ya yakın)       | Chico, V. J. S., Regino, A. G., Bonacin, R., & Reis, J. C. (2025). LLM-Based Automatic Generation of Multiple-Choice Questions With Meaningful Distractors. In *Anais do XXXVI Simpósio Brasileiro de Informática na Educação (SBIE 2025)*. Sociedade Brasileira de Computação. |
| Link / DOI                        | https://sol.sbc.org.br/index.php/sbie/article/view/38469 (makale sayfası) |
| Hedef Seviye                      | **Portekizce dil eğitimi / değerlendirmesi** bağlamında genel bir öğrenci kitlesi. Metinde belirli bir sınıf/yaş seviyesi net olarak belirtilmiyor; odak, “Portekizce MCQ’ler için kaliteli distractor üretimi”. |
| Soru Türü                         | **Portekizce çoktan seçmeli sorular (MCQ)** – soru kökü + doğru cevap + LLM tabanlı **“meaningful distractors”**. |
| Kullanılan Yöntem / Model        | • İki üretici LLM ile distractor üretimi: **gpt-4o-mini** (çok dilli bir LLM) ve **sabid-3** (Portekizce odaklı bir LLM).<br>• Üretilen distractor’ları değerlendirmek için **Claude-3 Haiku** hakem LLM’si kullanılıyor (Item Writing Flaw Theory – IWFT rehberliğinde).<br>• Distractor’lar arasındaki çeşitlilik ve benzerlik için **Self-BLEU** (dilsel çeşitlilik) ve **Self-Cosine** (semantik paylaşım) gibi metrikler kullanılıyor. |
| Veri Seti / Domain               | Domain, **Portekizce dil etkinlikleri ve değerlendirme soruları**. Çalışma, Portekizce MCQ’ler için distractor üretmeye odaklanıyor; kullanılan soru seti, Portekizce dilini ölçen maddelerden oluşuyor (detaylar makalenin deney bölümünde). |
| Çalışmanın Katkısı               | • Portekizce için **LLM tabanlı distractor üretimi** yapan bir framework öneriyor.<br>• Distractor’ların hem **gramatikal/biçimsel çeşitliliğini** (Self-BLEU) hem de **semantik yakınlığını** (Self-Cosine) ölçerek “iyi çeldirici” tanımını nicel hale getiriyor.<br>• İnsan yapımı distractor’larla LLM’in ürettiği distractor’ları karşılaştırarak kalite, çeşitlilik ve ayırt edicilik açısından analiz ediyor. |
| LGS’ye Benzerlik                 | • LGS İngilizce yapısı ile birebir aynı format: **stem + doğru cevap + 3–4 distractor**.<br>• Makalenin ana odağı, **“öğrenciyi doğru seviyede zorlayan ama haksız/yanıltıcı olmayan çeldiriciler”** tasarlamak; bu, LGS için de kritik bir konu.<br>• Dil Portekizce olsa da, distractor teorisi, metrikler ve LLM kullanım şekli **seviyeden bağımsız** ve LGS İngilizce sorularına doğrudan uyarlanabilir. |
| Uygulanabilir Fikirler           | • Kendi LGS sisteminde, doğru cevabı belirledikten sonra **LLM tabanlı bir “distractor üretim pipeline’ı”** eklemek: önce çok sayıda candidate distractor üret, ardından Self-BLEU / cosine benzerlik / LLM-hakem filtreleriyle en iyi 3–4’ü seçmek.<br>• Claude-3 Haiku benzeri bir hakem LLM’yi kullanarak distractor’ları **IWFT veya benzeri madde yazım kurallarına** göre otomatik etiketletmek (iyi / kötü / hatalı).<br>• Çeldirici üretiminde **genel amaçlı LLM (gpt-4o-mini) vs. dil-özel LLM (sabid-3)** karşılaştırmasını kendi LGS senaryona (örneğin Türkçe / İngilizce) uyarlamak. |
| Notlar                           | Bu makale, “**Distractor Generation**” kategorisi için güçlü bir referans. QG tarafında seçeceğin bir makale ile birlikte, LGS sistemi için **2 × QG + 2 × Distractor** dengesini kurmana yardımcı olacak yapıda. Şu an elindeki set içinde **2 QG + 1 Distractor** var; bir tane daha distractor makalesi eklediğinde kişi başı görev tamamlanmış olacak. |

---

## Kısa Uygunluk Özeti

- **Makale #1 (QG)** → İngilizce **çoktan seçmeli soru üretimi**, Transformer/LLM odaklı SLR → **QG kriterlerine uygun**.  
- **Makale #2 (QG)** → **K12 / ilkokul** seviyesi, okuduğunu anlama odaklı LLM tabanlı AQG + prompt pattern → **QG + LGS benzerlik kriterlerine çok uygun**.  
- **Makale #3 (Distractor)** → LLM tabanlı **MCQ + meaningul distractor** üretimi, Portekizce dil eğitimi bağlamında → **Distractor Generation kriterlerine uygun**.  

> Not: Kişi başı hedef seti (2 × QG + 2 × Distractor) tamamlamak için yalnızca **1 adet daha Distractor odaklı makale** eklemen gerekiyor.
