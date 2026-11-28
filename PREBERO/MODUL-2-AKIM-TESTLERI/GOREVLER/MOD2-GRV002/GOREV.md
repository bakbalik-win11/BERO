# MOD2-GRV002 – BERO bağımsız PF ve PF etkili akım ölçümü

- **Açılış tarihi:** 2026-11-24
- **Durum:** AÇIK – deney yaklaşımı 2026-11-25 tarihinde kullanıcıyla sadeleştirildi; fiziksel deney ve katsayı doğrulaması henüz yapılmadı.
- **İlgili donanım:** SCT013 akım ölçüm zinciri; satın alınmış ZMPT101B hazır modül; mevcut ESP32/ADS1115 deney altyapısı; FNIRSI 2D15P osiloskop.
- **Referans:** MOD2-GRV001 V1.6 akım ölçüm modeli. V1.6 dosyaları değiştirilmez.

## 1. Amaç – BERO için pratik ölçüm

BERO'nun hedefi ticari/laboratuvar sınıfı bir multimetre üretmek değildir. Hedef, evin her hattına ayrı PZEM takmayı gerektirmeyen, BERO'ya özel bir ölçüm yolu geliştirmektir:

- SCT013 tabanlı akım ölçümünün yük değişimlerine hızlı tepki vermesi.
- Akım değerinin deneylerde PZEM referansına mümkün olduğunca yakın olması.
- Gerçek PF'nin BERO'nun kendi gerilim ve akım ölçüm zinciriyle hesaplanabilmesi.
- Çalışma sırasında PZEM'e ihtiyaç duymadan akım ve PF bilgisinin üretilebilmesi.

PZEM yalnızca deney, karşılaştırma ve eğitim/referans verisi toplama aşamasında kullanılacaktır. Nihai BERO hattında PZEM bulunması zorunlu değildir. PZEM'in ölçüm/yayın gecikmesi ve ortalama davranışı da göz önünde tutulacak; BERO'nun hızlı tepki hedefi PZEM'in yayın hızına bağlanmayacaktır.

Bu hedef hobi/prototip ölçeğindedir. Sonuçlar BERO'nun belirlenen sensör, yük ve çalışma aralığı için değerlendirilir; evrensel ölçüm doğruluğu iddia edilmez.

## 2. Korunacak mevcut temel

- MOD2-GRV001 V1.6 referans akım yolu ve EXP/K(x) modeli korunacaktır.
- Mevcut model: `K(x)=26.89+5.39×exp(-x/0.882)`; baz ölçek K=27.59.
- PF araştırması V1.6 YAML'ına veya mevcut katsayısına doğrudan ek yapılması anlamına gelmez.
- Yeni bir düzeltme bulunursa ayrı deney sonucu ve ayrı model/sürüm olarak tutulur.
- PZEM karşılaştırma referansıdır; mutlak ground truth kabul edilmez.

## 2.1. Deney düzeneği ve cihaz kimlikleri

- **Ölçüm düzeneği:** MOD2-BENCH-01 — ESP32-D2 + ADS1115 No.10 + SCT013 30 A / 1 V. Bu, eski imha edilmiş üç kanallı fiziksel Modül 2 değildir; aktif masaüstü deney aracıdır.
- **PZEM referans yayımlayıcı:** PZEM-REF-WROOM-01 — kullanıcının mevcut olduğunu bildirdiği ESP32-WROOM + PZEM-004T V3.0. Arşiv ESPHome adı `bero-modul3-wroom`; UART TX GPIO19 / RX GPIO18, 9600 baud, 8N1 ve 5 saniyelik yayın. Eski firmware adı fiziksel BERO Modül 3 kimliği olarak kullanılmaz.
- **Yeni PF algılayıcı adayı:** ZMPT101B, MOD2-BENCH-01'e eklenecek; sensör kartı, pinler, sinyal seviyesi ve güvenlik uygunluğu fiziksel olarak kontrol edilmeden bağlanmış sayılmaz.
- **Mevcut referans kod:** MOD2-GRV001 V1.6 EXP/K(x) korunur; PF deneyi için kopya/ayrı model kullanılır. PZEM yayımlayıcıyı veya mevcut V1.6 YAML'i değiştirmek bu görevin parçası değildir.

## 3. Pratik deney sırası — kullanıcı kararı, 2026-11-28

Kullanıcı, çamaşır makinesi saha kaydının sonraki değerlendirmesinde akım sapmasının PF koşullarıyla ilişkisini teyit etti. Bu, PF'yi yeni akım denklemine katma gerekçesidir. Proje hobi/prototip ölçeğinde olduğundan önce kolay ve pratik deney yapılır; akademik veya ayrıntılı ölçüm yaklaşımı ilk kapı değildir.

**Öncelikli kısa yol:** ZMPT101B kartını güvenli biçimde tanı; sabit bir lamba yükünde ZMPT trimpotuyla BERO gerilim okumasını PZEM'e yaklaştır. ZMPT kartındaki trimpot gerilim kanalının genlik/ölçeğini ayarlar; PF koşulunu değiştiren eleman kullanıcının dimmeridir. Aynı lamba+dimmer ayarlarında PZEM V/I/P/PF ile SCT013 + ZMPT101B'den BERO'nun PF ve akımını oku. Bu deney noktalarından, EXP/K(x) bulunurken izlenen pratik grafik yaklaşımına benzer şekilde, PF'yi içeren yeni f(X) akım düzeltme adayı ara. PZEM bu aşamada referans etikettir; mutlak ground truth değildir.

Kısa yol yeterli sonuç vermezse ADS1115 zamanlaması, örnek eşleme, PHASE_CORRECTION ve daha ayrıntılı sinyal/faz incelemesi adım adım devreye alınır. Bunlar yedek araştırma araçlarıdır; ilk deneyi geciktiren ön koşullar değildir. Yeni katsayı V1.6'ya eklenmez, MOD2-GRV002'de ayrı tutulur.

