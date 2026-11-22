# Katsayı Raporu – ADS1115 No.10 / SCT013

**Görev:** MOD2-GRV001  
**Rapor türü:** Birim ve ölçüm zinciri kalibrasyon geçmişi  
**Durum:** AÇIK – 150 W ön analizi (24 eşleşme, K≈30.01) kaydedildi; bias/YAML teyidi ve 100 W verisi bekleniyor  
**Son güncelleme:** 2026-11-22

## 1. Raporun amacı

Bu rapor, ADS1115 **No.10** ile kullanılan SCT013 akım sensörü ve seçilmiş giriş kanalının ölçüm zinciri için katsayı geçmişini tutar. Amaç yalnızca bugün kullanılacak tek katsayıyı saklamak değil; 100 W, 150 W ve diğer referans yüklerde hangi katsayıların hangi gerçek ölçüm verisinden üretildiğini izlenebilir kılmaktır.

Bu kayıt sayesinde ileride:
- 150 W gibi aynı referans yükte eski ve yeni katsayılar karşılaştırılabilir.
- SCT sensörü değiştiğinde önceki sensörün katsayılarıyla yeni sensörün sonuçları karıştırılmaz.
- ADS1115 No.10 başka bir ADS1115 ile değiştirildiğinde kalibrasyon geçmişi korunur.
- Firmware/YAML, bağlantı veya ölçüm kanalı değişikliklerinin katsayıya etkisi incelenebilir.

**Önemli:** Katsayı tek başına ADS1115 entegresinin evrensel özelliği değildir. Kayıt, ADS1115 birim kimliğiyle birlikte SCT sensörü, kanal, analog bağlantı ve yazılım ölçüm zincirini de tanımlar. Başka ADC veya SCT'ye otomatik aktarılmaz.

## 2. Güncel kalibrasyon kararı

