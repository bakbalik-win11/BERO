# BERO PF araştırması – güncel durum ve saha verileri

- Tarih: 2026-11-22
- Kapsam: SCT013 akım ölçümü, ZMPT101B gerilim dalga biçimi, gerçek PF hesabı
- Durum: Araştırma açık; sayısal PF hesaplayan donanım zinciri henüz doğrulanmadı.
- Bu not, bugünkü V1.6 grafiğini, düşük PF deneylerini ve çamaşır makinesi saha kaydını birlikte konumlandırır. Farklı deney amaçları birbirine karıştırılmamalıdır.

## 1. Bugün depoya eklenen V1.6 kalibrasyon/doğrusallık grafiği

Grafik:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/VERI/V1.6/v1.6-kalibrasyon-ve-dogrusallik.jpg`

Açıklama:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/VERI/V1.6/ANALIZ-GRAFIKLERI.md`

Grafik iki panel içerir:
1. K(x) kalibrasyon fonksiyonu; x ekseni logaritmiktir. İdeal PF noktaları PF ≥ 0.90 olarak mavi işaretlenmiş, PF=0.76 ve 20.4 W olan düşük PF noktası ayrı turuncu işaretle gösterilmiştir.
2. 22 kademe PZEM referansı – BERO doğrusal karşılaştırması ve ±%4 hedef bandı. Düşük PF noktası ideal PF ölçüm grubundan ayrı tutulmuştur.

Bu grafik düşük PF noktasının normal yüksek PF kalibrasyon grubuyla aynı şartlarda değerlendirilmemesi gerektiğini görsel olarak hatırlatır. Tek başına PF düzeltme fonksiyonu üretmez; veri kaynağı olan ham CSV esas alınmalıdır.

## 2. Düşük PF deneyleri – mevcut kanıt

### 100 W akkor + dimmer (2026-11-21)

