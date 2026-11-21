# 150 W Sabit Yük – İki Kanallı Referans Kaydı

**Tarih:** 2026-11-22 (Türkiye saati; CSV zamanları UTC+3'e çevrilmiştir)  
**Görev:** MOD2-GRV001  
**Durum:** REFERANS KAYDI ALINDI – TEK KANAL KARŞILAŞTIRMASI BEKLİYOR  
**Kaynak:** Kullanıcının sağladığı `history (27).csv`  
**Firmware/YAML:** Mevcut iki kanallı V1.1; bu kayıt için yazılım değişikliği yapılmadı  
**Katsayı:** K=27.59 korundu

## 1. Amaç

Yaklaşık 150 W sabit yükte A0–A1 ve A2–A3 kanallarının birlikte çalışma davranışını kaydetmek. Bu kayıt, daha sonra yapılacak tek kanal ölçümleri için çift kanal referansıdır. ADS1115 kanal sıralaması veya örnekleme zamanlaması hakkında tek başına kök neden kanıtı değildir.

## 2. Donanım ve ölçüm düzeni

- Kontrol kartı: ESP32D2
- ADC: ADS1115 No.10, I²C 0x48
- I²C: SDA GPIO21, SCL GPIO22
- A0–A1: SCT akım kanalı
- A2–A3: ikinci SCT akım kanalı (biaslı hat)
- İki kanal aynı anda aktif
- Referans: PZEM; ground truth kabul edilmez.

Mevcut iki kanallı YAML ayarları: ADS1115 continuous mode, 860 SPS, PGA 2.048 V; iki `ct_clamp` için 200 ms pencere ve 1 s güncelleme. Bu deneyde ayarlar değiştirilmedi.

## 3. Kayıt kapsamı

- Kaynak dosya: `history (27).csv`
- Ham satır sayısı: 598
- Zaman aralığı: 2026-11-22 00:55:00–00:58:54 Türkiye saati
- PZEM güç: 36 geçerli (sıfır dışı) örnek
- PZEM akım: 15 geçerli (sıfır dışı) örnek
- A0–A1: 236 örnek
- A2–A3: 235 örnek

PZEM'in ilk sıfır değerleri açılış/geçiş kaydı olarak değerlendirildi ve akım karşılaştırma istatistiklerine alınmadı.

## 4. Sonuçlar

| Ölçüm | Örnek | Ortalama | Std. sapma | Min–Max |
|---|---:|---:|---:|---:|
| PZEM güç (W, sıfır dışı) | 36 | 150.981 W | 0.894 W | 149.6–152.5 W |
| PZEM akım (A, sıfır dışı) | 15 | 0.64913 A | 0.00177 A | 0.647–0.652 A |
| A0–A1 (A) | 236 | 0.59877 A | 0.00876 A | 0.57519–0.62008 A |
| A2–A3 (A) | 235 | 0.60157 A | 0.00563 A | 0.58906–0.61558 A |

- A0–A1 değişim katsayısı (CV): %1.462
- A2–A3 değişim katsayısı (CV): %0.936
- İki SCT kanalının ortalama farkı: 0.00280 A (A2–A3 daha yüksek).
- PZEM ile ±2 saniye en yakın zaman eşleştirmesinde 15 eşleşme bulundu:
  - A0–A1 MAPE: %8.061
  - A2–A3 MAPE: %7.065

Bu MAPE değerleri PZEM'i karşılaştırma referansı alır; mutlak doğruluk ölçüsü değildir. PZEM'in örnekleme aralığı seyrek olduğundan zaman eşleştirmesi sınırlıdır.

## 5. Teknik yorum

1. Kayıt, PZEM güç değerlerine göre yaklaşık 151 W seviyesinde kararlı bir yükü temsil ediyor.
2. İki SCT kanalının ortalamaları birbirine çok yakın; fark yaklaşık 2.8 mA.
3. Bu veri setinde A2–A3 kanalının CV değeri A0–A1'den düşüktür. Tek bir kısa oturum bu farkın kalıcı kanal/bias avantajı olduğunu kanıtlamaz.
4. Her iki SCT ortalaması da PZEM akım ortalamasının altındadır. PZEM ground truth değildir; K katsayısı bu kayda dayanarak değiştirilmez.
5. Her iki kanalın da birlikte çalıştığı bu kayıt, tek kanal okuma hipotezini henüz sınamaz.

## 6. Sonraki deney

Aynı sabit yük, sensör konumları ve kablolama korunarak ayrı firmware kopyalarıyla:

1. Yalnız A0–A1 aktif: en az 3 dakika kayıt.
2. Yalnız A2–A3 aktif: en az 3 dakika kayıt.
3. Her iki aşamada PZEM kaydı devam edecek.
4. 860 SPS, 200 ms pencere, 1 s güncelleme ve K=27.59 korunacak.
5. Mevcut çalışan iki kanallı YAML üzerine yazılmayacak.

Tek kanal kayıtları bu referansla karşılaştırılarak küçük dalgalanmanın çift kanal çalışma düzeniyle ilişkisi araştırılacak.

## 7. Değişiklik ve güvenlik notu

- Bu deneyde YAML, firmware, filtre, örnekleme süresi veya kalibrasyon katsayısı değiştirilmedi.
- ADS1115 A0–A3 pinlerinin her birinin GND'ye göre mutlak gerilimi besleme sınırları içinde tutulmalıdır.
- SCT yalnızca yalıtılmış tek iletkeni kavramalı; ESP32 GND şebekeye bağlanmamalıdır.

## 8. Arşiv notu

Bu rapor ve türetilmiş özet CSV GitHub'a kaydedilmiştir. Kullanıcının sağladığı ham `history (27).csv` dosyasının bu işlemde GitHub'a birebir kopyası eklenmemiştir; ham kaynak bu konuşmadaki ek dosyadır. Rapor istatistikleri bu ham dosyadan hesaplanmıştır.