- 1.5 A altı çalışma bölgesi için ampullerle (150 W'a kadar) ölçüm yapılacak; sonuçta bu bölge için **tek ortak katsayı** belirlenecek.
- 1.5 A üstü bölge ayrı olarak ütü, tost makinesi ve kettle kaynatma moduyla çalışılacak.
- Her referans yükün kendi katsayısı ayrıca hesaplanıp bu raporda saklanacak. Bu yük bazlı katsayılar geçmiş/karşılaştırma kaydıdır; doğrudan çalışma YAML'ına ayrı ayrı uygulanacakları anlamına gelmez.
- Yeni seri bias kullanılmadan yapılacak. Eski biaslı deneyler yeni seriyle birleştirilmeyecek.
- Mevcut K=27.59, yeni veriler değerlendirilene kadar korunur.
- PZEM karşılaştırma referansıdır; mutlak doğru (ground truth) kabul edilmez.
- 1.5 A sınırında katsayı seçimi ve yazılımsal bölge geçiş yöntemi henüz kararlaştırılmamıştır.

## 3. Kalibrasyon kimliği

| Alan | Kayıt |
|---|---|
| ADC birim kimliği | ADS1115 No.10 |
| I²C adresi | 0x48 |
| Kontrol kartı | ESP32D2 |
| SDA / SCL | GPIO21 / GPIO22 |
| ADC beslemesi | 3.3 V |
| Ortak referans | ESP32D2 GND – ADS1115 GND |
| SCT modeli | SCT013 30A/1V |
| SCT fiziksel kimliği / seri no | Henüz ayrıca etiketlenmedi |
| Aktif giriş | A0–A1 diferansiyel |
| Bias | Yeni kalibrasyon serisinde kullanılmayacak |
| Mevcut katsayı | K=27.59 |
| Mevcut yazılım referansı | MOD2-GRV001 V1.x; her yeni testte tam YAML dosyası yazılacak |
| Ölçüm zinciri | SCT013 → ADS1115 No.10 → ESP32D2 / ESPHome → Home Assistant |

SCT sensörü veya ADS1115 değişirse yeni bir kalibrasyon kimliği açılmalı; eski katsayı geçmişi silinmemelidir.

## 4. Katsayı hesaplama yöntemi

Mevcut Home Assistant SCT akım değeri K=27.59 uygulanmış ölçümdür. Yeni referans katsayı şu şekilde hesaplanır:

`K_{yeni}=K_{mevcut}\times\frac{I_{referans}}{I_{SCT,mevcut}}`

Burada:
- `K_mevcut`: Ölçüm sırasında YAML'da kullanılan katsayı (şu an 27.59).
- `I_referans`: Aynı kararlı zaman aralığındaki PZEM akım ortalaması.
- `I_SCT,mevcut`: Aynı zaman aralığındaki SCT akım ortalaması.

PZEM'in seyrek örneklemesi ve cihazın kendi ölçüm belirsizliği raporda belirtilir. Zaman eşleştirmesi, kararlı aralık seçimi ve dışlanan geçişler her deney için açıklanır. Yalnızca PZEM'in kararlı olması yeterli değildir; SCT serisinin de aynı aralıkta kararlı olması gerekir.

Her yük için önce ayrı katsayı hesaplanır. 1.5 A altı için tek ortak katsayının farklı yük sonuçlarından nasıl türetileceği, 100 W ve 150 W dahil yeni seri tamamlandıktan sonra veriye bakılarak kararlaştırılır. Önceden bir ortalama/ağırlıklandırma yöntemi varsayılmayacaktır.

## 5. Yeni biassız kalibrasyon serisi – sonuç tablosu

Aşağıdaki tablo yalnızca yeni ve aynı bağlantı yaklaşımıyla toplanacak veriler içindir. Henüz ölçülmemiş alanlar boş bırakılmıştır; eski deney sonuçları bu tabloya taşınmamıştır.

| Referans yük | PZEM akım ort. (A) | SCT akım ort. (A) | Eşleşmiş örnek sayısı | SCT std. sapma (A) | Hesaplanan yük katsayısı | Kararlı aralık / not |
|---|---:|---:|---:|---:|---:|---|
| 42 W ampul – 2026-11-22 CSV | 0.187714 | 0.154787 (14 eşleşmiş SCT örneği) | 14 | 0.002587 (tam SCT serisi, n=320) | **≈33.46 (ön sonuç)** | Bias yok; 0,02 A filtreli YAML kullanıcı teyidi; SSR dijital OFF/ON olaylarına rağmen PZEM gücü 42 W civarında; ayrıntı: `DENEYLER/42W-ADS1115-NO10-2026-11-22.md` |
| 57 W ampul – 2026-11-22 CSV | 0.264588 | 0.218940 (17 eşleşmiş SCT örneği) | 17 | 0.001670 (tam SCT serisi, n=246) | **≈33.34 (ön sonuç)** | PZEM gücü ort. 60.46 W; bias/YAML koşulları önceki 42 W oturumundan devam ettiği varsayılıyor, ayrıca teyit bekliyor; ayrıntı: `DENEYLER/57W-ADS1115-NO10-2026-11-22.md` |
| 100 W ampul – 2026-11-22 CSV | 0.469667 | 0.419415 (15 eşleşmiş SCT örneği) | 15 | 0.003318 (tam SCT serisi, n=289) | **≈30.90 (ön sonuç)** | PZEM gücü ort. 107.47 W; bias/YAML/kanal koşulları ayrıca teyit edilmeli; ayrıntı: `DENEYLER/100W-ADS1115-NO10-2026-11-22.md` |
| 150 W ampul – 2026-11-22 CSV | 0.641125 | 0.589506 (24 eşleşmiş SCT örneği) | 24 | 0.003404 (tam SCT serisi, n=193) | **≈30.01 (ön sonuç)** | Yük sürekli açık; SSR olayları dışlama nedeni değil. Bias ve YAML teyidi bekliyor; ayrıntı: `DENEYLER/150W-ADS1115-NO10-2026-11-22.md` |
| Diğer ampul yükleri | — | — | — | — | — | Gerektikçe eklenecek |

### Her yeni test için zorunlu kayıt

1. Test tarihi ve yerel saat aralığı.
2. ADS1115 No.10 ve I²C adresi.
3. SCT model ve fiziksel sensör kimliği.
4. Aktif diferansiyel giriş çifti (A0–A1).
5. Bias kullanılmadığının ve bağlantı düzeninin teyidi.
6. ESPHome cihaz adı ve testte kullanılan YAML dosya adı/sürümü.
7. Kayıt sırasında kullanılan mevcut K.
8. Yükün tanımı ve çalışma koşulu.
9. HA CSV kaynak dosyasının adı; mümkünse kaynak dosyanın arşiv konumu.
10. Kararlı aralıkların başlangıç/bitiş zamanları ve geçiş dışlama gerekçesi.
11. SCT/PZEM örnek sayıları, ortalama, standart sapma ve zaman eşleştirme yöntemi.
12. Hesaplanan katsayı, formülde kullanılan gerçek değerler ve teknik yorum.

## 6. Önceki 150 W kayıtları – tarihsel referans

Bu bölüm yeni biassız kalibrasyon serisi değildir. Daha önce ADS1115 No.10 ile alınmış 150 W kayıtlarını ileride karşılaştırabilmek için korur. Eski deneylerin bağlantı koşulları yeni seriyle aynı olduğu varsayılmamalıdır.

| Tarih / deney | Kanal | SCT ort. (A) | PZEM akım ort. (A) | Mevcut K | Geriye dönük hesaplanan katsayı* | Durum |
|---|---|---:|---:|---:|---:|---|
| 2026-11-22 / history (28).csv | A0–A1 | 0.583896 | 0.647182 | 27.59 | yaklaşık 30.58 | Tarihsel kayıt; yeni biassız seri olarak kullanılmaz |
| 2026-11-22 / history (30).csv | A2–A3 | 0.589707 | 0.643615 | 27.59 | yaklaşık 30.11 | Rapor bağlantı düzeninde bias bulunduğunu belirtiyor; yeni seriyle birleştirilmez |

*Geriye dönük katsayı, raporlanmış ortalamalara formül uygulanarak hesaplanmış karşılaştırma değeridir. Yeni kalibrasyon sonucu veya onaylanmış katsayı değildir. A0–A1 eski deneyinin bias durumu bu raporun dayandığı deney kaydında açıkça kesinleştirilmediğinden varsayım yapılmaz.

Kaynak deney raporları:
- `DENEYLER/150W-TEK-KANAL-A0A1-2026-11-22.md`
- `DENEYLER/150W-TEK-KANAL-A2A3-2026-11-22.md`

## 7. ADS1115 No.10 değişim / yeniden kalibrasyon geçmişi

| Tarih | ADC kimliği | SCT kimliği | Kanal | Firmware/YAML | Referans yük | Katsayı | Değişiklik nedeni / sonuç |
|---|---|---|---|---|---|---|---|
| 2026-11-22 | ADS1115 No.10 | SCT013 30A/1V; fiziksel seri no henüz yok | A0–A1 | V1.1 test kopyası; K=27.59 | 150 W tarihsel test | yaklaşık 30.58 (geriye dönük) | Yeni kalibrasyon değil; eski ölçümden türetilmiş kıyas değeri |

Yeni testler geldikçe her satır ayrı oturum/konfigürasyon olarak eklenir. Sensör değişimi, ADS1115 değişimi, kanal değişimi veya analog bağlantı değişimi açıkça işaretlenir.

## 8. Genel düşük bölge katsayısı – henüz belirlenmedi

| Alan | Sonuç |
|---|---|
| Bölge | 1.5 A altı |
| Kullanılacak referans yükler | Ampuller, 150 W'a kadar |
| Yük bazlı katsayılar | Yeni testlerden sonra doldurulacak |
| Tek ortak düşük bölge katsayısı | **BEKLEMEDE** |
| Birleştirme yöntemi | Veriler görüldükten sonra kararlaştırılacak |
| YAML'a uygulanma | Katsayı ve yöntem onaylandıktan sonra ayrı sürümle |

## 9. Yüksek bölge katsayısı – henüz belirlenmedi

| Alan | Sonuç |
|---|---|
| Bölge | 1.5 A üstü |
| Referans yükler | Ütü, tost makinesi, kettle kaynatma modu |
| Yük bazlı katsayılar | Testlerden sonra doldurulacak |
| Tek ortak yüksek bölge katsayısı | **BEKLEMEDE** |
| 1.5 A sınırındaki geçiş | Henüz kararlaştırılmadı |

## 10. Son karar ve değişiklik kaydı

- Bu rapor katsayıların izlenebilir geçmişidir; YAML değişikliği talimatı değildir.
- K=27.59 yeni testler tamamlanıp sonuçlar değerlendirilene kadar korunur.
- Her yeni katsayı, hangi ADS1115, SCT, kanal, YAML ve referans yükten üretildiği belirtilmeden geçerli kabul edilmez.
- Eski deneyler silinmez veya yeni seriyle birleştirilmez; yalnızca açıkça tanımlanmış karşılaştırma amacıyla kullanılır.


## 11. 2026-11-22 – Birleşik CSV kararlı kademe yeniden değerlendirmesi

Kullanıcının sağladığı `150-42-57-100.csv` dosyasında dört kararlı pencere birlikte yeniden hesaplandı. Bu sonuçlar, daha önce ayrı CSV'ler üzerinden kaydedilen ön hesaplardan farklı pencere kapsamı ve örnek sayıları kullanır; aşağıdaki birleşik pencere sonuçları ayrı bir analiz kaydıdır.

| Yük | UTC pencere | PZEM ort. (A) | A0–A1 ort. (A) | A0–A1 n / std (A) | K (K=27.59 bazında) |
|---|---|---:|---:|---:|---:|
| 42 W | 08:15:03–08:21:00 | 0.18725 | 0.153832 | 357 / 0.002482 | **33.58** |
| 57 W | 08:21:58–08:27:30 | 0.264316 | 0.219024 | 332 / 0.001659 | **33.30** |
| 100 W | 08:28:38–08:38:40 | 0.470103 | 0.423135 | 602 / 0.006738 | **30.65** |
| 150 W | 08:06:38–08:10:45 | 0.641114 | 0.589613 | 247 / 0.003392 | **30.00** |

- 42/57 W katsayıları birbirine yakın; 100/150 W katsayıları da birbirine yakındır. Bu dört kararlı pencere tek sabit katsayının tüm yük seviyelerinde aynı uyumu vermediğini gösterir.
- 100 W penceresi kendi içinde iki A0–A1 seviyesine ayrılır: ilk yaklaşık 230 saniyede ortalama 0.430886 A (K≈30.13), sonraki bölümde 0.418343 A (K≈30.97). PZEM iki alt aralıkta yaklaşık 0.470 A seviyesindedir. Bu nedenle tüm pencere K=30.65 değeri iki alt seviyenin birleşik sonucudur.
- Bias durumu ve YAML dosya/sürümü birleşik CSV'den kesin doğrulanamadı. Katsayılar ön sonuçtur; tek ortak düşük bölge katsayısı seçilmedi.
- K=27.59 ve çalışan YAML korunur; bu analiz firmware değişikliği talimatı değildir.

Ayrıntılı yöntem, pencere istatistikleri ve yorum: `../DENEYLER/150-42-57-100-BIRLESIK-KADEME-ANALIZI-2026-11-22.md`.
