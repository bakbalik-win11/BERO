# GRV-004 — ALT GÖREV 05: PZEM + ADC Birleşik Log / Yüksüz Referans
**Tarih:** 2026-10-10  
**Cihaz:** `esp32d1` — `192.168.0.8`  
**ESPHome:** `2026.9.1`  
**Dal:** `grv004-verified-adc-candidate-20261010`  
**Durum:** Log kaydı alındı; 100 W yük deneyi henüz yapılmadı.

## 1. Hedef
Aynı ADC sonuç satırında PZEM'in akım, güç ve gerilim değerlerini; BIAS, K1, K2 ve K3 kanallarının MIN, MAX, AVG ve STD değerleriyle birlikte kaydetmek. Bir sonraki deneyde kodu değiştirmeden yaklaşık 100 W dirençli yük bağlanarak iki ölçüm grubunun aynı log satırlarında karşılaştırılması hedefleniyor.

## 2. Kaydedilen kod
Mevcut kod sürümü ayrı, tarihli dosya olarak korunuyor:
[`esp32d1-4ch-1000-min-max-avg-std-pzem-log-continuous-20261010.yaml`](KOD/esp32d1-4ch-1000-min-max-avg-std-pzem-log-continuous-20261010.yaml)

Bu deney kaydında kodun üzerine yazılmadı. Dosya başlığında “PZEM bu deneyde yoktur” diyen eski açıklama var; ancak dosyanın gerçek içeriğinde PZEM UART/Modbus ve sensör ID'leri bulunuyor. Bu, açıklama satırının içerikle uyuşmayan bir yorum hatasıdır; işlevsel kod içeriği bu kayıt için değiştirilmedi.

## 3. Log arşivi
Ayrıştırılmış ADC tur satırları ve PZEM başlangıç bilgileri:
[`LOG-20261010-pzem-adc-yuksuz-referans.md`](LOG-20261010-pzem-adc-yuksuz-referans.md)

Not: Arşiv dosyası orijinal yüklemenin birebir ham kopyası değil; 17 adet ADC_TEST satırı ve PZEM ölçüm özeti kaynak logdan ayrıştırılarak kaydedildi. Orijinal 254 satırlık log kullanıcı tarafından sohbette sağlandı.

## 4. Deney koşulu ve gözlemler
Bu kayıtta yaklaşık:
- PZEM gerilim: **227.7–229.0 V**
- PZEM akım: **0.028 A** (görüntülenen yuvarlatılmış değer)
- PZEM güç: **1.5–1.7 W**
- Frekans: **49.9–50.0 Hz**
- ADC tur sayısı: **TUR=1–17**
- ADC ortalamaları yaklaşık:
  - BIAS: **1.6625–1.6652 V**
  - K1: **1.6612–1.6633 V**
  - K2: **1.6598–1.6614 V**
  - K3: **1.6552–1.6569 V**

PZEM'deki 1.5–1.7 W değerleri, bu kayıtta yaklaşık yüksüz/arka plan durumunu gösteriyor; bu durumun kesin sıfır yük olduğu ayrıca doğrulanmış değil. Kanal ortalamalarının bias çevresinde kalması tek başına akım kalibrasyonunu kanıtlamaz. MIN/MAX ve STD değerleri turdan tura değişiyor; özellikle K1'de bazı turlarda daha geniş aralıklar görülüyor.

## 5. Teknik notlar
- PZEM sensör güncellemesi 5 saniye, ADC birleşik satırı yaklaşık 10 saniyede bir geliyor. Bu nedenle aynı satırdaki PZEM değeri ADC örneklemesiyle tam eşzamanlı ölçüm olarak kabul edilmemeli; satır, o sırada mevcut son PZEM durumunu ilişkilendiriyor.
- Logda ESP32 minimum chip revision ve SRAM1/IRAM ile ilgili öneri uyarıları ve bir adet `safe_mode took a long time` uyarısı var. Bu kayıtta ADC_TEST ve PZEM satırlarının üretilmesi gözleniyor; bu tek başına 1000 örnek sayısını bağımsız olarak doğrulamaz.
- Fiziksel 100 W yük altında sonuç alınmadan SCT013 kalibrasyonu veya akım dönüşüm katsayısı belirlenmeyecek.

## 6. Bir sonraki deney — aynı kod, yaklaşık 100 W
1. Yukarıdaki YAML sürümünü değiştirmeden kullan.
2. Güvenli, kapalı ve uygun sınıfta bir bağlantı üzerinden yaklaşık 100 W akkor/dirençli yük uygula; açıkta şebeke bağlantısı yapma.
3. Yük sabitlendikten sonra en az 10 ADC_TEST turu kaydet.
4. Her turda aynı satırdaki `PZEM[A=... P=... V=...]` ve `K1/K2/K3 avg/std/min/max` alanlarını karşılaştır.
5. Yüksüz referans ile 100 W sonuçlarını karşılaştırmadan kalibrasyon katsayısı belirleme.
6. Kod, log ve rapor birbirinden ayrı, tarihli kayıtlar olarak korunacak; önceki deney üzerine yazılmayacak.

**Sonuç:** Birleşik PZEM + ADC log biçimiyle TUR=1–17 kaydı mevcut. Bir sonraki adım kod değişikliği değil, aynı kodla 100 W yük altında karşılaştırmalı log toplamaktır.
