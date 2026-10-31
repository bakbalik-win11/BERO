# BREAD-TOASTER-001 — Ekmek kızartma makinesi / Log 63 teknik raporu

- **Tarih:** 2026-10-31
- **Test ID:** BREAD-TOASTER-001
- **Yük:** Ekmek kızartma makinesi (KULLANICI BİLDİRİMİ). Cihaz etiketi/gücü ve marka-modeli paylaşılmadı.
- **Referans:** UNIT 3,30 A (KULLANICI BİLDİRİMİ). PZEM değildir. UNIT ölçümünün logdaki SCT kararlı penceresiyle tam zaman eşleşmesi ayrıca belgelenmedi.
- **Kaynak:** `esp32d1-logs (63).txt`; 32.064 bayt, 449 satır, 32.056 UTF-8 karakter.
- **Kaynak SHA-256:** `cf9254185e591650a06a990e5bc0f567ee499ba4ec541c4bb8748b132513f896`.
- **Cihaz/yazılım:** ESP32D1, ESP32 rev3.1, ESPHome 2026.10.1.
- **Kanal:** Modül 2 / SCT-1 GPIO32 ADC1_CH4; ortak bias GPIO35 ADC1_CH7.
- **Yapılandırma:** ADC 12 dB / 1 s; ct_clamp 0,20 s örnek penceresi / 2 s yayın. Mevcut K=24.22; firmware değişikliği yapılmadı.

## HEDEF

Ekmek kızartma makinesinin yaklaşık 3,3 A UNIT bildirimi çevresinde SCT-1 çıktısının davranışını mevcut firmware ve K=24.22 ile gözlemek. Bu kayıt Python modelleme, katsayı güncelleme veya kalibrasyon çalışması değildir.

## LOG — kararlı SCT bölümü

Toplam 51 SCT akım yayını bulundu. İlk yayın 22:31:30.257'de 3,027 A ve yalnız 186 örnek / 930 SPS ile raporlanmıştır. Sonraki pencerelerde örnek sayısı yaklaşık 3.500–3.667 ve SPS 17.635–18.335 aralığındadır. İlk düşük örnek sayılı açılış yayını kararlı istatistiklerden ayrı tutuldu; aşağıdaki özet kalan 50 yayını kapsar.

| Ölçüt | Sonuç |
|---|---:|
| Kararlı bölüm yayın sayısı | 50 |
| İlk / son yayın | 22:31:32.227 – 22:33:10.230 |
| Ortalama SCT akımı | 3,09636 A |
| Medyan | 3,094 A |
| Min–maks | 3,071–3,144 A |
| Örnek standart sapma | 0,01340 A |
| CV | %0,433 |
| Raw AC ortalaması | 0,127843 V |
| Raw AC min–maks | 0,12681–0,12979 V |
| SPS ortalaması | 18.117 |
| SPS min–maks | 17.635–18.335 |

## HESAP — UNIT ile betimleyici fark

- UNIT: 3,30 A (kullanıcı bildirimi).
- Kararlı SCT ortalaması: 3,09636 A.
- Mutlak fark: SCT − UNIT = −0,20364 A.
- UNIT'e göre aritmetik fark: −%6,17.

Bu yüzde, UNIT ile SCT ölçümlerinin aynı kararlı zaman penceresinde alındığı doğrulanmadığından **eşzamanlı doğruluk sapması değildir**. PZEM verisi bu logda yoktur. Değer yalnız mevcut iki bildirimin betimleyici aritmetik karşılaştırmasıdır.

## Analog ve cihaz gözlemleri

- GPIO35 ortak bias: 101 yayın; medyan 1,664 V, ortalama 1,66203 V, min–maks 1,565–1,669 V. 22:31:56.896'da görülen 1,565 V tekil düşük örneği izleyen örneklerde yaklaşık 1,66 V seviyesine dönmüştür; nedeni bu logdan belirlenemez.
- GPIO32 SCT ADC voltajı: 101 yayın; 1,483–1,843 V. Bunlar 1 saniyelik anlık ADC voltaj yayınlarıdır; doğrudan Raw AC RMS veya akım referansı olarak yorumlanmaz.
- Raw AC: kararlı 50 yayında ortalama 0,127843 V.
- ESPHome bağlantısı ve ADC/ct_clamp başlatma durumları OK. Logda ERROR, timeout, brownout veya reboot kaydı yok. Üç framework optimizasyon önerisi uyarısı vardır; ölçüm hatası olarak sınıflandırılmadı.

## SONUÇ

1. SCT-1, yaklaşık 3,1 A gösterge seviyesinde bu kısa log boyunca dar dağılım göstermiştir (CV %0,433).
2. UNIT 3,30 A ile SCT ortalaması arasındaki aritmetik fark −%6,17'dir. Zaman eşleşmesi doğrulanmadığı için bu sonuç kalibrasyon veya doğruluk kararı değildir.
3. Log, 3 A çevresinde yeni bir yük gözlemi sağlar; PZEM karşılaştırması içermez.
4. K=24.22 ve firmware korunmuştur. Bu tek logdan yeni katsayı/eğri türetilmemiştir.
5. Ekmek kızartma makinesi testi açık tutulur; tekrarlı log ve eşzamanlı UNIT/PZEM kararlı pencere kaydı beklenir.

## KANIT SINIRI / ARŞİV

- Kaynak dosyanın tam boyutu, satır sayısı ve SHA-256 değeri kaydedildi.
- Bu commit'te tam 449 satırlık ham TXT dosyası GitHub'a aktarılmadı; aşağıdaki evidence dosyası yalnızca seçilmiş gerçek log satırlarını içerir ve ham log yerine geçmez.
- Seçilmiş kanıt: [Log 63 evidence excerpt](../../logs/module2/2026-10-31-bread-toaster-001-module2-sct1-log63-evidence.txt).
- Kaynak dosya kullanıcı tarafından bu sohbet içinde sağlanmıştır; tam ham içerik konuşma eki olarak mevcuttur.

## DURUM

**ÖLÇÜLDÜ / YORUMLANDI — BREAD-TOASTER-001 açık.** Tek logluk SCT kararlılık gözlemi kaydedildi. Eşzamanlı referans doğrulaması, PZEM verisi ve tekrarlı deney bekleniyor.
