### Initial Literature Review Log
Researcher: Burak Erden  
Date: November 9, 2025  
Proposed Topic Area: LGS-QuestionGeneration
 
Not: Bu inceleme ve dokümanın bazı derleme, özetleme ve düzenleme adımlarında NotebookLM ve GPT-5 Mini kullanılmıştır.

---

## 1. Yönetici Özeti ve Öneri (Executive Synthesis & Recommendation)

Bu inceleme, Türkiye’de uygulanan LGS (Liseye Geçiş Sınavı) formatına uygun, yüksek bilişsel seviyede çoktan seçmeli ve okuma-anlama soruları üretebilen bir yapay zekâ modeli geliştirme hedefini konu almaktadır. İncelenen iki temel çalışma, soru üretimini iki yönlü bir perspektiften ele almaktadır:  
(1) Bhowmick ve arkadaşları tarafından sunulan **QGen** adlı modüler soru üretim sistemi, içerikten soruya giden otomatik bir üretim hattı sağlamaktadır.  
(2) Lee ve arkadaşlarının çalışması ise, **ChatGPT benzeri LLM modellerinin kontrollü kullanımını sağlayan prompt engineering protokolleri** ve **öğretmen-in-the-loop** doğrulama yaklaşımını vurgulamaktadır.

QGen, üretim sürecini içerik çıkarımı → soru üretimi → cevap çıkarımı → distractor üretimi → kalite filtreleme olarak modüllere ayırarak ölçeklenebilir bir yapı sunarken; Lee et al. çalışması, LLM çıktılarının kontrol altına alınmasında öğretmen rehberliğinde tasarlanan 2D soru tipi matrisinin önemini gösterir.

LGS-LLM projesi için en uygun çözüm, bu iki yaklaşımın birleşiminden doğacak hibrit bir mimaridir:
- **Türkçe uyarlanmış mT5/T5 tabanlı soru üretim modeli**
- **BERTurk tabanlı cevap-span çıkarımı**
- **Distractor üretimi için semantik kaynağa dayalı + LLM tabanlı sıralama kombinasyonu**
- **Kalite güvence için otomatik filtreleme + öğretmen doğrulama paneli**

---

## 2. Açıklamalı Kaynakça ve Analiz (Annotated Bibliography & Analysis)

### 2.1 Makale 1: Automating Question Generation From Educational Text  
**Bhowmick et al. (2023)**  

Bu çalışma, eğitim metinlerinden otomatik olarak çoktan seçmeli sorular üreten **QGen** adlı modüler bir sistem sunmaktadır. Sistem, soru üretimi (T5 / InstructGPT), cevap çıkarımı (RoBERTa / InstructGPT) ve distractor üretimi için hibrit yöntemler kullanır.

**Ana Bulgular:**  
- Soru üretiminde kullanılan T5 modelleri dilsel akıcılık açısından güçlü sonuçlar vermiştir.  
- Cevap çıkarımında EM ≈ 0.64 ve F1 ≈ 0.84 skorları elde edilmiştir; bu değerler makul ve uygulanabilir seviyededir.  
- Distractor üretiminde hibrit yaklaşım (sense2vec + LLM) ~%58 kabul edilebilir kalite sağlamıştır.  
- Özellikle **non-grounded** ve **hallucination** kaynaklı hata oranları azaltmak için filtreleme modülü kritik rol oynamıştır.

**LGS-LLM Projesine Katkısı:**  
QGen’in modüler yapısı, LGS soru üretiminde aşama aşama kalite optimizasyonu yapılabilmesini mümkün kılar. Özellikle distractor kalitesi ve içerik bağı işin merkezindedir.

---

#### QGen Sistemi (AI Question Generation System) Tartışması

