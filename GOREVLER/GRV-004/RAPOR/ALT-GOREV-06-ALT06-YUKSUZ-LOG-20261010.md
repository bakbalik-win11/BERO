# PROJE BERO — GRV-004 — ALT-GÖREV-06
## İlk yüksüz RMS logu ve yorum — 2026-10-10

### Hedef
BIAS referanslı ilk RMS sürümünde, yüksüz durumda K1/K2/K3 RMS gerilimlerini gözlemek. Sonraki deneyde yaklaşık 150 W yük altındaki değerlerle karşılaştırmak.

### Kaynak ve kapsam
Kullanıcının paylaştığı `esp32d1-logs (14).txt` dosyasından kaydedildi. Bu kayıt, ALT06 TUR=1–7 sonuçlarını ve PZEM'in yüksüz ölçümlerini içerir. Dosyanın sonu TUR=7 sonucundan önceki PZEM güncellemelerinde bitmektedir; burada görülmeyen devam logları eklenmemiştir.

### Cihaz bağlantısı
- ESPHome: 2026.9.1
- Cihaz: `esp32d1` — `192.168.0.8`
- API bağlantısı ve handshake başarılı.
- Başlangıçta ESPHome, `esp32d1.yaml` için doğrulanmış yapılandırma önbelleğini yükleyip yeniden doğrulamayı atladığını bildirdi.
- Başlangıç uyarıları: `minimum_chip_revision: "3.1"` ve `sram1_as_iram: true` önerileri.
- Bir kez `safe_mode took a long time for an operation (61 ms), max is 50 ms` uyarısı görüldü.

### ALT06 sonuçları — yüksüz

| Tur | PZEM akımı (A) | K1 RMS (V) | K2 RMS (V) | K3 RMS (V) | N |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.028 | 0.020269 | 0.013914 | 0.013700 | 1000 |
| 2 | 0.028 | 0.011212 | 0.014316 | 0.012127 | 1000 |
| 3 | 0.028 | 0.014027 | 0.013047 | 0.010881 | 1000 |
| 4 | 0.028 | 0.011655 | 0.010406 | 0.010793 | 1000 |
| 5 | 0.028 | 0.013743 | 0.015610 | 0.012216 | 1000 |
| 6 | 0.028 | 0.013951 | 0.014037 | 0.012193 | 1000 |
| 7 | 0.028 | 0.015757 | 0.012088 | 0.013235 | 1000 |

PZEM loglarında bu bölüm boyunca gerilim yaklaşık 227.6–228.7 V, güç yaklaşık 1.5–1.7 W, frekans 50.0 Hz olarak görünüyor. PZEM akımı her güncellemede 0.028 A.

### Ham ALT06 log satırları

```text
[20:37:09.015][W][ALT06:140]: TUR=1 PZEM=0.028A K1_RMS=0.020269V K2_RMS=0.013914V K3_RMS=0.013700V N=1000
[20:37:19.407][W][ALT06:140]: TUR=2 PZEM=0.028A K1_RMS=0.011212V K2_RMS=0.014316V K3_RMS=0.012127V N=1000
[20:37:29.824][W][ALT06:140]: TUR=3 PZEM=0.028A K1_RMS=0.014027V K2_RMS=0.013047V K3_RMS=0.010881V N=1000
[20:37:40.169][W][ALT06:140]: TUR=4 PZEM=0.028A K1_RMS=0.011655V K2_RMS=0.010406V K3_RMS=0.010793V N=1000
[20:37:50.551][W][ALT06:140]: TUR=5 PZEM=0.028A K1_RMS=0.013743V K2_RMS=0.015610V K3_RMS=0.012216V N=1000
[20:38:00.998][W][ALT06:140]: TUR=6 PZEM=0.028A K1_RMS=0.013951V K2_RMS=0.014037V K3_RMS=0.012193V N=1000
[20:38:11.445][W][ALT06:140]: TUR=7 PZEM=0.028A K1_RMS=0.015757V K2_RMS=0.012088V K3_RMS=0.013235V N=1000
```

