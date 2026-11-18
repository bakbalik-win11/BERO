# MAX4466 — Mikrofon yükselteç modülü donanım kaydı

## Kimlik ve envanter

- **Bileşen:** MAX4466 tabanlı mikrofon yükselteç modülü.
- **Adet:** Kullanıcı tarafından modüllerin teslim alındığı bildirildi; kesin adet henüz kaydedilmedi.
- **Stok durumu:** Mevcut; kullanıcı bildirimi.
- **Kullanım alanı:** BERO / PREBERO kapsamında ses sinyalini analog olarak almak ve mikrofon tabanlı gözlem/denemeler yapmak.
- **Modül kimliği:** Adet ve fiziksel kartlar sayıldıktan sonra MAX4466-01 … şeklinde atanacak.
- **Kart üreticisi / satıcı / SKU / PCB revizyonu:** Henüz kaydedilmedi.
- **Mikrofon kapsülü modeli:** Henüz doğrulanmadı.

## Üretici entegresi — MAX4466

MAX4466, Analog Devices (eski Maxim Integrated) üretimi, mikrofon ön yükselteci uygulamaları için tasarlanmış düşük güçlü bir op-amp entegresidir.

| Özellik | Üretici bilgisi |
|---|---|
| Üretici | Analog Devices |
| Entegre | MAX4466 |
| Besleme aralığı | 2,4–5,5 V |
| Çıkış | Rail-to-rail |
| Quiescent besleme akımı | Tipik 24 µA |
| Gain-bandwidth product | AV ≥ 5 koşulunda 600 kHz |
| Temel uygulama | Mikrofon ön yükselteci |

**Önemli ayrım:** MAX4466 entegresi tek başına mikrofon modülünün bütün teknik özelliklerini tanımlamaz. Piyasadaki breakout kartlarında mikrofon kapsülü, kazanç ayar potansiyometresi, bias ağı ve çıkış bağlantıları üreticiye göre değişebilir. Kartın tam şeması ve pin sırası fotoğraf/ölçümle doğrulanmadan varsayılmayacaktır.

## BERO'da kullanım ve bağlantı doğrulama

- Modül analog ses sinyali çıkışı verir; ESP32 ADC veya uygun harici ADC ile okunabilir.
- Modülün VCC, GND ve OUT pin sırası kart üzerindeki baskı/üretici belgesiyle doğrulanmalıdır.
- Besleme gerilimi, çıkışın DC çalışma noktası, sinyal genliği ve ADC giriş aralığı osiloskopla kontrol edilmelidir.
- Potansiyometre varsa kazanç ayarı olduğu varsayılmadan önce kart üzerindeki bağlantı izleri veya modül dokümanı kontrol edilmelidir.
- Mikrofon modülünün analog çıkışı, ADC giriş sınırlarını aşmamalıdır.
- İlk denemeler düşük gerilimli ve kontrollü ses kaynaklarıyla yapılmalıdır.

## BERO test kayıt alanları

| Test | Kaydedilecek bilgi | Durum |
|---|---|---|
| Fiziksel kimlik | Kart fotoğrafı, PCB revizyonu, mikrofon kapsülü ve potansiyometre bilgisi | Bekliyor |
| Besleme | VCC gerilimi ve akım | Bekliyor |
| DC çıkış | Sessizlikte OUT gerilimi | Bekliyor |
| Ses çıkışı | Osiloskopta dalga biçimi ve tepe-tepe gerilimi | Bekliyor |
| Kazanç | Potansiyometre konumu / çıkış değişimi | Bekliyor |
| ADC bağlantısı | ADC modeli, giriş aralığı, örnekleme ve ham kayıt | Bekliyor |
| Uzun süreli davranış | Gürültü tabanı, doyum, kopma ve kararlılık | Bekliyor |

## Üretici kaynakları

- [Analog Devices — MAX4466 ürün sayfası](https://www.analog.com/en/products/max4466.html)
- [Analog Devices — MAX4465–MAX4469 veri sayfası (PDF)](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX4465-MAX4469.pdf)

**Kayıt sınırı:** Üretici verileri MAX4466 entegresine aittir. BERO'daki mikrofon breakout kartının üreticisi, kapsülü, pin sırası, kazanç aralığı ve gerçek performansı henüz doğrulanmamıştır.
