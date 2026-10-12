# HDF-002 — Ölçüm Karakterini Öğrenmek ve Gerçek Hayatı Yakalamak

**Durum:** Açık — yöntem ve süreç tanımlandı; yeni deney veya model başarısı iddia edilmiyor.  
**Güncelleme:** 2026-10-12

**Aktif hedef:** Kaliteli SCT ham verisi üretmek; ayrı PZEM akışıyla aynı fiziksel yük durumunu temsil eden kararlı bölgeleri eşleştirmek; çok sayıda farklı akımda doğru etiketli veri oluşturmak; formülü sınav ESP'sinde gerçek referansla değerlendirmek.

> **Süreklilik:** HDF-001/GRV-001 geçmiş çalışmadır. Mevcut kod, log ve deney tecrübesi kullanılacak; aynı testler sırf yeniden yapmak için tekrarlanmayacaktır. Eski dosyalar ve kayıtlar korunur. HDF-002 yeni bir başlangıç veya sıfırlama değildir.

## 1. Ana ilke: hızlı ama kaliteli ham okuma

Öncelik, SCT akım dalgasını hızlı, düzenli ve gerçeği temsil edecek kalitede okumaktır. Kalite; hızlı örnekleme sırasında dalga biçimini bozmamak, yapay sıçramaları gerçek sinyalden ayırmaya elverişli olmak, zamanlama düzenini ve ham örnekleri korumaktır. En yüksek örnek sayısı tek başına başarı ölçütü değildir.

Önce depodaki mevcut HDF-001 kodları, logları ve deney tecrübesi incelenir. Mevcut kanıt yeterliyse tekrar deney yapılmaz. Yalnızca mevcut kayıtlarla cevaplanamayan zorunlu bir soru varsa küçük bir ek doğrulama düşünülür. Kullanıcı gereksiz testlerle boğulmaz.

## 2. Ölçüm mimarisi

### 2.1 SCT-ESP

- Bir ESP32-D, bir SCT-013 ölçüm zincirinden sorumludur.
- Görevi SCT sinyalini mümkün olan en hızlı, kaliteli ve sürdürülebilir biçimde okumak ve ham örnekleri Home Assistant'a (HA) aktarmaktır.
- ESP üzerinde akım/RMS hesabı, korelasyon, etiketleme veya model üretimi yapılmaz.
- Örnekleme döngüsü Wi-Fi/HA aktarım hızına bağlanmaz. Aktarım örnekleme zamanlamasını bozmamalı ve ham örnek kaybettirmemelidir.
- Sırf sıçrama görünümünü azaltmak için gerçek dalgalanmayı veya dalga şeklini silecek filtreleme yapılmaz.

### 2.2 Bias

Bias, akım hesabında ve sonraki F(X) formülünde gerekli bir girdidir. Bu nedenle SCT ham verisiyle doğru ilişki korunarak kaydedilir.

- Hedef düzen, SCT ve ona ait bias bilgisinin aynı ESP/ölçüm zincirinde okunup aynı kayıt akışıyla ilişkilendirilmesidir.
- Bias ölçümü SCT örneklemesini bozuyorsa öncelik SCT dalgasının kaliteli örneklenmesidir; mevcut donanım ve kodun desteklediği en yalın senkron kayıt yöntemi seçilir.
- Her SCT örneğinde bias ADC okumasının mutlaka tekrarlanacağı veya bias'ın değişmez olduğu varsayılmaz. Gerekli zaman ilişkisi korunur; gereksiz test serisi açılmaz.

### 2.3 PZEM-ESP

- PZEM ayrı bir ESP/bağımsız okuma zincirinde çalışır.
- Bu ESP yalnızca PZEM'in kendi ürettiği ölçüm verilerini okur ve HA'ya aktarır.
- PZEM'in kendi ölçüm/güncelleme hızını SCT hızına yetiştirmeye çalışmak hedef değildir.
- PZEM akımı, gerilim (V) ve güç faktörü (PF) birlikte korunur.
- PZEM verisinin yayın anı, içerdiği ölçümün kesin fiziksel zamanı sayılmaz.
- PZEM zinciri SCT örnekleme hızını sınırlamaz.

## 3. HA → masaüstü Python → Mac arşivi

1. SCT-ESP ve PZEM-ESP verileri HA'da birikir.
2. Masaüstündeki Python-A yeni verileri HA'dan alır ve aktarım bütünlüğünü doğrular.
3. Veri Mac'te kalıcı olarak yazılıp yeniden okunarak doğrulanmadan HA'daki kopya silinmez.
4. Doğrulanmış kayıtlar Mac arşivine alınır. Ham kaynak kayıtları değiştirilmez.
5. Sonraki süreçler bu arşiv üzerinde çalışır. Ham veri, bölgeler, etiketli veri, modeller ve doğrulama sonuçları ayrı saklanır.

