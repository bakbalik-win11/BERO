# ADR-002: Nominal 200 ms SCT penceresi

- **Durum:** İlk test ayarı olarak kabul edildi; deney onayı bekliyor.
- **Karar:** 200 ms nominal pencere; 2 kS/s'de yaklaşık 400 örnek.
- **Bağlam:** 50 Hz için nominal 10 çevrim.
- **Gerekçe:** Saniyelik tek özete indirgemeden kısa yük davranışını gözlemek.
- **Risk:** Gerçek şebeke frekansı tam 50 Hz değil; sabit pencere tam çevrime her zaman oturmayabilir.
- **Gözden geçirme:** E02'de kararlı yük pencere değişkenliği ve gerekirse çevrime senkron alternatif.
