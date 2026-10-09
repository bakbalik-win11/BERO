# GRV-001 — ESP32-D ile SCT-013 Akım Okuması

## Amaç

ESP32-D kullanarak SCT-013 akım sensöründen ölçüm almak; sinyalin ESP32 tarafından doğru okunabildiğini gözlemlemek ve okuma zincirinin davranışını ölçüm kayıtlarıyla doğrulamak.

## Kapsam

- ESP32-D ile SCT-013 bağlantısının ve kullanılan donanımın kaydı
- Sensör çıkışının ve ADC ham okumalarının gözlemlenmesi
- Okuma kararlılığının ve örnekleme davranışının incelenmesi
- Kullanılan dönüşüm/hesaplama adımlarının belgelenmesi
- Deneylerin, sonuçların ve edinilen tecrübenin bu görev altında saklanması

## Çalışma yöntemi

1. Test koşullarını ve bağlantıları kaydet.
2. Beklenen davranışı belirt.
3. Bir seferde tek değişkeni değiştir.
4. Ham ölçümleri ve kullanılan kod sürümünü sakla.
5. Sonucu doğrulandı, elendi veya belirsiz olarak işaretle.
6. Bir sonraki adımı ölçüm sonucuna göre belirle.

## Kapsam sınırı

Bu klasör, GRV-001 sırasında geliştirilen deney kodunu ve edinilen tecrübeyi tutar. Sensöre veya donanıma özel kalıcı uygulama kodunun ana yeri ilgili donanım/sensör klasörüdür. Görev kodu, deney ve doğrulama geçmişini korumak için burada tutulur.

MCP3208/SPI zamanlama doğrulaması bu görevin tanımı değildir; gerekirse ayrı bir görev olarak planlanır.

## Başarı ölçütü

ESP32-D ile SCT-013 okuma zincirinin davranışının tekrarlanabilir ölçümlerle gösterilmesi ve kullanılan yöntem, sınırlar ile sonuçların raporlanması.

## Durum

Başlangıç — test sonuçları henüz eklenmedi.