Mantıksal arşiv bölümleri: raw (değiştirilmemiş ham veri), validated (aktarımı doğrulanmış kayıt), regions (işaretli bölgeler), labeled (eşleştirilmiş/etiketlenmiş veri), models (sürümlü formüller), validation (sınav sonuçları), reports (raporlar). Bu tanım, klasörlerin kurulduğu veya aktarımın çalıştığı anlamına gelmez.

## 4. Python süreçleri

### Python-A — aktarım ve arşivleme
HA'dan yeni veriyi alır; kayıt bütünlüğünü kontrol eder; Mac'e yazar ve yeniden okuyarak doğrular; ancak bundan sonra HA'daki aktarılmış kopyayı siler. Ham kaydı değiştirmez.

### Python-B — eş bölge işaretleme ve etiketleme
- SCT ve PZEM akışlarını önce ayrı ayrı inceler.
- Her akışta kendi karakterine göre kararlı bölgeleri belirler.
- Aynı fiziksel yük durumuna karşılık gelen bölgeleri deney bağlamı ve yük durumu bilgisiyle eşleştirir.
- Amaç zaman damgalarını birebir eşlemek değil, aynı fiziksel durumu temsil eden eş bölgeleri işaretlemektir. Zaman bilgisi yardımcı kanıt olarak korunabilir; tek başına eşleşme kanıtı değildir.
- PZEM akım etiketi, ilgili V ve PF bilgileriyle birlikte SCT bölgesine aktarılır; bias bilgisi SCT verisiyle ilişkilendirilir.
- Yükün açılma/kapanma geçişleri eğitim verisine alınmaz; yalnızca kararlı bölgeler kullanılır.
- Eşleşmesi güvenilir olmayan bölge zorla etiketlenmez.
- Ham veri değiştirilmez; bölgeler ve etiketler ayrı kaydedilir.

### Python-C — birikimli model ve parametre analizi
- Her çalıştırmada önceki etiketli veri kümesini ve yeni doğrulanmış etiketleri okur.
- Birikimli veri kümesini korur; eski etiketler kaybolmaz.
- SCT karakteri, bias, V ve PF parametrelerinin katkısını inceler.
- Önce basit ilişki/katsayıyı, yeterli değilse daha kapsamlı I = F(SCT, Bias, V, PF) adayını araştırır.
- Modeli eğitimde kullanılmamış bağımsız bölgelerle sınar.
- Model sürümü, veri kümesi sürümü, parametreler ve doğrulama sonuçları kaydedilir; yeni model eskisinin üzerine yazılmaz.
- Model üretiminin bir hafta sürmesi sorun değildir; önemli olan veri ve doğrulama kalitesidir.

## 5. Eş bölgeler ve doğru etiket

Eşleştirme zaman eşlemesi değil, eş bölge işaretlemesidir. Aynı fiziksel yük durumu deney bağlamıyla desteklenmelidir. Kararlı bölgelerin sürelerinin eşit olması veya zaman damgalarının çakışması gerekmez.

Kararlı bölge ölçütleri gerçek veriden çıkarılır; kanıtlanmamış tolerans veya pencere değerleri uydurulmaz. SCT örneklerinin birebir aynı olması beklenmez; bölgenin seviyesi ve dalgalanma karakteri birlikte değerlendirilebilir.

Her etiket mümkün olduğunca şu bağlamı korur:
- deney/yük durumu ve bilinen yük koşulu;
- kaynak cihaz/kanal;
- SCT ham veri aralığı ve ona ait bias bilgisi;
- PZEM akım etiketi, V ve PF;
- varsa zaman bilgisi;
- bölge seçimi ve eşleştirme gerekçesi.

Öncelik, çok sayıda farklı akım seviyesinde doğru etiketlenmiş bölgeler oluşturmaktır. Aynı akım seviyesindeki tekrarlar da tutarlılık için saklanır. Nominal yükün her seferinde aynı akımı çektiği varsayılmaz; etiket ölçülen referans değerinden gelir.

## 6. Formül ve kabul hedefi

Araştırılan ilişki:

    I_tahmin = F(SCT_karakteri, Bias, V, PF)

Bu başlangıç hipotezidir; tüm parametrelerin mutlaka gerekli olduğu veya evrensel tek formül bulunacağı önceden kabul edilmez. Aşırı öğrenme başlı başına yasak değildir; pratik hedef, sınavda kabul edilebilir doğruluğa ulaşmaktır. Yine de eğitim verisine ezber uyum ile bağımsız veride başarıyı ayırmak için kullanılmamış bölgelerle doğrulama yapılır.

