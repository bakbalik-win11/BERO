# 18 W Akkor Ampul — Sürekli Açık Düşük Akım Gözlemi

**Test ID:** LOAD-18W-001  
**İlişkili deney:** E17-A  
**Tarih:** 2026-11-07  
**Yük:** 18 W akkor ampul (kullanıcı tarafından bildirildi)  
**İşletim:** Sürekli açık; test yükü için aç/kapa çevrimi yok  
**Durum:** CSV ANALİZİ YAPILDI — düşük akım karakteristik gözlemi

## Amaç ve düzenek

18 W sürekli yükte PZEM-004T V3.0 referans akışı ile ESP32D1 / Modül 2 / CH1-1T Faz (GPIO32) davranışını gözlemek. Bu kayıt kalibrasyon veya düşük akım doğruluk kabul testi değildir.

- Yük deney boyunca sürekli açık tutuldu; yük hattında aç/kapa çevrimi yapılmadı.
- PZEM: Modül 3 WROOM / PZEM-004T V3.0.
- SCT: ESP32D1 / Modül 2 / CH1-1T Faz, GPIO32 / ADC1_CH4.
- Ham SCT entity'si ayrıca izlendi.
- Firmware/K=24.22 ve ölçüm ayarları için bu oturumda değişiklik kaydı yoktur.
- Analiz aralığı kullanıcı kararıyla **10:30–12:00 (Europe/Istanbul)** olarak sınırlandı. PZEM'in devreye alınma geçişi ve 10:30 öncesi kayıtlar analize alınmadı.

## Kaynak CSV

- Dosya adı: `18w 3 saat.csv`
- Analizde kullanılan aralık: 2026-11-07 10:30:00–11:59:59.857 (+03:00), 90 dakika.
- Dosya boyutu: 1.200.152 bayt.
- Kaynak SHA-256: `7a6c63e48891a7bc92fdc705d70c6b2db8e8a2e88e204a43de10ff71e1e8ce52`.
- Ham CSV Git'e eklenmedi; dosya kullanıcı yüklemesinde korunur. Aşağıdaki özet kaynak CSV'den hesaplandı.

## PZEM sonuçları — LOG İLE DESTEKLENDİ

| Parametre | Örnek | Ortalama | Min–Maks |
|---|---:|---:|---:|
| Akım | 122 | 0,07824 A | 0,077–0,079 A |
| Aktif güç | 537 | 17,6350 W | 16,8–18,1 W |
| Gerilim | 977 | 227,0296 V | 220,1–230,7 V |
| Güç faktörü | 393 | 0,9950 | 0,99–1,00 |
| Frekans | 101 | 49,9505 Hz | 49,9–50,0 Hz |

## CH1 sonuçları — LOG İLE DESTEKLENDİ

Entity: `sensor.esp32d1_bero_mod2_ch1_1t_faz_akim`.

| İstatistik | Sonuç |
|---|---:|
| Örnek sayısı | 5.401 |
| Ortalama | 0,30571 A |
| Medyan | 0,29920 A |
| Standart sapma (örnek) | 0,04477 A |
| Değişim katsayısı | %14,64 |
| P95 | 0,36962 A |
| P99 | 0,48067 A |
| Min–Maks | 0,21478–1,29129 A |
| 0,41 A üzeri | 179 / 5.401 (%3,31) |
| 0,45 A üzeri | 102 / 5.401 |
| 0,50 A üzeri | 31 / 5.401 |

Ham SCT entity'si: 5.401 örnek; ortalama 0,012622 A, medyan 0,012353 A, min–maks 0,008868–0,053315 A. Ham SCT entity'si, hesaplanmış CH1 akımı ve PZEM akımı farklı katmanlardır; birimleri/semantik anlamları gözetilmeden doğrudan karşılaştırılmaz.

## Karakteristik ve yorum

- PZEM 90 dakika boyunca yaklaşık 0,078 A ve 17,6 W seviyesinde kararlı bir küçük yük kaydı üretmiştir.
- CH1 hesaplanmış akım ortalaması yaklaşık 0,306 A olsa da standart sapma 0,04477 A ve CV %14,64'tür.
- CH1'de 1,29129 A'ya ulaşan tekil yüksek değer vardır; 0,41 A üzerindeki örnek oranı %3,31'dir.
- Bu kayıt, 18 W koşulunda CH1 dağılımının 57 W oturumuna göre daha geniş ve yüksek sıçramaların daha belirgin olduğunu gösterir.
- Bu fark iki ayrı oturumun gözlemsel karşılaştırmasıdır; tek başına yük gücünün nedensel etkisini kanıtlamaz.

## Karar ve sınırlar

CH1 için geçerli proje sınıflandırması korunur: **0,24–0,41 A hesaplanmadı alanıdır.** 0,30571 A ortalama bu nedenle doğru akım ölçümü, kalibrasyon sonucu veya ±%4 doğrulaması olarak kabul edilmez. PZEM bu projede karşılaştırma referansıdır; mutlak ground truth değildir.

Firmware, K katsayısı, filtre veya yazılımsal sıfır eşiği değiştirilmedi. Bu kayıt düşük akım davranış karakteristiği olarak saklanır.

Ayrıntılı oturum ve 57 W karşılaştırması: [E17 — sürekli düşük yük gözlemleri](../../experiments/E17-low-current-continuous-load-observation/README.md), [57 W kayıt dosyası](../57w-incandescent/README.md).
