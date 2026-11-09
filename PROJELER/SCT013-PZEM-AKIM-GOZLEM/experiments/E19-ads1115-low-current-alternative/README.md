# E19 — ADS1115 ile düşük akım ölçüm alternatifi

- **Durum:** PLANLANDI — ADS1115 kartı kullanıcı tarafından sipariş edildi; fiziksel teslimat ve deney henüz yapılmadı.
- **Öncelik:** Düşük akım ölçüm zinciri için sınırlı bütçeli alternatif araştırması.
- **Bütçe:** Kullanıcı bildirimi yaklaşık 250 TL.
- **Zamanlama:** Kullanıcının hedefi hafta sonu ilk denemeleri yapmak; kesin tarih teslimat ve hazırlığa bağlı.
- **Kapsam:** Mevcut BERO ölçüm mimarisini değiştirmeden, SCT-013 30A/1V ile ADS1115 kartını ayrı bir deney düzeneğinde değerlendirmek.

## Amaç

Mevcut SCT + bias orta noktası + ESP32 dahili ADC yoluna alternatif olarak ADS1115 kullanıldığında özellikle 0,5 A altındaki ölçümlerde gürültü, sıfıra yakın okuma davranışı, kararlılık ve PZEM referansına göre sapmanın iyileşip iyileşmediğini araştırmak.

İkincil hedef, ADS1115 kartının giriş yapısı uygunsa harici bias bölücü kullanmadan güvenli ve kararlı ölçüm yapılıp yapılamayacağını sınamaktır. Bias'sız çalışma önceden kabul edilmiş bir özellik değildir; deney sorusudur.

## Deney mimarileri

1. **Mevcut referans yol:** SCT-013 30A/1V → mevcut bias devresi → ESP32 ADC.
2. **Alternatif yol:** Aynı model SCT-013 30A/1V → ADS1115 → ESP32 I²C.
3. **Referans ölçüm:** PZEM-004T V3.0; PZEM mutlak ground truth değil, BERO'nun karşılaştırma/etiketleme referansıdır.

Mümkün olduğunda aynı fiziksel yük ve aynı hat koşulu kullanılacaktır. Aynı anda karşılaştırma yapılırsa iki ayrı CT kullanımı ve sensörler arası fark ayrıca kaydedilir. Tek CT ile ardışık karşılaştırmada yük ve PZEM kararlılığı doğrulanır; bağlantı değişiklikleri enerjisiz koşulda yapılır.

## Temel sınırlar

- Mevcut BERO bias + ESP32 ADC yolu korunur; bu deney onu değiştirmez.
- MCP3208 yeniden gündeme alınmayacak; E19'un konusu değildir.
- 0,5 A altı hedef bölgedir; testler gerektiğinde 0,5 A üstüne taşarak geçiş bölgesini de kapsar.
- ±%4 sapma hedefi bir kabul hedefidir; deney sonucu önceden varsayılmaz.
- ADS1115 PGA ayarı harici yükselteç gibi sensör sinyalini fiziksel olarak büyütmez; ADC ölçüm aralığını/kazanç kademesini değiştirir.
- Diferansiyel okuma ortak-mod gürültüsünü azaltabilir; tüm gürültüyü yok etmez.
- Diferansiyel mod, AIN pinlerinin GND–VDD çalışma sınırlarını kaldırmaz. Giriş ortak-mod seviyesi ve kart üzerindeki direnç/koruma/bias ağı incelenmeden SCT uçları doğrudan bağlanmayacaktır.
- Paylaşılan internetteki burden dirençli akım çıkışlı CT şeması, BERO'daki 1V çıkışlı SCT-013 için doğrudan kopyalanmayacaktır. 1V modelin dahili burden yapısı esas alınır; kart şeması/PCB'si ayrıca incelenir.

## Deney aşamaları

1. Kartın ön/arka yüzünü, pin etiketlerini, besleme gerilimini, I²C adresini ve olası pull-up seviyelerini kaydet.
2. ADS1115 breakout üzerinde girişe bağlı direnç, kondansatör, koruma ve olası bias/common-mode elemanlarını incele.
3. SCT model etiketini doğrula: SCT-013 30A/1V. 100A/1V ile karıştırma.
4. Güvenli besleme ve giriş sınırları doğrulandıktan sonra yüksüz/akımsız taban ölçümü yap.
5. İlk yük denemesinde mevcut tur sayısını koru; ilk karşılaştırmada 5 tur gibi yeni bir değişken ekleme.
6. Düşük yük basamaklarında ADS1115 ve mevcut ESP32 ADC yolunu PZEM ile karşılaştır.
7. Single-ended ve differential yöntemleri yalnızca elektriksel giriş koşulları uygunsa ayrı koşullar olarak dene.
8. PGA ve veri hızı seçeneklerini giriş tepe gerilimi/clipping kontrolüyle değerlendir.
9. 200 ms ve daha uzun RMS pencerelerini karşılaştır; 20 ms tek periyot penceresini varsayılan doğru yöntem kabul etme.
10. Sonuçları aynı deney kimliği altında ham kayıt, özet istatistik ve yorumla sakla.

## Güvenlik

- Şebeke tarafındaki kablo kesme/ekleme veya açık iletkenle çalışma yapılmaz.
- CT yalnızca yalıtılmış tek bir iletkeni çevreler; faz ve nötr aynı CT içinden birlikte geçirilmez.
- Akım çıkışlı CT'lerde primer akım varken sekonder açık bırakılmaz. Bu deneydeki 30A/1V modelin kendi tipine ait üretici bağlantı koşulları ayrıca doğrulanır.
- ADS1115 analog girişleri besleme raylarının dışına çıkarılmaz; 3,3 V ile çalışan ESP32'ye 5 V I²C pull-up uygulanmadığı doğrulanır.
- Giriş topolojisi ve common-mode seviyesi doğrulanmadan doğrudan bağlantı veya enerjili deneme yapılmaz.

## Çıktılar

- Kart fotoğrafları ve bağlantı incelemesi.
- Kullanılan firmware/kod sürümü ve gerçek derleme/çalışma logu.
- Yüksüz taban ve her yük basamağı için örnek sayısı, ortalama, RMS, standart sapma, CV, yüzdelikler, minimum/maksimum, clipping/dropout gözlemi.
- PZEM'e göre sapma ve iki ADC mimarisinin karşılaştırması.
- Bias'sız çalışmanın güvenli/kararlı olup olmadığına dair kanıt ve sınırları.
- Deney sonunda: düşük akım alternatifi olarak kabul, kısmi kabul veya reddetme kararı.

**Sonuç durumu:** Henüz ölçüm yok. Bu kayıt yalnızca sipariş ve deney planını belgeliyor.
