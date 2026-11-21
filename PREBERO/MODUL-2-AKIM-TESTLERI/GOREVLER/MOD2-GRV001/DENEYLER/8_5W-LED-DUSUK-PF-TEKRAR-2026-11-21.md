# MOD2-GRV001 – 8.5 W LED düşük PF tekrar deneyi

**Tarih:** 2026-11-21  
**Modül:** Modül 2 – ESP32D2 / ADS1115 fiziksel modül No.10 / SCT013 30A-1V  
**Karşılaştırma:** Modül 3 PZEM  
**Yük:** Tek adet 8.5 W LED ampul  
**Firmware:** V1.1 – katsayı 27.59 (değiştirilmeyecek)  
**Dimmer:** Kullanılmayacak  
**Durum:** AÇILDI – ölçüm bekleniyor.

## 1. Amaç

Dimmer kullanılmadan, 8.5 W LED ampulün doğal çalışma koşulunda PZEM tarafından raporlanan güç faktörünü (PF) ve SCT/ADS1115 akım ölçümünü tekrar incelemek.

Önceki düşük yük çalışmalarında 15 W akkor ampul + 8.5 W LED kombinasyonunda yaklaşık 0.093 A civarında düşük akım kaydı görülmüş, bu bölgedeki ölçüm davranışı yeterince doğrulanamamıştı. Bu deneyde tek 8.5 W LED ampul ayrı yük olarak ele alınacaktır. Önceki ölçüm bu yeni deneyin sonucu sayılmayacaktır.

Ana araştırma sorusu: PZEM PF değeri ile SCT/ADS1115 akım sapması arasında tekrarlanabilir bir ilişki bulunabilir mi? İleride bu ilişki kullanılarak PF'ye bağlı düzeltme katsayısı oluşturulabilir mi?

## 2. Kapsam ve değişmeyecekler

- V1.1 YAML ve 27.59 katsayısı sabit kalacak.
- Firmware, ADS1115 PGA, örnekleme, filtre ve ct_clamp ayarları değiştirilmeyecek.
- Dimmer, faz kesme veya harici akım ayarlama yöntemi kullanılmayacak.
- Yalnızca tek 8.5 W LED ampul kullanılacak; aynı deney penceresinde başka yük eklenmeyecek.
- PZEM karşılaştırma referansıdır; kusursuz ground truth kabul edilmeyecektir.
- UT200B+ pens ölçümü, kablo geometrisi ve tek iletken kavrama koşulu güvenilir şekilde sağlanmadıkça bu deneyin zorunlu ölçümü değildir. Pens değeri varsa ayrı not edilir; PZEM/SCT zaman penceresiyle eşzamanlı olduğu varsayılmaz.

## 3. Donanım ve bağlantı bağlamı

- Yük: Tek 8.5 W LED ampul.
- Akım algılama: SCT013 30A/1V.
- ADC: ADS1115 fiziksel modül No.10, A0-A1 diferansiyel ölçüm.
- Kontrol/kayıt: ESP32D2 / Modül 2.
- Karşılaştırma: Modül 3 PZEM.
- Şebeke: 220–230 V, 50 Hz nominal.

Şebeke bağlantıları kapalı ve dokunmaya karşı korumalı düzende olmalıdır. Enerjili kablo veya klemens üzerinde değişiklik yapılmamalıdır.

## 4. Deney protokolü

1. V1.1 firmware'in çalıştığı ve 27.59 katsayısının değişmediği doğrulanır.
2. Dimmer olmadan tek 8.5 W LED ampul devreye alınır.
3. İlk açılış/geçiş davranışı analiz penceresine alınmaz.
4. Kararlı duruma geldikten sonra en az 60–120 saniye kayıt alınır.
5. Ampul kapatılıp yeniden açılarak ölçüm en az üç bağımsız çevrimde tekrarlanır.
6. Her çevrimde PZEM akım, gerilim, aktif güç ve PF ile SCT akım verisi aynı zaman aralığında kaydedilir.
7. Her kararlı pencerede mümkünse en az 10 geçerli PZEM akım/PF örneği hedeflenir. Daha az örnek varsa pencere düşük güvenli olarak işaretlenir.
8. Ampulün kararlı çalışma sırasında PF değeri değişmiyorsa bu durum özellikle kaydedilir; tek PF noktasından korelasyon modeli türetilmez.

## 5. Kaydedilecek alanlar

- Yerel başlangıç/bitiş zamanı (Europe/Istanbul)
- PZEM gerilim ortalaması (V)
- PZEM aktif güç ortalaması (W)
- PZEM akım ortalaması (A)
- PZEM PF ortalaması ve standart sapması
- PZEM geçerli örnek sayısı
- SCT/ADS1115 akım ortalaması (A)
- SCT standart sapması (A)
- SCT örnek sayısı
- V1.1 katsayısı (27.59)
- Pencere için hesaplanan gerekli katsayı
- SCT/PZEM sapması (%)
- Ampul çevrim numarası ve gözlemler

## 6. Hesaplamalar

Mevcut V1.1 çıkışı üzerinden:

`Sapma (%) = ((I_SCT - I_PZEM) / I_PZEM) × 100`

Pencere için gerekli katsayı:

`K_gerekli = 27.59 × (I_PZEM / I_SCT)`

Oran:

`R = I_SCT / I_PZEM`

PF düzeltme modeli araştırılırsa önce PF ile R veya K_gerekli arasındaki ilişki incelenecektir. PZEM PF değeri bağımsız gerçek PF standardı olarak değil, bu deneydeki ölçüm değişkeni olarak kullanılacaktır.

