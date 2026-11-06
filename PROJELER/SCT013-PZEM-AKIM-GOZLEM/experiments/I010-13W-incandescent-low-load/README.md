# I010 — 18 W yük düşük yük ayrışma deneyi

## Amaç

Mevcut 15 W ampulün HA grafiklerinde kirli/bozucu davranış gösterdiğine ilişkin kullanıcı gözlemi nedeniyle kontrollü test yükü olmaktan çıkarılmasının ardından, yeni **18 W yükün** OFF durumundan istatistiksel olarak ayrışıp ayrışmadığını incelemek.

## Deney kararı ve başlangıç durumu

- Önceki 13 W planı kullanıcı tarafından düzeltildi; **yeni test yükü 18 W'tır**.
- Kullanıcı 6 Kasım 2026 tarihinde 18 W yük ile yeni teste geçileceğini bildirdi.
- **Deney henüz başlamış sayılmaz.** Fiziksel bağlantı ve gerçek ON başlangıç zamanı bekleniyor.
- Mevcut 15 W ampul kullanılmayacak.
- 18 W tek başına test edilecek; 57 W veya başka yükle birleştirilmeyecek.
- CH1-1T, firmware ve ölçüm parametreleri mümkün olduğunca sabit tutulmalı; gerçek bağlantı ve yazılım koşulları başlangıçta ayrıca kaydedilecek.

## Analiz yöntemi

- Fiziksel OFF ve 18 W ON çevrimleri ayrı segmentlenecek.
- Tekil örnek sıçramaları karar sayılmayacak; ham veride korunacak.
- K uygulanmış CH1 çıktısı için eşik üstünde kalma süresi, devamlılık, pencere medyanı, MAD ve zaman kararlılığı incelenecek.
- 5, 10, 20, 30 ve 60 saniyelik aday pencereler karşılaştırılacak; bunlar henüz onaylanmış karar süreleri değildir.
- PZEM akım ve güç kayıtları aynı zaman pencerelerinde kendi geçerli timestamp'leriyle ayrı özetlenecek.
- ON/OFF dağılımlarının örtüşmesi ve çevrimler arası tekrarlanabilirlik raporlanacak.
- Ham kayıt değiştirilmeyecek; geçişler ve sıçramalar silinmeyecek.

## Beklenen yanıt

Temel soru, 18 W ON durumunun OFF referansından yeterli süre ve kararlılıkla ayrışıp ayrışmadığıdır. Sonuç yalnızca bu 18 W yük ve mevcut ölçüm zinciri için geçerli olacaktır; tek başına genel eşik oluşturmaz.

**Durum: SEÇİLDİ / BAĞLANTI VE VERİ BEKLENİYOR.**

## Düzeltme kaydı

Önceki taslakta 13 W yazılmıştı. Kullanıcının son bildirimiyle deney yükü **18 W** olarak düzeltildi. 13 W deneyi plan kapsamında değildir.
