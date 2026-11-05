# 2026-11-05 — Modül 2 + Modül 3 kısa ortak yük testi

## Kapsam ve kaynak
Kullanıcının paylaştığı iki ESPHome logu birlikte incelendi:
- Modül 2: `Yapıştırılan metin(20261105-160018).txt`, 18:58:08.013–19:00:06.374.
- Modül 3: `Yapıştırılan metin (2).txt`, 18:57:30.292–19:00:27.416.
- Kullanıcı, testte SSR çıkışında akkor ampul bulunduğunu ve fiziksel yanıp sönmeyi görmek istediğini belirtti. Bu, E11 yüksüz deneyi değildir.

## Modül 3
- Wi-Fi/API ve PZEM UART 9600 baud çalışıyor.
- PZEM ON: 0.186–0.187 A, 42.0–42.6 W. OFF: 0.000 A, 0.00 W.
- Gerilim 226.5–228.4 V; frekans 49.9–50.0 Hz.
- BOOT_ID: `83DAAD0A8A5C1FE6695D5E1BC1CB1C72`; EVENT_ID 30–35 sıralı üretildi.
- ON geçişinde GPIO_ON_CONFIRMED görülüyor. OFF geçişlerinde GPIO_OFF_READBACK_MISMATCH tekrarlanıyor; açık konu.
- Ampulün fiziksel yanıp sönmesi kullanıcı tarafından gözlem amacı olarak bildirildi; log tek başına görsel kanıt değildir.

## Modül 2
- Üç SCT kanalı sıralı çalıştı; 59 adet ALL CHANNELS COMPLETE kaydı var.
- Ortak bias: 1.644–1.678 V; ortalama yaklaşık 1.66185 V.
- ON kararlı bölümünde tipik yayınlar: SCT1 yaklaşık 0.35–0.39 A; SCT2 0.52–0.55 A; SCT3 0.68–0.71 A.
- OFF sonrası ilk çevrimde 19:00:04 civarı: SCT1 0.180 A, SCT2 0.229 A, SCT3 0.189 A. PZEM aynı OFF döneminde 0.000 A gösteriyor; SCT OFF değerleri sıfırdan belirgin biçimde farklı.
- 19:00:02.971'de SCT3 0.892 A sıçraması, EVENT_ID 34 OFF geçişine çok yakın. Geçişe denk gelen pencere kararlı örnek sayılmamalı.
- Kanalların isimlerinde farklı iletken/sarım yerleşimleri var: Faz 2T, Nötr 4T, Faz 3T. Bu kısa test doğrudan katsayı/kalibrasyon kıyası değildir.

## UDP 4210 karşılaştırması
Ortak BOOT_ID: `83DAAD0A8A5C1FE6695D5E1BC1CB1C72`.

| EVENT_ID | STATE | Modül 3 gönderim | Modül 2 alım | Sonuç |
|---:|---|---|---|---|
| 30 | OFF | 18:58:02.760 | Modül 2 logu başlamadan önce | Kapsam dışı |
| 31 | ON | 18:58:22.822 | 18:58:22.843 | Alındı |
| 32 | OFF | 18:59:02.753 | 18:59:02.838 | Alındı |
| 33 | ON | 18:59:22.753 | 18:59:22.843 | Alındı |
| 34 | OFF | 19:00:02.752 | Logda görünmüyor | Eksik |
| 35 | ON | 19:00:22.756 | Modül 2 logu bitmiş | Değerlendirilemez |

Ortak kapsamda 31–34 olaylarının 3'ü alıcı logunda mevcut, 1'i görünmüyor. Bu yalnızca kısa test bulgusudur; uzun dönem kayıp oranı değildir. 30 alıcı başlangıcından önce; 35 alıcı logu bittikten sonra.

## Sonuç ve sonraki adım
- Modül 2 ve Modül 3 aynı ağda çalışıyor; UDP gönderim ve alım yolu doğrulandı.
- Kısa kayıtta EVENT_ID 34 alıcı logunda görünmüyor; aktarım kayıpsız kabul edilemez.
- Modül 3 OFF GPIO geri okuma uyarısı açık.
- PZEM OFF 0.000 A iken SCT OFF okumaları sıfırdan farklı; yüksüz taban/yerleşim ayrıca incelenmeli.
- Bu akkor ampullü kısa test E11 değildir. Sonraki adım ampulü güvenli biçimde devreden çıkarıp E11 kısa yüksüz ortak kontrolünü yapmak. Uzun gözlem ancak bu kontrol kabul edilirse başlar.

## Log örnekleri
Modül 3:
```text
[18:59:22.750] HA_EVENT_PUBLISHED ... EVENT_ID=33,STATE=ON
[18:59:22.753] UDP_EVENT_SENT ... EVENT_ID=33,STATE=ON
[18:59:27.422] BERO PZEM Akım >> 0.187 A
[18:59:27.423] BERO PZEM Güç >> 42.40 W
```
Modül 2:
```text
[18:59:22.843] UDP_EVENT_RECEIVED ... EVENT_ID=33,STATE=ON
[18:59:22.856] HA_EVENT_PUBLISHED ... EVENT_ID=33 STATE=ON
[18:59:22.930] BERO Mod2 SCT3 Faz 3T Akim >> 0.669 A
[19:00:04.425] BERO Mod2 SCT1 Faz 2T Akim >> 0.180 A
[19:00:04.714] BERO Mod2 SCT2 Notr 4T Akim >> 0.229 A
[19:00:04.934] BERO Mod2 SCT3 Faz 3T Akim >> 0.189 A
```
