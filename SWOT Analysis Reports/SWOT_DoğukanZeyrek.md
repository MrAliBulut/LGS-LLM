# LGS-LLM Projesi – Bireysel SWOT Analizi  
**Hazırlayan:** Doğukan Zeyrek  
**Tarih:** 11 Kasım 2025  

---

## 🧩 Proje Özeti

**Proje Amacı:**  
Türkiye’deki resmi LGS (Liselere Geçiş Sınavı) İngilizce müfredatına uygun sınav soruları üretebilen yapay zekâ tabanlı bir sistem geliştirmek.

**Temel Yöntem:**  
Gelişmiş Prompt Engineering (İstem Mühendisliği) teknikleri kullanılarak, bağlama uygun ve kaliteli sınav soruları üretmek.

**Bilgi Tabanı (RAG Yaklaşımı):**  
Model, resmi LGS İngilizce ders kitapları ve geçmiş yıllara ait resmi sınav sorularıyla desteklenerek “grounding” yapılmıştır. Bu sayede üretilen soruların doğruluğu ve müfredata uyumu artırılmıştır.

**Ana Özellik:**  
Model hem metin tabanlı hem de görsel (image-based) sorular için istem (prompt) üretebilmektedir.

**Stratejik Karar:**  
Fine-tuning (modelin yeniden eğitilmesi) **kullanılmayacaktır.**  
Odak noktası, gelişmiş istem mühendisliği ve veri tabanlı üretimdir (RAG).

---

## 💪 Güçlü Yönler (Strengths)

1. **RAG ile Yüksek Güvenilirlik:**  
   Bilgi tabanlı üretim (RAG) yöntemi sayesinde, model müfredata uygun sorular üretir ve “halüsinasyon” riskini azaltır.

2. **Maliyet Verimliliği:**  
   Fine-tuning yapılmadığı için proje hem zaman hem de hesaplama açısından daha ekonomiktir.

3. **Ölçeklenebilir Yapı:**  
   Prompt tabanlı mimari sayesinde sistem, başka derslere veya dillere kolayca uyarlanabilir.

4. **Resmî Kaynaklara Dayanma:**  
   Modelin resmi kitaplar ve geçmiş sorularla beslenmesi, üretilen soruların geçerliliğini ve güvenilirliğini artırır.

5. **Dengeli Ekip Yapısı:**  
   Ekip üyelerinin farklı uzmanlık alanlarına odaklanması (prompt tasarımı, veri seti, değerlendirme) proje kalitesini yükseltir.

---

## ⚙️ Zayıf Yönler (Weaknesses)

1. **Prompt Kalitesine Bağımlılık:**  
   Çıktıların doğruluğu ve kalitesi, kullanılan istemlerin (promptların) ne kadar iyi tasarlandığına büyük ölçüde bağlıdır.

2. **Fine-tuning Eksikliği:**  
   Model yeniden eğitilmediği için bazı soru türlerinin inceliklerini tam olarak yakalayamayabilir.

3. **Veri Seti Duyarlılığı:**  
   Veri tabanındaki hatalar veya eksikler, modelin güvenilirliğini doğrudan olumsuz etkileyebilir.

4. **Değerlendirme Zorluğu:**  
   Üretilen soruların “eğitimsel kalitesini” (zorluk dengesi, dil doğruluğu, müfredat uyumu) ölçmek karmaşık bir süreçtir.

5. **RAG Entegrasyonu Karmaşıklığı:**  
   Farklı kaynaklardan doğru bilgiyi verimli şekilde çekmek teknik olarak zorlu bir iştir.

---

## 🌱 Fırsatlar (Opportunities)

1. **Eğitimde Yapay Zekâ Kullanımının Artması:**  
   Yapay zekâ destekli eğitim araçlarına yönelik talep giderek artmaktadır.

2. **Genişleme Potansiyeli:**  
   Sistem, gelecekte diğer LGS derslerine veya YKS sınavlarına kolayca uyarlanabilir.

3. **Öğretmen ve Kurum Desteği:**  
   Öğretmenler ve okullar, bu aracı kullanarak soru hazırlama süresini kısaltabilir.

4. **Eğitim Teknolojisi (EdTech) İş Birlikleri:**  
   Çevrimiçi eğitim platformlarıyla yapılacak iş birlikleri, projenin bilinirliğini ve kullanım oranını artırabilir.

5. **Açık Kaynak Katkısı:**  
   Geliştirilen yöntemlerin toplulukla paylaşılması, yeni fikirler ve iyileştirmeler için fırsatlar yaratabilir.

---

## ⚠️ Tehditler (Threats)

1. **Yasal ve Etik Riskler:**  
   Resmî kitap ve sınav içeriklerinin telif hakkı sorunları doğru yönetilmezse yasal sorunlar doğurabilir.

2. **Rekabet:**  
   Eğitim teknolojileri alanında hızla gelişen yapay zekâ çözümleri, projeyi sürekli yenilik yapmaya zorlayabilir.

3. **LLM Sınırlamaları:**  
   Temel dil modelinin hatalı veya eksik yanıt üretme olasılığı (özellikle çeviri ve anlam hataları) kaliteyi etkileyebilir.

4. **Veri Güncelliği:**  
   Müfredat değiştikçe veri tabanının düzenli olarak güncellenmemesi, sistemin eski ve hatalı sorular üretmesine yol açabilir.

5. **Kullanıcı Güveni ve Ön Yargı:**  
   Eğitimciler veya kurumlar, yapay zekâ tarafından üretilen sorulara başlangıçta temkinli yaklaşabilir; güven kazanmak zaman alabilir.

---

## 🎯 Stratejik Öneriler

| Strateji Türü | Açıklama | Örnek Uygulama |
|----------------|-----------|----------------|
| **SO (Strength–Opportunity)** | RAG altyapısı ve resmi kaynakları kullanarak projeyi güvenilir bir soru üretim sistemi olarak konumlandır. | Resmî yayıncılarla iş birliği yapılması. |
| **WO (Weakness–Opportunity)** | Prompt bağımlılığını azaltmak için sistematik bir prompt havuzu ve değerlendirme süreci oluştur. | İç prompt optimizasyon rehberi hazırlamak. |
| **ST (Strength–Threat)** | Resmî kaynaklara dayanarak rakiplerden ayrış ve yanlış bilgi üretim riskini en aza indir. | “Resmî müfredata tam uyum” vurgusuyla proje tanıtımı yapmak. |
| **WT (Weakness–Threat)** | Telif ve etik riskleri azaltmak için yalnızca lisanslı veya açık eğitim kaynaklarını kullan. | Kaynak doğrulama ve atıf modülü geliştirmek. |

---

## ✅ Sonuç

LGS-LLM projesi, **fine-tuning olmadan**, **Prompt Engineering** ve **RAG** yöntemlerini birlikte kullanarak maliyet açısından verimli, ölçeklenebilir ve yenilikçi bir yapı sunmaktadır.  
Ancak projenin uzun vadeli başarısı, **veri kalitesinin**, **prompt güvenilirliğinin** ve **yasal uyumun** korunmasına bağlıdır.  
Eğitimcilerin güvenini kazanmak ve sistemi sürdürülebilir hale getirmek için sürekli iyileştirme şarttır.

---
