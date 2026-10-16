# HDF2-GRV-002 / Alt Görev 1 — İlerleme Raporu

**Son güncelleme:** 2026-10-16  
**Durum:** AÇIK — ilk gerçek ham kayıt bekleniyor  
**Hedef:** Tek ESP32-WROOM ile SCT ve BIAS sinyallerini en yüksek güvenilir hızda yakalamak, ham veriyi Mac'e aktarmak ve dalgaları çizmek.

## İlerleme

| Step | İş | Durum | Kanıt |
|---|---|---|---|
| STEP-000 | Alt görevi ve kayıt düzenini oluşturma | TAMAM | Bu klasör ve ana görev README'si |
| STEP-001 | Önceki GRV-008.2 aday kodunu bulma ve depoya alma | KOD ADAYI KAYDEDİLDİ; DERLEME BEKLİYOR | KOD/GRV-008.2_candidate.ino ve Python alıcısı; derleme/test kanıtı yok |
| STEP-002 | Tek ESP'den ham SCT/BIAS örneklerini yakalama | BEKLİYOR | Henüz kayıt yok |
| STEP-003 | Ham veriyi Mac'e aktarma ve bütünlük kontrolü | BEKLİYOR | Henüz kayıt yok |
| STEP-004 | SCT ve BIAS dalgalarını çizme | BEKLİYOR | Henüz grafik yok |
| STEP-005 | Güvenilir en yüksek örnekleme hızını kanıtla belirleme | BEKLİYOR | Gerçek zamanlama ve kayıp ölçümü yok |

## Sabit teknik sınırlar

- İlk testte tek ESP32-WROOM; MCP3208 kullanılmaz.
- GPIO34 / ADC1_CH6 SCT ve GPIO35 / ADC1_CH7 BIAS adaylarıdır; fiziksel bağlantı test öncesi doğrulanır.
- 10 kHz başlangıç referansıdır; kanıtlanmış maksimum hız değildir.
- Ham örnekler korunur. Bu aşamada RMS, filtreleme, BIAS çıkarma, kalibrasyon veya akım hesabı yapılmaz.
- DMA callback süreleri tek başına gerçek ADC örnek aralığını kanıtlamaz.
- Üç ESP'li 1T/2T/4T yapısına ancak tek ESP zinciri doğrulandıktan sonra geçilir.

## Açık işler

1. ESP32-WROOM için uygun sürekli ADC örnekleme yolunu seçip kod adayını hazırlamak.
2. Derleme çıktısını ve kod sürümünü saklamak.
3. İlk ham kaydı almak; örnek sayısı/sırası, zamanlama ve taşma göstergelerini kontrol etmek.
4. Ham kayıt dosyasını Mac'te doğrulamak.
5. SCT ve BIAS grafiğini üretmek ve kanıtları bu klasöre kaydetmek.

## Kesin devam noktası

**STEP-001:** ESP32-WROOM dahili ADC sürekli örnekleme yöntemi ve mevcut kod adayı incelenecek. Kod derlenmeden veya fiziksel test yapılmadan başarı işaretlenmeyecek.

Her yeni “sakla” talebinde bu rapor ilerleme durumuyla güncellenecek ve yeni kod/log/rapor sürümleri bu klasöre eklenecek.


## 2026-10-16 — Önceden hazırlanmış GRV-008.2 kod adayları bulundu

Kullanıcının 2026-10-13 tarihli önceki çalışma kaydında yer alan ESP32-WROOM ADC Continuous/DMA kodu ve Python alıcısı Alt Görev 1'in KOD klasörüne kopyalandı. Yeni kod yazılmadı; adaylar yeniden kullanılmak üzere korunuyor.

- ESP kodu: `KOD/GRV-008.2_candidate.ino`
- ESP kod açıklaması: `KOD/GRV-008.2_candidate.md`
- Python alıcısı: `KOD/grv008_test_receiver.py`
- Python açıklaması: `KOD/grv008_test_receiver.md`

**Durum:** Aday kodlar kaydedildi. Henüz derleme, cihaza yükleme, TEST-001/100 frame veya gerçek dalga grafiği yapılmadı. Bu nedenle hiçbir test PASS değil.

**Teknik kontrol noktaları:** Arduino-ESP32 sürümüne göre API/derleme; frame boyu ve Python struct uyumu; callback zaman damgalarının gerçek örnekleme aralığını kanıtlamaması; gerçek Mac seri portunun ayarlanması.

**Kesin devam noktası:** Mevcut GRV-008.2 adayını yeni kod yazmadan incele, ESP32-WROOM hedefinde derle; derleme başarılıysa TEST-001'e geçip sensör bağlı/yük kapalı koşulunda 100 frame al.
