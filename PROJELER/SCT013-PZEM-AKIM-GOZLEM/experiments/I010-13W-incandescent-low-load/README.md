# I010 — 13 W akkor ampul düşük yük ayrışma deneyi

## Amaç

Mevcut 15 W akkor ampulün HA grafiklerinde kirli/bozucu davranış gösterdiğine ilişkin kullanıcı gözlemi nedeniyle kontrollü test yükü olmaktan çıkarılmasının ardından, ayrı bir 13 W akkor ampulün OFF durumundan istatistiksel olarak ayrışıp ayrışmadığını incelemek.

Kullanıcının deney gerekçesi: 13 W ampulün fiziksel boyutlarının/filament yapısının mevcut 15 W ampule daha benzer olması. Bu fiziksel benzerlik henüz ölçü veya üretici belgesiyle doğrulanmış değildir.

## Deney kararı ve başlangıç durumu

- Sonraki kontrollü düşük yük adayı: **13 W akkor ampul**.
- Kullanıcı 6 Kasım 2026 tarihinde bu ampulle ilerleme ve ampulü bağlama kararı verdi.
- **Deney henüz başlamış sayılmaz.** Fiziksel bağlantı, ON başlangıcı ve CSV kaydı bekleniyor.
- Mevcut 15 W ampul bu deneyde kullanılmayacak.
- 13 W tek başına test edilecek; 57 W ile birleştirilmeyecek.
- Önceki deneyle karşılaştırılabilirlik için mümkün olduğunca CH1-1T, aynı firmware ve aynı ölçüm parametreleri korunmalı. Gerçek bağlantı/firmware koşulları deney başlangıcında ayrıca kaydedilecek.

## Analiz yöntemi

- Fiziksel OFF ve 13 W ON çevrimleri ayrı segmentlenecek.
- Tekil örnek sıçramaları karar sayılmayacak; ham veride korunacak.
- K uygulanmış CH1 çıktısı için eşik üstünde kalma süresi, devamlılık, pencere medyanı, MAD ve zaman kararlılığı incelenecek.
- 5, 10, 20, 30 ve 60 saniyelik aday pencereler karşılaştırılacak; bunlar henüz onaylanmış karar süreleri değildir.
- PZEM akım ve güç kayıtları aynı zaman pencerelerinde kendi geçerli timestamp'leriyle ayrı özetlenecek.
- ON/OFF dağılımlarının örtüşmesi ve çevrimler arası tekrarlanabilirlik raporlanacak.
- Ham kayıt değiştirilmeyecek; geçişler ve sıçramalar silinmeyecek.

## Beklenen yanıt

Bu deneyin temel sorusu, 13 W ON durumunun OFF referansından yeterli süre ve kararlılıkla ayrışıp ayrışmadığıdır. Ayrışma görülürse bu, mevcut 15 W ampulden farklı bir düşük yük davranışı gösterir; tek başına genel bir eşik veya tüm ampuller için sonuç oluşturmaz.

**Durum: SEÇİLDİ / BAĞLANTI VE VERİ BEKLENİYOR.**
