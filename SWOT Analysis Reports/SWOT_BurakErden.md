# LGS Görsel (Image) R&D - SWOT Analizi

**Hazırlayan:** Burak Erden
**Tarih:** 12 Kasım 2025

## Proje Kapsamına Kısa Hatırlatma

Bu analiz, LGS-LLM projesinin "görsel soru" ayağı (image prompt üretimi, görsel eşleştirme ve görsel kalite kontrol) için hazırlanmıştır. Mevcut takım kararları doğrultusunda temel metodoloji RAG + Prompt Engineering olup fine-tuning planlanmamaktadır.

---

## Güçlü Yönler (Strengths)

- Uzmanlık odaklı rol: Görsel R&D'ye odaklanmış bir sorumluluk, görsel-soru kalitesini sistematik olarak iyileştirmemize imkân verir.
- RAG ile bağlamlandırma: Metin tabanlı bağlama ve resmi kaynaklara dayandırılmış prompt'lar, görsel içeriklerin pedagojik olarak doğru bağlamda üretilmesini kolaylaştırır.
- Çoklu model seçeneği: Mevcut ekosistemde (DALL·E, Midjourney, Stable Diffusion ve yeni metin→görsel modeller) hızlı prototipleme yapılabilir; hangi modelin LGS tarzına daha uygun olduğu A/B testleriyle bulunabilir.
- İnsan-in-the-loop (HITL): Ekipte çok sayıda öğretmen ve değerlendirici bulunduğundan, görseller için hızlı ve ölçeklenebilir doğrulama süreçleri kurmak mümkün.
- Şablonlu Prompt Şeması: Görseller için “Prompt Schema v1” (sahne, varlıklar, ilişkiler, kısıtlar, güvenlik) tanımlanarak tutarlılık ve izlenebilirlik artırılabilir.
- Deterministik üretim imkânı: ControlNet/Referans görüntü ve tohum (seed) kullanımıyla sürümler arası stil tutarlılığı sağlanabilir.

## Zayıf Yönler (Weaknesses)

- Stil ve uyuşma zorluğu: Görsellerin LGS formatına (basit, didaktik, açık) tutarlı şekilde uyması zor; modeller genelde sanatsal veya fazla karmaşık çıktılar üretme eğilimindedir.
- Eşleştirme problemi: Metin sorusu ile görselin pedagojik olarak birebir örtüşmesini sağlamak karmaşık; zayıf eşleştirme yanlış yorumlara yol açar.
- Lisans ve IP belirsizliği: Ticari görsel modellerin lisans koşulları ve üretilen görüntülerin kullanılabilirliği (eğitim/komersiyel) belirsiz olabilir; bu hukuki risktir.
- Maliyet ve gecikme: Yüksek kaliteli görsel üretimi API maliyetleri ve geçerlilik testleri ek bütçe/latency gerektirir; gerçek zamanlı kullanım pahalı olabilir.
- Değerlendirme zorluğu: Otomatik uyum skoru (ör. CLIP tabanlı) gürültülü olabilir; güvenilirlik için insan notlayıcıya bağımlılık artar.
- Platform kısıtları: Yerel üretim (Stable Diffusion) için gerekli GPU/driver kurulumu ve Windows ortamında araç uyumluluğu ekip için ekstra efor gerektirir.
- Sürüm kayması: API/model güncellemeleri aynı prompt için farklı çıktılar üreterek bakım yükünü artırır.

## Fırsatlar (Opportunities)

- Model ve araç gelişimi: Metin→görsel modeller hızla gelişiyor; kısa sürede LGS-uyumlu görseller üretmek daha ucuz ve güvenilir hale gelebilir.
- Modüler pipeline: Görsel üretim sürecini bağımsız bir servis olarak tasarlayıp, gerektiğinde devre dışı bırakmak veya ayrı ölçeklendirmek mümkün (ilk sürümde opsiyonel kılma).
- Eğitimciler için katma değer: Öğretmenlere doğrudan kullanılabilecek, düzenlenebilir görseller sunmak B2B fırsatları yaratır (yayınevleri, kurs merkezleri).
- Açık veri & synthetic data: Telif sorunlarını azaltmak için lisanslı veya açık kaynak görsellerden oluşan veri setleriyle fine-grained prompt kalibrasyonu yapılabilir; gerektiğinde sentetik (statik) görsel şablonları oluşturulabilir.
- Programatik görsel üretim: Basit grafik/tablo/akış diyagramları için SVG/Matplotlib/Mermaid gibi deterministik üretim, ölçme doğruluğunu garanti eder.
- Erişilebilirlik standartları: WCAG dostu renk paletleri, alt metin (alt-text) ve düşük görsel karmaşıklık ile kapsayıcı içerik üretimi marka güveni sağlar.

## Tehditler (Threats)

