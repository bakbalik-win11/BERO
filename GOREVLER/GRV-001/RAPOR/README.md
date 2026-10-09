# GRV-001 — ESP32–MCP3208 Ham Veri ve SPI Zamanlama Doğrulaması

## Amaç

ESP32'nin MCP3208'den ham ADC verisini doğru ve tekrarlanabilir biçimde okuyabildiğini doğrulamak; özellikle CS, SPI clock, veri çıkış/örnekleme kenarları ve RX zamanlamasını birbirinden ayırarak incelemek.

## Kapsam

- Tek kanal ve bilinen/sabit DC girişle başlangıç testi
- SPI bağlantı ve pin eşlemesinin kaydı
- CS etkinleşme süresi ve aktarım penceresinin incelenmesi
- MCP3208 veri çıkış kenarı ile ESP32 örnekleme kenarının doğrulanması
- Ham RX byte'larının ve 12 bit ADC sonucunun karşılaştırılması
- Tek değişkenli testler ve sonuçların kaydı

## Kapsam dışı

- SCT-013 akım kalibrasyonu ve nihai RMS doğruluğu
- Sensöre/donanıma özel kalıcı uygulama kodunun bu klasöre taşınması
- Aynı anda birden fazla donanım veya yazılım değişikliği

## Test kaydı

Her deney için şunları yaz:
1. Tarih ve test kimliği
2. Donanım bağlantısı ve giriş koşulu
3. Beklenen sonuç
4. Kullanılan kod/commit
5. Gerçek ölçüm ve ham veriler
6. Sonuç: doğrulandı, elendi veya belirsiz
7. Sonraki adım

## Başarı ölçütü

Bilinen giriş koşullarında ham ADC verisinin kararlı ve tekrarlanabilir okunması; CS ve SPI aktarım zamanlamasının açıklanabilir ve kayıtla doğrulanabilir olması.

## Durum

Başlangıç — test sonuçları henüz eklenmedi.
