# HDF2-GRV-002 / Alt Görev 1 — KOD-LOG-RAPOR

Bu klasör Alt Görev 1 boyunca üretilen kodları, ham test loglarını ve ilerleme raporlarını tarihli/sürümlü biçimde saklamak içindir.

## Kayıt kuralları

- Kullanıcı “sakla” dediğinde ilgili kod, log veya rapor bu klasöre kaydedilir.
- Her kayıtta step numarası, tarih, dosya sürümü ve durum belirtilir.
- Kod, log ve rapor birbirine referans verir; mümkünse aynı step kimliğini taşır.
- Eski sürümlerin üzerine yazılmaz; yeni sürüm veya yeni tarihli kayıt açılır.
- Derleme, cihaza yükleme ve fiziksel test sonuçları yalnızca gerçek kanıt varsa PASS olarak yazılır.
- Rapor tamamlanan adımları, kanıtları, açık sorunları ve kesin devam noktasını gösterir.
- Ham veriler değiştirilmeden korunur; analiz çıktıları ayrı dosyalar olur.

## Dosya düzeni

- KOD/ — firmware, Python araçları ve yardımcı betikler
- LOG/ — derleme, seri çıktı, test ve veri aktarım logları
- RAPOR/ — ana ilerleme raporu ve her step için raporlar

## Başlangıç durumu

Alt Görev 1 açık. Hedef, tek ESP32-WROOM ile SCT ve BIAS ham sinyallerini mümkün olan en yüksek güvenilir ve ölçülmüş hızda yakalamak, Mac'e aktarmak ve dalgayı çizdirmektir. Henüz derleme veya fiziksel test PASS olarak kaydedilmemiştir.

Sonraki aşama: tek ESP zinciri doğrulandıktan sonra 1T/2T/4T için üç ESP düzenini ayrı görevde kurmak.
