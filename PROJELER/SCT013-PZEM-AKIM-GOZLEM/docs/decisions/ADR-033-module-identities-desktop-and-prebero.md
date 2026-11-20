# ADR-033 — BERO modül kimlikleri ve PREBERO saha dönemi

- **Tarih:** 2026-11-20 (kullanıcı açıklamasıyla güncellendi)
- **Durum:** KABUL EDİLDİ — modül numaralandırması, PREBERO kapsamı ve fiziksel yaşam döngüsü
- **Karar sahibi:** Kullanıcı

## PREBERO ne demek?

**PREBERO**, BERO'nun kurulacağı eve henüz taşınılamadığı dönemde, BERO'nun kurulacağı evdeki kiracı çıkana kadar Sarıyer'deki mevcut evde yürütülen hazırlık, gözlem, deney ve veri toplama dönemidir.

Bu dönem yalnızca Modül 7'den ibaret değildir. **Modül 5, Modül 6 ve Modül 7'nin tamamı PREBERO kapsamındadır.** Amaç, mevcut evdeki çamaşır makinesini, bulaşık makinesini ve evin ana elektrik hattını izleyerek veri toplamak; cihaz davranışlarını incelemek ve BERO'nun kurulacağı eve geçmeden önce proje ilerlemesi sağlamaktır.

PREBERO, nihai BERO kurulumu değildir. Mevcut evdeki geçici saha/deney ortamıdır. BERO'nun kurulacağı eve geçiş, kiracının çıkması ve taşınma/kurulum koşullarının oluşmasına bağlıdır.

## Kabul edilen modül envanteri

| Kimlik | Tanım | İşlev / durum |
|---|---|---|
| **Modül 1** | Bağımsız bias trafosu / güç kutusu | Mevcut donanım; korunacak. Modül 4 masaüstü biaslı/bias'sız karşılaştırma deneylerinde kullanılacak. |
| Modül 2 | Eski üç kanallı biaslı SCT okuma modülü | Fiziksel olarak imha edildi. ADS1115 ile hedeflenen akım okuma sınırları içinde ölçüm yapılabildiğinden eski fiziksel modüle ihtiyaç kalmadı. Kodlar ve deney kayıtları tarihsel arşivdir. |
| Modül 3 | Eski PZEM + SSR olay modülü | Fiziksel olarak imha edildi. ADS1115 ölçüm yoluna geçiş ve eski düzenin artık gerekmemesi nedeniyle fiziksel modüle ihtiyaç kalmadı. Kodlar ve deney kayıtları tarihsel arşivdir. |
| **Modül 4** | Günlük masaüstü ESP32D2 + ADS1115 + SCT ölçüm düzeneği | Mevcut masaüstü deney düzeneği. Günlük ölçüm ve biaslı/bias'sız karşılaştırma çalışmaları burada yürütülür. |
| **Modül 5 — PREBERO** | Çamaşır makinesi gözlem modülü | Sarıyer'deki mevcut evde çamaşır makinesi davranışını izlemek ve veri toplamak için imal edilecek. |
| **Modül 6 — PREBERO** | Bulaşık makinesi gözlem modülü | Sarıyer'deki mevcut evde bulaşık makinesi davranışını izlemek ve veri toplamak için imal edilecek. |
| **Modül 7 — PREBERO** | Ana hat + PZEM gözlem modülü | Sarıyer'deki mevcut evin ana elektrik hattını PZEM ile birlikte izlemek ve veri toplamak için geliştirilecek. |

## Modül 1–4 ilişkisi

- Modül 1 imha edilmemiştir; mevcut bias trafosu/güç kutusu korunur.
- Modül 1, Modül 4 masaüstü düzenekte biaslı ve bias'sız ölçüm karşılaştırmalarında kullanılacaktır. Modül 1'in korunma gerekçesi budur.
- Modül 2 ve Modül 3 fiziksel olarak imha edilmiştir. Kullanıcı açıklamasına göre ADS1115 ile akımı istenen sınırlar içinde okuyabildiğimiz için eski fiziksel düzeneklere ihtiyaç kalmamıştır.
- Modül 2/3'ün eski YAML, firmware, log, deney ve karar kayıtları tarihsel kanıt olarak depoda tutulur; fiziksel modüllerin mevcut olduğu izlenimi verilmez.
- Modül 4 mevcut günlük masaüstü deney düzeneğidir. E22, Modül 4'te ileride yapılması düşünülen ayrı bir SCT karşılaştırma deneyidir; modül değildir.

## Modül 5–7: PREBERO saha veri toplama

- Modül 5 çamaşır makinesini gözler.
- Modül 6 bulaşık makinesini gözler.
- Modül 7 evin ana hattını PZEM ile birlikte gözler.
- Üç modül aynı PREBERO saha döneminin parçalarıdır; her biri ayrı modül ve ayrı veri kaynağıdır.
- Bu modüllerin amacı mevcut Sarıyer evinde veri toplamak, cihaz/ana hat davranışlarını incelemek ve BERO'nun kurulacağı eve geçişten önce teknik ilerleme sağlamaktır.
- PREBERO'da toplanan veriler ve edinilen deneyim, nihai BERO kurulumuna hazırlık girdisi olur. PREBERO donanımının nihai eve taşınacağı veya nihai BERO mimarisinin birebir aynı olacağı, ayrıca karar verilmeden varsayılmaz.
- Modül 5 ve 6'nın elektronik tasarımının ikiz olması kararı ADR-032'de korunur.
- Modül 7'nin PZEM ile ana hattı okuması üst düzey amaçtır; CT modeli, ölçüm topolojisi, ESP kartı, bağlantılar, haberleşme, firmware ve güvenlik düzeni ayrıca tasarlanıp doğrulanacaktır.

## E22 — Modül değil, henüz yapılmamış deney fikri

Modül 4'ün ESP32D2 + ADS1115 + SCT ölçüm zinciriyle ilgili mevcut çalışmaların başarılı/kararlı ilerlemesinden sonra, bir kanalda 30 A / 1 V, diğer kanalda 100 A / 1 V SCT ile karşılaştırma yapılması düşünülmüştür. E22 kapsamında 100 A / 1 V SCT ile bugüne kadar ölçüm alınmamış, bağlantı kurulmamış ve ayrı bir modül imal edilmemiştir. Ayrıntı [E22 deney kaydındadır](../../experiments/E22-sct100a-1v-ads1115-characterization/README.md).

## Tarihçe ve geçerlilik

- 2026-11-13 tarihli eski kayıtlarda 100 A / 1 V SCT + ADS1115 + PZEM fikri Modül 4 olarak adlandırılmıştı. Bu eski plan güncel değildir; fiziksel olarak kurulmuş modül/ölçüm kanıtı değildir.
- 2026-11-20 tarihli eski kayıtlarda çamaşır/bulaşık modülleri Modül 4/5 olarak adlandırılmıştı. Güncel kimlikler Modül 5/6'dır.
- Eski kayıtlar silinmez. Güncel modül kimlikleri ve PREBERO tanımı için bu ADR esas alınır.

## İlgili dosyalar

- [Modül 5 — Çamaşır makinesi](../devices/washing-machine/README.md)
- [Modül 6 — Bulaşık makinesi](../devices/dishwasher/README.md)
- [E22 — 30 A / 1 V ve 100 A / 1 V karşılaştırma fikri](../../experiments/E22-sct100a-1v-ads1115-characterization/README.md)
- [ADR-032 — İkiz gözlem modülleri](ADR-032-washing-dishwasher-twin-sensor-modules.md)
