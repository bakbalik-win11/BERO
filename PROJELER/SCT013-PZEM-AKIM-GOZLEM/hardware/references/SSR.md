# SSR — Donanım Referansı

> **Proje referans kopyası — 2026-10-27.** Kaynak: [`DONANIM/SSR/README.md`](../../../../DONANIM/SSR/README.md). Kaynak `DONANIM/` belgesi asıl kayıttır.
> Bu kopya, mevcut donanım notlarının bu projede erişilebilir olması içindir; önceki test düzeneğinin bu projeye bağlandığı veya SSR modelinin doğrulandığı anlamına gelmez.


Proje BERO'da ESP32-C3-SSR test düzeneğinde kullanılan SSR için kayıt klasörü.

## Mevcut proje bilgisi

- Kontrolcü: ESP32-C3
- Proje notlarında SSR kontrol pini: GPIO6
- GPIO6 yapılandırması, SSR'nin fiziksel çıkışının veya yükün gerçekten anahtarladığını tek başına doğrulamaz.
- Mevcut sohbet kayıtlarında SSR'nin üzerindeki üretici/model işareti kesin olarak belirlenmedi.

## Veri sayfası durumu

`datasheets/README.md` içinde üretici Omron'un G3MB serisi için resmî veri sayfası bağlantısı bulunur. **G3MB yalnızca aday referanstır; SSR üzerindeki model numarası doğrulanmadan bu veri sayfası donanımın kesin veri sayfası sayılmamalıdır.**

SSR'nin üzerindeki model/etiket fotoğrafı veya tam model numarası elde edildiğinde bu klasördeki veri sayfası kesinleştirilmeli.

## Güvenlik ve doğrulama

- SSR giriş gerilimi, çıkış türü (AC/DC), yük gerilimi ve akım kapasitesi model numarasından doğrulanmalıdır.
- ESP GPIO durumunun değişmesi, SSR çıkışının veya yükün değiştiğini kanıtlamaz.
- Şebeke gerilimiyle yapılan testler uygun izolasyon ve güvenlik önlemleriyle gerçekleştirilmelidir.