### Yorum
- ALT06 log satırları üretiliyor ve her turda N=1000 bildiriliyor.
- Yüksüz PZEM referansı bu bölümde 0.028 A.
- K1 RMS aralığı: 0.011212–0.020269 V.
- K2 RMS aralığı: 0.010406–0.015610 V.
- K3 RMS aralığı: 0.010793–0.013700 V.
- Bu veriler yalnızca yüksüz taban davranışını gösterir. Yükle birlikte değişim hakkında henüz sonuç çıkarılamaz.
- Standart ESPHome ADC sensörleri ayrı güncellendiği için her K örneğinin BIAS ile eşzamanlı olduğu garanti edilmez. Sonuçlar bu sınırlamayla değerlendirilmelidir.
- RMS sonuçları volt cinsindedir; henüz amper kalibrasyonu değildir.
- PZEM güncellemesi ile 1000 örneklik ADC penceresi tam zaman eşleştirilmiş kabul edilmemelidir.

### Sonraki adım
Mevcut YAML ve bu log kaydı korunacak. Yaklaşık 150 W yük altında aynı ALT06 sürümünden yeni log alınacak; yüksüz ve yük altındaki RMS aralıkları karşılaştırılacak. Kalibrasyon katsayısı bu kayıtla belirlenmeyecek.

### Kod durumu
Bu rapor yalnızca log ve yorum kaydıdır. ALT06 YAML bu işlem sırasında değiştirilmedi. Derleme başarısı bu logdan çıkarılamaz.


---

## Aynı logun devamı — yüksüz devamı ve yaklaşık 150 W yük — 2026-10-10

### Kaynak
Kullanıcının ikinci log dosyası: `esp32d1-logs (15).txt`. Bu dosya TUR=1–27 ALT06 sonuçlarını ve yük altındaki PZEM güncellemelerini içeriyor. Aşağıda rapora daha önce eklenmemiş TUR=8–27 sonuçları kaydedilmiştir. Böylece yüksüz ve yüklü bölümler aynı görev raporunda tutulur.

### Yüksüz devamı — TUR=8–20

| Tur | PZEM (A) | K1 RMS (V) | K2 RMS (V) | K3 RMS (V) |
|---:|---:|---:|---:|---:|
| 8 | 0.028 | 0.016213 | 0.012659 | 0.012104 |
| 9 | 0.028 | 0.011834 | 0.016316 | 0.012804 |
| 10 | 0.028 | 0.014963 | 0.013930 | 0.011849 |
| 11 | 0.028 | 0.012726 | 0.011387 | 0.011201 |
| 12 | 0.028 | 0.012322 | 0.011741 | 0.010543 |
| 13 | 0.028 | 0.013460 | 0.012111 | 0.014520 |
| 14 | 0.028 | 0.017528 | 0.009095 | 0.010994 |
| 15 | 0.028 | 0.015436 | 0.015408 | 0.016598 |
| 16 | 0.028 | 0.014640 | 0.015047 | 0.011194 |
| 17 | 0.028 | 0.012012 | 0.010991 | 0.011988 |
| 18 | 0.028 | 0.009019 | 0.009124 | 0.009782 |
| 19 | 0.028 | 0.018212 | 0.014160 | 0.015165 |
| 20 | 0.028 | 0.013580 | 0.011953 | 0.012475 |

### Yük geçişi ve yaklaşık 150 W bölümü

TUR=21, PZEM'in yükün devreye girdiğini gösterdiği geçiş turudur: 0.338 A / 67.3 W. TUR=22–27 sırasında PZEM yaklaşık 147.6–148.8 W ve 0.650–0.652 A gösterir.