QGen sistemi, Bhowmick ve arkadaşları tarafından geliştirilen ve eğitim metinlerinden otomatik olarak çoktan seçmeli sorular (MCQ) üretmek üzere tasarlanmış, uçtan uca, modüler bir yapay zekâ sistemidir [1-4]. Aşağıda, kaynaklarda sunulan bilgiler doğrultusunda kapsamlı bir tartışma sunulmaktadır.

1. Amaç ve Kapsam

QGen’in temel amacı, öğretmenlerin Soru Bazlı Aktiviteler (QBA) hazırlama yükünü azaltmaktır [4]. Araştırmalar, öğretmenlerin QBA hazırlamaya haftada minimum 2.5 saat harcadığını ve zaman eksikliğinin (%63) bu süreçteki en büyük sorun olduğunu belirtmektedir [4]. QGen, bu ihtiyaca yanıt olarak, metin içeriğine dayanan (content-grounded) MCQ'lar üretmeyi hedefler [3, 4]. Üretilen her MCQ; soru metni, doğru cevap tahmini ve yanıltıcı seçeneklerden (distractor) oluşur [3, 4]. Bu hedef doğrultusunda sistem, hem otomatik üretim hattı desteği hem de insan denetimine elverişli çıktılar üretmek üzere tasarlanmıştır.

2. Tasarım Felsefesi ve Öncelikler

QGen, tasarımında özellikle eğitim alanı için kritik olan bazı ilkelere öncelik vermiştir:

- Ölçeklenebilirlik, Güvenilirlik ve Gizlilik: QGen, GPT-4 gibi en son teknolojiye sahip, yüksek kaliteli modeller yerine, eğitim alanında hayati kabul edilen ölçeklenebilirlik, güvenilirlik ve gizliliği önceliklendirmiştir [1, 2, 4-6]. Bu nedenle, QGen çalışmasında büyük LLM'lere kıyasla gecikme (latency), gizlilik ve güvenilirlik endişeleri nedeniyle T5 ve GPT-3 gibi daha küçük transformer tabanlı modellerin kullanımını savunur [2, 5, 7]. Bu yaklaşım, hem maliyet hem de öngörülebilirlik açısından eğitim kurumları için daha uygulanabilir bir çözüm sağlar.
- Modüler Mimari: QGen, esneklik sağlamak amacıyla modüler bir mimari benimsemiştir. Bu modüler çerçeve, her bir bileşenin (soru, cevap, distractor) bağımsız geliştirilmesine ve optimizasyonuna olanak tanır, böylece çeşitli dil modellerinin entegrasyonu kolaylaşır [2, 5, 8, 9]. Modülerlik aynı zamanda hata izolasyonu, A/B denemeleri ve farklı veri kaynaklarının paralel kullanımını mümkün kılar.

3. QGen'in Beş Modüllü Mimarisi

QGen, bir girdi metnini çoktan seçmeli bir soruya dönüştürmek için tasarlanmış beş ana modülden oluşur [2, 4, 5]:

