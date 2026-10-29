# SCT analog ön uç

**Durum: Hobi projesi için temel bağlantı ve bias yapısı belgelendi.** SCT013 jack üzerinden bias devresine bağlanacak ve ESP32'nin dahili ADC'siyle okunacaktır. Bu aşamada harici ADC kullanılmayacak; MCP3208 sonraki aşamaya ayrılmıştır.

## Mevcut bias devresi

Kullanıcı beyanına göre breadboard üzerinde:
- İki adet 10 kΩ dirençle oluşturulmuş orta nokta.
- **Mevcut kayıtlı durum:** orta nokta ile GND arasında 104 kodlu, 100 nF kondansatör.
- **İlk SCT bağlantılı ölçüm öncesi plan:** [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md) uyarınca mevcut 100 nF'ye paralel 10 µF bypass eklenmesi planlandı; fiziksel değişiklik henüz yapılmadı.
- Bias seviyesi yaklaşık **1,65 V** kabul edilir; bu aşamada ayrıca ölçülüp doğrulanması istenmiyor.

Bu kayıt, SCT AC sinyalinin bias noktasına kuplaj ayrıntılarının ölçümle doğrulandığı anlamına gelmez. Belirgin bir bağlantı sorunu normal kullanım sırasında görülürse not edilir; bu görev için laboratuvar düzeyinde doğrulama gerekmez.

## Eldeki SCT modelleri

- **SCT013-030:** Envanterde bulunan model; testte kullanıldığında test kaydına bu model kodu yazılır.
- **SCT013-100A-1V:** Envanterde bulunan gerilim çıkışlı model; testte kullanıldığında test kaydına bu model kodu yazılır.

Bu modellerin çıkış türleri aynı kabul edilmez. Hangi modelin kullanılacağı test bazında belirtilir; henüz tek bir model tüm testler için sabitlenmemiştir. Test sırasında kullanılan model ve bağlantı bilgisi kayıtla eşleştirilmelidir.

## Bu aşamanın kapsamı

- ESP32 dahili ADC kullanılacak; MCP3208 sonraki aşamadadır.
- Bias ayrı bir kanal/kayıt alanı olarak ileride yazılım ve veri kaydı aşamasında tutulacaktır; bu T004 ön koşulu değildir.
- ADC maksimum giriş aralığı, clipping payı, bias toleransı, yüksüz gürültü istatistiği veya en yüksek akımda clipping için laboratuvar düzeyinde hesap/ölçüm T004 kapanış şartı değildir.
- Ölçülmemiş değerler ölçülmüş gibi yazılmaz.

## Temel güvenlik

Hobi düzeyinde temel elektrik güvenliği ve sağduyulu bağlantı kontrolü uygulanır. Enerjili devrede bağlantı değiştirilmez ve açık iletkenlere dokunulmaz.

## Yeni belge incelemesi (2026-10-29)

Kullanıcının sağladığı SCT013-030 raporu ve CT satürasyonu metni genel teknik referans olarak incelendi; bunlar BERO'da uygulama veya fiziksel test kanıtı değildir.

- SCT013-030 nominali 30 A AC RMS → yaklaşık 1 V AC RMS; nominal oran 30 A/V (yaklaşık 33,33 mV/A).
- Gerilim çıkışlı modelde dahili burden direnci vardır; ek burden eklenmesi önerilmez.
- BERO devresinde 2 × 10 kΩ bölücünün orta noktasındaki mevcut 100 nF'ye paralel 10 µF eklenmesi, 50 Hz'de daha düşük AC empedans sağladığı için [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md) kapsamında planlandı. E00A'nın ilk SCT bağlantılı koşulundan önce uygulanması hedefleniyor; fiziksel değişiklik ve ölçüm henüz yok.
- Satürasyon genel CT riskidir; BERO'da kanıtlanmış arıza değildir.
- Raporun ESP32/ADS1115/RMS örnek kodları BERO firmware'i değildir. Dahili ADC ve T005/E01 kapsamı korunur.

## Bias kondansatörü kararı

Mevcut fiziksel kayıt 104 (100 nF) kondansatörü gösterir. E00A'nın ilk SCT bağlantılı koşulundan önce planlanan değişiklik, mevcut 104'ü yerinde bırakıp aynı Vmid–GND noktalarına 10 µF elektrolitik kondansatör ekleyerek paralel bağlamaktır. ADC GPIO'suna ayrıca 100 nF eklemek zorunlu değildir ve ilk E01 düzenine dahil edilmemiştir; kaynak empedansı/bant genişliği etkisi ayrıca değerlendirilir. Ayrıntı ve kaynaklar: [ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md).

## Bias kondansatörlerinin görev ayrımı

[ADR-007](../docs/decisions/ADR-007-bias-midpoint-capacitor.md) uyarınca 10 µF elektrolitik ve mevcut 104 (100 nF) seramik aynı Vmid–GND noktalarına paralel bağlanacak. 10 µF, 50 Hz bileşeni için daha düşük empedanslı baypas sağlar; 104 daha yüksek frekanslarda tamamlayıcı baypas sağlayabilir. İki parça da paraziti tamamen ortadan kaldırmaz. SCT'nin diğer çıkış ucu ESP32 ADC pinine gidecek; gerçek GPIO kart modelinin pin planıyla ayrıca doğrulanacak. GPIO34, ESP32-C3 kartlarında mevcut değildir.
