# E08 — SCT karakterizasyon protokolü

## Amaç
SCT sinyalinin örnekleme hızı, hesaplama yöntemi, iletken tur sayısı ve yük koşuluna göre davranışını incelemek. PZEM/SCT zaman eşleştirmesi veya kalibrasyon bu deneyin hedefi değildir.

## Ortak ölçüm düzeni
- Öncelikli sensör: SCT013-030 (30 A / 1 V).
- ADC: seçilecek ESP32 kartının dahili ADC'si; kart ve GPIO uygulama öncesinde kaydedilir.
- Hedef hızlar: 1 kS/s, 2 kS/s, 2,5 kS/s. Gerçekleşen hız ayrıca ölçülür.
- İletken tur sayısı: 1, 2 ve 4.
- Başlangıç penceresi: 200 ms; nihai optimum olduğu varsayılmaz.
- Her pencerede aynı örneklerden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanır. Ortalama, standart sapma, min/max ve örnek sayısı da kaydedilir.
- PZEM veya başka ESP'nin ortalama akımı varsa genel koşul notu olabilir; SCT pencereleriyle zaman eşleştirilmez.

## Aşamalar
1. Yüksüz uzun okuma: temel gürültü, bias davranışı ve pencere değişkenliği. Ayrıntı: [stage-01-no-load.md](stage-01-no-load.md).
2. 100 W akkor: üç hız × üç kablo turu matrisi. Ayrıntı: [stage-02-100w-matrix.md](stage-02-100w-matrix.md).
3. 150 W akkor ve 8,5 W LED: aynı matris, yük etkisini incelemek için. Ayrıntı: [stage-03-load-comparison.md](stage-03-load-comparison.md).
4. Aç-kapa testi: geçiş ve kararlı görünen bölge davranışı. Ayrıntı: [stage-04-on-off.md](stage-04-on-off.md).

## Analiz ilkeleri
- Her yöntemin kendi pencere değişkenliği ve tekrar edilebilirliği incelenir; RMS, Peak ve Peak-to-Peak ham değerleri birbirleriyle doğrudan sıralanmaz.
- Tur sayısı amper-tur etkisini artırır, gerçek yük akımını artırmaz.
- Kararlılık eşiği, gerekli ardışık pencere sayısı ve kesin kayıt süresi sonuçlar görülmeden sabitlenmez.
- Sürekli ham ADC arşivi varsayılan değildir; pencere özetleri ve deney notları kaydedilir.

Durum: PLANLANDI. Donanım, firmware ve ölçüm yapılmadı.