1. Modül 0: İçerik Çıkarımı (Content Extraction): Bir konu (topic) verildiğinde, ilgili metni (context) bir kaynaktan çeker [2, 8]. Bu aşama, kaynak metnin segmentlenmesi, eğitim düzeyine göre uygun pasajların seçilmesi ve gerekirse özetlenmesini kapsar.
2. Modül 1: Soru Üretimi (Question Generation): Giriş içeriğiyle alakalı ve ona dayanan sorular üretir [2, 4]. Bu modülde T5 tabanlı transformer modelleri (SQuAD veri kümesinde ince ayarlanmış T5-base/T5-large) ve InstructGPT kullanılır [2, 4, 5, 10]. Model çıktıları genellikle birden fazla alternatif soru taslağı (beam veya n-best list) olarak üretilir ve sonraki modüller için aday havuzu sağlar.
3. Modül 2: Doğru Cevap Tahmini (Correct Answer Prediction): Üretilen her soru için, sorunun oluşturulduğu içerikteki doğru cevap aralığını (answer span) belirler [2, 4, 5]. Bu amaçla RoBERTa modeli (SQuAD2.0 üzerinde eğitilmiş) veya InstructGPT kullanılır [2, 4, 5, 11]. Cevap çıkarımı; span tabanlı değerlendirme, confidence skorları ve gerekiyorsa içerik geri bağlama (content-backchecking) ile doğrulanır.
4. Modül 3: Distractor Üretimi (Distractor Generation): Verilen soru ve doğru cevap için yanıltıcı seçenekler (distractor) üretir [2, 4, 5]. Bu modül için InstructGPT (few-shot promptlarla) veya Ensemble yaklaşımı (sense2vec, WordNet, ConceptNet, Densephrases ve insan tarafından derlenmiş MCQ veri kümeleri kombinasyonu) gibi hibrit yöntemler kullanılır [2-5, 8, 12]. Hibrit strateji, semantik yakınlık, sözcüksel çeşitlilik ve pedagojik uygunsuzlukları değerlendiren çoklu filtrelerle desteklenir.
5. Filtreleme Modülü (Filtering): Kötü kalitedeki, içerikle temellenmemiş (non-grounded), tekrarlanan veya birden fazla doğru cevabı olan MCQ'ları eler [2, 4, 5, 7, 13, 14]. Filtreleme katmanı, perplexity tabanlı anormallik tespiti, semantic-consistency kontrolleri ve dilbilgisel doğruluk değerlendirmelerini birleştirir.

4. Performans ve Kalite Sonuçları

QGen, hem nicel hem de nitel değerlendirmelerle test edilmiştir:
- Nicel Sonuçlar:
	- Soru Kalitesi (Modül 1): Üretilen soruların ortalama perplexity değeri 37.3 ve ortalama sorgu iyi-biçimlilik (query well-formedness) skoru ≈0.864 olarak bulunmuştur, bu da doğal dil kalitesi ve dilbilgisel doğruluk açısından yüksek kaliteye işaret eder [2, 6].
	- Cevap Doğruluğu (Modül 2): Cevap tahmini için ortalama Exact Match (EM) skoru 0.64 (cevap dizisinin %64 oranında tam eşleşmesi) ve F1-skoru 0.84 olarak elde edilmiştir, bu da makul bir doğruluk seviyesidir [2, 4-6].
	- Distractor Kalitesi (Modül 3): İnsan değerlendirmesine göre, üretilen MCQ'ların ≈%58'i kabul edilebilir yanıltıcı seçeneklere sahiptir; bu yanıltıcı seçenekler doğru cevaptan ayırt edilemez olarak bulunmuştur [2, 5, 6, 15, 16].
- Nitel Sonuçlar:
	- İnsan annotatörler tarafından yapılan değerlendirmede, Hibrit varyant (Modül 1: T5-large, Modül 2: RoBERTa-large, Modül 3: Instruct GPT) ve Fixed prompt GPT varyantı (tüm modüller Instruct GPT), üretilen MCQ'ların sırasıyla ~%92 ve ~%93.53'ünün "arzu edilen kalitede" olduğunu göstermiştir [2, 5, 6, 17].
- Sık Görülen Hata Tipleri: QGen’de en sık rastlanan hata tipleri arasında içerikle temellenmemiş (non-grounded) sorular (~%12), hallucination/yanlış çıkarım (~%10) ve distractor tür hataları (~%12) yer almaktadır [2, 6].

5. LGS Projesi İçin Önemi ve Uygulanabilirliği

