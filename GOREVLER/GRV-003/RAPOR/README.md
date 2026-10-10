# GRV-003 — Trafo Bias Yapısının Kurulması ve Doğrulanması

## Amaç

SCT013 akım ölçüm zincirinde kullanılan trafo bias/güç yapısını ayrı bir görev olarak belgelemek; fiziksel kurulumu ve ölçülen çıkış değerini kayıt altına almak.

## Fiziksel kurulum

Trafo devresi, ana sistemden ayrı bir **güç kutusu** olarak kuruldu. Kutu **taşınabilir** yapıdadır; güç devresi gerektiğinde bağımsız olarak taşınıp kullanılabilir.

Kayıtlı bileşenler ve güç zinciri:

1. **RN130421 PCB tipi trafo:** 6 V AC, 2.0 VA.
2. **KBU610 köprü doğrultucu:** trafonun AC çıkışını doğrultmak için.
3. **2200 µF / 35 V elektrolitik kondansatör:** doğrultulmuş gerilimi filtrelemek için.
4. **L78L33 (TO-92) regülatör:** regüle 3.3 V çıkış elde etmek için.

Zincir: **Trafo → KBU610 köprü doğrultucu → 2200 µF / 35 V filtre kondansatörü → L78L33 → 3.3 V çıkış.**

## Fiziksel ölçüm sonucu

- **Regülatör çıkışı: 3.30 V — fiziksel olarak net ölçüldü.**
- ESP32D1 GPIO32, GPIO33 ve GPIO34 üzerinde ayrıca **1.65 V** okunduğu bildirildi.
- PZEM ve SCT013 sensörleri enerjiyi ESP32'den almıyor.

3.30 V, güç kutusunun regüle çıkışında ölçülen fiziksel değerdir. GPIO'lardaki 1.65 V okumaları ayrı ölçüm noktalarıdır; bunlar birbirinin yerine kullanılmamalıdır.

## GRV-004 ile ilişkisi

GRV-004 kapsamındaki ESP32D1 + PZEM + SCT013 birleşik deneyi bu bias/güç yapısıyla birlikte ele alınacaktır. Güç kutusunun ayrı ve taşınabilir olması, bu devrenin ana sistemden bağımsız incelenebilmesini sağlar.

## Kalan kayıt işi

- Fiziksel kablo/terminal bağlantılarını ve ölçüm noktalarını fotoğraf veya şema ile eklemek.
- 3.30 V ölçümünde kullanılan cihazı ve ölçüm noktasını, varsa fotoğraf/log ile ilişkilendirmek.
- GPIO32/33/34 üzerindeki 1.65 V ölçümlerini ayrı ayrı kayıt altına almak.

## Durum

**Fiziksel güç kutusu kuruldu; regüle çıkış 3.30 V olarak ölçüldü.** Bağlantı şeması ve görsel kanıt bu rapora henüz eklenmedi.
