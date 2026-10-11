# HDF-002 — PZEM Referanslı Ampirik Akım Kalibrasyonu

**Durum:** Açık — yaklaşım tanımlandı; eşleştirilmiş veri toplama ve modelleme bekliyor.  
**Açılış tarihi:** 2026-10-11  
**Ön koşul:** HDF-001 dondurulmuştur ve tarihsel kanıt olarak korunur. Bu yeni hedef HDF-001'i silmez, yeniden başlatmaz veya onun dosyalarını değiştirmez.

## 1. Hedef

Mevcut sensör/ADC ölçüm zincirinin ürettiği veriyi PZEM'in akım ve güç faktörü (PF) okumalarıyla eşleştirerek, sensör verisinden PZEM referansına yaklaşan ampirik bir akım tahmin fonksiyonu öğrenmek. Model önce Python'da kurulup ölçümlerle iyileştirilecek; yalnızca bağımsız doğrulamada kabul ölçütünü karşılarsa ESP32'ye taşınacak ve ESP üzerinde PZEM ile tekrar karşılaştırılacaktır.

Temel model biçimi:

`PZEM_current = f(sensor_data, bias, optionally_other_justified_features)`

İlk modelde mevcut ADC/sensör özellikleri ve bias birlikte değerlendirilir. Bias'ı baştan yok saymak veya sabit kabul etmek yerine ölçüp veri kümesine koy. Ek özellik (ör. RMS, tepe değer, örnek dağılımı, sıcaklık veya kanal kimliği) ancak ölçülebilir gerekçesi ve veri desteği varsa eklenir.

## 2. Kapsam ve sıra

1. **Mevcut kayıtları kullan:** HDF-001 ve GRV-001–GRV-006 içindeki kod, log, CSV, sensör özellikleri, bias bilgisi ve PZEM kayıtlarını incele. Önceki kanıtı yeniden yazma; kullanılabilir veriyi kaynağına atıfla seç. Veri şeması/model için gerekli bir alan yoksa bunu açıkça kaydet.
2. **Eşleşmiş örnek üret:** Aynı ölçüm penceresi ya da açıkça tanımlanmış yakın zaman aralığı için ADC/sensör özellikleri, bias, kanal/sensör kimliği ve PZEM akımı birlikte kaydedilsin. PZEM PF de aynı örneğe etiket olarak kaydedilsin. Yük ve çalışma koşulları, birimler, zaman damgaları, ölçüm penceresi ve sensör/koşullandırma zinciri korunur.
3. **Tekrarlı veri topla:** Farklı yük/akım seviyelerini kapsa; her noktada tekrarlar al ve kararlı/kararsız durumu işaretle. Örnek sayısı ve tekrar planı ilk veri incelendikten sonra belirlenir; ölçüm yapılmadan yeterli veri olduğu iddia edilmez.
4. **Python'da basit modeli kur:** Önce anlaşılır bir global doğrusal/kalibrasyon fonksiyonu gibi basit seçenekleri değerlendir. Hata grafikleri ve artıklar sistematik eğrilik/bölge farkı gösterirse ve her bölge için yeterli bağımsız veri varsa parçalı/bölgesel fonksiyonu değerlendir. Yalnızca eğitim verisini daha iyi uydurması bölgesel model için gerekçe değildir.
5. **PF'yi ayrı değerlendir:** PZEM PF etiketini ayrı hedef değişken olarak incele. Sensör verisinin PF'yi tahmin etmeye yeterli bilgi taşıyıp taşımadığını bağımsız doğrulamada göster; akım modeli başarılı diye PF başarısı varsayılmaz. PF için kullanılabilir bilgi yoksa veya tahmin kararsızsa bunu sonuç olarak kaydet.
6. **Bağımsız doğrula:** Model seçimini eğitim verisinde yap; doğrulama verisini model/özellik seçimi için kullanma. Mümkünse ölçüm oturumlarını veya yük noktalarını bütün halde ayır ki aynı koşulun tekrarları eğitim ve doğrulamaya bölünüp sonucu yapay olarak iyileştirmesin. Eğitimde görülmeyen ölçüm/koşullarda sonuçları raporla.
7. **Kabul kararı ver:** Python tahminlerini PZEM ile eşleştir; nokta bazlı mutlak hata, yüzde hata, MAE/RMSE, sapma eğilimi ve hedef dışındaki örnekleri raporla. Başarı eşiği karşılanmadan ESP'ye aktarım yok.
8. **ESP32'ye aktar ve karşılaştır:** Kabul edilen formülü ve katsayıları açık, kopyalanabilir kodla ESP32 uygulamasına taşı. ESP cihaz adı mevcut tercih uyarınca `esp32d1` kalır; başka ESP adları kullanıcı istemedikçe değiştirilmez. Yeni kod derleme onayı gelene kadar görev kod klasörüne taşınmaz. Kullanıcı derleme başarısını doğruladıktan sonra cihaz çıktısı PZEM ile aynı koşullarda karşılaştırılır ve sonuç ayrı kayıt edilir.

## 3. Kabul ölçütü — öneri, henüz kullanıcı onayı bekliyor

