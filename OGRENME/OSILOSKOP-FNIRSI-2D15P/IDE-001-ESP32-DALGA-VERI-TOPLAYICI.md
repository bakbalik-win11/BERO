# IDE-001 – ESP32 Tabanlı Dalga Verisi Toplayıcı

- Tarih: 2026-11-22
- Tür: Bağımsız öğrenme / kişisel elektronik geliştirme fikri
- Durum: Fikir aşaması; donanım seçimi, devre ve yazılım henüz yapılmadı.
- BERO/PREBERO kapsamı: Dışında. Bu çalışma ana BERO ölçüm zincirini değiştirmeyecek.

## 1. İhtiyaç

FNIRSI 2D15P ile dalga biçimini ekranda görüyoruz ve ekran görüntüsü saklayabiliyoruz. Kullanıcının mevcut kullanımında dalganın sayısal örneklerini PC'ye doğrudan aktaran bir veri çıkışı bulunmuyor.

İstenen ek araç, dalgayı yalnızca resim olarak değil, örneklenmiş sayısal veri olarak bilgisayara aktarabilmelidir.

## 2. Hedef

ESP tabanlı düşük frekanslı dalga verisi toplayıcı / eğitim amaçlı basit osiloskop yapmak.

İlk hedef profesyonel osiloskopu, FNIRSI'yi veya kalibre edilmiş laboratuvar cihazını ikame etmek değildir. Öncelik, sinyalin sayısal örneklerini almak, PC'de çizmek ve analiz edebilmektir.

## 3. Planlanan veri akışı

Sinyal → güvenli analog ön uç → ADC → ESP örnek tamponu → USB seri/yerel aktarım → PC Python → grafik ve CSV.

Her veri kaydında mümkünse:
- Örnek sıra numarası.
- Örnek zaman bilgisi veya doğrulanmış sabit örnekleme aralığı.
- Ham ADC kodu.
- Kalibre edilmiş gerilim değeri.
- Örnekleme hızı ve ADC yapılandırması.
- Kullanılan giriş aralığı ve analog kazanç.

## 4. İlk öğrenme hedefleri

Bu cihazı tasarlamadan önce FNIRSI derslerinde şu kavramlar öğrenilecek:
1. Vp, Vpp ve Vavg.
2. RMS ve dalga şekline bağlı RMS hesabı.
3. Periyot ve frekans.
4. Duty cycle ve DC offset.
5. Faz, gürültü ve harmonikler.
6. Örnekleme aralığı, sample rate ve aliasing.
7. Trigger ve tek kayıt penceresi.

## 5. Teknik kararlar henüz verilmedi

Aşağıdakiler deney hedefi belirlendikten sonra seçilecek:
- ESP32 varyantı.
- Dahili ADC veya harici ADC.
- ADC çözünürlüğü, gerçek örnekleme hızı ve giriş aralığı.
- Analog bias/kazanç/koruma/anti-alias filtresi.
- Örnek tamponu ve tetikleme yöntemi.
- USB seri, Wi-Fi veya başka aktarım yolu.
- Python grafik ve CSV şeması.

ESP32 varyantlarının ADC özellikleri aynı kabul edilmeyecek. Yalnızca pazarlama amaçlı teorik örnekleme hızı esas alınmayacak; gerçek örnekleme düzeni ve kararlılığı test edilecek.

## 6. Güvenlik

- Şebeke gerilimi doğrudan ESP32 veya ADC pinlerine bağlanmayacak.
- İzolasyon, koruma ve analog ön uç tasarlanmadan şebeke üzerinde deney yapılmayacak.
- İlk prototip yalnızca FNIRSI'nin düşük gerilimli jeneratörü veya güvenli düşük gerilimli kaynak ile denenecek.
- SCT013 ile çalışma yapılırsa sensör çıkışı, bias ve giriş aralığı önceden doğrulanacak.

## 7. Kabul ölçütü – ilk prototip

1. Bilinen düşük frekanslı bir kare dalga güvenli girişten örneklenir.
2. ESP örnekleri sıra ve zaman bilgisiyle PC'ye aktarır.
3. PC örnekleri grafik olarak gösterir.
4. Aynı örnekler CSV dosyasına kaydedilir.
5. Grafikten periyot/frekans ve Vpp hesaplanır; FNIRSI ekranıyla karşılaştırılır.
6. Başarı gösterilmeden cihazın doğruluğu veya bant genişliği hakkında iddia yazılmaz.

## 8. Durum

Yalnızca fikir ve gereksinim taslağıdır. Devre şeması, kod, BOM, ESP/ADC seçimi veya fiziksel prototip mevcut değildir.