1. **Kartı tanıma ve güvenlik ön testi:** ZMPT101B hazır kartının PCB revizyonu, pinleri, beslemesi, op-amp bilgisi ve çıkış/bias aralığı kaydedilir. Şebeke uygulamasından önce giriş devresi, izolasyon/mesafeler, terminal koruması ve kapalı test düzeneği gözden geçirilir. İlk elektriksel ön test gerekiyorsa güvenli, izole düşük gerilimli AC ile yapılır.
2. **Sabit yükte gerilim ayarı:** Güvenlik koşulları sağlanınca sabit lamba yükü altında ZMPT trimpotuyla BERO gerilim okuması PZEM'e yaklaştırılır. Bu yalnızca gerilim genlik/ölçek ayarıdır; PF veya faz telafisi değildir.
3. **Kolay PF ve akım noktaları:** Aynı lamba ve dimmer düzeninde birkaç sabit dimmer ayarı seçilir. Her kararlı noktada PZEM V/I/P/PF ile BERO gerilim, SCT akım, BERO PF ve V1.6 akımı kaydedilir. Kullanıcının verdiği dimmer: https://www.amazon.com.tr/dp/B09RNBDXK2. Dimmer akım seviyesini ve dalga şeklini de değiştirebilir; bu sınır kayda yazılır.
4. **Deneysel denklem adayı:** V1.6 EXP/K(x) geliştirme yaklaşımına benzer şekilde deney grafiğinden PF girdili basit f(X) akım düzeltme adayı aranır. Biçim ve katsayı önceden belirlenmez; mevcut V1.6 değiştirilmez. Sonuç PZEM'e göre tek noktada eşleşmekle doğrulanmış sayılmaz.
5. **Basit kontrol tekrarı:** Seçilen noktaların en az birini yeniden ölç; mümkünse denklem çıkarırken kullanılmamış bir dimmer ayarı/yükle kısa kontrol yap. İlk kolay deneyden anlamlı ve tekrarlanabilir sonuç çıkmazsa sonraki adıma geç.
6. **Yedek ayrıntılı inceleme:** Gerekirse ADS1115 gerçek zamanlama/kanal aralığı, örnek eşleme, PHASE_CORRECTION ve daha ayrıntılı faz/sinyal yaklaşımını incele. PHASE_CORRECTION gerilim trimpot ayarından ayrı tutulur. Bu çalışmalar ilk kısa deneyin ön koşulu değildir.
7. **Saha sentezi:** PF'li akım düzeltme adayı laboratuvar/masaüstü verisinden sonra çamaşır makinesi kaydıyla, ardından uygun olduğunda bulaşık makinesiyle karşılaştırılır. V1.6 korunur; yeni model ve sonucu MOD2-GRV002 altında tutulur.

Bu sıra, önceki geniş ADS1115 karakterizasyon önerisini tamamen silmez; o öneriler isteğe bağlı teknik başvurudur. Pratik ilk denemede zamanlama yetersizliği görülürse ölçüm mimarisi yeniden değerlendirilir.

## 4. Deney adımları ve ilerleme

| Adım | İş | Durum |
|---|---|---|
| 0 | MOD2-GRV001 V1.6'yı koruma ve yeni işi MOD2-GRV002 altında yürütme | TAMAMLANDI |
| 0A | FNIRSI 2D15P DMM ile SCT013-030 çıkışında 0,05 A karşılığı yaklaşık 1,67 mV RMS değerini doğrudan gözlemle | PLANLANDI — 2026-11-28; fiziksel sonuç yok |
| 0B | 2D15P DDS + pasif bölücü ile düşük seviyeli 50 Hz AC uyarı oluşturup UT61E+ ölçüm tepkisini ön incele | PLANLANDI — DMM/DDS eşzamanlılığı doğrulanacak |
| 0C | Mevcut FNIRSI SG-002 ile UT61E+ DC gerilim ve 4–20 mA döngü ölçümünü kontrol et | PLANLANDI — SG-002 DC kaynak; AC sinüs kaynağı değil |
| 1 | ZMPT101B kartı ve kapalı/güvenli test düzeni ön kontrolü | BEKLİYOR |
| 2 | Sabit lamba yükünde ZMPT trimpotuyla gerilim okumasını PZEM'e yaklaştırma | BEKLİYOR |
| 3 | Sabit lamba + dimmer ayarlarında PZEM ve BERO PF/akım noktalarını kaydetme | BEKLİYOR |
| 4 | Deney verisinden PF girdili pratik f(X) akım düzeltme adayı çıkarma | BEKLİYOR |
| 5 | Kısa tekrar/kullanılmamış ayar ile kontrol | BEKLİYOR |
| 6 | Gerekirse ayrıntılı ADC zamanlama/faz/PHASE_CORRECTION incelemesi | KOŞULLU – kısa yol yetersiz kalırsa |
| 7 | Adayı çamaşır ve uygun olduğunda bulaşık makinesi kayıtlarıyla sentezleme | BEKLİYOR |

Sıra, fiziksel güvenlik ve deney bulgularına göre güncellenebilir. Her adımda ham veri, ayar, yük, zaman penceresi ve yorum saklanır. Başarısız/sonuçsuz denemeler de korunur.


## 5. Veri toplama ve karşılaştırma kuralları

- PZEM ve EXP ölçümleri aynı zaman penceresiyle eşleştirilmelidir. Farklı yayın periyotları varsa pencere bazında özetleme yöntemi açıkça kaydedilir.
- Yalnızca en yakın zaman damgasını seçmek, zaman farkı büyükse geçerli eşleşme sayılmaz.
- Ham veri değiştirilmez; temizlenmiş/eşleştirilmiş veri ayrı çıktı olarak tutulur.
- Her kayıtta yük türü/çalışma modu ve kararlı pencere notu tutulur.
- PF ile akım seviyesi ve yük türü birlikte değişebileceğinden, korelasyon tek başına PF'nin nedensel etkisi sayılmaz.
- Mümkün olduğunda benzer akım seviyelerinde farklı PF koşulları ve benzer PF koşullarında farklı yükler karşılaştırılır.
- Eğitimde kullanılan veri ile doğrulama verisi ayrılır.
- PZEM verisi BERO'yu PZEM'e göre kalibre eder; PZEM'in kendi algoritmasından bağımsız mutlak doğruluğu kanıtlamaz.

Önerilen CSV alanları:
`timestamp,window_id,load_state,dimmer_setting,V_pzem,I_pzem,P_pzem,PF_pzem,zmpt_raw,zmpt_v_rms,sct_raw,sct_i_rms,P_bero,PF_bero,phase_correction,I_v1_6,error_A,ratio,sample_timing,notes`

Kullanılmayan/elde olmayan alanlar uydurulmaz; boş bırakılır.

## 6. İlk mevcut veri kaynakları