## 7. Korelasyon ve düzeltme katsayısı için karar ölçütü

Bu tek ampul deneyi düşük PF bölgesinde yeni ve tekrarlı bir gözlem noktası sağlayabilir. Ancak tek bir LED yükünün PF değeri sabitse, üç aç/kapa tekrarı üç ayrı PF seviyesi oluşturmaz. Dolayısıyla yalnızca bu deneyden PF-katsayı eğrisi veya genel düzeltme fonksiyonu çıkarılamaz.

PF ile düzeltme ilişkisi araştırmasının ilerleyebilmesi için:
- Birbirinden farklı doğal PF seviyelerinde birden fazla yük/ yük kombinasyonu ölçülmeli.
- Her PF/akım çalışma noktası tekrarlanmalı.
- Akım seviyesi ve PF etkileri birbirinden mümkün olduğunca ayrılmalı.
- Model, katsayıyı oluşturan verilerden ayrı bir doğrulama veri setinde sınanmalı.
- PZEM'in referans niteliği sınırlı tutulmalı; mevcut veriler kesin gerçek akım iddiası olarak sunulmamalı.

Yeterli farklı PF noktası ve bağımsız doğrulama olmadan PF düzeltmesi firmware'e uygulanmayacaktır.

## 8. Önceki deneyle ilişki

2026-11-21 tarihli dimmer gözlemlerinde PF düştükçe PZEM ve SCT/ADS1115 ölçümleri arasındaki ilişkinin değiştiği görüldü. Ancak dimmer akım dalga biçimini ve akım seviyesini birlikte değiştirdiği için PF'nin tek başına etkisi izole edilemedi. Bu yeni deney dimmer kullanmadan, LED sürücüsünün doğal akım biçiminde düşük PF davranışını gözlemlemeyi amaçlar.

Önceki dimmer deneyinin sonuçları bu dosyaya kopyalanmayacak; yalnızca araştırma gerekçesi olarak anılacaktır.

## 9. Sonuç durumu

- Deney protokolü açıldı.
- Henüz yeni ölçüm verisi alınmadı.
- 27.59 katsayısı korunuyor.
- Korelasyon veya düzeltme katsayısı sonucu henüz yok.
- Sonuçlar, kullanıcı tarafından sağlanacak yeni CSV/log üzerinden kararlı pencerelerle analiz edilecek.


## 10. 2026-11-21 ölçüm sonuçları ve gün sonu durumu

**Ölçüm oturumu:** Gün için kapatıldı. Araştırma konusu tamamen sonuçlandırılmış değildir.

### Çevrim 1 – kullanıcı ekran görüntüleri

- SCT/PZEM akım grafiği: yaklaşık 18:36:09–18:36:18.
- PZEM akım: 0.052 A.
- SCT/ADS1115 akım: 0.095 A.
- PZEM PF grafiği: yaklaşık 18:37:25–18:37:34; görünen değer 0.67.
- UT200B+ pens: kullanıcı tarafından 0.044 A olarak bildirildi.
- SCT/PZEM oranı: 0.095 / 0.052 = 1.827.
- SCT'nin PZEM'e göre farkı: +82.7%.
- Pens/PZEM oranı: 0.846 (pens düşük akımda bağımsız doğrulanmış referans değildir).

### Çevrim 2 – kullanıcı ekran görüntüleri

- Akım grafiği: yaklaşık 18:38:10–18:39:35.
- PZEM akım göstergesi: 0.053 A.
- SCT/ADS1115 göstergesi: 0.096 A.
- PZEM gerilimi: 227.0 V.
- PZEM PF grafiği: yaklaşık 18:38:45–18:40:05; görünen değer 0.66.
- SCT/PZEM oranı: 0.096 / 0.053 = 1.811.
- SCT'nin PZEM'e göre farkı: +81.1%.
- Grafikte PZEM akımının bir bölümde sıfıra düştüğü veri boşluğu/geçersiz alan görülüyor; bu bölüm kararlı pencere kabul edilmedi.
- Bu çevrimde pens değeri ayrıca bildirilmedi.

### Değerlendirme ve sınırlamalar

- İki çevrimde PZEM PF 0.66–0.67, PZEM akımı 0.052–0.053 A ve SCT akımı 0.095–0.096 A seviyelerinde birbirine yakın sonuçlar verdi.
- İki çevrimin SCT/PZEM oranları 1.827 ve 1.811; fark yaklaşık %0.9. Bu, bu çalışma noktasında ilk tekrar edilebilirlik işaretidir.
- İki çevrim, protokolde hedeflenen üç çevrimi tamamlamaz. Üçüncü çevrim alınmadı.
- Ekran görüntüleri, tam zaman serisi CSV'sinin yerini tutmaz. Bu nedenle ortalama, standart sapma ve örnek sayısı hesapları yapılmış gibi sunulmamıştır. Görseldeki gösterge değerleri raporlanmıştır.
- Tek doğal PF noktası ve tek yük ile PF-katsayı korelasyonu veya genel düzeltme fonksiyonu çıkarılamaz.
- 27.59 katsayısı ve V1.1 firmware değişmedi.

**Oturum kararı:** 8.5 W LED düşük PF tekrar ölçüm oturumu, iki gözlem çevrimiyle gün sonunda durduruldu. Deneysel bulgu korunacak; üçüncü tekrar ve farklı PF/akım noktaları daha sonraki çalışmada yapılabilir.
