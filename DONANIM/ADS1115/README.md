# ADS1115 — ADC modülü donanım kaydı

## Kimlik ve envanter

- **Bileşen:** ADS1115 tabanlı ADC breakout/modül.
- **Adet:** 10 adet.
- **Stok durumu:** Mevcut; kullanıcı bildirimi.
- **Kullanım alanı:** BERO'da SCT013 analog sinyalinin harici ADC üzerinden okunması ve sensör/ADC davranış deneyleri.
- **Modül kimliği:** ADS1115-01 … ADS1115-10 (envanter takip etiketleri; kart üzerindeki üretici seri numarası değildir).
- **Kart üreticisi / satıcı / SKU:** Henüz kaydedilmedi.
- **PCB revizyonu ve üzerindeki ADS1115 entegre işaretlemesi:** Her kart için fiziksel kontrol bekliyor.
- **Önceki farklı marka ADS1115:** Yeni 10'lu gruptan ayrı tutulacak; eski modülün envanter kimliği ve adedi ayrıca netleştirilecek.

> Adet bilgisi 10 adet modül olarak kullanıcı tarafından bildirilmiştir. Bu kayıt, on kartın aynı üretim partisi, aynı PCB revizyonu veya aynı elektriksel performansta olduğunu kanıtlamaz.

## Üretici entegresi — ADS1115

ADS1115, Texas Instruments üretimi 16 bit, I²C arayüzlü, delta-sigma analog-sayısal dönüştürücüdür. Dört tek uçlu giriş veya iki diferansiyel giriş seçeneği vardır; giriş çoklayıcısı ve programlanabilir kazanç yükselteci (PGA) içerir.

| Özellik | Üretici verisi |
|---|---|
| Çözünürlük | 16 bit |
| Mimari | Delta-sigma |
| Giriş | 4 tek uçlu veya 2 diferansiyel |
| Arayüz | I²C |
| Programlanabilir veri hızı | 8–860 SPS |
| PGA tam ölçek aralıkları | ±0,256 V ile ±6,144 V |
| Besleme aralığı | 2,0–5,5 V |
| I²C adres seçenekleri | ADDR pinine bağlı 4 adres |
| Çalışma sıcaklığı | −40 °C … +125 °C |

**Önemli ayrım:** PGA ayarı ADC'nin ölçüm tam ölçek aralığını değiştirir; harici analog yükselteç değildir. Modül kartının besleme, pull-up, regülatör ve giriş koruma devresi üretici entegresinin özelliklerinden ayrı değerlendirilmelidir.

## BERO'da mevcut kullanım / test bağlamı

- Önceki ESP32D2 denemesinde I²C: SDA GPIO21, SCL GPIO22.
- Önceki kart bağlantısında ADDR → GND ile I²C adresi 0x48 olarak taramada görüldü.
- Önceki denemelerde A0–A1 diferansiyel okuma kullanıldı.
- ESPHome loglarında Gain 2, Resolution 16 ve Sample rate 7 ayar metinleri görüldü. Bu ayarlar ve log ifadeleri her yeni firmware için yeniden doğrulanmalıdır.
- Yeni 10'lu gruptan modüllerle yapılan ilk gözlemlerde yüksüz durumda zaman zaman NaN ve yaklaşık 0,1 A civarında sayısal okuma görüldü. Bu gözlem bir kalibrasyon sonucu veya gerçek yüksüz akım kanıtı değildir.
- Kullanıcı, yeni modüllerde henüz spike gözlemlemediğini bildirdi. Uzun süreli kayıt devam ediyor; kararlılık sonucu henüz kesinleşmedi.
- Önceki farklı marka ADS1115'in yüksüz davranışı farklı gözlendi. Marka farkının sebep olduğu henüz kanıtlanmadı.

## SCT013 bağlantısı ve güvenlik notları

ADS1115 analog girişleri, entegre besleme raylarına göre sınırlandırılmıştır. PGA tam ölçek aralığı, giriş pinlerinin mutlak maksimum gerilim sınırını yükseltmez. SCT013 AC çıkışı doğrudan tek uçlu ADC girişine uygulanmamalıdır: negatif yarım dalga giriş sınırını ihlal edebilir.

BERO'da biaslı ve biasız bağlantı karşılaştırması planlanmıştır. Biasız deney öncesinde osiloskopla ADC girişinin GND'ye göre gerilim aralığı kontrol edilmeli; giriş sınırı ihlali riski giderilmeden ADC'ye doğrudan bağlantı yapılmamalıdır. Diferansiyel ölçüm de giriş pinlerinin ortak-mod ve mutlak gerilim sınırlarını ortadan kaldırmaz.

Kartın A0/A1 pinleri, besleme gerilimi, pull-up gerilimleri ve gerçek giriş topolojisi kart üzerindeki devre izleri/ölçümle doğrulanmalıdır. ESP32 ile I²C lojik seviyeleri uyumlu olmalıdır.

## Modül bazlı kabul / karakterizasyon kayıtları

Her kart ayrı kimlikle test edilir. Yeni partiye tek bir ortak katsayı veya ortak davranış atfedilmez.

| Kimlik | Fiziksel kart/PCB revizyonu | I²C adresi | İlk I²C testi | Yüksüz davranış | Yük testi | Katsayı / kalibrasyon |
|---|---|---|---|---|---|---|
| ADS1115-01 | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Yapılmadı |
| ADS1115-02 | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Yapılmadı |
| ADS1115-03 | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Yapılmadı |
| ADS1115-04 | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Yapılmadı |
| ADS1115-05 | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Yapılmadı |
| ADS1115-06 | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Yapılmadı |
| ADS1115-07 | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Yapılmadı |
| ADS1115-08 | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Yapılmadı |
| ADS1115-09 | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Yapılmadı |
| ADS1115-10 | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Bekliyor | Yapılmadı |

Karakterizasyon deneyinde aynı ESP32, SCT, kablo/turn oranı, I²C ayarı, PGA, veri hızı, filtre ve firmware koşulları korunmalı. PZEM karşılaştırma referansıdır; mutlak ground truth olarak tanımlanmaz. Her yük seviyesinde 5–10 eşleştirilmiş ADS/PZEM kaydı ve bireysel satırlar saklanır. Katsayı tek yük noktasından genellenmez.

## Üretici kaynakları

- [Texas Instruments — ADS1115 ürün sayfası](https://www.ti.com/product/ADS1115)
- [Texas Instruments — ADS111x veri sayfası, SBAS444E (PDF)](https://www.ti.com/lit/ds/symlink/ads1115.pdf)

**Kayıt sınırı:** Yukarıdaki elektriksel özellikler TI entegresine aittir. Breakout kartının üreticisi, PCB devresi, gerçek giriş koruması ve BERO'daki ölçüm performansı ayrıca doğrulanmalıdır.