- Çamaşır makinesi uzun pamuklu saha kaydı ve raporu: `PREBERO/MODUL-3-CAMASIR-MAKINESI/GOREVLER/MOD3-AKM001/RAPOR/MOD3-AKM001-V1.6-UZUN-PAMUKLU-SAHA-TESTI-2026-11-22.md`
- PF saha gözlemleri, 100 W dimmer ve 8.5 W LED kayıtlarının değerlendirmesi: `DONANIM/ZMPT101B/PF-ARASTIRMA-GUNCEL-DURUM-2026-11-22.md`
- V1.6 kalibrasyon referansı: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.6/RAPOR/V1.6-TAM-ARALIK-TEK-FONKSIYON-DOGRULAMA-2026-11-22.md`

Bu kaynaklar ilk grafik için adaydır; ham CSV dosyalarının erişilebilirliği ayrıca kontrol edilir. Raporlarda özetlenen değerler ham veri yerine geçirilmez.

## 7. Donanım ve güvenlik sınırları

- ZMPT101B hazır modülün PCB revizyonu, pin sırası, besleme ve OUT davranışı fiziksel kart üzerinde doğrulanmadan kesin kabul edilmez.
- İlk analog testler yalnızca güvenli, galvanik olarak izole düşük gerilimli AC kaynakla yapılır.
- FNIRSI 2D15P'nin pil ile çalışması, girişlerinin galvanik olarak izole olduğunu kanıtlamaz. Osiloskop ground klipsleri şebeke fazına/nötrüne bağlanmaz. Ototransformatör izolasyon sağlamaz.
- Şebeke bağlantısı ve ölçüm güvenliği ayrı tasarım/uygulama kapısıdır; açık breadboard üzerinde şebeke deneyi yapılmaz.
- ADS1115 kanalları eşzamanlı örneklemez. Mevcut ADC'nin PF için yeterli olduğu varsayılmaz; gerçek zamanlama ve hata deneyle görülür. Bu görev başında yeni ADC satın alma kararı yoktur.
- PZEM'in ortalama/yayın gecikmesi, BERO'nun tepki performansının ölçüsü olarak kullanılmaz. Tepki süresi BERO'nun kendi ham/işlenmiş örnekleriyle ayrıca ölçülür.

## 8. Başarı değerlendirmesi

Başarı tek bir mükemmel doğruluk sayısına indirgenmez. Raporlarda ayrı ayrı değerlendirilir:
1. Akım değeri: PZEM referansına göre hata ve tekrarlanabilirlik.
2. Tepki: yük değişimine BERO'nun yanıt süresi ve pencere gecikmesi.
3. PF: BERO PF değerinin PZEM karşılaştırması ve farklı yüklerde tutarlılığı.
4. Bağımsız çalışma: normal ölçüm sırasında PZEM olmadan akım ve PF üretilebilmesi.
5. Sınırlar: hangi yük/akım/PF aralıklarında güvenilir olduğu ve nerede belirsiz kaldığı.

Bu plan için henüz fiziksel test, PF katsayısı veya firmware doğrulaması yapılmamıştır. İlk iş ZMPT101B kartını tanımak ve güvenli ön kontrolü tamamlamaktır.


## 9. Önceki pratik SCT–ZMPT faz deneyi tartışması – 2026-11-25

Bu bölüm, 2026-11-25 tarihli beyin fırtınasında netleşen deney yaklaşımını kaydeder. Henüz fiziksel deney yapılmamış, katsayı bulunmamış ve yazılım doğrulanmamıştır.

### Hedef

SCT013 akım ölçümü ile ZMPT101B gerilim ölçümünü birlikte kullanarak PF hesabını iyileştirmek; bunu ilk aşamada osiloskopta dalga inceleme ve karmaşık faz çıkarma döngülerine girmeden, basit bir hesaplama formülü ve ayarlanabilir düzeltme parametresiyle denemek.

- PZEM'in PF değeri deney sırasında referans/karşılaştırma değeri olacaktır.
- SCT ve ZMPT sinyallerinden elde edilen BERO PF çıktısı PZEM PF ile karşılaştırılacaktır.
- Yazılımda başlangıçta tek bir `PHASE_CORRECTION` parametresi denenebilir.
- Tek parametre farklı yüklerde yeterli olmazsa, ölçüm sonuçlarına göre bu parametreyi kullanan basit bir `PHASE_CORRECTION(PF/çalışma noktası)` fonksiyonu değerlendirilebilir.
- Fonksiyonun biçimi ve katsayıları önceden belirlenmeyecek; deneyle bulunacak.
- Kullanıcıya yayınlanacak çıktı düzeltme katsayısı değil, BERO'nun hesapladığı PF değeridir. Düzeltme parametresi hesaplamanın içinde kalır.
- Bu yaklaşımın farklı yüklerde işe yaradığı henüz kanıtlanmış değildir. PZEM'e tek bir noktada eşitlemek başarı sayılmaz; başka yüklerde de kontrol gerekir.

### Basit deney düzeni ve yükler

1. **İlk küçük deney:** Yarın mevcut donanımla yapılabilecek, bağlantıları ve sinyal seviyeleri önceden kontrol edilmiş kısa bir deneme. İlk hedef sistemi çalıştırmak ve PZEM ile aynı koşuldaki PF değerlerini karşılaştırmaktır.
2. **Dirençli yük:** PF≈1 başlangıç kontrolü ve ölçüm zincirinin temel referansı.
3. **Potansiyometreli trimmer/dimmer yükü:** Ayar değiştikçe PZEM PF ve BERO PF davranışını karşılaştırma. PF'nin sabit olduğu varsayılmayacak; her ayarda PZEM değeri kaydedilecek.
4. **8.5 W LED:** Düşük akım sınırını ayrıca gözlemleme. Önceki deneyde SCT akımı düşük bölgede güvenilirlik sorunu gösterdiğinden bu yük faz kalibrasyonunun ana referansı yapılmayacak.
5. **Çamaşır makinesi kaydı:** Farklı çalışma evreleri ve değişken PF koşullarında sonradan doğrulama kaynağı. Değişken yük olduğu için ilk katsayı ayarının tek kaynağı olmayacak.

### Uygulama yaklaşımı

- İlk adımda hazır/temel SCT–ZMPT PF hesaplama yaklaşımı kullanılacak; gereksiz algoritma geliştirme yapılmayacak.
- Gerilim ve akım ölçek katsayıları ile faz düzeltme parametresi birbirinden ayrı tutulacak. Böylece genlik kalibrasyonu faz düzeltmesiyle karıştırılmayacak.
- PZEM PF referansı, aynı yük ve mümkün olduğunca aynı zaman penceresindeki BERO PF çıktısıyla karşılaştırılacak.
- Önce sabit `PHASE_CORRECTION` değeri elle değiştirilerek sonuç gözlenecek. Gerekirse basit bir fonksiyona geçilecek.
- Osiloskop ilk küçük deney için zorunlu araç değildir. Gerekli görülürse yalnızca güvenli ve uygunluğu doğrulanmış düşük gerilimli sinyallerin incelenmesinde yardımcı araç olarak kullanılabilir.
- 8.5 W LED'deki düşük SCT akım performansı, faz düzeltme başarısızlığıyla karıştırılmayacak.
- PZEM'in yayın/ortalama gecikmesi dikkate alınacak; karşılaştırma eş zamanlı olmayan tekil örnekler üzerinden yapılmayacak.

### Güvenlik ve doğrulama sınırı

Kullanıcı nihai sensör kalibrasyonunu 220–230 V AC çalışma koşuluna göre planlamak istemektedir. Ancak fotoğraftaki hazır modülün giriş dirençleri, PCB yalıtım mesafeleri ve şebeke tarafı güvenliği henüz fiziksel olarak doğrulanmamıştır. Bu nedenle 220–230 V AC bağlantısına yalnızca kart ve kapalı/korumalı test düzeneği uygunluğu önceden gözden geçirildikten sonra geçilir. Modülün OUT tarafının düşük gerilimli olması tek başına bütün kartın/ölçüm düzeninin güvenli olduğunu kanıtlamaz. Osiloskop şebeke girişine bağlanmayacaktır; osiloskopun izolasyonu varsayılmayacaktır.

RN130424 12 V / 2 VA transformatör mevcut deney donanımıdır; ancak primeri 230 V AC ile beslendiğinden primer tarafı şebeke güvenliği gerektirir. Bu transformatörün varlığı tek başına güvenli test düzeneği oluşturmaz.

### Başarı ölçütü

- BERO PF çıktısının PZEM PF referansına yakınlaşması.
- Aynı ayarların tekrarlandığında benzer sonuç vermesi.
- Bulunan düzeltmenin yalnızca tek yükte değil, farklı yüklerde de makul davranması.
- Düzeltme parametresinin kullanıcıya PF çıktısı olarak sunulmaması; son çıktının BERO PF olması.

Bu bölüm bir deney kararıdır; deney sonucu, doğrulanmış katsayı, güvenli şebeke bağlantısı veya tamamlanmış PF algoritması anlamına gelmez.


## 10. Kullanıcı kararı — pratik ilk yöntem, 2026-11-27

- İlk hedef, ZMPT101B hazır kartının gerilim okumasını PZEM'e yaklaştırmaktır; fiziksel trimpot çıkış genliğini ayarlamak için kullanılacaktır.
- Ardından SCT013 ve ZMPT101B ile faz/PF ilişkisi pratik biçimde denenir. PZEM aynı pencere için karşılaştırma referansıdır.
- Sabit ampul ve dimmer ayarları farklı yük koşulları sağlar. Her ayarda gerçek PZEM PF ölçülür; nominal PF varsayılmaz.
- Ölçülen gerilim genliği ayarı, PHASE_CORRECTION ve PF'ye bağlı akım düzeltmesi ayrı tutulur.
- BERO PF'si akım düzeltme adayına girdi olabilir. Yeni aday MOD2-GRV002 kapsamında değerlendirilir; V1.6 korunur.
- Beş yapay zekâ yanıtının önceki teknik sentezi ve kapsamlı ADS1115 test önerileri başvuru notudur; mevcut pratik ilk yöntemin zorunlu ön koşulu değildir.
- Bu bir deney planı kararıdır. Donanım testi, katsayı, güvenli şebeke bağlantısı veya başarılı PF sonucu değildir.


## 11. Kullanıcı yönlendirmesi — önce kolay deney, 2026-11-28

- Çamaşır makinesi saha kaydının sonraki değerlendirmesinde PF koşullarının akım sapmasıyla ilişkisi teyit edilmiştir; ayrıntılı sayı ve grafikler kaynak raporlardadır.
- Bu bir hobi projesidir; önce kolay, pratik ve sabit yükle tekrarlanabilir deneme yapılır.
- Sabit lamba yükünde ZMPT101B trimpotu PZEM gerilim okumasına göre ayarlanır. PF farklı noktaları için lamba dimmeri değiştirilir; trimpot ve dimmer görevleri karıştırılmaz.
- Yeni ZMPT101B + SCT013 zincirinin PF okuması ve PZEM referanslı akım farkı birlikte kaydedilir; EXP/K(x) yöntemine benzer biçimde PF girdili yeni bir f(X) adayına bakılır.
- Kolay deney işe yaramaz veya tekrarlanmazsa daha ayrıntılı faz/zamanlama araştırması açılır. Akademik ayrıntı başlangıç şartı değildir.
- Bu öncelik önceki ayrıntılı pratik faz planını silmez; onu yedek/başvuru yaklaşımı olarak konumlandırır.


## 12. Sensör çıkışını bağımsız DMM ile tanıma — 2026-11-28

Kullanıcı, ADC/ESP32/ADS1115/MCP3208 katmanlarına geçmeden önce sensörün kendi elektriksel tepkisini doğrudan görmek istedi. Bu nedenle PF/ZMPT deneylerinden önce kısa bir ön karakterizasyon deneyi planlandı.

- **Cihaz:** FNIRSI 2D15P'nin DMM modu.
- **Sensör:** SCT013-030, 30 A / 1 V.
- **Deney hedefi:** 0,05 A RMS primer akımına karşılık gelen yaklaşık 1,67 mV RMS AC çıkışın DMM ekranında ayırt edilebilir ve tekrarlanabilir olup olmadığını görmek.
- **Teorik oran:** 1 V / 30 A = 33,333 mV/A; 0,05 A × 33,333 mV/A ≈ 1,667 mV RMS.
- **Öncelik:** Bu deney, ZMPT101B kartı ve PF deneyine geçmeden önce yapılacak ilk kısa kontrol olarak belirlendi.
- **Sınır:** 2D15P üretici teknik bilgisinde en düşük ACV aralığı 1,9999 V ve gösterge 19.999 count olarak listelenir; teorik ekran basamağı 0,1 mV'dir. Düşük mV bölgesindeki AC doğruluğu ve minimum güvenilir giriş seviyesi açıkça verilmediğinden yalnızca ekran çözünürlüğünden ölçüm doğruluğu sonucu çıkarılmaz.
- **Bağlantı:** Sensörün 1 V gerilim çıkışı DMM'nin VΩ-COM girişleriyle ölçülür. DMM akım girişi kullanılmaz; bias, harici burden, amplifikatör ve ADC eklenmez.
- **Güvenlik:** Kelepçe tek yalıtılmış primer iletkeni kavrar. DMM yalnızca sensör çıkışına bağlanır. Şebeke yükü kullanılacaksa kapalı/korumalı düzen gerekir; osiloskop girişleri ve ground klipsleri şebekeye bağlanmaz.
- **Kanıt durumu:** Deney henüz yapılmadı; ölçüm, log, ekran görüntüsü veya sonuç yoktur.

Ayrıntılı deney planı: [FNIRSI 2D15P DMM – SCT013-030 – 0,05 A testi](DENEYLER/FNIRSI-2D15P-DMM-SCT013-030-005A-2026-11-28.md).

Bu ön test sensör çıkışının gözlenebilirliğini değerlendirir; SCT013-030'un 0,05 A seviyesindeki mutlak doğruluğunu kanıtlamaz.


## 14. Analog ölçü aletleri için mevcut kaynaklarla test planı — 2026-11-28

Kullanıcı envanterinde FNIRSI SG-002 ve FNIRSI 2D15P bulunduğu doğrulandı. Yeni bir küçük DDS modülü satın almadan önce mevcut cihazların yetenekleri kullanılacak:

1. **Gerçek sensör ön testi:** SCT013-030 30 A / 1 V çıkışı, FNIRSI 2D15P DMM modunda doğrudan ölçülecek. 0,05 A karşılığı 1,67 mV RMS hedefi görünürlük/kararlılık testidir; sensör doğruluğu iddiası değildir.
2. **Düşük AC seviyede DMM karakterizasyonu:** 2D15P DDS 50 Hz sinüs çıkışının 0,1 Vpp minimum seviyesi, 20 kΩ seri / 1 kΩ şönt direnç ile nominal 1/21 oranında zayıflatılabilir. 100 mVpp kaynak yaklaşık 1,68 mV RMS; 0,2/0,5/1,0 Vpp kaynak ayarları yaklaşık 3,37/8,42/16,84 mV RMS üretir. Bu yardımcı test gerçek CT davranışını simüle etmez ve kalibrasyon standardı değildir.
3. **Eşzamanlılık sınırı:** 2D15P'nin DDS ve DMM işlevlerinin aynı anda çalıştığı belgelenmemiştir. Aynı cihazın kendi DDS çıkışını DMM ile aynı anda ölçtüğü varsayılmaz. İki cihazın aynı sinyalle eşzamanlı karşılaştırılması gerekiyorsa mevcut SANEC jeneratörünün modeli/çıkışı önce tanımlanır.
4. **DC testleri:** FNIRSI SG-002, 0–10 V sınıfı DC gerilim ve 4–20 mA dahil DC akım döngüsü için kullanılır. Kılavuzdaki 50HZ ibaresi ekran gösterim modudur; AC sinüs üretim modu değildir.
5. **Alternatif jeneratörler:** FYE050, AD9833 ve XR2206 şimdilik satın alma listesine alınmaz. Mevcut kaynaklarla deney yapılamadığı veya otomatik frekans taraması gerektiği kanıtlanırsa yeniden değerlendirilir.

Ayrıntılı kayıtlar:
- [2D15P DMM / SCT013-030 / DDS yardımcı deneyi](DENEYLER/FNIRSI-2D15P-DMM-SCT013-030-005A-2026-11-28.md)
- [SG-002 DC analog gerilim ve akım döngüsü testi](DENEYLER/FNIRSI-SG002-DC-ANALOG-SIMULATOR-TESTI-2026-11-28.md)

Bu ekler plan kaydıdır; henüz fiziksel test, ölçüm logu veya doğrulanmış sonuç yoktur.


## 15. Ölçüm altyapısı çalışma kuralı — 2026-11-28

MOD2-GRV002 deneyleri ve devam eden BERO analog sensör çalışmaları, [Ölçüm Altyapısı ve Sensör Doğrulama Stratejisi V1.0](../../../OLCUM-ALTYAPISI/OLCUM-STRATEJISI-V1.0.md) sırasına göre yürütülür:

**Sensörün ham çıkışı → bağımsız DMM → osiloskopla dalga biçimi → analog ön uç → ADC ham kodu → yazılım hesabı → kalibrasyon.**

- Sensörün kendi çıkışı bağımsız olarak anlaşılmadan ADC/ESP32 ölçümü sensörün gerçek davranışı diye yorumlanmaz.
- Mevcut 2D15P, SG-002, SANEC sinyal jeneratörü ve lojik analizör öncelikle kullanılacaktır.
- Tek planlanan yeni cihaz UT61E+'tır. Başka DDS/jeneratör satın alımı mevcut altyapının somut bir test gereksinimini karşılayamadığı gösterilmeden açılmaz.
- Kaynak ayarı, bağımsız ölçüm, dalga biçimi, ADC ham kodu ve PZEM karşılaştırması ayrı kanıt sınıflarıdır.
- Bu kural MOD2-GRV001 V1.6 dosyalarını değiştirmez; yeni deneyler kendi dosyalarında tutulur.


## 16. PF hesabında SCT akım genlik hatasının etkisi ve pratik deney sırası — 2026-11-28

Bu bölüm, kullanıcıyla yapılan görüşmede netleşen hesaplama yaklaşımını ve deney kararını kaydeder. **Henüz fiziksel deney yapılmış, PF sonucu alınmış veya yeni düzeltme fonksiyonu doğrulanmış değildir.**

### 16.1 Temel ayrım: gerilim ölçeği, akım ölçeği ve PF

- **ZMPT101B trimpotu:** Gerilim kanalının çıkış genliğini/ölçeğini ayarlamak içindir. BERO'nun hesapladığı gerilim RMS değeri, aynı çalışma koşulunda PZEM gerilim RMS değerine yaklaştırılır. Trimpot PF ayarı yapmaz ve tek başına faz hatasını düzeltmez.
- **Dimmer:** 100 W akkor lamba deneyinde farklı yük/dalga biçimi ve PF çalışma noktalarını oluşturmak için kullanılır. Örneğin hedef PF≈0,50 noktası dimmerle seçilir; o noktadaki gerçek PF PZEM'den okunur ve ayar sabitlenir. PF değeri ZMPT trimpotuyla ayarlanmaz.
- **SCT013 akım ölçeği:** Kullanıcının teyidine göre PF≈1 koşulundaki akım kalibrasyonu daha önce başarılmıştır. Bu mevcut kalibrasyon ve MOD2-GRV001 V1.6 referansı korunur; PF<1 deneyine geçerken SCT katsayısı baştan ayarlanmaz.

### 16.2 Akım genlik hatası PF hesabını zorunlu olarak bozmaz

BERO PF hesabı yalnızca (V_{RMS}) ve (I_{RMS}) değerlerinden çıkarılamaz. Aynı zaman penceresine ait gerilim ve akım örnekleriyle gerçek güç de hesaplanmalıdır:

- (V_{RMS}=\sqrt{\operatorname{mean}(v[n]^2)})
- (I_{RMS}=\sqrt{\operatorname{mean}(i[n]^2)})
- (P=\operatorname{mean}(v[n]\,i[n]))
- (PF=P/(V_{RMS}\,I_{RMS})) (yük yönü/işaret kuralı tutarlı uygulanır; tüketim PF'si raporlanırken gerekiyorsa mutlak değer kullanılır).

Bu örnek-çarpım yöntemi sinüs varsayımıyla yalnızca \(\cos(\varphi)\) hesaplamaktan farklıdır; dalga biçimi bozulmasının etkisini de toplam gerçek PF içinde tutar.

**Ölçek hatasının sade matematiksel sonucu:** SCT örnekleri gerçek akım dalgasının yalnızca sabit ve doğrusal bir katsayıyla ölçeklenmiş hali ise, yani (i_{ölçüm}[n]=k_i\,i_{gerçek}[n]), aynı örneklerden hesaplanan aktif güç de (k_i) ile, RMS akım da |(k_i)| ile ölçeklenir. Pozitif bir sabit kazanç hatasında bu katsayı PF oranında sadeleşir. Dolayısıyla SCT'nin amper cinsinden ölçeği PZEM ile henüz eşleşmiyor olsa bile, dalga biçimi ve zaman ilişkisi korunuyorsa PF hesaplanabilir.

Bu sonuç **her SCT hatası için geçerli değildir**. Aşağıdaki durumlarda hata PF'ye de taşınabilir ve genlik katsayısı sadeleşmesi yeterli olmaz:

- SCT/analog ön ucun faz veya frekans cevabı nedeniyle dalga biçimini zamana göre kaydırması,
- dalga biçiminin bozulması, kırpılması, doyum veya doğrusal olmayan davranış,
- gürültü ve ofsetin yeterince giderilmemesi,
- gerilim ve akım örneklerinin aynı zaman penceresine ait olmaması,
- ADC kanallarının ardışık örneklenmesinden kaynaklanan ve hesaba katılmayan kanal zaman farkı.

Bu nedenle “SCT akımı fazla gösteriyor” gözlemi tek başına PF'nin de yanlış olduğunu kanıtlamaz; aynı şekilde PF'nin doğru çıkacağı da deney öncesinde garanti edilemez.

### 16.3 MOD2-GRV002 için güncel pratik sıra

1. Güvenlik ve kart bağlantı ön kontrolünü tamamla.
2. Sabit besleme koşulunda ZMPT101B gerilim RMS değerini trimpotla PZEM gerilim RMS değerine yaklaştır; bu ayarın gerilim ölçeği ayarı olduğunu kaydet.
3. 100 W akkor lamba ve dimmerle hedef çalışma noktası oluştur. Örneğin PZEM PF≈0,50 gösterdiğinde dimmer konumunu sabitle. PZEM'in ölçtüğü PF'yi kaydet; nominal değer varsayma.
4. Daha önce PF≈1 için elde edilen SCT akım kalibrasyon katsayısını değiştirmeden, SCT ve ZMPT kanallarından aynı pencereye ait ham örnekleri al.
5. Ofsetleri gidererek (V_{RMS}), (I_{RMS}), (P=\operatorname{mean}(v[n]i[n])) ve BERO PF değerini hesapla. Kanal örnek zaman farkı bilinmiyorsa sonucu doğrulanmış PF olarak etiketleme.
6. BERO PF'yi aynı kararlı pencerenin PZEM PF değeriyle karşılaştır. Aynı kayıtta BERO akımını PZEM akımıyla da karşılaştır.
7. Birden fazla PF ve yük noktasında veri biriktir. PF'ye bağlı akım düzeltme fonksiyonu ancak tekrarlanabilir hata eğilimi görülürse ve ayrı verilerle doğrulanırsa aday kabul edilir.

### 16.4 Korunacak kararlar ve kanıt durumu

- PF hesabı için SCT'nin amper ölçeğini önce PZEM'e eşitlemek zorunlu ön koşul değildir; sabit genlik kazancı PF oranında sadeleşebilir.
- Gerilim/akım RMS değerlerini bilmek tek başına PF hesabına yetmez; örnek bazında eşzamanlı gerçek güç hesabı gerekir.
- Gerilim trimpot ayarı, SCT akım kalibrasyonu, PF hesabı ve PF'ye bağlı akım düzeltme modeli birbirinden ayrı tutulur.
- MOD2-GRV001 V1.6 ve PF≈1 akım kalibrasyonu korunur. Yeni PF/akım düzeltme adayı yalnız MOD2-GRV002 altında geliştirilir.
- İlk aşamada ayrıntılı osiloskop faz açısı analizi zorunlu değildir. Pratik deney ve PZEM karşılaştırması sonuç vermezse faz/zamanlama incelemesi yedek yöntem olarak açılır.
- **Kanıt durumu:** Bu bölüm matematiksel gerekçe ve deney planıdır. ZMPT101B trimpot ayarı, PF≈0,50 deneyi, ADC zaman eşlemesi ve PF hesabı henüz fiziksel olarak doğrulanmamıştır.


## 17. PF düzeltmesinde çok değişkenli deney matrisi ve zaman penceresi — 2026-11-28

Bu bölüm, kullanıcının önerdiği üç ayrımı deney protokolüne dönüştürür. Amaç PF ile SCT/PZEM sapması arasındaki ilişkiyi tek değişkenliymiş gibi yorumlamamak; akım seviyesi, dalga biçimi, yük türü ve örnekleme zamanlamasını ayrı izlemektir. **Bu kayıt deney tasarımıdır; yeni ölçüm veya doğrulanmış fonksiyon sonucu değildir.**

### 17.1 Aynı PF, farklı fiziksel akım dalgaları

Aynı gerçek PF değerine farklı yükler ve dalga biçimleriyle ulaşılabilir. Örnekler:
- Faz kesmeli dimmerle çalışan akkor lamba: kesilmiş/darbeli akım ve artmış harmonik içerik ihtimali.
- LED sürücüsü: doğrultucu/kondansatör giriş yapısına bağlı darbe karakterli akım ihtimali.
- Motor/indüktif yük: farklı faz, akım seviyesi ve geçiş davranışı.

Bu yüzden tek bir PF sütunu SCT hata davranışını açıklamak için yeterli değildir. Her çalışma noktasında mümkün olduğunca şu bağımsız değişkenler kaydedilir:

| Değişken | Kayıt / amaç |
|---|---|
| Yük etiketi ve yük tipi | 100 W akkor, dimmerli akkor, LED sürücü, motor vb.; fiziksel yük sınıfını ayırır |
| Dimmer/ayar konumu | Deney tekrarında aynı koşulu kurmak için; mümkünse işaretli konum veya yüzde |
| PZEM PF | Kararlı çalışma noktasının karşılaştırma etiketi |
| PZEM V_RMS, I_RMS, P | Gerilim, akım ve aktif güç bağlamı |
| BERO V_RMS, I_RMS | Kendi ölçüm zincirinin büyüklükleri |
| Akım tepe değeri I_peak | Ham örnekleme yeterliyse tepe davranışı |
| Crest factor | I_peak / I_RMS; tepe karakterini akım seviyesinden bağımsız karşılaştırmaya yardımcı olur |
| Dalga biçimi notu | Osiloskop/gözlem; sinüzoidal, faz kesilmiş, darbe karakterli, kırpılmış vb. |
| Örnekleme ve kalibrasyon kimliği | ADC kimliği, MUX, SPS, PGA, YAML, akım modeli/katsayısı, kayıt sürümü |

Harmonik/THD sütunu yalnızca örnekleme bant genişliği ve analog zincir bu ölçümü destekliyorsa doldurulur. Yeterli örnekleme olmadan harmonik veya crest factor kesin ölçülmüş gibi raporlanmaz.

**Mevcut kayıtların söylediği ve söylemediği:**
- 2026-11-21 tarihli 100 W dimmer denemesinde PZEM PF 1,00'dan 0,61'e inerken SCT/PZEM akım oranı 0,921'den 1,507'ye çıktı. Ancak PZEM akımı da yaklaşık 0,463 A'dan 0,338 A'ya değişti; ham dalga biçimi/harmonik kaydı bulunmadığından PF, akım seviyesi ve dimmer dalga biçimi etkileri tek başına ayrıştırılamaz. Ayrıntı: PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/RAPOR/DIMMER-100W-PF-ETKISI-2026-11-21.md.
- 8,5 W LED tekrarında iki çevrimde PZEM PF 0,66–0,67, PZEM akımı 0,052–0,053 A, SCT akımı 0,095–0,096 A görüldü; SCT/PZEM oranı 1,811–1,827 idi. Bu düşük akım + LED sürücüsü + düşük PF koşulunun birlikte bulunduğu bir gözlemdir; tek başına nüve doğrusal olmaması veya PF nedenselliği kanıtı değildir. Ayrıntı: PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/DENEYLER/8_5W-LED-DUSUK-PF-TEKRAR-2026-11-21.md.
- Bu iki deney birbirinin yerine geçmez; ayrı yük/akım/dalga biçimi koşulları olarak tutulur.

**Katsayı adlandırma notu:** K=27.59, ADS1115 No.10 / SCT013 30A-1V için eski V1.1 zincirinde kullanılan baz ölçek katsayısıdır; tek başına “güncel alt bant katsayısı” diye adlandırılmaz. Aktif V1.6 referans modeli K(x)=26.89+5.39e^(-x/0.882) biçimindedir. PF araştırması V1.6 modelini değiştirmez; yeni model ayrı görev/sürümde tutulur.

### 17.2 PZEM kararlılığı ve BERO örneklerinin zaman penceresi

- Yük veya dimmer ayarı değiştirildiğinde geçiş/settling bölgesi analiz penceresine alınmaz.
- PZEM-REF-WROOM-01 arşiv yapılandırmasında değerleri 5 saniyede bir yayınlar. Bu nedenle kararlılık kararı tek PZEM örneğine göre verilmez; ardışık yayınlarda V/I/P/PF değerlerinin seçilen tolerans içinde plato oluşturması beklenir. Tolerans ve minimum kararlı örnek sayısı her test protokolünde önceden belirtilir.
- Kararlı pencere belirlendikten sonra PZEM ve BERO verileri aynı yerel başlangıç/bitiş zamanlarıyla eşleştirilir. PZEM örnekleri seyrek olduğundan PZEM serisine sahte ara örnek üretmek için interpolasyon yapılmaz; PZEM pencere özeti/örnek sayısı karşılaştırma etiketi olarak saklanır.
- BERO'nun ham gerilim ve akım örnekleri gerçekten zaman damgalıysa, ADC kanalları arasındaki ölçülmüş dönüşüm farkı Δt kaydedilir. Gerekli olduğunda iki ADC serisi ortak zaman ızgarasına enterpole edilebilir. Bu yalnızca bilinen küçük zaman kaymasını azaltır; kayıp harmonikleri, yetersiz örnek sayısını veya aliasing'i geri getirmez.
- Her pencere için başlangıç/bitiş, PZEM örnek sayısı, BERO örnek sayısı, ortalama/medyan, standart sapma ve dışlanan geçişlerin nedeni kaydedilir. Yetersiz PZEM örneği olan pencereler düşük güvenli olarak işaretlenir.

### 17.3 ADS1115 ham örneklemenin mevcut sınırı

Mevcut MOD2-GRV001 YAML kayıtlarında ADS1115 No.10 için 860 SPS, ct_clamp için 200 ms sample_duration ve 1 s update_interval kullanılmıştır. Bu yapı Home Assistant'a RMS akım sonuçları yayımlar; mevcut CSV/HA akım varlıkları tek başına gerilim ve akımın ham dalga örneklerini vermez. Gerçek v[n] ve i[n] kaydı için ayrıca ham örnek toplama/yazma yolu gerekir.

ADS1115 tek ADC ve paylaşılan giriş MUX'u kullanır; kanal dönüşümleri eşzamanlı değildir. İki analog kanal sırayla okunursa 860 SPS toplam dönüşüm hızının teorik olarak kanal başına yaklaşık 430 SPS'ye bölünmesi beklenir; gerçek hız ve zaman farkı donanım/yazılım üzerinden ölçülerek kaydedilmelidir. 430 örnek/s, 50 Hz'de kanal başına yaklaşık 8,6 örnek/periyot eder. Bu hız temel dalga hakkında ilk gözlem sağlayabilir; faz kesmeli akımdaki yüksek harmonikleri ve tepe değerini güvenilir biçimde karakterize etmek için yeterli kabul edilmez.

Bu nedenle:
- Önce gerçek ham örnek zaman damgalarını ve efektif örnek hızını ölç.
- Gerilim ve akım kanallarının MUX sırasını ve Δt'yi kaydet.
- Enterpolasyonu yalnızca ölçülmüş zaman farkı düzeltmesi olarak kullan; örnekleme yetersizliğinin çözümü sayma.
- Eğer amaç gerçek PF'yi bozulmuş dalga biçiminde hesaplamaksa, ADC'nin bant genişliği/örnekleme yeterliliği ayrıca geçiş kapısıdır. ADS1115 verisi bu koşulu sağlayamazsa daha hızlı eşzamanlı/çok kanallı bir örnekleme yolu ayrı değerlendirilir.
- Mevcut ct_clamp RMS sensörleriyle elde edilen değerlerden akım sapması korelasyonu kurulabilir; fakat bunlar tek başına P=mean(v[n]i[n]) gerçek güç hesabının veya PF_BERO ham dalga hesabının yerine geçmez.

### 17.4 Ampirik düzeltmenin geçerlilik alanı

- Yeni ampirik fonksiyon yalnızca ölçülmüş ve etiketlenmiş yük tipi, akım aralığı, PF ve dalga biçimi alanında geçerli aday sayılır.
- PF, akım seviyesi ve yük tipi etkileri mümkün olduğunca çapraz noktalarla ayrılır: benzer I_RMS seviyesinde farklı PF; benzer PF seviyesinde farklı I_RMS; aynı PF/akım civarında farklı yük tipi.
- Fonksiyonun kurulduğu verilerden ayrı doğrulama kayıtları tutulur.
- Motor kalkışı, çamaşır makinesi evre geçişi veya yeni bir sürücü/dalga biçimi, modelin otomatik olarak kapsadığı kabul edilmez; ayrı doğrulama gerektirir.
- PZEM karşılaştırma/etiketleme aracıdır; mutlak ground truth olarak sunulmaz.

### 17.5 Her deney noktasında tutulacak kayıt paketi

Her sabit çalışma noktası için tek kimlikli veri bloğu oluştur:
- Deney ID, tarih, yük etiketi/türü, dimmer konumu ve kararlı pencere başlangıç/bitişi.
- PZEM V/I/P/PF örnekleri, yayın zamanları, örnek sayısı ve pencere istatistikleri.
- BERO ham ADS1115 gerilim ve akım dizileri, her örneğin zaman damgası, MUX, PGA, SPS ve ADC kimliği.
- Kullanılan YAML/firmware sürümü, SCT kimliği ve kalibrasyon modeli/katsayısı.
- BERO V_RMS, I_RMS, aktif güç, PF, I_peak ve crest factor; örnekleme yetersizse ilgili alan “hesaplanmadı/güvenilmez” olarak işaretlenir.
- PZEM-BERO farkı, SCT/PZEM oranı, veri kalitesi ve teknik yorum.
- Ham CSV/LOG dosyası ile analiz raporu ayrı saklanır; yalnızca özet tablo ham verinin yerine geçmez.

**Kanıt durumu:** Önceki 100 W dimmer ve 8,5 W LED verileri bu çok değişkenli tasarımın gerekçesidir. Ham gerilim/akım dalga dizileri, zaman eşlemesi ve ADS1115'in PF için yeterliliği henüz doğrulanmadı.


### 17.6 Yarınki kayıt için pratik etiketler ve ölçüm penceresi alanları — 2026-11-28

Her log satırı veya kararlı pencere bloğu bir durum etiketi taşımalıdır:

- `settling`: Yük/dimmer ayarı yeni değişti; PZEM'in yeni yayını ve kararlı plato koşulu henüz oluşmadı. Analiz ve fonksiyon eğitimi için kullanılmaz.
- `steady`: Önceden belirlenmiş kararlılık şartı sağlandı; bu satır/blok kararlı pencere analizine alınabilir.
- Gerekirse `invalid`: veri boşluğu, geçersiz/NaN okuma, bağlantı kesilmesi veya pencere bozulması var; hesaplamaya alınmaz.

PZEM-REF-WROOM-01'in 5 saniyelik değeri yayınlama aralığı, PZEM'in kendi iç ölçüm/ortalama algoritmasının tam süresiyle aynı şey olarak kabul edilmez. Ayar değişiminden sonra en az bir tam 5 saniyelik yayın aralığı geçmesini bekle; ardından ardışık PZEM yayınlarının önceden belirlenmiş toleranslarda kararlı kaldığını görmeden pencereyi `steady` olarak işaretleme. Kararlılık toleransı ve gereken ardışık yayın sayısı deney başlamadan tanımlanır. Geçişe ait tüm satırlar `settling` olarak saklanır; silinmez, fakat kararlı analizden dışlanır.

#### 200 ms örnekleme penceresi ile 1 s yayın aralığını ayır

Mevcut ESPHome `ct_clamp` davranışında:
- `sample_duration: 200ms`: Her `ct_clamp` ölçüm güncellemesinde örneklerin toplandığı tek ölçüm penceresinin süresidir.
- `update_interval: 1s`: Yeni ölçüm/örnekleme çevriminin başlatılma aralığıdır.
- Bu iki değer, saniyede beş adet 200 ms pencerenin biriktirildiği anlamına gelmez. Mevcut yapı için her güncellemenin kendi 200 ms örnekleme fazı ve ayrı 1 s güncelleme ritmi vardır.
- ESPHome `ct_clamp` debug çıktısı, 200 ms fazında alınan gerçek kaynak örnek sayısını (`num_samples`) ve buradan hesaplanan efektif SPS değerini yazabilir. Bu sayı gerçek logdan alınmalı; ADC ayarındaki 860 SPS değeri doğrudan gerçek örnek sayısı kabul edilmemelidir.

Her ölçüm bloğunda şu zaman alanlarını ayrı tut:
- `load_change_timestamp`: yük/dimmer değişiminin zamanı.
- `pzem_publish_timestamp`: PZEM değerinin WROOM/HA tarafında yayınlandığı zaman.
- `measurement_window_start` ve `measurement_window_end`: BERO'nun gerçek örnekleme penceresinin başlangıç/bitişi; zaman damgası alınamıyorsa `estimated` diye işaretle.
- `measurement_window_duration_ms`: gerçekleşen ölçüm penceresi süresi.
- `ct_clamp_sample_duration_ms`: yapılandırılmış değer (mevcut referans YAML'de 200 ms).
- `ct_clamp_update_interval_ms`: yapılandırılmış değer (mevcut referans YAML'de 1000 ms).
- `source_sample_count`: 200 ms sırasında gerçekten okunan ADC kaynak örnek sayısı; debug/ham logdan alınamıyorsa boş bırak.
- `effective_sample_rate_sps`: gerçek örnek sayısı / gerçek pencere süresi ile hesaplanır.
- `window_status`: `settling`, `steady` veya `invalid`.

**Uygulama sınırı:** Mevcut Home Assistant `ct_clamp` RMS varlığı tek başına örnek başına zaman damgası, kaynak örnek sayısı veya ham dalga örneklerini taşımaz. Bu alanları doldurmak için debug log veya ayrı zaman damgalı ham veri kaydı gerekir. Alanları elde etmeden tahmini değer yazılmaz. Deneyin kısa veri kaydı için bu metadata ayrı bir CSV/JSON yan dosyasında tutulabilir ve özet satırındaki `window_id` ile birleştirilebilir.
