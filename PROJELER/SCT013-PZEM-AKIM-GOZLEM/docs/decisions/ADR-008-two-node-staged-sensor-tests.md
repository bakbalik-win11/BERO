# ADR-008: İki ölçüm düğümünün görev ayrımı ve ESP-2 aşamalı sensör testleri

- **Durum:** KABUL EDİLDİ — mimari/test sırası kararı; fiziksel bağlantı ve testler henüz doğrulanmadı.
- **Tarih:** 2026-10-30
- **Kaynak:** Kullanıcı kararı.
- **Kapsam:** SCT013 ana ölçüm kolunun diğer sensör ve haberleşme işlerinden yalıtılması; ACS712-5A, ZMCT103C-5A ve PZEM'in ayrı bir ESP düğümünde aşamalı denenmesi.

## Karar

1. **ESP-1 yalnızca SCT013 ölçümüne ayrılır.** Bu düğüme PZEM, ACS712, ZMCT103C veya başka görev eklenmez. Önceliği SCT sinyalinin hızlı ve düzenli örneklenmesidir.
2. **ESP-2 karşılaştırma düğümüdür.** PZEM-004T V3.0, bir adet ACS712-5A ve bir adet ZMCT103C-5A bu düğümde ele alınır.
3. ESP-2 üzerinde bütün sensörler ilk denemeden itibaren birlikte çalıştırılmaz. Her bileşen ve kombinasyon aşağıdaki sırayla ayrı ayrı doğrulanır.
4. Her aşamada bağlantı, derleme/çalışma durumu, seri/HA logu ve beklenen-gerçekleşen davranış kaydedilir. Bir aşama doğrulanmadan sonraki aşamaya geçilmez.
5. ESP-1 ve ESP-2'nin fiziksel kart modeli, pin eşlemesi ve analog ön uç bağlantıları bu kararla belirlenmiş sayılmaz; ayrıca doğrulanacaktır.

## ESP-2 test sırası

1. **PZEM tek başına:** Haberleşme ve mevcut ölçüm alanlarının okunması.
2. **ACS712-5A tek başına:** Yüksüz çıkış tabanı ve kontrollü yükte sensör çıkışının gözlenmesi.
3. **ZMCT103C-5A tek başına:** Analog ön uç doğrulandıktan sonra yüksüz taban ve kontrollü yük davranışının gözlenmesi.
4. **PZEM + ACS712-5A:** Birlikte çalışma, veri güncelleme ve kaynak/zamanlama etkileşimi.
5. **PZEM + ZMCT103C-5A:** Birlikte çalışma, veri güncelleme ve kaynak/zamanlama etkileşimi.
6. **PZEM + ACS712-5A + ZMCT103C-5A:** Önceki aşamalar başarılıysa üçlü çalışma ve etkileşim kontrolü.

## Kapsam ve güvenlik notları

- Bu karar sensörlerin ölçüm hassasiyetini, 50 mA algılama başarısını veya ±%4 doğruluğu kanıtlamaz.
- ACS712 modülünün besleme/çıkış aralığı ESP32 ADC sınırlarıyla uyumlu hale getirilmeden ADC'ye doğrudan bağlanmayacaktır. Kartın gerçek devresi ve çıkış seviyesi doğrulanmalıdır.
- ZMCT103C modülünün burden/çıkış devresi ve analog bağlantı topolojisi görülmeden bağlantı şeması kesinleştirilmeyecektir.
- Şebeke akım yolu üzerinde modül kullanımı uygun muhafaza, izolasyon ve güvenli bağlantı gerektirir; açık breadboard üzerinde şebeke akımı taşınmaz.
- PZEM'in ESP-2'de bulunması, ESP-1'in SCT örnekleme döngüsüne PZEM yükü bindirilmemesi içindir. ESP-2 içindeki PZEM haberleşmesinin sensör edinimini etkileyip etkilemediği kombinasyon testlerinde ayrıca gözlenir.

## İlgili kayıtlar

- [ESP-2 aşamalı düşük akım karşılaştırma planı](../../experiments/E09-low-current-sensor-comparison/README.md)
- [Fiziksel donanım envanteri](../../hardware/inventory.md)
- [E08 — SCT sinyalini tanıma](../../experiments/E08-sct-characterization/README.md)
