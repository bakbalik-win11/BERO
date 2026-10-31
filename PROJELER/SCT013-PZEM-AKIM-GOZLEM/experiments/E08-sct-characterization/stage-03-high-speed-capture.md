# Aşama 3 — Yüksek hızlı ham ADC edinimi hazırlığı

**DURUM: KAPATILDI — GEREKSİZ (2026-10-31)**

## Kapanış kararı

Kullanıcının bildirimine göre yeni/harici kodla ±%4 ölçüm sapması hedefi sağlandı. Bu nedenle 50 Hz ham dalga şeklini bilgisayara aktarma, her ADC örneğini tek tek zaman damgasıyla saklama ve bu amaçla ESP-IDF ADC Continuous/DMA firmware'i geliştirme artık gerekli değildir.

Bu belge tarihçe ve karar izi olarak korunur; uygulanacak iş değildir.

## HEDEF (tarihsel)

İlk tasarım hedefi, kısa ve zaman damgalı ham ADC pencereleri alıp 50 Hz yük sinyalini bilgisayarda görüntülemekti. Bu hedef ölçüm sistemine ulaşmak için ara basamaktı; nihai proje kabul ölçütü değildi.

## LOG

- 2026-10-30 tarihinde ADC Continuous/DMA yaklaşımı araştırma ve tasarım adayı olarak belgelendi.
- Bu aşama için firmware yazılmadı, derlenmedi, cihaza yüklenmedi ve fiziksel ham dalga kaydı alınmadı.
- Kullanıcı 2026-10-31 tarihinde ±%4 hedefinin yeni/harici kodla sağlandığını bildirdi ve bu ara edinim işlerinin kapatılmasını istedi.

## SONUÇ

- **Durum:** KAPATILDI — GEREKSİZ.
- **Kapanan kapsam:** PC'ye ham 50 Hz dalga aktarımı; her ADC örneğine ayrı zaman damgası; bu edinim için DMA/ADC Continuous geliştirmesi.
- **Kapanmayan işler:** E08'in diğer yük karakterizasyon aşamaları, Python model/eğitim hattı veya bağımsız genelleme testi bu belgeyle tamamlanmış sayılmaz.
- **Çalışan yol:** E00F'nin mevcut ESPHome ct_clamp ölçüm yolu korunur; bu karar firmware veya donanım değişikliği gerektirmez.
- **Kanıt sınıfı:** ±%4 sonucu KULLANICI RAPORU; dört koşulun sayısal özeti ve sınırlamalar [ADR-009](../../docs/decisions/ADR-009-measurement-target-met-close-raw-capture.md) içindedir.
