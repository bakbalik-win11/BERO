# Geçersiz ve şüpheli okuma kuralları

## Kesin geçersiz
- Seri timeout veya taşıma hatası.
- Parse/protokol hatası.
- Kütüphanenin döndürdüğü -1.0 benzeri sentinel/hata değeri.
- NaN veya sonsuz sayısal değer.
- Zorunlu zaman/alan eksikliği.

Bunlar fiziksel ölçüm gibi ortalama, filtre, regresyon veya eşleştirme hesabına girmez. Hata durumunu ve ham hata bilgisini koru.

## Şüpheli; doğrulama gerekir
- Gerilimin aniden sıfıra inmesi.
- Enerji sayacının geriye gitmesi, sıfırlanması veya fiziksel olarak açıklanamayan sıçrama.
- Aynı zaman damgası veya beklenmedik uzun süre tekrarlanan okumalar.
- Fiziksel olarak uyumsuz alanlar.

Şüpheli değerleri otomatik silme; gerçek kesinti, cihaz yeniden başlaması veya sayacın sıfırlanması ihtimalini doğrula. anomaly_flags ekle ve doğrulanana kadar kararlı ölçüm analizinden ayrı tut.

Örnek: (240 + (-1)) / 2 = 119,5 V sahte sonuç verir; -1 hata göstergesi ise bu ortalama yapılmaz.