Pratik kabul hedefi yaklaşık ±%4 bağıl akım sapmasıdır. Sıfıra yakın akımda bağıl hata anlamsızlaşabileceğinden ayrıca mutlak amper hata ölçütü gerekir. PZEM referansının kendi hatası da sonuçların yorumunda korunur.

## 7. Sınav ESP'si ve PZEM korelasyonu

Uygun model sınav ESP'sine yüklenir. Sınav ESP'si SCT ve ilgili bias girdisinden akım tahmini üretir; PZEM ayrı ESP'sinde çalışır. Python, tahmin ile PZEM verisini aynı fiziksel duruma ait kararlı eş bölgeler üzerinden karşılaştırır.

Korelasyonla birlikte bağıl/ mutlak hata, ortalama sapma ve akım aralığına göre hata incelenir. Yüksek korelasyon tek başına doğru akım ölçümü kanıtı değildir; tahmin sürekli fazla veya eksik olabilir.

**Ek fiziksel test otomatik olarak şart değildir.** Önce mevcut ham arşivdeki, model kurulurken kullanılmamış uygun bölgeler değerlendirilir. Arşiv soruyu güvenilir biçimde cevaplayabiliyorsa yeni test yapılmaz. Veri yetersizse yalnızca eksik kanıtı sağlayacak en küçük doğrulama düşünülür.

## 8. Süreç sırası

1. HDF-001'deki mevcut SCT kodu/logları ve tecrübeyi kullan; aynı testleri baştan yapma.
2. SCT için hızlı, kaliteli ve dalgayı temsil eden ham okuma yolunu esas al; bias ilişkisini aynı zincirde koru.
3. PZEM'i ayrı ESP'de kendi hızında tut.
4. Her iki ham akışı HA'da biriktir.
5. Python-A veriyi alıp doğrulasın; Mac kopyası doğrulanınca HA kopyasını silsin.
6. Ham arşivi koru; Python-B kararlı eş bölgeleri fiziksel yük durumuna göre eşleştirip etiketlesin.
7. Python-C birikimli etiketli veriden parametreleri ve en sade işe yarar formülü araştırsın.
8. Model sürümlerini kaydet; uygun modeli sınav ESP'sine yükle.
9. Sınav ESP'si tahmini ile PZEM'i eş bölgelerde karşılaştır; korelasyon ve hata raporu çıkar.
10. Yeni veri geldikçe modeli yeniden üret; ham veriyi ve model geçmişini koru.

## 9. Çalışma sınırları

- HDF-001 deneylerini baştan tekrarlamak varsayılan iş değildir.
- ESP'ler ölçüm okur; etiketleme, korelasyon ve model üretimi masaüstü Python tarafındadır. Sınav ESP'si yüklenen formülü çalıştırıp tahmin üretir.
- PZEM'in ölçüm hızı SCT'ye uydurulmaz.
- Birebir zaman damgası veya paket senkronizasyonu eş bölge eşleştirmenin ön koşulu değildir.
- Ham kaynak dosyaların üzerine yazılmaz; HA kopyası Mac'teki kalıcı kopya doğrulanınca silinir.
- Yeni test, aktarım, model veya başarı gerçekleşmiş gibi gösterilmez.
- Donanım sadeleştirmesi ve paket optimizasyonu, kaliteli ham veri ve eş bölge/model süreci anlaşılmadan öncelik kazanmaz.

## 10. Tamamlanma ölçütleri

HDF-002'nin başarılı sayılması için:
1. SCT dalgasını hızlı ve kaliteli temsil eden mevcut/iyileştirilmiş okuma yöntemi kanıtla tanımlanmalı.
2. SCT ve bias doğru ilişkilendirilmeli; PZEM akışı bağımsız kalmalı.
3. Ham veri HA'dan Mac'e bütünlük doğrulamasıyla aktarılmalı ve arşiv korunmalı.
4. Kararlı eş bölgeler gerekçeli biçimde eşleştirilmeli ve farklı akım seviyelerinde doğru etiketlenmeli.
5. Parametre katkıları incelenmeli ve formül/model sürümlenmeli.
6. Sınav ESP'si tahmini PZEM ile eş bölgelerde karşılaştırılmalı; korelasyon ve hata raporlanmalı.
7. Yaklaşık ±%4 hedefinin hangi koşullarda sağlandığı veya sağlanmadığı gösterilmeli.

**Kanıt sınırı:** Bu belge hedef ve süreç mimarisini kaydeder. Yeni ölçüm, aktarım, model, ESP yüklemesi veya ±%4 başarısı gerçekleştiğini iddia etmez.
