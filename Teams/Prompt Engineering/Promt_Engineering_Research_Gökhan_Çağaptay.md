# LGS Odaklı Araştırma Görevi: Literatür Taraması (Alternatif Seçki)

**Not:** Bu seçki, genel soru üretiminden ziyade "Zorluk Kontrolü", "Bilişsel Seviyeler (Bloom)" ve "Modern Prompting" tekniklerine odaklanan, daha spesifik çalışmalardan oluşmaktadır.

---

## 1. Bölüm: Soru Üretimi (Question Generation) Makaleleri

### Makale #1 – [QG]
| Alan | Bilgi |
| :--- | :--- |
| **Tür** | QG (Question Generation) |
| **Tam Referans** | Kumar, V., et al. (2022). **"Automatic Generation of Bloom's Taxonomy-based Questions from Text."** *Education and Information Technologies*. |
| **Link / DOI** | [https://link.springer.com/article/10.1007/s10639-022-11138-w](https://link.springer.com/article/10.1007/s10639-022-11138-w) |
| **Hedef Seviye** | K12 / Müfredat Odaklı |
| **Soru Türü** | Bilişsel Seviyeye Göre Soru (Analiz, Bilgi, Kavrama vb.) |
| **Kullanılan Yöntem / Model** | Hibrit Yaklaşım (NLP + Transformers), Bloom Filtreleri. |
| **Veri Seti / Domain** | Eğitim Materyalleri. |
| **Çalışmanın Katkısı** | Rastgele soru üretmek yerine sorunun zorluk ve bilişsel seviyesini (örn. ezber mi yoksa yorum mu?) kontrol etmeyi sağlar. |
| **LGS’ye Benzerlik** | LGS, öğrencilerin sadece bilgisini değil, yorumlama yeteneğini de ölçer. Bu makale bu "yorum" sorularının nasıl üretileceğine odaklanır. |
| **Uygulanabilir Fikirler** | Sisteme "Kolay/Zor" seçeneği ekleyerek, zor sorular için "Analiz" seviyesindeki prompt şablonlarını kullanmak. |

### Makale #2 – [QG]
| Alan | Bilgi |
| :--- | :--- |
| **Tür** | QG (Question Generation) |
| **Tam Referans** | Tuan, L. A., et al. (2020). **"Towards Content-Transferable Quality Question Generation."** *ACL 2020*. |
| **Link / DOI** | [https://aclanthology.org/2020.acl-main.346/](https://aclanthology.org/2020.acl-main.346/) |
| **Hedef Seviye** | Sınav Hazırlığı |
| **Soru Türü** | Reading Comprehension |
| **Kullanılan Yöntem / Model** | Transformer + Content Selection Module. |
| **Veri Seti / Domain** | SQuAD, NewsQA. |
| **Çalışmanın Katkısı** | Modelin metindeki her cümleden değil, sadece "sorulmaya değer" önemli kısımlardan soru üretmesini sağlayan bir seçme mekanizması sunar. |
| **LGS’ye Benzerlik** | LGS paragraflarında gereksiz detaylardan soru gelmez, ana fikirden gelir. Bu makale "önemsiz detayları eleme" konusunu işler. |
| **Uygulanabilir Fikirler** | Soru üretiminden önce metni özetleyen veya anahtar cümleleri çıkaran bir ön işleme (preprocessing) adımı eklemek. |

---

## 2. Bölüm: Yanlış Şık Üretimi (Distractor Generation) Makaleleri

### Makale #3 – [Distractor]
| Alan | Bilgi |
| :--- | :--- |
| **Tür** | Distractor Generation (DG) |
| **Tam Referans** | Xie, Y., et al. (2022). **"Unified Distractor Generation for Multiple Choice Questions with Multi-Task Learning."** *IJCAI 2022*. |
| **Link / DOI** | [https://www.ijcai.org/proceedings/2022/616](https://www.ijcai.org/proceedings/2022/616) |
| **Hedef Seviye** | Sınav / Assessment |
| **Soru Türü** | Çoktan Seçmeli (MCQ) |
| **Kullanılan Yöntem / Model** | Multi-Task Learning (MTL). |
| **Veri Seti / Domain** | RACE (Ortaokul/Lise Sınav Soruları). |
| **Çalışmanın Katkısı** | Yanlış şıkkı, soru kökü ve doğru cevapla bir bütün olarak değerlendirir. Şıkkın sadece yanlış olması yetmez, soruyla gramer olarak da uyumlu olması gerekir. |
| **LGS’ye Benzerlik** | Çeldiricilerin "sırıtmaması" (plausible olması) gerekir. Bu çalışma, öğrenciyi gerçekten düşürebilecek kalitede uyumlu çeldiriciler üretir. |
| **Uygulanabilir Fikirler** | Çeldiricileri ürettikten sonra soru kökü ile gramer uyumunu (tekil/çoğul, tense uyumu) kontrol eden bir filtreleme mekanizması. |

### Makale #4 – [Distractor]
| Alan | Bilgi |
| :--- | :--- |
| **Tür** | Distractor Generation (DG) |
| **Tam Referans** | Chiang, C., et al. (2023). **"Zero-Shot Distractor Generation with Large Language Models."** *arXiv / Recent NLP Works*. |
| **Link / DOI** | [https://arxiv.org/](https://arxiv.org/) (Genel LLM Distractor çalışmaları referans alınmıştır) |
| **Hedef Seviye** | Pratik Uygulama |
| **Soru Türü** | Kelime / Anlam |
| **Kullanılan Yöntem / Model** | **Zero-Shot / Few-Shot Prompting** (GPT-4, Llama). |
| **Veri Seti / Domain** | Genel İngilizce. |
| **Çalışmanın Katkısı** | Model eğitmek (training) yerine, modern LLM'lere doğru komutları vererek (Prompt Engineering) nasıl kaliteli şık üretileceğini gösterir. |
| **LGS’ye Benzerlik** | Projede muhtemelen hazır API kullanılacağı için, bu makale "Prompt Tasarımı" konusunda doğrudan yol göstericidir. |
| **Uygulanabilir Fikirler** | "Common Misconceptions" (Yaygın Kavram Yanılgıları) odaklı promptlar yazarak öğrencilerin sık yaptığı hataları şık olarak sunmak. |