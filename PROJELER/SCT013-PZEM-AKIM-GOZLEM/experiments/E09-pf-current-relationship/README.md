# E09 — PF koşulu ile SCT/PZEM akım karşılaştırması

## Amaç

PZEM-004T'nin yayınladığı PF değerini, PZEM'in CT üzerinden ölçtüğü akım ve SCT'nin aynı yük koşulundaki sinyal/tahminiyle birlikte incelemek. Amaç PF ölçmek veya SCT'den PF tahmin etmek değildir. Amaç, farklı PF koşullarında akım büyüklüğünün ve SCT-PZEM tahmin farkının nasıl davrandığını gözlemlemek; PF bilgisinin modele eklenmesinin yararlı olup olmadığını belirlemektir.

Bu deney, E00A/E00/T005/E01 temel ADC adımlarının ve E08 SCT karakterizasyonunun yerine geçmez. PZEM'in güncelleme/ölçüm penceresi davranışının yorum için gerekli olduğu noktada E03/E04 bulguları da dikkate alınır. Bu nedenle E09 uzun vadeli plan olarak kaydedilmiştir; aktif ilk deney sırasını değiştirmez.

## Temel bakış

PZEM-004T 100 A varyantında gerilim doğrudan ölçüm hattından, akım harici CT üzerinden algılanır. PZEM'in PF yayını bu ölçüm zincirinden raporlanan birleşik bir ölçüm alanıdır; PF, CT'den bağımsız ikinci bir akım sensörü değildir.

Düşük PF'li yükte aynı gerilim ve aktif güç için RMS akımın yükselmesi beklenebilir. Bu, yükün elektriksel karakteristiğinin fiziksel sonucu olabilir; tek başına ölçüm hatası değildir. Bu nedenle düşük PF koşulunda SCT'nin daha yüksek akım genliği göstermesi otomatik olarak hata kabul edilmez.

Bu ilke test sonuçlarına da uygulanır: Yükler arası ham genlik veya akım seviyesi doğrudan başarı/hata sıralaması için kullanılmaz. Her yükün ölçülen gerilimi, aktif gücü, PZEM akımı ve PF'si birlikte değerlendirilir. SCT-PZEM farkı ve ±%4 eğitim verisi içi uyum, aynı yük/ortak kararlı alan bağlamında raporlanır. Düşük PF ile hata arasında ilişki görülürse bu önce gözlemsel ilişki olarak yazılır; PF'nin SCT veya PZEM CT akım ölçümünü bozduğu sonucuna tek başına varılmaz.

## Deney koşulları

Başlangıçta mevcut test yükleri kullanılır:
- 100 W akkor
- 150 W akkor
- 8,5 W LED

Her yükte gerçekleşen gerilim, aktif güç, PZEM akımı ve PZEM PF değeri ölçüm sırasında kaydedilir; nominal lamba gücü veya beklenen PF gerçek ölçüm yerine kullanılmaz. Mümkünse aynı yük koşulu tekrarlı kayıtlarla gözlenir. Yükler arasında gerçek akımın aynı olması beklenmez.

SCT tarafında ilgili karakterizasyon aşamasında belirlenen sensör, kablo turu, örnekleme hızı ve pencere özellikleri korunur. Farklı konfigürasyonlar aynı grup gibi birleştirilmez.

## Kayıt alanları

Her kararlı gözlem/ortak alan için mümkün olduğu ölçüde:
- Yük kimliği/türü ve deney koşulu
- PZEM gerilimi (V), akımı (A), aktif gücü (W), PF ve okuma durumu
- PZEM istek zamanı, yanıt zamanı ve ardışık güncelleme aralığı
- SCT sensör kimliği, kablo turu, örnekleme hızı
- SCT ham kayıt/pencere referansı ve bias çıkarılmış RMS, mutlak Peak, Peak-to-Peak
- Kararlılık/ortak alan kimliği ve zaman sınırları
- Varsa SCT model tahmini, model sürümü ve PZEM akımına göre bağıl hata

PZEM'in PF ve akım alanlarının aynı Modbus okumasında gelmesi, cihaz içindeki tüm ölçümlerin aynı fiziksel zaman penceresinden geldiğini kanıtlamaz. PZEM güncelleme ve ölçüm penceresi belirsizliği kayıtta korunur; SCT örnekleriyle milisaniye hassasiyetinde eşleştirme varsayılmaz.

## İncelenecek sorular

1. Yük türü değiştikçe PZEM'in raporladığı PF ve CT akımı nasıl değişiyor?
2. Aynı aktif güç/gerilim civarında PF azaldığında PZEM RMS akımı yükseliyor mu? Gerçek koşullar ve değerler kaydedilir; ideal formül yalnızca uygun sinüzoidal koşullar için karşılaştırma referansıdır.
3. Aynı kararlı yük koşulunda SCT özellikleri PZEM akımıyla ne kadar tutarlı?
4. SCT-PZEM bağıl hata, PZEM'in raporladığı PF koşuluna göre değişiyor mu?
5. Gözlenen fark yük türü/dalga şekli, SCT/ADC özellikleri veya PZEM'in ölçüm/güncelleme davranışıyla ilişkili olabilir mi?
6. PF bilgisini modele girdi olarak vermek, PF'siz modele kıyasla eğitim verisi içi uyumu ne kadar değiştiriyor?

## Analiz ve raporlama

Sonuç değerlendirme kuralı: Düşük PF koşulunda yüksek RMS akım veya SCT genliği, kendi başına `OUT_OF_RANGE` gerekçesi değildir. `OUT_OF_RANGE` kararı yalnızca ilgili kararlı alanın model tahmini ile o alanın geçerli PZEM akımı arasındaki ±%4 ölçütüne göre verilir. Bunun nedenleri incelenirken yükün V/W/PF/I değerleri, dalga şekli/yük türü, SCT yapılandırması ve PZEM ölçüm/güncelleme davranışı birlikte ele alınır.

- Önce yük bazında PZEM gerilim, aktif güç, akım ve PF değerleri birlikte gösterilir.
- Ardından SCT özellikleri ve SCT-PZEM akım farkı aynı yük/kararlı alan bağlamında incelenir.
- Hata özeti hem yük bazında hem de gözlenen PF aralıkları bazında raporlanır. PF aralıkları veri görüldükten sonra seçilir; önceden keyfi eşik belirlenmez.
- İlk model PF girdisi olmadan eğitilir ve eğitildiği aynı etiketli kararlı veri üzerinde değerlendirilir.
- İstenirse aynı veri ve koşullarda PF girdili ikinci model denenir. İki modelin farkı PF bilgisinin katkısı olarak raporlanır.
- PZEM PF değeriyle hata arasında ilişki görülmesi tek başına PF'nin SCT veya PZEM CT ölçüm hatasına neden olduğunu kanıtlamaz. Yük türü, akım dalga şekli, örnekleme/pencereleme ve PZEM ölçüm davranışı birlikte yorumlanır.

## Durum

**PLANLANDI — henüz uygulanmadı.** Donanım kurulumu, firmware, kayıt, fiziksel ölçüm ve model karşılaştırması yapılmadı. E09 mevcut aktif E00A → E00/T005/E01 → E08 sırasını değiştirmez; uygun aşamada PZEM davranışı ve ortak kararlı alan etiketleme hazırlığıyla ilişkilendirilir.
