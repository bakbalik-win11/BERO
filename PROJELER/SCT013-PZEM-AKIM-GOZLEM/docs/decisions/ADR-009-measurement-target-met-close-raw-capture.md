# ADR-009 — ±%4 ölçüm hedefinin sağlanması ve ara edinim işlerinin kapatılması

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ
- **İlgili kapsam:** Dış kaynaklı çalışan kod, SCT/PZEM karşılaştırmaları ve Faz 1 kapanışı

## Bağlam

SCT013 ölçüm yolu için hedeflenen sapma sınırı ±%4 idi. Dış kaynaklı ESPHome ct_clamp kodu kullanılarak yapılan karşılaştırmalarda hedef sağlandı. Böylece hedefe ulaşmak için tasarlanmış, artık gerekmeyen ham dalga/örnekleme ara işlerinin sürdürülmesine ihtiyaç kalmadı.

## Ölçüm sonuçları

| Yük | Referans (A) | Kod sonucu (A) | Sapma |
|---|---:|---:|---:|
| 100 W akkor | 0,446–0,447 | 0,4471 | yaklaşık %0 |
| 150 W akkor | 0,616 | 0,615 | −%0,2 |
| Kettle düşük/kararlı | 0,637 | 0,656 | +%3,0 |
| Kettle kaynama | 6,39 | 6,15 | −%3,8 |

Dört koşulun tamamı ±%4 sınırındadır. Bu karşılaştırmalar kullanıcı tarafından paylaşılan deney logları ve ölçüm kayıtlarıyla desteklenmektedir. Bu sonuç Faz 1'in kabul ölçütünü karşılar.

## Karar

1. Faz 1 — çalışan kodu bulmak ve ±%4 hedefine ulaşmak — TAMAMLANDI.
2. Faz 1 kapsamında hedefe ulaşmak için tasarlanmış, henüz yapılmamış tüm deney ve işler KAPATILDI — HEDEFE ULAŞILDI. Yapılmamış işler yapılmış deney olarak gösterilmez.
3. Ham 50 Hz dalga aktarımı, her ADC örneğine ayrı timestamp ekleme ve bu işler için DMA/ADC Continuous geliştirme işleri kapatıldı.
4. Çalışan ölçüm yolu ve mevcut ayarları korunur.
5. Faz 2, bulunan kodun PZEM referans verisiyle eğitilmesi/iyileştirilmesidir; bu ADR Faz 2'nin tamamlandığı anlamına gelmez.

## Sonuç

±%4 hedefi sağlandı. Faz 1 kapandı. Yeni aktif çalışma Faz 2'dir.
