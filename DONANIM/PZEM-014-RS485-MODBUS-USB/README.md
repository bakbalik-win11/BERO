# PZEM-014 — AC RS485 Modbus Güç Tüketim Ölçer + USB

## Kapsam ve model ayrımı
Bu belge, PZEM-014 AC RS485 Modbus ölçer ve ürünle birlikte satılan USB–RS485 adaptörünü kapsar. PZEM-014 ekransızdır; ölçüm verileri RS485 üzerinden okunur. “+ USB” genellikle paketteki USB–RS485 adaptörünü anlatır; modülün kendisinde USB veri portu olduğu anlamına gelmez.

**PZEM-014 ile PZEM-016'yı karıştırma:**
- PZEM-014: 0–10 A, dahili şönt üzerinden akım ölçümü.
- PZEM-016: 0–100 A, harici akım trafosu ile ölçüm.

## Kaynaklar
- [PZEM-014/016 kullanım kılavuzu — PDF](https://m.media-amazon.com/images/I/81wHLsuaIOL.pdf)
- [ManualsLib — PZEM-014 manual](https://www.manualslib.com/manual/3810945/Morning-Pzem-014.html)
- [Komponentci ürün sayfası](https://www.komponentci.net/pzem-014-ac-rs485-modbus-guc-tuketim-olcer-usb-pmu47188)
- [Motorobit ürün sayfası](https://www.motorobit.com/pzem-014-ac-rs485-modbus-guc-tuketim-olcer)
- [Modbus RTU ve USB örnek Python projesi](https://github.com/BrucesHobbies/energyMaster/blob/main/pzem.py)

## Teknik özellikler

| Ölçüm | PZEM-014 aralığı | Çözünürlük / doğruluk |
|---|---:|---|
| AC gerilim | 80–260 V | 0,1 V; ±0,5% olarak listelenmiş |
| AC akım | 0–10 A | 0,001 A; ±0,5% olarak listelenmiş |
| Aktif güç | 0–2,3 kW | 0,1 W; ±0,5% olarak listelenmiş |
| Güç faktörü | 0,00–1,00 | 0,01; ±1% olarak listelenmiş |
| Frekans | 45–65 Hz | 0,1 Hz; ±0,5% olarak listelenmiş |
| Aktif enerji | 0–9999,99 kWh | 1 Wh; ±0,5% olarak listelenmiş |
| Başlangıç akımı | 0,01 A | Kılavuz değeri |
| Haberleşme | RS485, Modbus-RTU | 9600 baud, 8N1 |
| Boyut | yaklaşık 90 × 60,5 × 23 mm | Satıcı/kılavuz listesi |

Bu değerler üretici dokümanındaki teknik beyanlardır; bağımsız kalibrasyon sonucu değildir.

## Haberleşme ve USB
PZEM-014'ün haberleşme katmanı RS485'tir. Birlikte gelen USB dönüştürücü bilgisayarda COM veya tty seri portu olarak görünebilir.

- PZEM RS485 A → adaptör A
- PZEM RS485 B → adaptör B
- GND/5V bağlantıları yalnızca kılavuz ve adaptör etiketine göre yapılmalı.
- A/B isimlendirmesi adaptörler arasında değişebildiğinden haberleşme yoksa pinout ve A/B eşlemesi kontrol edilir.
- Tipik seri ayar: 9600 baud, 8 data bit, no parity, 1 stop bit (9600 8N1).

## Modbus notları
Kılavuzda 0x04 Input Register okuma, 0x03 Holding Register okuma, 0x06 tek register yazma, 0x42 enerji sıfırlama ve 0x41 fabrika kalibrasyon/servis işlevi listelenir. Kalibrasyon ve enerji sıfırlama komutları normal okuma yazılımında otomatik çağrılmamalıdır.

## Elektriksel güvenlik
- AC terminalleri şebeke gerilimiyle bağlantılıdır; 230 V AC ölümcül olabilir.
- Enerji varken kablo bağlama veya sökme. İlk kurulum uygun koruma, muhafaza ve yetkin elektrikçiyle yapılmalıdır.
- USB–RS485 adaptörünün galvanik izolasyonlu olduğunu varsayma. USB bağlantısı şebeke tarafını güvenli hale getirmez.

## BERO devreye alma
1. Cihaz etiketini ve USB–RS485 adaptörünün modelini kaydet.
2. PZEM-014 (10 A dahili şönt) olduğunu doğrula; PZEM-016 ile karıştırma.
3. Şebeke bağlantısını enerjisizken kılavuza göre kontrol ettir.
4. USB adaptörünün COM/tty portu oluşturduğunu doğrula.
5. 9600 8N1 ve slave adresini kılavuza göre ayarla.
6. İlk testte yalnızca okuma sorguları kullan.
7. Ölçümleri uygun referans cihazla karşılaştır.

**Doğrulama durumu:** Ürün sayfası ve PZEM-014/016 kılavuzu incelendi. BERO'daki cihaz revizyonu ve adaptörün pinout/izolasyon bilgisi fiziksel olarak doğrulanmadı.