# PZEM davranışı: bilinenler ve bilinmeyenler

## Çıktılar
PZEM-004T V3 ailesi AC gerilim, akım, aktif güç, aktif enerji, frekans ve PF alanlarını seri arayüzden sunar. Fiziksel modülün varyantı ve kılavuzu doğrulanmalıdır.

## Zaman ölçeği
- **Üretici belgesi:** Kullanılan kılavuzlarda kesin iç yenileme penceresi/ortalama filtresi belgelenmemiştir.
- **Kullanıcı raporu / belirli bir test:** Bazı gözlemlerde yük algılama ve kararlı seviyeye oturma saniyeler sürmüştür. Bu, tüm modüller için garanti değildir.
- **HİPOTEZ:** Yaklaşık iki saniyelik yumuşatma penceresi doğrulanmış üretici bilgisi değildir.
- **Tasarım başlangıcı:** Yaklaşık 1 s sorgu aralığı; yanıt süresi, tekrar eden okumalar ve alan bazlı değişim zamanları kaydedilir.
- **Bilinmiyor:** V/I/P/PF alanlarının eşzamanlı güncellenmesi, iç etkin pencere ve düşük akım doğruluğu.

## Veri kalitesi
- Her okumada istek zamanı, yanıt zamanı, yanıt süresi ve read_status.
- Timeout, parse/transport hatası, NaN ve -1.0 gibi sentinel değerler geçersiz.
- Ani sıfır veya enerji sayacı anormalliği önce şüpheli olarak işaretlenir; gerçek kesinti/reset olasılığı kontrol edilir.
- Hata değerlerini ortalama ve filtrelere katma.

## Kaynaklar
- PZEM V3 kılavuz kopyası: https://mathieu.carbou.me/MycilaPZEM/PZEM-004T-V3.0-Datasheet-User-Manual.pdf
- ESPHome PZEM bileşeni: https://esphome.io/components/sensor/pzemac/
- Kullanıcı hata raporu: https://github.com/olehs/PZEM004T/issues/22
