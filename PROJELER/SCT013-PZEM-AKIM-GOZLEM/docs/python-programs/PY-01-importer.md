# PY-01 — BERO Importer

- Durum: TASLAK — kullanıcı incelemesi bekliyor.
- Tür: Kullanıcı tarafından başlatılan ana giriş noktası; küçük görev modüllerini yönetir.
- Platform: Windows ARM64 ve macOS ARM64.
- Çalışma alanı: Harici SSD.
- İlgili kararlar: ADR-026, ADR-029, ADR-030.
- İlgili görev: T007.

## Amaç

Kullanıcının Home Assistant History arayüzünden dışa aktardığı dosyaları SSD'deki gelen-kutudan güvenli biçimde alıp özgün içeriği değiştirilmeden RAW arşive taşımak. HA Recorder'a bağlanmaz; HA geçmişini silmez veya değiştirmez.

## Sorumluluk sınırı

Yalnız dosya kabulü, kaynak bütünlüğü, CSV doğrulaması, tekrar kontrolü, RAW arşivleme, manifest ve alım logundan sorumludur. PZEM/SCT kararlılık analizi, olay eşleştirmesi veya eğitim etiketi üretmez.

## Alt görevler

1. IMP-01 Gelen-kutu tarama: tamamlanmış dosyaları bulur; kopyalanması süren dosyayı işleme almaz. Tamamlanma kontrol yöntemi henüz seçilmedi.
2. IMP-02 Hash/tekrar kontrolü: SHA-256 hesaplar. Daha önce arşivlenmiş aynı içerik için ikinci RAW kopya üretmez.
3. IMP-03 CSV doğrulama: okunabilirliği, kolon başlıklarını ve temel satır yapısını inceler. Gerçek CSV görülmeden kolon/entity adı varsaymaz.
4. IMP-04 RAW arşivleme: doğrulanan dosyanın özgün baytlarını arşive alır. Arşiv hash'i kaynak hash'iyle eşleşmeden başarılı sayılmaz.
5. IMP-05 Hata/karantina: bozuk dosyayı silmez; karantinaya alır veya gelen-kutuda bırakır, hata nedenini kaydeder.

## Girdi

- SSD gelen-kutu alanındaki HA History dışa aktarım dosyası.
- Yinelenenleri tanımak için alım manifestosu.
- Gerçek CSV şeması incelendikten sonra onaylanmış doğrulama kuralları.

## Çıktı

- Değiştirilmemiş RAW kaynak dosyası.
- Dosya adı, hash, boyut, alım zamanı, doğrulama sonucu, arşiv yolu ve importer sürümünü içeren manifest kaydı.
- İşlem logu ve varsa karantina kaydı.

## Hata ve yeniden başlatma davranışı

- Kaynak dosya arşive güvenli biçimde kopyalanıp hash doğrulaması tamamlanmadan gelen-kutudan kaldırılmaz.
- Kesinti sırasında kalan geçici arşiv kopyası doğrulanmış nihai dosya sayılmaz.
- Yeniden başlatmada manifest ve hash ile son güvenli aşama bulunur.
- Aynı dosya tekrar görülürse mükerrer arşiv oluşturulmaz.
- Bir dosyanın hatası sıradaki bağımsız dosyaları engellemez.
- Manifest/log yazılamazsa işlem başarılı olarak işaretlenmez.

## Başarı ölçütleri

- Gerçek HA CSV okunup doğrulanır.
- Arşiv hash'i kaynak hash'iyle aynıdır.
- Yinelenen dosya ikinci kez arşivlenmez.
- Bozuk dosya kaybolmaz; hata nedeni görünür.
- Zorla kapatma ve yeniden açma testinde son güvenli adımdan devam eder.
- Windows ARM64 ve macOS ARM64 üzerinde ayrı çalıştırma testleri yapılır.

## Kapsam dışı

HA API/Recorder erişimi; HA tarafında veri silme; kaynak CSV'yi dönüştürme; SCT/PZEM analizi, kararlılık ve eğitim.

## Açık sorular

- Gelen-kutu tek seferlik mi taranacak, kullanıcı başlatınca izlenecek mi?
- Arşiv klasörlemesi tarih, oturum veya hash üzerinden mi?
- Dosya kopyasının tamamlandığı nasıl anlaşılacak?
- Manifest JSON Lines mı, SQLite mı olacak?
