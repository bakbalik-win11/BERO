# BERO Günlük Kontrol Listeleri

Bu klasör, her takvim günü için tiklenebilir iş akışı kontrol listesini tutar. Teknik deneylerin ayrıntıları HISTORY ve ilgili görev raporlarında kalır.

- Günlük dosya biçimi: `YYYY/YYYY-MM-DD.md`
- Her günün yeni dosyası GitHub Actions tarafından Türkiye saatiyle yaklaşık 03.05'te oluşturulur ve otomasyon günlük dizinindeki bağlantı listesini de en yeni tarih üstte kalacak şekilde günceller.
- Aynı tarihli dosya varsa üzerine yazılmaz.
- Kutular yalnızca ilgili işlem gerçekten tamamlandıktan sonra işaretlenir.
- “Ara rapor”, “günü kapa” ve fikirden göreve geçiş işlerinde asistan ilgili günlük kutuları ve proje kayıtlarını kontrol eder.
- Kullanıcıdan yalnızca teknik gerçekler/kanıtlar beklenir: deney koşulları ve ham ölçümler, derleme sonucu, gerektiğinde donanım/yapılandırma değişikliği onayı. Rutin kayıt, bağlantı, indeks ve tik takibi asistanın sorumluluğudur.
- İlk otomasyon çalışması için [GitHub Actions iş akışı](https://github.com/bakbalik-win11/BERO/actions/workflows/daily-bero-checklist.yml) sayfasından çalıştırma durumu kontrol edilmelidir; GitHub Actions kapalıysa etkinleştirilmelidir.

## Her gün okunacak kısa akış

- [BERO Günlük Açılış ve Kapanış Kartı](BERO_GUNLUK_AKIS.md) — kullanıcı ve asistan için kısa açılış, çalışma ve kapanış kontrolü.

## Günlükler

En yeni tarih en üstte listelenir.

- [2026-10-09](2026/2026-10-09.md) — ilk günlük kontrol listesi