- Resmi düzenleyici riskleri: MEB/ÖSYM benzeri kurumların kendi resmi içerik araçlarını geliştirmesi veya telif/etik gereksinimler, projeyi sınırlayabilir.
- Uygunsuz içerik/filtreleme: Görsel modellerin bazen uygunsuz, yanıltıcı veya kültürel olarak duyarsız çıktılar üretmesi; içerik filtresi kurulmazsa güven kaybı yaşanır.
- Bağımlılık riskleri: Tek bir tedarikçi/modele bağlı kalmak, API fiyat/lisans değişikliklerinde projeyi savunmasız bırakır.
- Pedagojik geçerlilik sorunu: Görseller sadece estetikse, LGS'nin ölçme amaçlarına hizmet etmez; pedagojik doğruluğun sağlanamaması güvenilirliği zayıflatır.
- Politikalarla çakışma: Bazı modellerin "çocuk/öğrenci" görsellerine getirilen kısıtları, LGS bağlamında tipik sahneleri üretmeyi engelleyebilir.
- Kültürel hassasiyet: Semboller, kıyafetler veya metin üzerindeki ibareler yanlış anlaşılmalara ve itibar riskine neden olabilir.

## Ayırt Edici Tasarım Kararları (Image R&D)

- Üç Şeritli Pipeline: (1) Deterministik Şerit (SVG/şablon tabanlı grafikler), (2) Kısıtlı Üretim Şeridi (ControlNet/referans görüntü ile), (3) Serbest Üretim Şeridi (hızlı fikir prototipleri). Soru tipine göre şerit seçimi yapılır.
- Prompt Schema v1: Sahne, varlıklar, ilişkiler, renk/ölçek kısıtları, metin üzerindeki ibareler, güvenlik/etik kuralları, kültürel notlar alanları zorunlu.
- “Golden Set”: Her soru tipi için örnek görsel–prompt–onaylı çıktı üçlülerinden oluşan küçük bir altın standart seti; regresyon kontrolleri buna göre yapılır.

## Özgün Ölçütler ve KPI'lar (Image R&D)

- VAM (Visual–Text Alignment Metric): CLIP benzeri bir ölçütle metin–görsel uyumu; minimum eşik ve sapma aralığı tanımlı.
- AER (Alignment Error Rate): İnsan değerlendiricinin “yanlış yönlendirir” etiketi verdiği görsel oranı; hedef ≤ belirlenen eşik.
- QA Onay Oranı: İlk geçişte onaylanan görsel yüzdesi; hedef ≥ belirlenen eşik.
- Birim Maliyet: Onaylanan görsel başına toplam maliyet (üretim + doğrulama); bütçe tavanı ile izlenir.
- Üretim Süresi SLA: Tek görsel için uçtan uca hedef süre; aşımlar raporlanır.

## Uygulama Önerileri (Kısa, Öncelikli Adımlar)

1. Minimal Viable Görsel (MVG) konsepti: İlk sürümde yalnızca birkaç güvenli, şablonlanmış görsel tipi (ör. basit grafik, tablo, resim eşleştirme) destekleyin.
2. Görsel–Metin eşleştirme kural setleri: Her soru tipi için zorunlu görsel özellikleri (renk, perspektif, ölçütler, açıklama metni) tanımlayın ve prompt'ları buna göre şablonlayın.
3. İnsan doğrulama ve etiketleme pipeline'ı: Görselleri hızlıca sınıflandırıp onaylayacak küçük bir QA hattı kurun; hatalı örnekleri prompt bankasına geri besleyin.
4. Lisans/repo stratejisi: Kullanım amaçlarına göre açık-kaynak veya lisanslı görüntü havuzları oluşturun; ticari kullanım sorularını projenin erken aşamasında netleştirin.
5. Maliyet & ölçek planı: API çağrılarını önbelleğe alacak, gerektiğinde düşük çözünürlüklü prototipler üretip sadece onaylananları yüksek çözünürlükte render edecek bir maliyet optimizasyonu uygulayın.
6. Erişilebilirlik: Kontrast ve alt metin politikalarını zorunlu hale getirin; görsel karmaşıklığı için üst sınır belirleyin.
7. Güvenlik/Gözetim: Kültürel ve yaşa uygunluk kontrol listeleri, otomatik içerik filtreleri ve loglama ile denetlenebilirlik sağlayın.

## Kişisel Stratejik Öneri (Sonuç)

Görsel R&D, projenin ayırt edici avantajı olabilir ancak yanlış yönetilirse zaman ve güven kaybına yol açar. İlk hedefimiz "pedagojik olarak güvenli, basit ve eşleştirilebilir" görseller üretmek olmalıdır. Üç şeritli pipeline, Prompt Schema v1, Golden Set ve ölçülebilir KPI’larla yönettiğimizde; kalite, maliyet ve hız üçgeninde sürdürülebilir bir denge kurabilir, gerektiğinde görsel modülü devre dışı bırakabilecek modülerlikte ilerleyebiliriz. Böylece hem riskleri minimize eder hem de ileride güçlü bir B2B ürünü haline getirebiliriz.


