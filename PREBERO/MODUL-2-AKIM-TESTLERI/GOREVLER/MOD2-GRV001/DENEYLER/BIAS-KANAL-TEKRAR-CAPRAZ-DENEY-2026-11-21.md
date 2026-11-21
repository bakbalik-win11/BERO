# MOD2-GRV001 – Bias kanal tekrar çapraz deneyi (3. deney)

**Tarih:** 2026-11-21  
**Durum:** AÇILDI – fiziksel bağlantı ve ölçüm bekleniyor.  
**Amaç:** İlk iki çapraz deneyde gözlenen ortalama ölçüm farkının bias bağlantısını takip ettiği bulgusunu üçüncü bir tersleme ile tekrar etmek; biasın ölçüm sonucuna pozitif katkısı olduğu hipotezini teyit etmeye çalışmak.

## 1. Önceki iki deneyin özeti

| Deney | A0–A1 | A2–A3 | Gözlenen yüksek ortalama |
|---|---|---|---|
| 1. deney | Bias yok | Bias var | A2–A3 / biaslı kol |
| 2. deney | Bias var | Bias yok | A0–A1 / biaslı kol |
| 3. deney (bu kayıt) | Bias yok | Bias var | Sonuç ölçümden sonra değerlendirilecek |

İlk iki deneyde yüksek ortalamanın biaslı kola taşınması, biasın ölçüm sonucunu etkilediği yönünde bulgudur. Üçüncü deney bu örüntünün tekrar edip etmediğini sınayacaktır.

## 2. Üçüncü deney bağlantısı

| ADS1115 kanalı | Koşul |
|---|---|
| A0–A1 | **Bias yok** |
| A2–A3 | **Bias var** |

Bu bağlantı ilk deneyin kanal eşlemesini tekrar eder; ikinci deneyin tersidir.

## 3. Sabit tutulacak koşullar

- Fiziksel ADC: ADS1115 No.10, I²C 0x48.
- Kontrol kartı: ESP32D2.
- İki ayrı SCT013 30A/1V sensörü kullanılacak.
- Aynı SCT sensörleri, aynı faz iletkeni, aynı yön ve mümkün olduğunca aynı fiziksel konum korunacak. Sensörler yer değiştirmeyecek.
- Yük/çalışma noktası önceki iki deneye mümkün olduğunca yakın tutulacak.
- Bias beslemesi **Modül 1** olarak kalacak. Bu deneyde ESP kartından bias beslemesine geçilmeyecek; besleme kaynağını değiştirmek ayrı bir deney değişkenidir.
- Mevcut iki kanallı YAML aynen kullanılacak; kod, firmware, K=27.59 ve diğer ölçüm parametreleri değiştirilmeyecek.
- Mevcut çalışan tek kanallı V1.1 YAML korunacak; üzerine yazılmayacak.

## 4. Değiştirilecek tek fiziksel koşul

Bias bağlantısı A0–A1'den alınarak A2–A3 koluna taşınacak. Başka bir kablo, sensör konumu, yazılım ayarı, katsayı veya besleme değiştirilmeyecek.

## 5. Deney öncesi kontroller

1. Bağlantı değişikliğini enerji kesikken yap.
2. Bias orta noktasının DC gerilimini ölç ve kaydet.
3. A0, A1, A2 ve A3 pinlerinin her birinin GND'ye göre mutlak gerilimlerini kontrol et.
4. ADS1115 girişleri GND−0.3 V ile VDD+0.3 V sınırları içinde kalmalı; diferansiyel ölçüm bu mutlak sınırları değiştirmez.
5. İki SCT'nin aynı iletkeni aynı yönde ölçtüğünü ve fiziksel konumlarının değişmediğini teyit et.
6. Bağlantı fotoğrafı veya açık fiziksel bağlantı teyidini deney kaydına ekle.
7. ESPHome logu ve Home Assistant dışa aktarımını deney zaman aralığıyla birlikte sakla.

## 6. Değerlendirme yöntemi