QGen sistemi, LGS-LLM projesi için doğrudan teknik bir temel oluşturur [15]. Modüler mimarisi sayesinde LGS'nin özel gereksinimlerine adapte edilebilir [15].
- Mimari Adaptasyonu: Türkçe ortam için QGen mimarisinin Modül 1'inde T5 yerine mT5 veya Türkçe’ye ince ayarlanmış T5/BART benzeri modeller kullanılması önerilmiştir [2, 15, 18]. Modül 2'de (Cevap Çıkarımı) ise BERTurk gibi Türkçe BERT türevleri, SQuAD benzeri Türkçe veri üzerinde ince ayarlanarak kullanılabilir [2, 18].
- Kalite Kontrolü: QGen'in detaylı filtreleme koşulları (8 koşul), LGS gibi yüksek riskli sınavlar için kritik olan içerikle temellenmemiş sorular, yanlış cevap tahminleri, kötü üretilmiş distractorlar ve tekrarlanan MCQ'lar gibi hataları otomatik olarak tespit etmek için temel alınabilir [13, 14].
- Hibrit Yaklaşım: QGen'in modüler yapısı ve Lee et al.'in öğretmen doğrulama protokolü birlikte uygulandığında, ölçeklenebilir, güvenilir [7, 12, 18] ve öğretmen kabul edilebilir bir sistem inşa etme fırsatı sunar [10, 18].

QGen, bir çoktan seçmeli soruyu, içerik anlama, doğru cevabı çıkarma ve inandırıcı yanıltıcı seçenekler oluşturma gibi aşamalara ayıran bir "montaj hattı" gibidir. Her bir modülün bağımsız olarak optimize edilebilmesi, LGS gibi spesifik bir kalite ve format standardı gerektiren bir sınav için esneklik ve sağlamlık sağlamaktadır.


### 2.2 Makale 2: Few-shot is enough: exploring ChatGPT prompt engineering method for automatic question generation in English education  
**Lee et al. (2024)**

Bu çalışma, ChatGPT gibi büyük dil modellerinin doğrudan kullanılmasından ziyade, dikkatle tasarlanmış **prompt şablonları** ve **öğretmen-in-the-loop doğrulama** süreçlerinin, soru üretim kalitesini artırdığını göstermektedir. Çalışma, soru türlerini sınıflandırmak için **2D Matris Yaklaşımı** sunar.

**Ana Bulgular:**  
- Few-shot prompt yaklaşımı uzman değerlendirmelerinde yüksek geçerlilik (CVI≈0.89, IRA≈0.76) sağlamıştır.  
- Cloze ve Yes/No soru tiplerinde düşük geçerlilik tespit edilmiş; bu türler için farklı prompt protokolleri gereklidir.  
- Öğretmen rehberli doğrulama süreci, kaliteyi ve kabul edilebilirliği artırmada anahtar rol oynamıştır.

**LGS-LLM Projesine Katkısı:**  
Bu çalışma, model çıktılarını kontrol altına almak ve LGS’nin hedeflediği bilişsel seviyeleri doğru temsil etmek için **öğretmen kontrollü geri bildirim döngüsünün zorunlu olduğunu** göstermektedir.

---

## 3. LGS-LLM İçin Teknik Yol Haritası

| Aşama | Önerilen Yöntem | Model / Araç |
|------|-----|-----|
| Soru Üretimi | Türkçe uyarlanmış generatif model | mT5 / T5-BART Fine-tune |
| Cevap Çıkarımı | Span tahmini | BERTurk / Tr-RoBERTa |
| Distractor Üretimi | Hibrit: semantik adaylar + LLM sıralama | WordNet + sense2vec + LLM Scoring |
| Filtreleme | Otomatik kalite denetimi | Perplexity / semantic consistency checks |
| Doğrulama | Öğretmen paneli + rubrik | CVI / IRA tabanlı değerlendirme |

---

## 4. Sonuç
Bu iki çalışma birlikte değerlendirildiğinde, LGS-LLM projesi hem teorik hem pratik olarak uygulanabilir görünmektedir.  
En kritik başarı faktörleri:
- Türkçe modellerin ince ayarı
- Distractor üretiminde hibrit yaklaşım
- Öğretmen destekli doğrulama ve değerlendirme süreci

Bu unsurlar sağlandığında, sistemin LGS düzeyinde yüksek nitelikli soru üretimi gerçekleştirmesi mümkündür.