| Tur | PZEM akımı (A) | PZEM güç (W) | K1 RMS (V) | K2 RMS (V) | K3 RMS (V) |
|---:|---:|---:|---:|---:|---:|
| 21 — geçiş | 0.338 | 67.3 | 0.033078 | 0.052178 | 0.017943 |
| 22 | 0.652 | 148.4 | 0.060279 | 0.096495 | 0.025806 |
| 23 | 0.651 | 147.6 | 0.061477 | 0.096912 | 0.027131 |
| 24 | 0.650 | 148.0 | 0.061258 | 0.097390 | 0.028674 |
| 25 | 0.651 | 148.5 | 0.061239 | 0.096445 | 0.028377 |
| 26 | 0.650 | 148.1 | 0.061167 | 0.096428 | 0.028003 |
| 27 | 0.651 | 148.5 | 0.062316 | 0.097448 | 0.027686 |

### Ham yük geçişi ve yük altı ALT06 satırları

```text
[20:40:26.378][W][ALT06:140]: TUR=20 PZEM=0.028A K1_RMS=0.013580V K2_RMS=0.011953V K3_RMS=0.012475V N=1000
[20:40:36.751][W][ALT06:140]: TUR=21 PZEM=0.338A K1_RMS=0.033078V K2_RMS=0.052178V K3_RMS=0.017943V N=1000
[20:40:47.138][W][ALT06:140]: TUR=22 PZEM=0.652A K1_RMS=0.060279V K2_RMS=0.096495V K3_RMS=0.025806V N=1000
[20:40:57.519][W][ALT06:140]: TUR=23 PZEM=0.651A K1_RMS=0.061477V K2_RMS=0.096912V K3_RMS=0.027131V N=1000
[20:41:07.898][W][ALT06:140]: TUR=24 PZEM=0.650A K1_RMS=0.061258V K2_RMS=0.097390V K3_RMS=0.028674V N=1000
[20:41:18.275][W][ALT06:140]: TUR=25 PZEM=0.651A K1_RMS=0.061239V K2_RMS=0.096445V K3_RMS=0.028377V N=1000
[20:41:28.655][W][ALT06:140]: TUR=26 PZEM=0.650A K1_RMS=0.061167V K2_RMS=0.096428V K3_RMS=0.028003V N=1000
[20:41:39.040][W][ALT06:140]: TUR=27 PZEM=0.651A K1_RMS=0.062316V K2_RMS=0.097448V K3_RMS=0.027686V N=1000
```

### Karşılaştırmalı yorum

- Yüksüz TUR=1–20'de PZEM akımı 0.028 A iken, yaklaşık 150 W yük altında TUR=22–27'de 0.650–0.652 A ölçülüyor.
- Yük altındaki RMS değerleri yüksüz gözlenen aralıkların belirgin biçimde üstüne çıkıyor. K1 yaklaşık 0.061–0.062 V, K2 yaklaşık 0.096–0.097 V, K3 yaklaşık 0.026–0.029 V seviyesinde.
- Yük geçişi TUR=21'de K1/K2/K3 RMS değerleri de ara seviyeye çıkıyor. Bu, yükle ilişkili bir yanıt olduğuna dair ilk güçlü gözlem.
- Bu sonuçlar, mevcut uygulamanın RMS değerlerinin yükle değişimi yakaladığını destekler; fakat henüz doğrulanmış amper ölçümü veya kalibrasyon değildir.
- BIAS ve K örnekleri standart ESPHome ADC sensörleriyle ayrı güncellendiğinden eşzamanlılık garanti edilmez. PZEM değeri de ADC penceresiyle tam zaman eşleşmiş kabul edilmemelidir.
- İkinci dosya TUR=27 satırından sonraki PZEM güncellemeleriyle bitiyor; TUR=28 ve sonrası bu kayda eklenmedi.

### Sonraki adım
Bu iki yük durumunun aynı raporda kaydı tamamlandı. Mevcut YAML değiştirilmedi. Bir sonraki teknik adım, mümkünse eşzamanlı örnekleme sağlayan ADC okuma düzenine geçmek ve ardından PZEM referansıyla kalibrasyon deneyini planlamaktır.


