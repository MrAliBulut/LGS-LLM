# 📚 İngilizce Ders Kitapları & LGS Veritabanları Kapsamlı Raporu

**Son Güncelleme:** 14 Aralık 2025

Bu rapor, ilgili dört MongoDB veritabanının (DB) temel yapısını, koleksiyon dizinlerini, şema parametrelerini ve operasyonel notlarını özetlemektedir.

---

## 1. Genel Veritabanı Yapısı ve İlişkiler

Veri tabanlarının temel mimarisi, içerik türüne ve kullanım amacına göre standartlaşmıştır.

| Yapısal Bileşen | Açıklama | İlişki |
| :--- | :--- | :--- |
| **Glosari (Sözlük)** | Ünite bazlı kelime listeleri (`u*_glossary`). | Bağımsız (Ünite Numarası ile ilişkilendirilir). |
| **Soru/Aktiviteler** | Ünite ve türe göre ayrılmış soru koleksiyonları (`u*_..._text_questions`, `u*_..._image_questions`). | GridFS'e `image_file_id` (ObjectId) ile referans verir. |
| **GridFS** | Görsel dosyaların depolandığı ikili koleksiyonlar (`fs.files`, `fs.chunks`). | Sorulara ve ünite dokümanlarına görsel ID'si ile referans sağlar. |
| **Loglama** | Veri yükleme işlemlerinin meta kayıtları (`upload_logs`). | Operasyonel kayıttır, diğer verilerle doğrudan ilişkili değildir. |



---

## 2. Veritabanı Dizinleri ve Şema Parametreleri Özeti

### 2.1. `5th_grade_english_textbook` (5. Sınıf)

| Dizin (Koleksiyon) Adı | Şema Parametreleri (Önemli Alanlar) | Operasyonel Notlar |
| :--- | :--- | :--- |
| `u*_glossary` (1'den 9'a) | `term` (string), `translation` (string), `unit` (int) | `term` alanında **unique index** önerilir. Tekrar eklemeleri önler. |
| `upload_logs` | `filepath`, `collection`, `timestamp`, `status` | Yükleme operasyonlarının takibi. |
| `u*_..._questions` | `ask`, `text`, `answer_key`, `image_file_id` (ObjectId) | Sorular ve GridFS referansları. |
| **Örnek Varyasyon** | `u8_lifeintheuniverse&future_text_question` | **İsimlendirme standardizasyonu gereklidir.** |

### 2.2. `6th_grade_english_textbook` (6. Sınıf)

| Dizin (Koleksiyon) Adı | Şema Parametreleri (Önemli Alanlar) | Operasyonel Notlar |
| :--- | :--- | :--- |
| `u*_glossary` (1'den 9'a) | `title`/`term`, `unit`, `words`/`entries` (array) | `unit` ve `term` üzerinde indeksleme önerilir. |
| `u*_..._questions` | `ask`, `text`, `answer_key`, `question_code`, `image_file_id` | `question_code` (string) alanının kullanılması önemlidir. |
| **Örnek Varyasyon** | `u4_weather&emotions_image_questions` | Koleksiyon adlarında özel karakter (`&`) kullanılmıştır. |

### 2.3. `secondary_school_english_textbook` (Ortaokul/Lise)

Bu DB, ünite adlarını konu başlığı olarak kullanır ve **u1'den u10'a** kadar uzanır.

| Dizin (Koleksiyon) Adı | Şema Parametreleri (Önemli Alanlar) | Operasyonel Notlar |
| :--- | :--- | :--- |
| `u*_friendship...science` | `ask`, `text`/`options`/`statements`, `answer_key`, `image_file_id` | `text_questions` ve `image_questions` ayrımı tutarlıdır. |
| **Koleksiyonlar** | `u1_friendship_...`, `u3_inthekitchen_...`, `u9_science_...` | Konu bazlı filtreleme için uygundur. |

### 2.4. `lgs_database` (Sınav Odaklı)

Bu yapı, LGS görsel soruları için özel şemalara sahiptir ve referans ilişkisi kurar.

| Dizin (Koleksiyon) Adı | Şema Parametreleri (Önemli Alanlar) | Operasyonel Notlar |
| :--- | :--- | :--- |
| `english_questions` | `ask`, `text`, `answer_key`, **`image_question_id`** (ObjectId) | `lgs_image_questions` koleksiyonuna referans içerir. |
| `lgs_image_questions` | `question_id`, `year` (int), `topic`, `image_file_id` (ObjectId) | Sınav yılı (`year`) ve soru kimliği (`question_id`) önemli arama alanlarıdır. |
| `fs.files` | `metadata.label = question_id` etiketi içerir. | Hızlı görsel eşleştirme sağlar. |


---

## 3. Operasyonel Parametreler ve Doğrulama

### 3.1. Bağlantı ve Ortam Parametreleri

* **URI:** `MONGODB_URI` (Ortam değişkeni ile sağlanır)
* **Kimlik:** `MONGODB_USERNAME` ve `MONGODB_PASSWORD` (Ortam değişkenleri)
* **Yükleme Yöntemi:** JSON dosyalarından Upsert (Update/Insert) veya `insert_many` işlemleri.
* **Loglama:** İşlem sonuçları `upload_logs` koleksiyonuna kaydedilir.

### 3.2. Hızlı Doğrulama Komutları

Bu komutlar, terminal üzerinden anlık durum kontrolü sağlar:

```bash
# Tüm Veritabanlarında Koleksiyonları Listele
mongosh "${MONGODB_URI}/<DB_NAME>" --eval 'db.getCollectionNames()'

# Belge Örneği Çekme (Limit 2)
mongosh "${MONGODB_URI}/<DB_NAME>" --eval 'db.<COLLECTION_NAME>.find().limit(2).pretty()'

# GridFS Dosya Sayısı
mongosh "${MONGODB_URI}/<DB_NAME>" --eval 'db.fs.files.find().count()'

# Son Yükleme Loglarını Kontrol Et
mongosh "${MONGODB_URI}/5th_grade_english_textbook" --eval 'db.upload_logs.find().sort({timestamp:-1}).limit(5).pretty()'
