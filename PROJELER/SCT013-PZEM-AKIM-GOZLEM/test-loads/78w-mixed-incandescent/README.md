# 78,10 W Karma Akkor Yük — Ölçülebilir Alan Başlangıç Kaydı

**Test ID:** LOAD-78W-001  
**Tarih:** 2026-11-07  
**Yük düzeni:** 57 W + 18 W akkor ampul; nominal toplam 75 W  
**PZEM aktif güç bildirimi:** 78,10 W  
**İşletim:** Sürekli açık; aç/kapa deneyi değil  
**Durum:** EKRAN GÖZLEMİ KAYDEDİLDİ — ölçülebilir alan başlangıç noktası olarak kabul edildi

## Amaç ve karar

18 W ve 57 W deneylerinde CH1 hesaplanan akım değeri 0,24–0,41 A hesaplanmadı alanında kaldı. 100 W kısa deneyinde CH1 ve PZEM ortalamaları yakınlaştı. 57 W + 18 W karma yükte kullanıcı PZEM'in 78,10 W gösterdiğini bildirdi ve paylaşılan HA History ekranında CH1 ile PZEM akım göstergeleri birbirine yakın göründü.

**Kullanıcı kararı (2026-11-07):** Mevcut sabit test yükleriyle ölçülebilir alanın başlangıcı 78 W olarak kabul edilecek. Bu kurulumda 78 W ve üzerindeki yüklerde CH1 sayısal akım değeri verilebilir; 78 W altındaki alan için önceki deney sınıflandırmaları korunur.

Bu karar mevcut CH1 / SCT-1T / K=24.22 kurulumuna ve bugüne kadarki test yüklerine özgüdür. Fiziksel sensörün evrensel alt ölçüm sınırı veya tüm yük tipleri için garanti değildir.

## Düzenek

- Yükler: 57 W + 18 W akkor ampul.
- Toplam nominal etiket gücü: 75 W (kullanıcı tarafından belirtilen yüklerin toplamı).
- PZEM: Modül 3 WROOM / PZEM-004T V3.0.
- SCT: ESP32D1 / Modül 2 / CH1-1T Faz, GPIO32.
- Kayıt kaynağı: Kullanıcının 2026-11-07 tarihinde paylaştığı Home Assistant History ekran görüntüsü ve PZEM 78,10 W kullanıcı bildirimi.
- Kaynak CSV bu kayıt için henüz sağlanmadı; tam zaman aralığı ve örnek sayısı doğrulanmadı.
- Firmware/K=24.22 değiştirildiğine dair bilgi yoktur; bu deneyde katsayı değişikliği yapılmadı.

## Ekran gözlemi — LOG GÖRÜNTÜSÜ / KULLANICI BİLDİRİMİ

Paylaşılan grafiğin son lejant değerleri:
- PZEM akımı: 0,341 A.
- CH1 hesaplanan akım: 0,366 A.
- CH1 ham SCT entity'si: 0,01512 A.
- PZEM aktif güç: kullanıcı bildirimi 78,10 W.

Ekran lejantındaki bu son değerler tekil anlık/son yayın değerleridir; CSV kararlı pencere istatistiği değildir.

**Ekran değerlerinden hesap:** CH1 ile PZEM akımı arasındaki mutlak fark 0,025 A; PZEM'e göre bağıl fark yaklaşık %7,33'tür. Bu nedenle bu ekran görüntüsü ±%4 kabulünü kanıtlamaz. Kullanıcının kararı, bu yük noktasında CH1'in artık sayısal değer verebilecek ölçüm bölgesine geçtiği yönündedir; katsayı doğrulaması ayrı değerlendirilir.

## Önceki sabit yüklerle bağlam

| Yük | PZEM gücü / akımı | CH1 davranışı | Sınıf |
|---|---|---|---|
| 18 W | ort. 17,635 W / 0,07824 A | ort. 0,30571 A; SD 0,04477 A; hesaplanmadı bandında | Ölçülebilir değil |
| 57 W | ort. 59,8405 W / 0,26307 A | ort. 0,35550 A; SD 0,01786 A; hesaplanmadı bandında | Ölçülebilir değil |
| 78,10 W | 0,341 A son ekran değeri | 0,366 A son ekran değeri | Ölçülebilir alan başlangıcı — kullanıcı kararı |
| 100 W kısa | CSV analizinde PZEM ort. 0,46923 A; CH1 ort. 0,46924 A | CH1 SD 0,01333 A; yaklaşık 8 dk analiz | Ölçülebilir; güçlü karşılaştırma |

100 W kaydının ayrıntısı ayrı test yükü kaydında tutulur. 78,10 W ekranındaki son değerler ile 100 W CSV ortalamaları aynı tür istatistik değildir; doğrudan eşdeğer hassasiyette karşılaştırılmamalıdır.

## Karar ve açık sınırlar

- **Ölçülebilir alan başlangıcı: 78 W** olarak kabul edildi.
- 78 W noktası için CH1 sayısal değeri raporlanabilir; ekranda görülen değer 0,366 A'dır.
- 78 W noktasında katsayının ±%4 içinde olduğu henüz doğrulanmış değildir; ekran son değerlerinden hesaplanan fark yaklaşık %7,33'tür.
- 78 W için CSV, uzun kararlı pencere istatistikleri ve zaman aralığı henüz yoktur.
- K=24.22 bu kararla değiştirilmedi.
- 18 W ve 57 W kayıtlarının 0,24–0,41 A hesaplanmadı sınıfı tarihsel kayıt olarak korunur.
- 78 W sınırı mevcut CH1 kurulumuna özgüdür; başka SCT kanalı, sarım sayısı, CT modeli veya analog ön uç için otomatik genellenmez.

**Sonraki doğrulama:** 78 W karma yükte CSV alınırsa kararlı pencere ortalama/medyan/SD/P95 ve PZEM-SCT farkı hesaplanarak bu başlangıç noktası yeniden incelenebilir.
