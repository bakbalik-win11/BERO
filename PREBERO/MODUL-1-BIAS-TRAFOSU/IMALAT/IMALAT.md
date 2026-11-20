# Modül 1 – Şebeke Karakterinde Bias Gerilim Aktarımı – İmalat Kaydı

> **Durum: FİZİKSEL İMALAT TAMAMLANDI**
>
> Modül mevcut fiziksel yapısıyla imal edilmiştir. Kapalı kutu içindedir ve bağlantıları soketlidir. Bu dosya yeni imalat yapılacak bir şablon değil, mevcut donanımın imalat ve ölçüm kaydıdır.

## 1. Amaç

Modülün basit yaklaşımı, şebeke karakterini taşıyan gerilimi bias girişine aktarmaktır. Modül 1 bu aktarım için kullanılan fiziksel donanımdır. Masaüstü ESP ile yapılan akım/sinyal deneyleri Modül 2 kapsamındadır; Modül 1 bu deneylerde bias gerilimi sağlayan donanım olarak kullanılabilir.

## 2. Fiziksel imalat durumu

- İmalat: Tamamlandı.
- Muhafaza: Kapalı kutu.
- Bağlantı biçimi: Soketli.
- Modül yeniden imalat beklemiyor.
- Mevcut fiziksel düzen, eski kurulumun devamı niteliğindedir.

## 3. İmalat sırasında kaydedilmiş donanım bilgileri

Aşağıdaki parça ve yapı bilgileri önceki imalat kayıtlarından korunmuştur. Bu liste yeni bir envanter sayımı değildir.

| Parça / model | Önceki kayıttaki bilgi |
|---|---|
| RN130421, 6 V / 2.0 VA PCB tipi trafo | Kullanıldığı bildirilmiş |
| KBU610 / kullanıcı yazımı KBU610VETH | Köprü doğrultucu olarak kaydedilmiş |
| 2200 / 35 V kondansatör | Önceki kayıtta yer alıyor |
| L78L33, TO-92 | 3,3 V regülatör olarak kaydedilmiş |
| İki adet direnç | Ayrı ayrı 9,82 kΩ ölçülmüş |
| Seramik kondansatör, 104 | Önceki kayıtta 100 nF olarak tanımlanmış |
| Elektrolitik kondansatör, “10 50V” | Önceki kayıtta işaretleme bu şekilde aktarılmış |
| ESP | Önceki kayıtta bias karşılaştırması bağlamında anılmış |

## 4. Multimetre ölçüm kayıtları

Bu ölçümler önceki imalat sırasında alınmış ve kayda geçirilmiştir:

| Ölçüm noktası | Kaydedilen değer | Açıklama |
|---|---:|---|
| Modül çıkışı | 3,31 V | Bias yapısına uygulanan gerilim |
| Birinci direnç | 9,82 kΩ | Direnç devreden ayrılarak ölçüldü |
| İkinci direnç | 9,82 kΩ | Direnç devreden ayrılarak ölçüldü |
| İki direncin birleşim noktası | 1,65 V | Bias orta nokta gerilimi |

Bu değerler mevcut imalatın geçmiş ölçüm kayıtlarıdır. Yeni deney ölçümleriyle karıştırılmaz.

## 5. Bağlantı ve muhafaza

- Modül kapalı kutu içindedir.
- Modül bağlantıları soketlidir.
- Soketli yapı, modülün deney düzenine bağlanmasını ve gerektiğinde ayrılmasını sağlar.
- Bu dosyada soketlerin pin numaraları veya kablo eşleşmeleri hakkında yeni bir bilgi üretilmemiştir.
- Modülün fiziksel imalatı tamamlanmıştır; bu nedenle aşağıdaki kayıtlar yeni imalat işi olarak değil, mevcut donanımın tanımı olarak okunmalıdır.

## 6. Modül 2 ile ilişki

Masaüstü ESP üzerinde yürütülen akım/sinyal deneyleri Modül 2 – Masaüstü 4 Kanal / Akım Testleri kapsamındadır. Modül 1, bu deney düzeninde bias gerilimi sağlayan mevcut donanım olarak kullanılabilir. Deney kodu, ESP bağlantıları, loglar, ham veriler ve deney yorumları Modül 2'nin ilgili görevinde tutulur.

## 7. İmalat revizyon kaydı

| Tarih | Kayıt |
|---|---|
| 2026-11-20 | Önceki imalat ve multimetre ölçüm bilgileri kayda geçirildi. |
| 2026-11-21 | Fiziksel imalatın tamamlandığı; kapalı kutu ve soketli bağlantı yapısı bildirildi. |
| 2026-11-21 | Modülün kapsamı, şebeke karakterinde bias girişine gerilim aktarımı sağlayan mevcut donanım olarak netleştirildi. Masaüstü ESP deneylerinin Modül 2 kapsamında tutulması kararlaştırıldı. |

**Not:** Modül 1'in fiziksel imalatı tamamlanmıştır. Yeni masaüstü ESP deneylerinin tamamlanması veya ölçüm katsayılarının belirlenmesi Modül 1'in imalat durumunu değiştirmez.
