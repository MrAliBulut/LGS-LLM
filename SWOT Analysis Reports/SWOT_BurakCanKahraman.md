# LGS Soru Üretim Sistemi - SWOT Analizi

##  Güçlü Yönler (Strengths)

- **Ölçeklenebilirlik:**  
  Tek bir sistemle, LGS'deki her ders ve her konu için saniyeler içinde binlerce özgün soru üretebilme kapasitesi.

- **Veri Odaklılık:**  
  Son 10 yılın LGS (ve TEOG) sorularını analiz ederek, MEB'in soru kalıplarını, sevdiği konu dağılımlarını ve "yeni nesil" kalıplarını öğrenme potansiyeli.

- **Kişiselleştirme:**  
  Öğrencinin sadece zayıf olduğu kazanımlara yönelik "zor" seviyede denemeler üretebilme.

- **Maliyet (Uzun Vadede):**  
  Yüzlerce öğretmenin bir araya gelip soru yazma maliyetine kıyasla, iyi eğitilmiş bir modelin operasyonel maliyeti daha düşük olabilir.


##  Zayıf Yönler (Weaknesses)

- **Kalite Kontrol Zorunluluğu:**  
  AI "halüsinasyon" görebilir; yani yanlış bilgiye dayalı, çeldiricisi mantıksız veya müfredat dışı sorular üretebilir.  
  Her bir sorunun uzman LGS branş öğretmenleri tarafından onaylanması (**Human-in-the-Loop**) şarttır.

- **"Yeni Nesil" Soruların Zorluğu:**  
  LGS soruları, basit bilgi soruları değildir. Karmaşık okuduğunu anlama, görsel yorumlama, mantıksal akıl yürütme ve çok adımlı problem çözme gerektirir.  
  Bu, mevcut LLM'ler için bile en zor üretkenlik alanıdır.

- **Önyargı (Bias):**  
  Model, geçmiş sorulara aşırı odaklanırsa (**overfitting**), MEB'in o sene deneyeceği yeni bir soru tarzını öngöremez ve sürekli eski tarzı taklit eder.

- **Yüksek Başlangıç Maliyeti:**  
  Kaliteli bir model (GPT-4o, Gemini 1.5 Pro vb.) API kullanımı, potansiyel ince ayar (**fine-tuning**) ve en önemlisi uzman öğretmen ekibinin maliyeti yüksek olacaktır.


##  Fırsatlar (Opportunities)

- **Devasa Pazar:**  
  Türkiye'de LGS'ye hazırlanan milyonlarca öğrenci, veli, özel okul, kurs merkezi (dershane) ve yayınevi potansiyel müşteridir.

- **Resmi Validasyon:**  
  ÖSYM'nin bile bu alana girmesi (bkz. Kaynak Araştırması), pazarın bu fikre hazır olduğunu göstermektedir.

- **B2B Satış Modeli:**  
  Sadece öğrencilere değil, kendi soru havuzunu oluşturmak isteyen yayınevlerine, okullara veya kurs merkezlerine **SaaS (Hizmet Olarak Yazılım)** modeliyle satılabilir.

- **Genişleme:**  
  Sistem kurulduktan sonra, aynı mantık **YKS (TYT/AYT)**, **KPSS**, **DGS** gibi diğer sınavlara uyarlanabilir.


##  Tehditler (Threats)

- **Resmi Kurumlar (En Büyük Tehdit):**  
  MEB veya ÖSYM, kendi geliştirdiği (veya HAVELSAN gibi bir kuruma geliştirdiği) “Resmi AI Soru Bankası”nı ücretsiz veya düşük ücretle sunarsa, pazar tamamen kaybedilebilir.

- **Büyük Rakipler:**  
  Türkiye’deki büyük eğitim yayıncıları (A Yayınları, B Test Okul vb.) sizden daha büyük bütçeler ve hazır öğretmen kadrolarıyla aynı projeyi hızlıca kopyalayabilir.

- **Güvenilirlik Sorunu:**  
  Üretilen soruların "sınavda çıkacak sorulara yakın" olduğu iddiası gerçekleşmezse (ki bu zordur), ürün “çöp” olarak damgalanabilir.  
  **Güvenilirlik**, bu projenin temelidir.

- **Müfredat Değişiklikleri:**  
  MEB’in sık yaptığı köklü müfredat değişiklikleri, modelin eğitildiği geçmiş verileri (eski soruları) geçersiz kılabilir.
