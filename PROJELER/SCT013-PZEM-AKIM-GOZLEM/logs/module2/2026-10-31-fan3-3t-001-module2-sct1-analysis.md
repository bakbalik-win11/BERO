# FAN-3-3T-001 — üç primer tur log analizi

## Kaynak ve kapsam
- Kaynak dosya: `esp32d1-logs (47).txt`
- Kaynak boyutu: 129.554 bayt; 1.744 satır.
- Kaynak SHA-256: `fb48997412ced2a9f769b3084bec9f63dab8ef7174efea23062ce4e63dbc735c`
- Ölçüm akım yayınları: 18:30:59.057–18:38:49.014 (+03:00), 236 yayın, yaklaşık 7 dk 50 sn.
- Önceki `esp32d1-logs (46).txt` dosyası bu uzun logun birebir başlangıç önekidir; ayrı oturum veya ek ölçüm olarak sayılmadı. Dosya 46 SHA-256: `27567257b0cdf05766899da3f5d8db59410069e236a92037e5c72321df0f659e`.

## Donanım ve firmware (logdan)
- ESP32D1 / Modül 2; SCT-1 GPIO32 / ADC1_CH4; ortak bias GPIO35 / ADC1_CH7.
- ESPHome 2026.10.1; cihaz derleme zamanı 2026-10-31 15:55:25 +0300.
- ADC attenuation 12 dB, entity güncellemesi 1 s; ct_clamp penceresi 200 ms, yayın aralığı 2 s.
- SPS: ortalama 17.321,6; min–maks 16.890–18.430.
- Firmware katsayısı K=24.22; yazılımsal sıfır eşiği yok.
- YAML açılış/kapanış snapshot'ı: `firmware/archive/FAN-3-3T-001-2026-10-31-esp32d1-sct1.yaml`; aktif YAML ile aynı içerik olduğu arşivleme sırasında kontrol edildi. Binary eşleşmesi iddia edilmez.

## Akım ve analog istatistikleri
| Alan | Yayın | Ortalama | Medyan | Min–maks |
|---|---:|---:|---:|---:|
| Firmware akım göstergesi, tüm yayınlar | 236 | 0,416089 A | 0,413 A | 0,392–0,932 A |
| Firmware akımı, tekil sıçrama hariç | 235 | 0,413894 A | 0,413 A | 0,392–0,454 A |
| Raw AC, tüm yayınlar | 236 | 0,017180 V | 0,01704 V | 0,01620–0,03849 V |
| Raw AC, sıçrama hariç | 235 | 0,017089 V | 0,01704 V | 0,01620–0,01873 V |
| Bias GPIO35 | 471 | 1,662684 V | 1,662 V | 1,642–1,686 V |
| SCT ADC GPIO32 | 471 | 1,657652 V | 1,651 V | 1,618–1,701 V |

- Tekil sıçrama: 18:31:57.032'de Raw AC 0,03849 V ve akım 0,932 A. Bu değer ham veri içinde korunmuştur; ana dağılım özeti için ayrıca işaretlenerek dışarıda bırakılmıştır. Otomatik veri silme yapılmadı.
- Logda 3 derleyici/optimizasyon uyarısı var. Görünen kayıtta runtime `[E]`, brownout veya reboot işareti yok.

## Üç tur normalizasyonu ve tek tur karşılaştırması
- 235 olağan yayının firmware akım göstergesi / 3 sonucu: ortalama **0,137965 A**, medyan **0,137667 A**, min–maks **0,130667–0,151333 A**.
- FAN-3 için en güncel UNIT bildirimi 0,142 A'dır (kullanıcı bildirimi; PZEM değildir). Normalize ortalama UNIT bildiriminden yaklaşık **-%2,84**, medyan yaklaşık **-%3,05** farklıdır. Bu yalnızca betimleyici aritmetik karşılaştırmadır; 0,30 A altı için ±%4 kabul/ret uygulanmaz.
- Önceki tek tur FAN-3 logu: akım ortalaması 0,224612 A; Raw AC ortalaması 0,009273 V.
- Bu 3T logunun sıçrama hariç akım ortalaması / önceki 1T ortalaması yaklaşık **1,843x**; Raw AC oranı yaklaşık **1,843x**. İdeal 3x doğrusal artış gözlenmedi. /3 hesabının UNIT'e yakın çıkması tek başına sarım doğrusal davranışını veya kalibrasyonu kanıtlamaz.

## Kanıt sınırları
- Logda PZEM akımı, gerilimi, aktif güç veya PF yoktur. UNIT 0,142 A logun içinden okunmamıştır; önceki kullanıcı bildirimidir.
- Logun kendisi fiziksel primer tur sayısını kaydetmez. 3T düzeni deney bağlamına dayanır; logdan bağımsız fiziksel fotoğraf/işaret doğrulaması yoktur.
- ct_clamp 200 ms ölçüm penceresi ve 2 s yayın hattı gözlenmiştir; bu log fiziksel sensörün saf tepki süresini ölçmez.
- Bu deney düşük akım gözlemidir; ±%4 doğrulaması, PZEM doğrulaması veya genel kalibrasyon değildir.

## Kapanış kararı
FAN-3-3T-001, mevcut logla **düşük akım üç-tur gözlem oturumu** olarak kapatıldı. K=24.22 ve firmware değiştirilmedi; gösterge/3 yalnız deneysel normalizasyon olarak tutuldu. Tekil sıçrama ham kayıtta korundu. Ayrı düşük akım ESP/model eğitimi, ek uzun loglar ve PZEM akım+PF ile eşleşmiş kararlı pencereler sonraki işlerdir.

## İlgili kayıtlar
- [Test kaydı](../../test-loads/fan3-3turn/README.md)
- [Kapanış YAML snapshot](../../firmware/archive/FAN-3-3T-001-2026-10-31-esp32d1-sct1.yaml)
- [Önceki tek tur FAN-3 logu](2026-10-31-fan3-module2-sct1-long-full.txt)
- [Önceki tek tur FAN-3 analizi](2026-10-31-fan3-module2-sct1-long-analysis.md)
