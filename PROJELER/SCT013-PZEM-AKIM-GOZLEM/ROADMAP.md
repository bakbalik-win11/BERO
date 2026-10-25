# Yol haritası

Bir fazın kabul ölçütü sağlanmadan sonraki faz tamamlandı sayılmaz. Kutular yalnız depoda kanıt olduğunda işaretlenir.

## Faz 0 — Hazırlık ve güvenlik
- [ ] 0.1 Fiziksel SCT varyantı, PZEM modeli/CT'si, MCU, ADC, burden/bias ve VREF'i belgeleyin.
  - **Bitti sayılır:** gerçek etiketler/fiziksel ölçümler envanterde kayıtlı.
- [ ] 0.2 220–240 V güvenlik kontrolleri.
  - **Bitti sayılır:** kontrol listesi yetkin kişi tarafından incelendi.
- [ ] 0.3 True-RMS referans cihazı ve üç rezistif yük seviyesi hazırlayın.
  - **Bitti sayılır:** referans ve yük kimlikleri kayıtlı.

## Faz 1 — SCT analog ön uç
- [ ] 1.1 Burden/bias ve ADC aralık payını doğrula.
- [ ] 1.2 Yüksüz ofset ve gürültü tabanını ölç.
- [ ] 1.3 En az üç seviyede kalibrasyon yap.
  - **Bitti sayılır:** önceden belirlenmiş hata hedefi sağlanmış; clipping yok; calibration_id kayıtlı.

## Faz 2 — SCT edinim
- [ ] 2.1 Gerçek örnekleme hızını ve sapmayı ölç.
- [ ] 2.2 2 kS/s ve nominal 200 ms penceresini dene.
- [ ] 2.3 RMS, ADC ortalaması, min/max, örnek sayısı ve clipping sayaçlarını üret.
  - **Bitti sayılır:** kararlı yükte pencere değişkenliği raporlanmış.

## Faz 3 — PZEM edinim
- [ ] 3.1 Yaklaşık 1 s sorgu başlangıcı; istek/yanıt zamanları ve read_status kaydı.
- [ ] 3.2 V/I/P/PF alanlarının değişim zamanlarını ayrı incele.
- [ ] 3.3 Sentinel, timeout ve parse hatalarını ayıkla.
  - **Bitti sayılır:** en az 10 dakikalık kayıt ve hata oranı var.

## Faz 4 — Zaman hizalama
- [ ] 4.1 Tek monotonik saat kaynağı kullan.
- [ ] 4.2 SCT RMS değişimiyle olay algıla.
- [ ] 4.3 Olay sonrası yaklaşık 3 s'yi başlangıç transition_or_settling etiketi yap.
  - **Bitti sayılır:** geçiş/kararlı kayıtlar ayrılmış; süre cihaz deneyine göre gözden geçirilmiş.

## Faz 5 — Kayıt şeması
- [ ] 5.1 Zorunlu ve önerilen alanları uygula, örnek kayıtları doğrula.
- [ ] 5.2 Olay tamponu prosedürünü belirle.
  - **Bitti sayılır:** bir saatlik örnek kayıt şema ile uyumlu; olay kesiti test edilmiş.

## Faz 6 — Deneyler
- [ ] 6.1 E03: dirençli yük aç/kapat, en az 5 tekrar.
- [ ] 6.2 E04: PZEM alanlarının değişim zamanı.
- [ ] 6.3 E05: aynı yükte 1 / 2 / 2,5 kS/s; opsiyonel 500 S/s.
- [ ] 6.4 E01, E02, E06: gürültü, kararlı yük ve farklı yük tipleri.
  - **Bitti sayılır:** her deneyin protokolü, metadata'sı, verisi ve sonucu mevcut.

## Faz 7 — Analiz ve karar
- [ ] 7.1 Kararlı aralıkta SCT–PZEM farkı, pencere değişkenliği, olay gecikmesi ve clipping.
- [ ] 7.2 Hızı, pencereyi, polling aralığını ve düşük akım sınırını ölçüme göre kararlaştır.
  - **Bitti sayılır:** her karar kendi veri setinden bir metrikle gerekçeli.

## Faz 8 — İşletme ve bakım
- [ ] 8.1 PZEM hata oranı, tekrar eden okumalar, ADC ofseti ve clipping izle.
- [ ] 8.2 Düzenli kalibrasyon yap; donanım değişikliğinde yeni calibration_id aç.
  - **Bitti sayılır:** kayıtlı bakım ve kalibrasyon geçmişi.

## Karar kapıları
- **G1:** SCT kalibrasyonu hata hedefinde ve clipping yok.
- **G2:** PZEM hata okumaları saptanıyor; geçersiz değerler hesaplardan dışlanıyor.
- **G3:** hız seçimi hedef yüklerde ölçülmüş sonuçlarla gerekçelendirilmiş.
