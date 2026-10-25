# ADR-005: Geçersiz PZEM okumaları özetlere katılmayacak

- **Durum:** Kabul edildi.
- **Karar:** Timeout, parse/transport hatası, NaN ve -1.0 gibi hata göstergeleri geçersizdir; ortalama ve filtrelerden çıkarılır. Ani sıfır gerilim ve enerji sayacı anormallikleri önce şüpheli olarak işaretlenir.
- **Bağlam:** Hata göstergesini fiziksel değer gibi ortalamak sahte sonuç üretir. Örneğin (240 + (-1)) / 2 = 119,5 V.
- **Gerekçe:** Haberleşme hatası ve gerçek ölçüm ayrı temsil edilmelidir.
- **Risk:** Her sıfır hata değildir; gerçek kesinti veya sayaç reseti mümkündür.
- **Gözden geçirme:** E03/E04 ve kasıtlı iletişim hata testi.
