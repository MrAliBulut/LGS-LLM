# LGS Görsel Sorular & Ders Kitabı Veri Yükleme Planı

## 1. Genel Amaç

- 8. sınıf İngilizce ders kitabı içeriklerini `english_textbook_units` koleksiyonuna aktarmak.
- LGS çıkmış sorular içinde görsel içerenleri yeni `lgs_image_questions` koleksiyonuna işlemek.
- Görsel dosyalarını GridFS üzerinde saklayıp ilgili alanlara referans vermek.
- Metin tabanlı `english_questions` koleksiyonuyla görsel sorular arasındaki ilişkiyi kurmak.

## 2. Koleksiyon Şemaları

### 2.1 english_textbook_units

| Alan             | Tip                              | Açıklama                                   |
| ---------------- | -------------------------------- | ------------------------------------------ |
| unit_no          | int                              | Ünite numarası                             |
| title            | string                           | Ünite adı                                  |
| objectives       | [string]                         | Öğrenme hedefleri                          |
| vocabulary       | [{word, definition, example}]    | Kelime listesi                             |
| sample_dialogues | [{title, text}]                  | Diyalog veya okuma parçası                 |
| activities       | [{activity_no, instructions}]    | Etkinlik açıklamaları                      |
| images           | [{filename, caption, gridfs_id}] | Ünite içi görseller                        |
| source_pdf       | string                           | Kaynak dosya adı                           |
| metadata         | obj                              | Ek bilgiler (sayfa aralığı, revizyon, vb.) |

### 2.2 lgs_image_questions

| Alan            | Tip      | Açıklama                                 |
| --------------- | -------- | ---------------------------------------- |
| question_id     | string   | Özgün kimlik (örn. `lgs_2018_q15_img`)   |
| year            | int      | LGS yılı                                 |
| topic           | string   | Konu etiketi                             |
| question_number | int      | Sınavdaki sıra                           |
| text            | string   | Soru metni                               |
| ask             | string   | Sorunun asıl istediği                    |
| image_file_id   | ObjectId | GridFS dosya ID'si                       |
| image_caption   | string   | Görsel kısa açıklaması                   |
| answer_key      | string   | Doğru şık                                |
| source_pdf      | string   | Çıkış PDF adı                            |
| tags            | [string] | Ek etiketler (ör. `visual`, `listening`) |
| created_at      | datetime | Yükleme zamanı                           |
| notes           | string   | QA notları                               |

### 2.3 Ortak Soru Alanları

| Alan                               | Tip                                    | Açıklama                 |
| ---------------------------------- | -------------------------------------- | ------------------------ |
| `_id`                              | ObjectId                               | MongoDB belge ID'si      |
| `ask`                              | string                                 | Ana yönerge              |
| `text`                             | string                                 | Diyalog/pasaj metni      |
| `image_file_id`                    | ObjectId                               | Ana görsel ID'si         |
| `image_caption`                    | string                                 | Görsel açıklaması        |
| `context_images`                   | [{name, image_file_id, image_caption}] | Ek görseller             |
| `options`/`statements`/`sentences` | array                                  | Soru tipine göre bloklar |
| `answer_key`                       | string                                 | Tekli cevap              |
| `correct_option_label`             | string                                 | Çoktan seçmeli şık       |
| `correct_option_text`              | string                                 | Doğru şık metni          |
| `answer_keys`                      | object                                 | Bölüm bazlı anahtar      |
| `context`                          | misc                                   | Özel alanlar             |

## 3. Süreç Akışı

1. Şema onayı ve paylaşımı.
2. İçerik çıkarma (metin + görsel listeleri).
3. Görsellerin hazırlanması ve GridFS yüklemesi.
4. Json + metadata ile koleksiyon insert işlemleri.
5. Doğrulama ve raporlama döngüsü.

## 4. Görev Dağılımı

### Muhammed Göymen (@firat-sowft)

- Şema belgelerini ve zorunlu alanları yönetir.
- Atlas erişimlerini doğrular, raporlar.

### Serhat Çelik (@serhatcelikq)

- Ders kitabı PDF/OCR, LGS görsel soru metinleri.
- Eksik görselleri bildirir.

### Ömer Efe Peltek (@OmerEfee)

- Görsel standardizasyonu, GridFS yüklemeleri.
- `upload_images.py` çıktıları ve ID listeleri.

### Ramazan Tunç (@Ramazant22)

- LGS görsel soruları işaretleme, scriptlerle yükleme.
- `english_questions` ile referans eşleştirmeleri.
- QA çıktıları ve hata raporları.

## 5. Ders Kitabı Yükleme Durumu

- Üniteler 1 ve 10 Muhammed tarafından tamamlandı.
- Üniteler 2-4 Ramazan tarafından yüklendi.
- Üniteler 5-7 Serhat tarafından yüklendi.
- Üniteler 8-9 Ömer tarafından yüklendi.

## 6. Raporlama İlkeleri

- Her ekip üyesi günlük raporda tamamlanan işler, eklenen belge sayısı ve blokajları belirtir.
- GridFS metadata alanlarında ortak etiket standardı (`label`, `unit`, `question`) kullanılır.
- QA için örnek `find` çıktıları paylaşılır.

## 7. secondary_school_english_textbook Koleksiyonları

| Koleksiyon Adı                      |
| ----------------------------------- |
| `fs.chunks`                         |
| `fs.files`                          |
| `u10_naturalforces_image_questions` |
| `u10_naturalforces_text_questions`  |
| `u1_friendship_image_questions`     |
| `u1_friendship_text_questions`      |
| `u2_teenlife_image_questions`       |
| `u2_teenlife_text_questions`        |
| `u3_inthekitchen_image_questions`   |
| `u3_inthekitchen_text_questions`    |
| `u4_onthephone_image_questions`     |
| `u4_onthephone_text_questions`      |
| `u5_theinternet_image_questions`    |
| `u5_theinternet_text_questions`     |
| `u6_adventures_image_questions`     |
| `u6_adventures_text_questions`      |
| `u7_tourısm_image_questions`        |
| `u7_tourısm_text_questions`         |
| `u8_chores_image_questions`         |
| `u8_chores_text_questions`          |
| `u9_science_image_questions`        |
| `u9_science_text_questions`         |

## 9. lgs_database Koleksiyonları

| Koleksiyon Adı            |
| ------------------------- |
| `english_question_topics` |
| `english_questions`       |
| `fs.chunks`               |
| `fs.files`                |
| `lgs_image_questions`     |
