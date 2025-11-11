LGS-LLM Projesi SWOT Analizi
---Güçlü Yönler (Strengths)

Net proje kapsamı ve stratejik yön: Proje hedefi (LGS İngilizce soruları üretmek) ve kullanılacak yöntem (Prompt Engineering + RAG yaklaşımı) açıkça tanımlanmış. Bu, ekip üyeleri arasında hedef birliğini sağlar.

Resmî kaynaklara dayanma: Modelin bilgi tabanı, MEB tarafından yayınlanmış İngilizce ders kitapları ve geçmiş LGS sorularıdır. Bu, içerik güvenilirliğini ve müfredat uyumunu güçlendirir.

Finetuning yerine RAG kullanımı: Finetuning sürecinden kaçınılması, maliyeti ve teknik karmaşıklığı azaltırken, modelin güncel verilerle kolayca beslenebilmesine imkân verir.

Görsel soru üretimi: Sadece metin değil, görsel tabanlı soru üretimi için promptlar tasarlanması, projeyi klasik LLM tabanlı sistemlerden daha yenilikçi hale getirir.

---Zayıf Yönler (Weaknesses)

Finetuning yapılmaması nedeniyle sınırlı özelleşme: Model, RAG ile desteklense de, yalnızca prompt düzeyinde özelleşme sağlandığı için LGS formatına tam olarak adapte olmama riski vardır.

Veri bütünlüğü riski: Kaynak veri setinin (kitaplar ve geçmiş sorular) düzgün etiketlenmemesi veya eksik olması, model çıktılarının kalitesini etkileyebilir.

Prompt mühendisliğine yüksek bağımlılık: Projenin başarısı büyük ölçüde doğru prompt tasarımına bağlı. Yanlış yapılandırılmış promptlar çıktının kalitesini düşürebilir.

Görsel üretim kısmında teknik karmaşıklık: Görsel soru promptlarının oluşturulması ve test edilmesi, metin tabanlı sorulara kıyasla daha fazla koordinasyon ve teknik bilgi gerektirir.

---Fırsatlar (Opportunities)

Eğitim teknolojilerinde artan yapay zeka kullanımı: MEB ve özel kurumların yapay zekâ tabanlı ölçme-değerlendirme araçlarına ilgisi artıyor; proje bu trendden faydalanabilir.

Ulusal ölçekte uygulanabilirlik: LGS haricinde YKS veya ortaöğretim düzeyindeki diğer sınav sistemlerine kolayca uyarlanabilir.

Açık kaynak topluluğu ve iş birliği: GitHub üzerinde yürütülen proje yapısı, topluluk katkısına ve akademik geri bildirime açık.

LLM teknolojilerindeki hızlı gelişim: Yeni model güncellemeleriyle (ör. GPT-5 gibi) proje çıktılarının kalitesi zamanla doğal olarak artabilir.

---Tehditler (Threats)

Yapay zekâ içerik güvenliği ve etik riskler: Modelin yanlış, taraflı veya hatalı sorular üretmesi, öğrenci değerlendirmelerinde olumsuz sonuçlar doğurabilir.

Veri telif hakları: Resmî kitap ve sınav sorularının kullanımı, açık veri politikalarıyla çelişebilir ve yasal düzenlemeler gerektirebilir.

Eğitim otoritelerinin kabul süreci: Üretilen soruların “resmî standartlara uygunluğu” MEB veya denetim birimlerince onaylanmazsa, proje yaygın kullanıma geçemeyebilir.

Teknolojik bağımlılık riski: Proje belirli bir LLM (örneğin OpenAI tabanlı) sistemine bağlı kalırsa, API erişim maliyetleri veya lisans sınırlamaları uzun vadede sorun yaratabilir.