Rapor:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/RAPOR/DIMMER-100W-PF-ETKISI-2026-11-21.md`

Seçilmiş kararlı pencerelerde PZEM PF 1.00'dan 0.61'e inerken SCT/PZEM akım oranı yaklaşık 0.921'den 1.507'ye çıkmıştır. Dimmer hem akım dalga biçimini hem akım seviyesini hem de PF'yi birlikte değiştirdiği için bu sonuç PF'nin tek başına nedensel etkisini kanıtlamaz. Dimmer kalibrasyon taraması kapatılmıştır; bu veriler normal kalibrasyon grubuna karıştırılmayacaktır.

### Tek 8.5 W LED (2026-11-21)

Rapor:
`PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/8_5W-LED-DUSUK-PF-TEKRAR-2026-11-21.md`

İki gözlem çevriminde PZEM PF yaklaşık 0.66–0.67, PZEM akımı 0.052–0.053 A ve SCT/ADS1115 akımı 0.095–0.096 A olarak kaydedildi. İki çevrimde SCT/PZEM oranı yaklaşık 1.81–1.83 düzeyinde birbirine yakındı. Bu, o tek çalışma noktasında tekrar edilebilir bir fark işaretidir; tek PF seviyesi ve tek yük genel PF-katsayı modeli kurmak için yeterli değildir.

## 3. Çamaşır makinesi uzun pamuklu programı – saha gözlemi

Rapor:
`PREBERO/MODUL-3-CAMASIR-MAKINESI/GOREVLER/MOD3-AKM001/RAPOR/MOD3-AKM001-V1.6-UZUN-PAMUKLU-SAHA-TESTI-2026-11-22.md`

- Yaklaşık 78 dakikalık gerçek makine programı kaydedilmiştir.
- PZEM PF kayıtları ısıtma bloğunda yaklaşık 1.00; düşük/orta akım motor/yıkama bölümlerinde yaklaşık 0.53–0.73 bandında gözlenmiştir.
- Isıtma bloğunda SCT–PZEM akım farkı düşük/negatif yöndeyken, ısıtma sonrası düşük akımlı bölümlerde pozitif yönde olmuştur.
- Kullanıcının saha kaydını olumlu değerlendirmesi, V1.6 akım veri yolunun gerçek çamaşır makinesi programı boyunca kayıt üretebilmesi ve makine çalışma motiflerinin kayıtta görünmesi hedefi içindir.
- Bu kayıt ZMPT101B ile gerçek PF ölçümü değildir. PF değerleri PZEM'den alınmıştır; ZMPT101B gerilim dalga biçimi kaydı yoktur.

Bu saha gözlemi PF araştırmasına gerçek cihaz çalışma durumları sağlar. Ancak PF ile akım sapması arasında nedensel ilişki kurmak için aynı anda yük türü, akım seviyesi, dalga şekli, SCT transfer davranışı, kanal zamanlaması ve PZEM algoritması etkileri de ayrıştırılmalıdır.

## 4. Son V1.6-DIAG1 deneyiyle ayrım

2026-11-22 tarihli DIAG1 çalışmasında yaklaşık 8.5 W seviyesindeki küçük yükte SCT013-030'un akım var/yok ayrımı yapabilmesi başarı kriteriydi. Kullanıcı bu sonucu başarılı olarak onayladı.

Bu bir düşük güçte akım algılama başarısıdır; mutlak akım doğruluğu veya PF testi değildir. PF araştırması ayrı kalır ve V1.6 kalibrasyon dosyasını değiştirmez.

## 5. PF araştırmasının asıl teknik hedefi

Sadece PZEM PF değerini okuyup SCT katsayısını PF'ye göre değiştirmek hedef değildir. Hedef, güvenli ve zaman hizalı gerilim/akım dalga biçimlerinden gerçek PF'yi hesaplamaktır:

- P = mean(v_ac[n] × i_ac[n])
- Vrms = sqrt(mean(v_ac[n]²))
- Irms = sqrt(mean(i_ac[n]²))
- S = Vrms × Irms
- True PF = P / S

Bunun için ZMPT101B gerilim örnekleri ile SCT013 akım örnekleri aynı zaman tabanında toplanmalı; analog sensör faz gecikmesi, ADC dönüşüm süresi, kanal zaman farkı ve jitter ayrı karakterize edilmelidir. Yalnızca cos(phi) gerçek PF yerine geçmez.

## 6. Açık teknik kapılar ve sıralama

1. ZMPT101B hazır modülün PCB revizyonu, beslemesi, OUT DC ofseti ve salınımı fiziksel olarak tanımlanmalı.
2. İlk sinyal deneyi yalnızca güvenli, galvanik olarak izole düşük gerilimli AC kaynakla yapılmalı.
3. FNIRSI 2D15P jeneratörünün bağımsız DC offset yeteneği doğrulanmadan +0.9 V offset varmış gibi bağlantı kurulmayacak.
4. Osiloskop ground klipsleri şebeke faz/nötrüne bağlanmayacak; ototransformatör galvanik izolasyon kaynağı sayılmayacak.
5. ADS1115 iki kanalı eşzamanlı örneklemez. Gerçek SPS, RDY zamanlaması, MUX kanal farkı ve jitter ölçülmeden PF için yeterli kabul edilmeyecek.
6. Önce iki kanalda aynı güvenli 50 Hz sinyalin zamanlama/kanal davranışı test edilmeli; sonra her sensör analog zinciri bağımsız karakterize edilmeli.
7. Gerçek donanım verisi, ham CSV, analiz grafiği ve yorum birlikte saklanmalı. Sentetik testler gerçek donanım sonucu gibi sunulmayacak.

## 7. Teknik karar

- V1.6 akım algılama ve kalibrasyon dosyaları bu PF notu nedeniyle değiştirilmez.
- MOD3-AKM001 uzun pamuklu saha görevi kapalı kalır; bu testin olumlu sonucu korunur.
- PF çalışması ZMPT101B + SCT013 zaman hizalı dalga biçimi araştırması olarak ayrı yürütülür.
- Düşük PF gözlemleri araştırma gerekçesidir; henüz PF'ye bağlı düzeltme katsayısı veya algoritma kararı değildir.


## 8. Kullanıcının proje başarısı ve PF araştırması ayrımı – 2026-11-22

Kullanıcı, bugüne kadarki akım ölçüm çalışmasının ana sonucunu şöyle netleştirdi:

1. İlk fazda SCT013 + ADS1115 ölçüm zinciri sağlıklı ve tekrarlanabilir bir çalışma motifi verdi; yüksek PF / PF≈1 koşullarında PZEM referansıyla uyum sağlandı.
2. Tek fonksiyonlu K(x) modeli, PF≈1 ideal çalışma koşullarında geniş akım aralığında PZEM referansına yakın sonuç verdi. Bu, V1.6'nın temel başarısı ve korunacak kalibrasyon kararıdır.
3. Açık kalan ana araştırma alanı düşük PF koşullarında ortaya çıkan akım sapmasıdır. Bu durum henüz PF'nin tek başına nedensel etkisi olarak kanıtlanmış değildir; gerçek PF için ZMPT101B gerilim ve SCT013 akım dalga biçimleri zaman hizalı ölçülmelidir.
4. Yaklaşık 15 W altındaki çok düşük güç/akım bölgesi kullanıcı tarafından mevcut uygulama açısından önemsiz / önceliksiz kabul edilmiştir. Bu alt bölgeyi iyileştirmek için mevcut K(x) modelini yeniden şekillendirmek planlanmamaktadır.

Referans rapordaki sayılar ve sınırlamalar:
- V1.6 genel ortalama bağıl hata -%0.17, medyan -%0.32 (raporda grafik üzerinden aktarılan karşılaştırmalı metrikler).
- 14.6 W noktasında -%10.28; 20.4 W / PF=0.76 noktasında +%12.25.
- 60.5 W noktasında -%4.89 tekil sonuç raporda korunmuştur; sebebi çözülmüş sayılmaz.
- PZEM referans olarak kullanılmıştır, mutlak ground truth değildir.

**Araştırma yönü:** V1.6'nın geniş aralıklı, PF≈1 koşullarındaki başarısını tekrar kalibrasyonla bozmak yerine koru. PF sapmasını ayrı gerçek-PF ölçüm araştırmasında ele al. Yaklaşık 15 W altını bu aşamada kapsam dışı/önceliksiz tut.
