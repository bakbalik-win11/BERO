# MOD2-GRV001 – Bias kanal çapraz deneyi
**Tarih:** 2026-11-21  
**Durum:** AÇILDI – yeni bağlantı düzeniyle ölçüm bekleniyor.  
**Fiziksel ADC:** ADS1115 No.10, I²C 0x48  
**Kontrol kartı:** ESP32D2  
**Amaç:** İlk karşılaştırmada görülen farkın bias bağlantısını mı, yoksa ADS1115 kanal/sensör kolunu mu izlediğini çapraz bağlantıyla incelemek.

## 1. Önceki deneyin bağlantısı
| ADS1115 kanalı | Koşul |
|---|---|
| A0–A1 | Bias yok |
| A2–A3 | Bias var |

İlk deneyin verileri ve yorumu önceki raporda korunur; bu yeni deney önceki verinin üzerine yazmaz.

## 2. Yeni deney bağlantısı – kullanıcı tarafından bildirilen
| ADS1115 kanalı | Yeni koşul |
|---|---|
| A0–A1 | **Bias var** |
| A2–A3 | **Bias yok** |

Kanal çiftlerinin bağlantı düzeni çaprazlanmıştır. Bias artık A0–A1 ölçüm kolundadır. A2–A3 ölçüm kolunda bias bulunmayacaktır.

## 3. Sabit tutulacaklar
- Aynı fiziksel ADS1115 No.10 ve ESP32D2 kullanılacak.
- İki kanallı mevcut YAML kullanılacak; bu deney için YAML veya firmware değişikliği yapılmayacak.
- Mevcut çalışan tek kanallı V1.1 dosyasına dokunulmayacak.
- Aynı iki SCT013 sensörü, aynı faz iletkeni, aynı yön ve aynı fiziksel konum korunacak.
- Yük ve diğer test koşulları ilk deneyle karşılaştırılabilir tutulacak.
- Kanal isimleri yazılımda A0–A1 ve A2–A3 olarak kalır; fiziksel bias eşlemesi bu rapordaki yeni düzene göre yorumlanır.

## 4. Yazılım ve ölçüm yapılandırması
Mevcut iki kanallı YAML:  
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/MOD2-GRV001_V1.1_IKI-KANAL-DENEY.yaml`

Bu YAML'de iki kanal için ADS1115 diferansiyel okuma, 200 ms ct_clamp penceresi, 1 saniye güncelleme ve mevcut K=27.59 filtresi tanımlıdır. Kod değiştirilmediği için bu deney ham ADC dalga biçimi deneyi olarak adlandırılmaz; mevcut yapılandırmanın ürettiği iki akım kanalının karşılaştırmasıdır.

## 5. Deney öncesi kontrol
- Bias orta noktasının DC gerilimini ölç ve kaydet.
- A0, A1, A2 ve A3 pinlerinin her birinin GND'ye göre mutlak gerilimini kontrol et.
- ADS1115 girişleri GND−0.3 V ile VDD+0.3 V sınırları içinde kalmalıdır; diferansiyel ölçüm bu sınırı değiştirmez.
- Bağlantı değişikliklerini enerjisiz durumda yap.
- Fiziksel bağlantı doğrulanmadan ölçüm sonucu alınmış kabul edilmez.

## 6. Beklenen kayıtlar
- Bağlantı fotoğrafı veya açık bağlantı teyidi.
- Bias orta noktasının DC ölçümü ve A0/A1/A2/A3 mutlak pin gerilimleri.
- ESPHome çalışma logu.
- Home Assistant CSV verisi varsa kaynak dosya ve zaman aralığı.
- Her kanal için örnek sayısı, ortalama, standart sapma, minimum ve maksimum.
- Önceki deneyle aynı yöntem kullanılarak karşılaştırma.

## 7. Yorum ölçütü
Bias etkisi kanallar arasında taşındığında ölçüm farkı da bias ile birlikte kanal değiştiriyorsa bias etkisi lehine bulgu oluşur. Fark aynı kanal/sensör kolunda kalırsa kanal, SCT toleransı veya fiziksel yerleşim etkisi olasılığı güçlenir. Tek çapraz deney kesin nedensellik kanıtı sayılmaz.

## 8. Mevcut durum
**Deney açıldı; fiziksel ölçüm henüz yapılmadı.** Bu dosya yalnızca yeni bağlantı düzenini ve test planını kaydeder. Sonuç, log veya başarı iddiası içermez. İlk deneyin verileri değiştirilmemiştir.
