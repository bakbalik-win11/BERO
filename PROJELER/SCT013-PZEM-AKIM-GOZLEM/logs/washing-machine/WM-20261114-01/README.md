# WM-20261114-01 — Çamaşır makinesi tam program kaydı

## Kayıt kimliği
- **RECORD_ID:** WM-20261114-01
- **Kayıt tarihi:** 2026-11-14
- **Kayıt durumu:** TAM PROGRAM KAYDI MEVCUT (kullanıcı kitaplığında) / içerik analizi bekliyor
- **Deney:** E21 — Çamaşır makinesi program davranışı analizi
- **Program adı:** Uzun program — dosya adında Pamuklu 60° olarak belirtilmiş; paneldeki tam ad/ayar teyidi ayrıca alınabilir
- **PROGRAM_ID:** Henüz atanmadı; program adı ve seçenekler doğrulandıktan sonra verilecek
- **Program etiketi:** UZUN / PAMUKLU 60°. Kaynak dosya adı: `wm-uzun pamuklu 60 - 2026-11-14.csv` (kullanıcı kitaplığındaki dosya listesi ekran görüntüsünden).

## HEDEF
Çamaşır makinesinin seçilen bir tam programını baştan sona akım zaman serisiyle kaydetmek. İlk analizde genel davranış ve gözle görülen bölümler çıkarılacak. Evre adları, yalnızca akım grafiğine bakılarak kesinleştirilmeyecek.

## Kayıt bilgileri — tamamlanınca doldurulacak
- Makine marka/model:
- Paneldeki programın tam adı:
- Sıcaklık:
- Sıkma devri:
- Ek seçenekler:
- Yaklaşık yük miktarı/niteliği:
- Başlangıç zamanı (yerel saat, UTC+03:00):
- Bitiş zamanı (yerel saat, UTC+03:00):
- Kullanıcı tarafından gözlenen olaylar:
- Kullanılan ESP / cihaz kimliği:
- Firmware / ESPHome sürümü:
- YAML yolu ve Git commit:
- SCT modeli / ölçülen iletken:
- ADS1115 gain / SPS / giriş modu:
- ct_clamp sample_duration:
- update_interval / yayın aralığı:
- Katsayı:
- Filtre / eşik durumu:
- Home Assistant entity_id:
- CSV dosya adı, boyutu ve SHA-256:

## Veri dosyası adlandırması
- Ham kaynak: `WM-20261114-01_raw-ha-history.csv`
- Metadata ve gözlem: `WM-20261114-01_metadata.md` (bu kayıt dosyası)
- İlk grafik/analiz: `WM-20261114-01_analysis.md`
- İleride çıkarılacak evre tablosu: `WM-20261114-01_segments.csv`

Ham CSV değiştirilmeyecek. Temizleme, dönüştürme ve grafik çıktıları ayrı türetilmiş dosyalarda tutulacak.

## Program sınıflandırma ilkesi
Her çekim için RECORD_ID farklıdır. Aynı programın tekrar kayıtları aynı PROGRAM_ID altında gruplanabilir. PROGRAM_ID ancak paneldeki tam program adı ve seçili ayarlar (sıcaklık, sıkma, seçenekler) öğrenildikten sonra atanır. Program veya önemli ayarlar farklıysa aynı sınıfa otomatik konulmaz; yeni sınıf/variant kararı ayrıca verilir.

Önerilen kalıcı kimlik biçimi: `WMP-001`, `WMP-002`, ...
- `WMP`: washing-machine program class
- sıra numarası: depoda tanımlanan program sınıfı
- Örnek yalnızca biçim örneğidir; WMP-001 henüz atanmış değildir.

“Uzun program” gibi kısa etiketler `PROGRAM_TAG` alanında tutulabilir; gerçek panel adı ve PROGRAM_ID'nin yerine geçmez.

## İlk analiz çıktısı
1. CSV bütünlüğü ve zaman aralığı.
2. Akım zaman serisinin genel grafiği.
3. Belirgin yükselme, düşme, bekleme ve tekrar eden örüntülerin tarafsız segmentasyonu.
4. Segment başlangıç/bitiş zamanları ve süreleri.
5. Kullanıcı gözlemleriyle ilişkilendirme; doğrulanmamış makine içi işlem yorumları HİPOTEZ olarak etiketlenir.

## Durum
Tam program CSV'si kullanıcı kitaplığında mevcuttur. Kullanıcının doğrulaması: bu kayıt baştan sona tam programdır. İlk nitel gözlemde ısıtma, sağ-sol tambur dönüşleri ve sıkma davranışları ayırt edilebilir bulunmuştur. CSV'nin repo kopyası, bütünlük kontrolü, Python analizi ve ayrıntılı zaman aralıkları henüz yapılmamıştır.
