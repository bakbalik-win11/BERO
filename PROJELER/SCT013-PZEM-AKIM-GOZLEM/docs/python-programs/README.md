# BERO Python program envanteri

- Durum: TASLAK — kullanıcıyla gözden geçirilecek; görev sınırları dondurulmadı.
- Tarih: 2026-11-06
- Platform: Windows ARM64 (Surface 11 / Snapdragon X Elite) ve macOS ARM64 (Mac mini 2024 / Apple M4).
- Çalışma/veri alanı: ADR-029 uyarınca harici SSD.

## Tasarım kararı adayı

Kullanıcının açıp çalıştıracağı iki ana program korunur. Bunlar tek parça büyük Python dosyaları değildir; küçük, bağımsız ve ayrı ayrı yeniden çalıştırılabilir görev modüllerini çağıran iki giriş noktasıdır.

| Program | Kullanıcıya görünen adı | Sorumluluk | Girdi | Kalıcı çıktı |
|---|---|---|---|---|
| PY-01 | BERO Importer | Gelen-kutu dosyalarını doğrulayıp değişmez RAW arşive almak | HA History dışa aktarım dosyaları | RAW, manifest, log |
| PY-02 | BERO Analyzer | RAW arşivi incelemek ve türetilmiş analiz/eğitim çıktıları üretmek | Yalnız PY-01 arşivi | PROCESSED, TRAINING, rapor, checkpoint |

## Küçük görev modülleri — ilk taslak

### PY-01 BERO Importer

| Görev ID | Modül adı önerisi | Tek sorumluluk | Başarılı çıktı |
|---|---|---|---|
| IMP-01 | inbox_scan | Gelen-kutudaki tamamlanmış dosyaları bulmak; kopyalanmakta olan dosyayı almamak | İşlenecek dosya listesi |
| IMP-02 | source_hash | SHA-256 hesaplamak ve yineleneni belirlemek | Hash/duplicate sonucu |
| IMP-03 | ha_csv_validate | CSV okunabilirliğini, başlıklarını ve satır yapısını doğrulamak | Doğrulama raporu |
| IMP-04 | raw_archive | Özgün dosyayı değiştirmeden RAW arşive almak | Arşiv dosyası ve manifest |
| IMP-05 | quarantine | Hatalı dosyayı kayıpsız biçimde karantinaya almak veya gelen-kutuda tutmak | Hata kaydı ve korunmuş kaynak |

### PY-02 BERO Analyzer

| Görev ID | Modül adı önerisi | Tek sorumluluk | Başarılı çıktı |
|---|---|---|---|
| ANL-01 | archive_inventory | RAW dosyaları ve manifestoları listelemek | Arşiv envanteri |
| ANL-02 | ha_data_profile | Kolon/entity, zaman, birim, boş/geçersiz/tekrar değer özetini çıkarmak | Veri profili |
| ANL-03 | event_packet_check | PZEM ve SCT olay akışlarını ayrı ayrı ADR-022/024 ile doğrulamak | Paket bütünlüğü raporu |
| ANL-04 | pzem_stability | PZEM akışında kararlı alan adaylarını bulmak | PZEM kararlılık çıktısı |
| ANL-05 | sct_stability | SCT kanallarında bağımsız kararlı alan adaylarını bulmak | Kanal bazlı SCT çıktısı |
| ANL-06 | stable_overlap | Aynı geçerli ON paketindeki kararlı alanların zaman kesişimini bulmak; ADR-028'i uygulamak | Eşleşmiş alan tablosu |
| ANL-07 | training_label | PZEM referans etiketini eşleşen SCT alanına eklemek; seti tek kanalda üretmek | Kanal bazlı eğitim verisi |
| ANL-08 | full_record_eval | Model/katsayıyı tam ham kayıtta davranış açısından değerlendirmek | Değerlendirme raporu |
| ANL-09 | report_export | Doğrulanmış görev çıktılarını rapora dönüştürmek | Rapor ve özet |

## Ortak çalışma kuralları

- Her görev tek sorumluluk, açık girdi/çıktı sözleşmesi ve sürüm kimliği taşır.
- Görevler SSD'de doğrulanmış ara çıktılar üzerinden haberleşir; birbirlerinin belleğine bağımlı olmaz.
- Görev kimliği + görev sürümü + girdi hash'i, tekrar çalıştırma/checkpoint anahtarının adayıdır.
- Yarım çıktı geçerli sonuç sayılmaz; geçici çıktı doğrulanınca nihai ada geçirilir.
- RAW dosyalar ve önceki başarılı çıktılar üzerine yazılmaz.
- Bir dosyanın/görevin hatası diğer bağımsız işleri durdurmaz.
- Ana giriş noktaları görev sırasını yönetir; algoritmaları kendi içinde taşımaz.
- Timeout, retry, paralellik ve checkpoint sıklığı gerçek veri/test görülmeden sabitlenmez.

## Henüz kararlaştırılmayanlar

1. İki ana program ve alt görev ayrımı son onaylı değildir; taslaktır.
2. Görevlerin ayrı Python dosyası mı yoksa paket içi modül mü olacağı.
3. Görev çalıştırıcı ve kalıcı durum deposunun teknik seçimi.
4. Gerçek CSV şeması, entity eşleme ve manifest biçimi.
5. Kararlılık algoritmalarının parametreleri.
6. Görevlerin otomatik sırası ve kullanıcı onayı gerektiren adımlar.

## İlgili kararlar

- ADR-026 — İki programın görev sınırı
- ADR-029 — Taşınabilir SSD çalışma alanı
- ADR-030 — Küçük ve devam edebilir görevler
- Python veri hattı mimarisi
- T007

Bu envanter tasarım tartışması içindir. Hiçbir görev uygulanmış veya test edilmiş sayılmaz.