- **Akım:** PZEM referansından en fazla ±%10 sapma hedefi önerilir. Ölçüt, bağımsız doğrulama örneklerinde tanımlı geçerli çalışma aralığında değerlendirilir.
- **Sıfıra yakın akım:** Yüzde hata sıfıra yaklaşırken anlamını kaybeder. Bu nedenle bir mutlak hata eşiği ve/veya sıfır çevresinde deadband ayrıca sayısal olarak belirlenmelidir. Eşik; PZEM çözünürlüğü, sensör gürültüsü ve uygulamanın kabul ettiği en küçük akım dikkate alınarak veri ve kullanıcı kararıyla seçilir. **Bu mutlak eşik şu an belirlenmiş değildir; öneri olarak bekler ve onaylanmadan kesin kabul ölçütü sayılmaz.**
- **Raporlama:** Yalnızca ortalama yüzde hatayı vermek yeterli değildir. Mutlak hata, yüzde hata (uygulanabildiğinde), MAE/RMSE, en kötü sapma, tekrarlanabilirlik ve tolerans içinde kalan örnek oranı birlikte gösterilir.
- **PF:** Akımdan ayrı model ve ayrı doğrulama kararı. PF için başarı eşiği veriler görülmeden uydurulmaz; tanımlanması gerekirse gerekçesiyle önerilir ve kullanıcı kararı bekler.
- **ESP aşaması:** Python'da kabul edilen modelin ESP uygulaması, derleme kanıtı ve cihaz/PZEM karşılaştırması olmadan tamamlandı sayılmaz.

## 4. Veri ve model kayıt kuralları

- Ham log ve kaynak CSV'ler değiştirilmeyecek; temizlenmiş/eşleştirilmiş veri yeni dosyaya yazılacak ve kaynak dosyalara iz bırakacak.
- Her satırda en az kaynak/zaman bilgisi, sensör ve kanal kimliği, ölçüm koşulu, ADC/sensör özellikleri, bias, PZEM akımı ve PZEM PF bulunmalı; eksik değerler sessizce doldurulmamalı.
- Sensör örnek penceresi ile PZEM okumasının zaman farkı kaydedilmeli. Kararlı olmayan yük değişimlerinde eşleşme geçersiz/ayrı sınıf olarak işaretlenmeli.
- Katsayılar sensör modeli, ölçüm kanalı ve analog koşullandırma zincirine bağlıdır. SCT-013, ACS712 5A/20A/50A ve ZMCT/ZMCA için aynı yöntem uygulanabilir; **her sensör/ölçüm zinciri ayrı katsayı veya modelle fit edilir.** Bir model diğer sensöre aktarılmış kabul edilmez.
- ACS712 varyantları ve ZMCT/ZMCA adları/kapsamı envanterdeki gerçek parçayla eşleştirilir; gerilim kazancı, bias, filtreleme, ADC aralığı ve sensör çıkış özelliği belgelenir.
- Kodun yanında aynı sürüm adına sahip .md bulunur: amaç, veri kaynağı, model/özellikler, koşullar, ölçütler, çalıştırma çıktısı, sonuç, sınırlamalar ve sıradaki adım. Kodlar tam ve kopyalanabilir tutulur.
- Derleme isteyen kod, kullanıcı derlemenin başarılı olduğunu doğrulamadan görev klasörüne taşınmaz. Bu hedef açılırken henüz yeni kod veya derleme sonucu iddia edilmemektedir.

## 5. Görev sırası

| Görev | Amaç | Durum |
|---|---|---|
| [GRV-007 — PZEM etiketli ampirik akım kalibrasyonu](../../GOREVLER/GRV-007/RAPOR/README.md) | Mevcut kanıtları envanterle, sensör/ADC + bias ile PZEM akım/PF okumalarını eşleştir, Python kalibrasyonunu ve bağımsız doğrulamayı yürüt | Açık — kapsam tanımlandı; yeni eşleşmiş ölçüm/model sonucu yok |

GRV-007 içindeki basamaklar; veri envanteri ve şema, eşleşmiş ölçüm, model/özellik seçimi, bağımsız doğrulama, ardından kabul edilirse ESP aktarımı ve PZEM karşılaştırmasıdır. Bir basamakta başarısızlık veya veri yetersizliği, yeni bir sıfırlama sebebi değil kayıtlı bir bulgu ve sonraki karar girdisidir.

## 6. HDF-001 ile ilişki

HDF-001 mevcut “Akımı Okuma” hedefidir. Kullanıcının açık talebiyle HDF-001 **FROZEN / DO NOT DELETE** olarak işaretlenmiştir. Dondurulması; HDF-001 klasörünü, bağlı görevleri, kodları, raporları, logları, geçmişi veya Git kayıtlarını silmek/değiştirmek anlamına gelmez. Bu kayıtlar daha önce deneneni ve eldeki kanıtı gösteren tarihsel temel olarak korunur. HDF-002 ayrı hedeftir ve HDF-001 dosyalarını yeniden kullanıp üzerine yazmaz.

## 7. Durum

**Açık — plan ve kabul yaklaşımı kaydedildi.** Eşleşmiş veri üzerinde Python modelinin fit edildiği, ±%10 hedefinin sağlandığı, PF'nin tahmin edilebildiği, kodun derlendiği veya ESP/PZEM karşılaştırmasının yapıldığı iddia edilmemektedir.
