# 150 W Akkor Ampul — Karşılaştırmalı Ölçüm Kaydı

**Yük ID:** LOAD-150W-INC  
**Yük:** 150 W akkor ampul  
**Amaç:** Modül 2 / ESP32D1 üzerinde 150 W akkor yükle SCT kanalı ölçümlerini, firmware sürümünü, logları ve referans karşılaştırmalarını ayrı bir yük kaydında izlemek.  
**Durum:** LOAD-150W-001 fiziksel test sonucu analiz edildi; UNIT referansına göre ±%4 değerlendirmesi olumlu. PZEM karşılaştırması henüz yok.

## Tarihsel Faz 1 kıyası — yeni test sonucu değildir

ROADMAP ve Faz 1 deney arşivinde daha önce şu sonuç kayıtlıdır:

- Referans: 0,616 A
- Kod sonucu: 0,615 A
- Sapma: yaklaşık −%0,2

Bu değer tarihsel Faz 1 karşılaştırmasıdır. Yeni Modül 2 testinde kullanılacak ampulün aynı fiziksel ampul olduğu, besleme koşullarının eşleştiği veya referansın aynı cihazdan alındığı doğrulanmadı. Bu nedenle 0,616 A yeni test için kesin beklenen değer ya da PZEM referansı değildir.

## Yeni Modül 2 test koşulu

- Modül: BERO-SCT-OKUMA-TEST-002 / ESP32D1.
- Kanal: SCT-1 / sarı kablo / GPIO32 / ADC1_CH4.
- Ortak bias: turuncu kablo / GPIO35 / ADC1_CH7.
- Besleme: masaüstü harici güç kaynağı (kullanıcı bildirimi).
- Yük: 150 W akkor ampul.
- ESPHome: 2026.10.1; ESP32 rev3.1.
- Ölçüm: ADC 12 dB; ct_clamp 200 ms; yayın 2 s; K=24.22.
- Yazılımsal sıfırlama eşiği: yok.

## UNIT başvuru protokolü

Her test yükü için önce o yükün UNIT ölçümü alınır. SCT sonucu önce aynı yükün UNIT değeriyle karşılaştırılır. PZEM ölçümü sonraki aşamada eklenir; UNIT değeri PZEM değeri olarak adlandırılmaz. Bu oturumda UNIT okumaları 0,598 A ve 0,599 A olarak kullanıcı tarafından bildirildi; geçici referans ortalaması 0,5985 A'dır.

## Karşılaştırma tablosu

| Test ID | Tarih / saat | ESP / düzenek | SCT kanalı | Kod / sürüm | Log / analiz | Referans | Kod sonucu | Sapma | ±%4 durumu |
|---|---|---|---|---|---|---|---:|---:|---|
| LOAD-150W-001 | 2026-10-31, 16:31:30–16:44:32 (+03:00) | ESP32D1 / Modül 2 / masaüstü besleme | SCT-1 / GPIO32 / sarı | ESPHome 2026.10.1; ct_clamp 200 ms; K=24.22 | Ham kaynak: `esp32d1-logs (36).txt`; SHA-256 aşağıda. [Uzun log analizi](../../logs/module2/2026-10-31-load-150w-001-sct1-long-analysis.md) | UNIT 0,5985 A (kullanıcı bildirimi); PZEM yok | Ortalama 0,60821 A; medyan 0,608 A; n=391 | +%1,62 (ortalama) | 388/391 (%99,23) bant içinde |

### LOAD-150W-001 ham log kimliği

- Kullanıcı dosyası: `esp32d1-logs (36).txt`
- Boyut: 211.455 bayt
- SHA-256: `a407bc3363a804a4a72c06e0163119d3fac2243e8c802a7ff781038f699bdb4e`
- Log aralığı: 16:31:30.179–16:44:32.407 (+03:00)
- 391 akım yayını. Dosya 35'teki ilk 133 ölçüm bu logun başında aynen bulundu; aynı testin devamıdır, ayrı test değildir.
- Ham logun tam metni henüz GitHub'a eklenmedi; dosya kimliği ve analiz kaydedildi. Ham log aktarımı açık arşiv işidir.

## LOAD-150W-001 sonuç özeti

- UNIT okumaları: 0,598 A ve 0,599 A; ortalama 0,5985 A.
- UNIT ±%4 bandı: 0,57456–0,62244 A.
- SCT: 391 yayın; ortalama 0,6082148 A; medyan 0,608 A; min–maks 0,591–0,655 A; örnek SD 0,006595 A.
- Ortalama sapma: +%1,6232.
- Bandın içinde: 388/391 (%99,23).
- Bandın dışında kalanlar: 16:32:11.126 / 0,624 A; 16:32:57.122 / 0,655 A; 16:41:23.103 / 0,626 A.
- Raw AC ortalaması 0,0251121 V; ortak bias ortalaması 1,6636003 V; SCT-1 ADC ortalaması 1,661110 V.
- ct_clamp raporlanan SPS ortalaması yaklaşık 17.411.
- Üç derleyici/optimizasyon uyarısı; hata, brownout veya reboot işareti yok.
- K katsayısı 24.22 olarak korundu; değişiklik önerilmiyor.
- PZEM değeri logda yoktur. Bu sonuç UNIT karşılaştırmasıdır, PZEM doğrulaması değildir.

## Test oturumu kayıt standardı

Her yeni oturum ayrı Test ID alır; önceki satırlar değiştirilmez.

1. Tarih, başlangıç/bitiş saati ve gerçek log aralığı (Türkiye saati, UTC+03:00).
2. Ampulün fiziksel kimliği/etiketi ve test koşulu.
3. ESP, modül, SCT kanalı, kablo rengi ve GPIO.
4. Masaüstü besleme bilgisi; mümkünse ESP girişindeki gerilim ölçümü.
5. Firmware YAML snapshot'ı, commit SHA ve ESPHome derleme zamanı.
6. Ham log, satır sayısı, dosya boyutu ve SHA-256.
7. UNIT ve PZEM değerleri; ölçüm zamanı ve kararlı pencere.
8. Akım yayın sayısı, medyan, ortalama, standart sapma, min–maks ve kararlı pencere.
9. Referansla sapma; yalnız karşılaştırılabilir/eşzamanlı veri varsa.
10. ±%4 sonucu, teknik yorum, kanıt sınıfı ve açık eksikler.

## Sonraki adım

LOAD-150W-001 arşiv analiz adımı tamamlandı. Sıradaki ayrı deney SCT bağlı, primer akımı olmayan boşta okuma tabanını ölçmektir. Bu testte yazılımsal sıfır eşiği eklenmeyecek; ölçüm dağılımı ham haliyle gözlenecektir.

## Güvenlik

SCT yalnız tek yalıtılmış iletkeni çevrelemelidir; faz ve nötr birlikte geçirilmez. SCT/kanal bağlantısı değiştirilirken yük enerjisiz olmalıdır. Şebeke tarafı kapalı ve korumalı lamba düzeneğinde tutulmalıdır.
