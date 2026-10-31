# ADR-009 — ±%4 ölçüm hedefinin sağlanması ve ham edinim ara işlerinin kapatılması

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ
- **Karar sahibi:** Kullanıcı
- **İlgili kapsam:** E00F ölçüm yolu, E08 yüksek hızlı ham edinim hazırlığı, ±%4 ölçüm kabul hedefi

## Bağlam

Ham 50 Hz dalga şeklini bilgisayara aktarma, her ADC örneğini ayrı zaman damgasıyla saklama ve DMA/ADC Continuous edinimi geliştirme, sağlıklı ölçüme ulaşmak için tasarlanmış ara basamaklardı. Kullanıcı, yeni/harici kodla ±%4 sapma hedefine ulaşıldığını bildirdi. Bu nedenle bu ara basamaklara artık ihtiyaç yoktur.

## Karar

1. PC'ye ham 50 Hz dalga aktarımı işi kapatılır.
2. Her ADC örneğini ayrı zaman damgasıyla saklama işi kapatılır.
3. Bu iki gereksinim için DMA/ADC Continuous firmware geliştirme işi kapatılır.
4. E00F'nin çalışan ESPHome ct_clamp kodu ve mevcut donanım/ayarları korunur.
5. ±%4 sonucu yeni/harici kodla elde edilmiş olarak kaydedilir; harici kaynak dosya bu depoda mevcutmuş gibi gösterilmez.

## Ölçüm özeti — KULLANICI RAPORU

| Yük | Referans (A) | Kod sonucu (A) | Sapma |
|---|---:|---:|---:|
| 100 W akkor | 0,446–0,447 | 0,4471 | yaklaşık %0 |
| 150 W akkor | 0,616 | 0,615 | −%0,2 |
| Kettle düşük/kararlı | 0,637 | 0,656 | +%3,0 |
| Kettle kaynama | 6,39 | 6,15 | −%3,8 |

Dört koşulun tamamı ±%4 sınırındadır. Bu tablo, önceki konuşmada kullanıcının sunduğu karşılaştırmaların mevcut özetinden aktarılmıştır. Ham ölçüm dosyaları, referans cihaz kimliği ve harici kodun kaynak/versiyonu bu ADR hazırlanırken bağımsız olarak yeniden incelenmemiştir. Bu nedenle kanıt etiketi KULLANICI RAPORU olarak kalır.

## Sonuçlar ve sınırlar

- Bu karar, kullanıcının bildirdiği ölçüm hedefinin karşılandığını ve ara edinim işlerinin gereksiz olduğunu kaydeder.
- Harici kodun BERO deposuna taşındığı, yeniden derlendiği veya bağımsız doğrulandığı iddia edilmez.
- BERO Python eğitim/model hattı, veri etiketleme ve bağımsız genelleme testi tamamlanmış sayılmaz.
- E08'in diğer yük karakterizasyon aşamaları otomatik olarak kapanmaz.
- E00F firmware, cihaz kimliği, GPIO bağlantıları, 200 ms ct_clamp penceresi, 2 s yayın aralığı ve 24.22 katsayısı bu kararla değiştirilmez.

## HEDEF / LOG / SONUÇ

- **HEDEF:** ±%4 ölçüm hedefine ulaşıldıktan sonra artık gerekmeyen ara geliştirmeleri kapatmak.
- **LOG:** Kullanıcı dört yük koşulundaki referans/kod karşılaştırmalarını sundu; değerler yukarıdaki tabloda kaydedildi.
- **SONUÇ:** ±%4 sınırı dört koşulda da sağlandı (KULLANICI RAPORU). Ham dalga aktarımı, tekil ADC zaman damgası ve DMA edinimi KAPATILDI — GEREKSİZ.