- Her kanal için örnek sayısı, ortalama, standart sapma, minimum, maksimum ve CV hesaplanacak.
- PZEM akımı karşılaştırma referansı olarak kullanılacak; ground truth kabul edilmeyecek.
- PZEM ve SCT kayıtları aynı yöntemle ±2 saniye içinde zaman eşleştirilecek.
- Biaslı ve biassız kolların PZEM'e göre ortalama farkı ve MAPE değeri raporlanacak.
- İlk iki deneyle birlikte değerlendirildiğinde yüksek ortalamanın yine biaslı A2–A3 koluna geçip geçmediği incelenecek.
- Biaslı kolun PZEM'e daha yakın olması ölçüm sonucuna pozitif katkı lehine; yalnızca daha yüksek değer üretmesi tek başına doğruluk artışı kanıtı değildir.
- Gürültü/kararlılık katkısı, standart sapma ve CV sonuçları üzerinden ayrıca değerlendirilecek. Önceki deneylerde CV farkı tutarlı olmadığından gürültü azalması varsayılmayacak.

## 7. Hipotez ve karar sınırı

**Hipotez:** Bias bağlantısı hangi kanala taşınırsa taşınsın, aynı koşullarda biaslı kolun ölçümü benzer yönde değişir ve PZEM karşılaştırma referansına daha yakın kalır.

Üçüncü deneyde bias A2–A3'e taşındığında daha yüksek ortalama yeniden A2–A3'te görülür ve PZEM karşılaştırması da biaslı kol lehine sonuçlanırsa, biasın bu yaklaşık 0.47 A çalışma bölgesinde ölçüm sonucuna tekrarlanabilir pozitif katkı yaptığı yönündeki kanıt güçlenecektir.

Bu sonuç tek başına:
- biasın tüm akım aralığında gerekli olduğunu,
- her koşulda gürültüyü azalttığını,
- ölçümün mutlak doğruluğunu,
- tek K katsayısının tüm aralıkta yeterli olduğunu

kanıtlamaz. İki ayrı SCT sensörünün tolerans farkı ve ADS1115 kanallarının ardışık dönüşümü yorum sınırı olarak kalır.

## 8. Deney tamamlanınca arşivlenecek çıktılar

- Gerçek ESPHome logu.
- Kaynak Home Assistant CSV dosyası.
- Analiz/ eşleştirme CSV dosyası.
- İstatistik ve PZEM karşılaştırmasını içeren teknik rapor.
- Sonuç yorumu ve karar.
- Kaynak verinin birebir arşivlenip arşivlenmediği açıkça belirtilecek; kaynak dosya yoksa varmış gibi yol yazılmayacak.

**Durum güncellemesi (2026-11-21):** HA kaynak verisi alındı, analiz edildi ve arşivlendi. Fiziksel kanal-bias eşlemesi kullanıcı tarafından ayrıca teyit edilmelidir. Sonuçlar ve yorum için V1.1 raporuna bakınız.


## 9. Üçüncü deney veri sonucu (2026-11-21)

HA dışa aktarımı `history (10).csv` üzerinden 199 A0–A1, 199 A2–A3 ve 15 PZEM akım kaydı analiz edildi. Planlanan eşlemeye göre A0–A1 biassız ortalama 0.459638 A, A2–A3 biaslı ortalama 0.472490 A oldu. PZEM ortalaması 0.469267 A. ±2 saniye eşleştirmede MAPE A0–A1 için %2.508, A2–A3 için %1.819 bulundu.

Üçüncü deneyde de planlanan biaslı kolun ortalaması daha yüksek ve PZEM referansına göre MAPE daha düşüktür. Ancak fiziksel bağlantı eşlemesi ayrıca teyit edilmelidir. Biaslı kolun CV değeri %2.138, biassız kolun %1.871 olduğundan bu veri gürültü azalmasını desteklemez. PZEM ground truth değildir; K=27.59 korunmuş, yeni K hesaplanmamıştır.

**Arşiv:**
- Ham HA CSV: `V1.1/LOG/V1.1-BIAS-KANAL-TEKRAR-HA-KAYNAK-2026-11-21.csv`
- PZEM eşleştirme: `V1.1/LOG/V1.1-BIAS-KANAL-TEKRAR-PZEM-ESLESTIRME-2026-11-21.csv`
- Rapor: `V1.1/RAPOR/V1.1-BIAS-KANAL-TEKRAR-2026-11-21.md`

Ayrı ESPHome logu bu veri paketinde bulunmamaktadır. MOD2-GRV001 görevi açık kalır.
