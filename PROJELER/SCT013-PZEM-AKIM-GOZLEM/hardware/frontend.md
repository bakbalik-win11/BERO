# SCT analog ön uç

**Durum: Hobi projesi için temel bağlantı ve bias yapısı belgelendi.** SCT013 jack üzerinden bias devresine bağlanacak ve ESP32'nin dahili ADC'siyle okunacaktır. Bu aşamada harici ADC kullanılmayacak; MCP3208 sonraki aşamaya ayrılmıştır.

## Mevcut bias devresi

Kullanıcı beyanına göre breadboard üzerinde:
- İki adet 10 kΩ dirençle oluşturulmuş orta nokta.
- Orta nokta ile GND arasında 104 kodlu, 100 nF kondansatör.
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
