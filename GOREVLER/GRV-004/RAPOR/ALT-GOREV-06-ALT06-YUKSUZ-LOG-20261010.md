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