---

## ALT06 — İlk deneysel akım tahmini hesabı (iki çalışma durumu)

### Kullanılan ortalamalar

Hesap, yüksüz TUR=1–20 ve yük altındaki TUR=22–27 ALT06 sonuçlarının aritmetik ortalamalarını kullanır.

| Büyüklük | Yüksüz ortalama | Yaklaşık 150 W ortalama |
|---|---:|---:|
| PZEM akımı | 0.028000 A | 0.650833 A |
| K1 RMS | 0.01412795 V | 0.06128933 V |
| K2 RMS | 0.01286700 V | 0.09685300 V |
| K3 RMS | 0.01231810 V | 0.02761283 V |

Akım farkı: `ΔI = 0.65083333 - 0.02800000 = 0.62283333 A`.

### İlk doğrusal tahmin denklemleri

İki ortalama çalışma noktası arasında her kanal için ayrı doğru kuruldu:

```text
I_K1 = 0.028000 + 13.20643 * (K1_RMS - 0.01412795) A
I_K2 = 0.028000 +  7.41592 * (K2_RMS - 0.01286700) A
I_K3 = 0.028000 + 40.72208 * (K3_RMS - 0.01231810) A
```

RMS değerleri volt cinsindedir; katsayıların birimi A/V'dir. Bu denklemler yalnızca bu deneyin yüksüz ve yaklaşık 150 W ortalama noktalarına dayanan **ön kalibrasyon / doğrusal interpolasyon modelleridir**.

### Yük altı turlarına uygulandığında

| Tur | PZEM (A) | K1 tahmini (A) | K2 tahmini (A) | K3 tahmini (A) |
|---:|---:|---:|---:|---:|
| 22 | 0.652 | 0.6375 | 0.6482 | 0.5773 |
| 23 | 0.651 | 0.6533 | 0.6513 | 0.6312 |
| 24 | 0.650 | 0.6504 | 0.6548 | 0.6940 |
| 25 | 0.651 | 0.6502 | 0.6478 | 0.6820 |
| 26 | 0.650 | 0.6492 | 0.6477 | 0.6667 |
| 27 | 0.651 | 0.6644 | 0.6552 | 0.6538 |

### Yorum ve sınırlar

- Ortalama iki çalışma noktasıyla kurulan modelin ortalama tahmini, tanımı gereği PZEM'in iki ortalamasını karşılar; bu durum bağımsız doğrulama değildir.
- Yük altındaki tekil turlarda K1 ve K2 tahminleri PZEM çevresinde daha yakın görünür. K3'ün tahminleri daha fazla saçılır; bu deneyde K3 daha zayıf/oynak bir tahmin adayıdır.
- Yalnızca iki çalışma durumu kullanıldı: yüksüz ve yaklaşık 148 W. Bu nedenle doğrusal davranışın başka akımlarda geçerli olduğu söylenemez.
- PZEM'in 5 saniyelik güncellemesi ADC örnek penceresiyle tam senkron değildir; kanal örnekleri ve BIAS da eşzamanlı garanti edilmemektedir.
- Düşük akımda PZEM'in 0.028 A ve 1.5–1.7 W göstermesi taban noktası olarak kullanıldı; bu, gerçek sıfır akım ölçümü değildir.
- Denklemler çalışma hipotezidir; doğrulanmış akım ölçer sonucu veya üretim kodu olarak kullanılmamalıdır.

### Sonraki doğrulama
Mevcut YAML korunacak. Bir sonraki deneyde mümkünse ara yük seviyeleri (ör. yaklaşık 50 W ve 100 W) kaydedilip aynı katsayılarla tahmin hesaplanmalı ve PZEM ile karşılaştırılmalı. Daha güvenilir kalibrasyondan önce eşzamanlı örnekleme sorunu ayrıca çözülmelidir.
