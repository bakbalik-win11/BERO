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
