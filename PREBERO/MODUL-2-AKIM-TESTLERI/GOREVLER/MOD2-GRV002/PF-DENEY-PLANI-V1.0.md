# MOD2-GRV002 — BERO PF Deney Planı V1.0

- **Tarih:** 2026-11-28
- **Durum:** PLAN KABUL EDİLDİ — fiziksel deney ve PF algoritması doğrulaması bekliyor.
- **Amaç:** ZMPT101B gerilim bilgisi ve SCT013 akım ölçümünü kullanarak BERO'nun PF davranışını incelemek; SCT/PZEM akım farkının PF, akım seviyesi ve gerçek yük dalga biçimiyle ilişkisini kontrollü deneylerle ayırmak.
- **Bu belgenin rolü:** MOD2-GRV002 için tek ve güncel uygulama planıdır. GOREV.md içindeki önceki görüşme/teknik karar bölümleri tarihsel gerekçe olarak korunur. Uygulama sırası konusunda bu V1.0 planı esas alınır.

---

## 1. Deneyin temel yaklaşımı

BERO'nun amacı her hatta PZEM kullanmak değil; kendi sensörleriyle akım ve PF bilgisini üretebilmektir. PZEM yalnızca geliştirme ve karşılaştırma döneminde referans/etiket sağlar.

Çalışma prensibi:

1. Önce ZMPT101B'nin gerilim ölçeğini PZEM gerilimine yaklaştır.
2. PF≈1 koşulunda daha önce elde edilmiş SCT akım kalibrasyonunu koru; bu araştırma için yeniden ayarlama yapma.
3. Dimmerli yapay yüklerle sınırlı kalma; gerçek hayattaki PF'li yükleri kullan.
4. PZEM'in kararlı çalışma noktasını bekle; BERO verisini aynı kararlı dönemden al.
5. PF, akım büyüklüğü, tepe davranışı ve yük tipini ayrı değişkenler olarak kaydet.
6. Önce basit ve tekrarlanabilir ilişkileri ara. Osiloskopta ayrıntılı faz/harmonik incelemesini yalnızca sonuçları açıklamak gerektiğinde kullan.

**Ana hedef:** Her yük için tek bir katsayı uydurmak değil; BERO'nun hangi yük, akım, PF ve dalga biçimi aralığında ne kadar sapma yaptığını anlamak ve yalnızca kanıtın desteklediği kapsamda düzeltme geliştirmek.

## 2. Korunacak mevcut kararlar

- **SCT PF≈1 kalibrasyonu:** Kullanıcının daha önce başarılı olarak teyit ettiği mevcut akım kalibrasyonu korunur. PF<1 deneylerinde SCT katsayısı baştan ayarlanmaz.
- **MOD2-GRV001 V1.6:** Aktif referans model ve YAML değiştirilmez:  
  `K(x)=26.89+5.39×exp(-x/0.882)`
- **K=27.59 notu:** Bu değer eski V1.1 / ADS1115 No.10 zincirindeki baz ölçek katsayısıdır. Güncel V1.6 modelinin yerine geçen genel bir “alt bant katsayısı” olarak adlandırılmaz.
- **ZMPT101B trimpotu:** Yalnızca BERO gerilim kanalının genlik/ölçek ayarını PZEM gerilim RMS değerine yaklaştırır. PF ayarı veya faz telafisi değildir.
- **Dimmer:** PF çalışma noktasını değiştirmek için kullanılır. Örneğin PF≈0.50 hedeflenebilir; gerçek değer PZEM'den okunur. PF değeri dimmer konumundan tahmin edilmez.
- **PZEM:** Karşılaştırma ve veri etiketleme aracıdır; mutlak kalibrasyon standardı/ground truth kabul edilmez.
- **Yeni düzeltme:** Bulunursa MOD2-GRV002 içinde ayrı model/sürüm olarak tutulur; V1.6'ya doğrudan eklenmez.
- **Yeni cihaz:** UT61E+ sipariş edildiği bildirildi; fiziksel teslim ve kontrol yapılana kadar mevcut cihaz sayılmaz. Şu aşamada başka DDS/jeneratör satın alımı planlanmaz.

## 3. Donanım ve görev dağılımı

| Donanım | Deneydeki görevi | Sınır |
|---|---|---|
| ZMPT101B hazır modül | Şebeke gerilimini düşük gerilimli temsilî sinyale dönüştürmek; BERO gerilim RMS ölçümü | PCB, pin, besleme, çıkış/bias ve şebeke tarafı güvenliği fiziksel olarak doğrulanmadan bağlanmaz |
| SCT013-030 30 A / 1 V | Tek yalıtılmış iletkenden akım sinyali | PF≈1 kalibrasyonu korunur; akım genlik hatası ile PF hesabı ayrı değerlendirilir |
| MOD2-BENCH-01: ESP32-D2 + ADS1115 No.10 | Mevcut akım ölçüm zinciri ve ilk karşılaştırmalar | Mevcut ct_clamp RMS yayını ham dalga örneği değildir; MUX kanalları eşzamanlı değildir |
| PZEM-REF-WROOM-01 + PZEM-004T V3.0 | V/I/P/PF karşılaştırma etiketi | Arşiv yapılandırmasında WROOM/HA yayını 5 saniye aralıklıdır; PZEM'in iç ölçüm/ortalama penceresi bu yayın aralığından çıkarılamaz |
| FNIRSI 2D15P | DMM ile sensör çıkışı ön gözlemi; gerektiğinde düşük gerilimli dalga biçimi gözlemi | Osiloskopun bataryalı olması girişlerin şebekeden izole olduğunu kanıtlamaz; şebekeye prob/ground bağlanmaz |
| UNI-T UT61E+ | Sipariş tesliminden sonra bağımsız düşük AC mV / DC ölçümleri | Üretici spesifikasyonlu DMM'dir; kalibrasyon sertifikalı standart değildir |

## 4. Aşama 0 — Güvenlik ve ölçüm hazırlığı

1. ZMPT101B kartının PCB revizyonu, pin sırası, besleme gerilimi, OUT davranışı ve varsa op-amp/filtre yapısı kaydedilir.
2. Kartın şebeke tarafındaki dirençleri, izolasyon mesafeleri, terminal koruması ve kapalı muhafaza/test düzeneği incelenir.
3. İlk analog ön test gerekiyorsa güvenli, galvanik olarak izole düşük gerilimli AC kaynak kullanılır. İzolasyon ve güvenlik uygunluğu doğrulanmadan şebeke bağlantısı yapılmaz.
4. Şebeke deneyi açık breadboard veya açıkta erişilebilir klemenslerle yapılmaz.
5. SCT kelepçesi yalnızca tek yalıtılmış primer iletkeni kavrar; faz ve nötr birlikte kelepçelenmez.
6. DMM yalnızca sensörün düşük gerilimli çıkışına uygun giriş/kademe ile bağlanır. SCT013-030 30 A / 1 V gerilim çıkışlı sensörde harici burden eklenmez.
7. Osiloskop şebeke fazına/nötrüne bağlanmaz. Bataryalı çalışma galvanik izolasyon kanıtı değildir.

### Kısa SCT ham çıkış ön kontrolü

Ölçüm altyapısı stratejisinin parçası olarak, SCT013-030 çıkışının DMM ile doğrudan gözlenmesi kısa bir ön kontrol olarak yapılabilir. 0.05 A karşılığı teorik yaklaşık 1.67 mV RMS değerin görülmesi yalnızca görünürlük/kararlılık kontrolüdür; düşük akım doğruluğu kanıtı değildir. Akım bağımsız doğrulanamıyorsa yük noktası “yaklaşık” olarak etiketlenir. Bu kısa ön kontrol PF deneyini gereksiz yere geciktiren uzun bir karakterizasyon çalışmasına dönüştürülmez.

## 5. Aşama 1 — ZMPT101B gerilim ölçeğini PZEM'e eşitleme

1. Önce güvenli bağlantı ve kart ön kontrolü tamamlanır.
2. Sabit ve bilinen bir yükle (100 W akkor lamba gibi, dimmersiz dirençli başlangıç koşulu) ölçüm yapılır.
3. PZEM'in aynı kararlı çalışma dönemindeki gerilim RMS değeri referans alınır.
4. BERO'nun ZMPT101B çıkışından hesapladığı gerilim RMS değeri gözlenir.
5. ZMPT101B trimpotu yalnızca gerilim genliğini/ölçeğini ayarlamak için kullanılır; BERO gerilim RMS değeri PZEM'e yaklaştırılır.
6. Ayar ve çalışma koşulu kaydedilir, ardından PF yük deneyleri boyunca trimpota dokunulmaz. Besleme gerilimi veya fiziksel bağlantı değişirse yeniden kontrol gerekir.

**Bu aşamanın çıktısı:** Sabitlenmiş ZMPT101B gerilim ölçek ayarı. Bu işlem faz telafisi veya PF kalibrasyonu sayılmaz.

## 6. Aşama 2 — Korunan PF≈1 akım referansı

- SCT013'ün daha önce PF≈1 dirençli yük koşulunda elde edilmiş akım kalibrasyonu başlangıç referansı olarak korunur.
- Bu deney planında yeni PF noktaları için K yeniden ayarlanmaz.
- Dirençli yük/PF≈1 noktası gerekiyorsa yalnızca karşılaştırma kontrolü olarak tekrar kaydedilir; V1.6 değişikliği yapılmaz.
- Düşük akımlı LED noktalarında mevcut ölçümün gürültü/alt sınır belirsizliği ayrıca belirtilir.

## 7. Aşama 3 — Gerçek hayat yükleriyle deney sırası

### 7.1 İlk seri: 1 → 2 → 3 LED ampul

Kullanıcının elindeki üç LED ampul ilk gerçek hayat deney serisidir.

1. Tek LED ampul çalıştırılır; ampul kimliği ve nominal gücü kaydedilir.
2. İkinci LED eklenir; yeni yük değişim zamanı kaydedilir ve yeni pencere açılır.
3. Üçüncü LED eklenir; aynı prosedür tekrarlanır.
4. Her basamakta PZEM V/I/P/PF ve BERO akım ölçümü kaydedilir.
5. Ampuller aynı marka/model/watt ise aynı sürücü ailesi altında toplam akım basamaklanmış olur. Farklılarsa her ampul ve kombinasyon ayrı `load_id` ile etiketlenir.
6. PF, crest factor veya dalga biçiminin ampul sayısıyla aynı kalacağı varsayılmaz; her noktada gözlenir.

**Yorum:** PF ve crest factor benzer kalırken SCT/PZEM oranı akımla değişirse genlik/düşük seviye etkisi ihtimali güçlenir. PF veya crest factor de değişirse sonuç yalnızca akım genliğine bağlanmaz.

### 7.2 İkinci seri: vantilatör

- Her sabit hız kademesi ayrı çalışma noktasıdır.
- İlk kalkış/geçiş bölümü ayrı tutulur; kararlı hız dönemi için yeni `window_id` açılır.
- PF, akım ve dalga biçimi önceden varsayılmaz; ölçülür.
- Vantilatör motor tipi veya hız kontrol yöntemi biliniyorsa kaydedilir; bilinmiyorsa tahmin edilmez.

### 7.3 Üçüncü seri: telefon şarjı

- Adaptör modeli ve mümkünse telefon/şarj durumu kaydedilir.
- Uzun süre kararlı kalması beklenmez.
- Kısa süreli kararlı aralıklar bulunursa ayrı `steady` pencereleri açılır.
- Akım/PF sürekli değişiyorsa veri `dynamic` olarak saklanır; geçersiz sayılmaz veya silinmez.

### 7.4 Son kontrollü seri: 100 W dimmerli akkor

- Dimmerli akkor gerçek ev yüklerinin yerine geçmez; ayrı kontrollü dalga biçimi grubudur.
- PF hedefleri (ör. 0.8, 0.65, 0.50) yalnızca deney hedefidir. Erişilen gerçek PF PZEM'den alınır.
- Her dimmer adımı sonrası yeni pencere açılır; kararlı duruma gelmeden veri noktası oluşturulmaz.
- Dimmerin aynı anda akım seviyesini ve dalga biçimini değiştirdiği raporda belirtilir.

### Önerilen deney önceliği

1. 1/2/3 LED ampul.
2. Vantilatörün sabit hız kademeleri.
3. Telefon şarjı (kısa steady pencereler ve dynamic kayıt).
4. 100 W dimmerli akkor (kontrollü karşılaştırma).
5. Uygun olgunluğa geldikten sonra çamaşır makinesi/bulaşık makinesi çalışma evreleriyle ayrı saha doğrulaması.

## 8. Aşama 4 — Kararlı pencere ve zaman eşleme protokolü

Her yük/dimmer/hız değişiminde:

1. `load_change_timestamp` kaydedilir ve yeni `window_id` oluşturulur.
2. Geçiş süresince `window_status=settling` kullanılır. Bu satırlar silinmez, fakat kararlı nokta analizine girmez.
3. PZEM-REF-WROOM-01 yayın aralığı 5 saniyedir. En az bir tam yayın aralığı geçmesi beklenir; ardından önceden belirlenmiş tolerans içinde en az üç ardışık PZEM yayınında V/I/P/PF kararlılığı aranır.
4. BERO ölçümü de aynı zaman aralığında kararlı olmalıdır. Koşul sağlanınca yeni/aynı kimlikli pencere `steady` olarak işaretlenir.
5. Değerler değişmeye devam ediyor ama veri geçerliyse `dynamic`; bozuk/eksik/NaN/bağlantı hatası varsa `invalid` olarak işaretlenir.
6. PZEM'in 5 saniyelik yayın aralığı, PZEM'in kendi iç ölçüm/ortalama penceresinin tam süresi olarak kabul edilmez. `pzem_publish_timestamp` yalnızca yayın anıdır.
7. PZEM'in seyrek örnekleri interpolasyonla yapay şekilde çoğaltılmaz. Kararlı pencere özeti ve mevcut PZEM örnek sayısı kullanılır.

**200 ms / 1 s ayrımı:**
- `ct_clamp_sample_duration_ms=200`: Her ct_clamp RMS ölçüm çevrimindeki örnek toplama penceresi.
- `ct_clamp_update_interval_ms=1000`: Yeni RMS ölçüm çevriminin güncelleme aralığı.
- Bunlar saniyede beş adet 200 ms pencerenin birleştirilmesi demek değildir.
- Gerçek `source_sample_count` ve `effective_sample_rate_sps` yalnız debug/ham logdan elde edilirse yazılır. ADC ayarındaki teorik 860 SPS gerçek örnek sayısı yerine kullanılmaz.

## 9. Veri modeli — her deney noktasında saklanacak alanlar

| Grup | Alanlar |
|---|---|
| Kimlik | `experiment_id`, `window_id`, `load_id`, tarih/saat |
| Yük | Yük tipi, marka/model, nominal W, ampul adedi, dimmer konumu veya vantilatör hız kademesi, telefon şarj bilgisi |
| Durum | `window_status=settling/steady/dynamic/invalid`, not |
| Zaman | `load_change_timestamp`, `pzem_publish_timestamp`, `measurement_window_start`, `measurement_window_end`, `measurement_window_duration_ms` |
| PZEM | `V_pzem`, `I_pzem`, `P_pzem`, `PF_pzem`, örnek/yayın sayısı |
| BERO RMS | `zmpt_v_rms`, `sct_i_rms`, kullanılan V1.6 çıkışı ve akım hata/oranı |
| Dalga biçimi | `I_peak`, crest factor, dalga biçimi notu; yalnız örnekleme bunu destekliyorsa |
| ADC/zamanlama | ADC kimliği, MUX, PGA, SPS ayarı, gerçek örnek sayısı, efektif SPS, kanal arası `Δt` |
| Yazılım | YAML/firmware sürümü, SCT kimliği, kalibrasyon modeli/katsayısı |
| Kanıt | Ham dosya adı, log konumu, analiz raporu bağlantısı |

Önerilen pencere özeti CSV başlığı:

`experiment_id,window_id,load_id,window_status,load_change_timestamp,pzem_publish_timestamp,measurement_window_start,measurement_window_end,measurement_window_duration_ms,load_type,load_model,nominal_power_w,load_count,setting,pzem_v_rms,pzem_i_rms,pzem_p_w,pzem_pf,bero_v_rms,bero_i_rms,bero_p_w,bero_pf,i_peak,crest_factor,source_sample_count,effective_sample_rate_sps,adc_id,mux,pga,sample_rate_setting,delta_t,yaml_version,calibration_model,notes,raw_file`

Elde olmayan alanlar boş/unknown bırakılır; değer uydurulmaz.

## 10. PF hesabı ve mevcut ADC sınırı — kritik ayrım

### 10.1 Gerçek PF hesabı

Yalnızca gerilim RMS ve akım RMS değerlerini bilmek PF'yi hesaplamak için yeterli değildir. Gerçek PF için aynı zaman tabanına ait gerilim ve akım örnekleri gerekir:

`V_RMS = sqrt(mean(v[n]^2))`

`I_RMS = sqrt(mean(i[n]^2))`

`P = mean(v[n] * i[n])`

`PF_BERO = P / (V_RMS * I_RMS)`

Örnekler ofsetten arındırılmalı; gerilim ve akım aynı pencereyi temsil etmeli ve kanal zaman farkı bilinmelidir. Bu yöntem bozulmuş dalga biçimlerinde yalnızca sinüs varsayımıyla `cos(phi)` hesaplamaktan daha uygundur.

**Sabit kazanç özelliği:** SCT örnekleri gerçek akım dalgasının yalnızca pozitif sabit bir kazançla çarpılmış hali ise, aynı katsayı P ve I_RMS içinde bulunur ve PF oranında sadeleşir. Bu nedenle SCT'nin amper ölçeği PZEM ile henüz eşleşmiyor olsa bile PF doğru hesaplanabilir. Bu; faz/frekans hatası, dalga biçimi bozulması, kırpılma, doyum, doğrusal olmama, gürültü/ofset veya zaman kayması varsa garanti edilmez.

### 10.2 PZEM PF etiketi ile BERO'nun bağımsız PF'sini karıştırma

- Mevcut `ct_clamp` RMS sensörleri ve PZEM PF yayınlarıyla SCT/PZEM akım oranı ile PZEM PF arasındaki ampirik ilişki incelenebilir. Bu, **PZEM PF etiketli akım sapması analizi**dir.
- Bu veri tek başına BERO'nun bağımsız PF ölçtüğünü göstermez.
- BERO'nun kendi PF'si için ZMPT ve SCT'den zaman damgalı ham örnekler gerekir; `ct_clamp` RMS çıktıları anlık `v[n]` ve `i[n]` dizisinin yerini tutmaz.

### 10.3 ADS1115 için geçiş kapısı

- Mevcut ADS1115 No.10 ayarı 860 SPS, tek ADC ve paylaşılan MUX'tur; kanal dönüşümleri eşzamanlı değildir.
- İki kanal dönüşümlü okunursa kanal başına yaklaşık 430 SPS teorik değer oluşabilir; gerçek hız ve kanal arası `Δt` ölçülmeden bu sayı kesin kabul edilmez.
- 430 SPS kanal başına 50 Hz'de yaklaşık 8.6 örnek/periyot demektir. Bu, temel dalga için sınırlı gözlem sağlayabilir; dimmer/LED akımındaki yüksek harmonikleri ve crest factor'ü güvenilir ölçmek için yeterli olduğu varsayılmaz.
- Mevcut 200 ms `ct_clamp` RMS / 1 s yayın düzeni ham dalga kaydı değildir.
- Gerçek PF algoritması için önce ham çift kanal örneklerinin zaman damgası, efektif örnek hızı, kanal gecikmesi ve dalga biçimi yeterliliği test edilir. Yetersiz bulunursa daha hızlı/eşzamanlı örnekleme çözümü ayrıca değerlendirilir; bu karar ölçüm kanıtına dayanır.

## 11. Analiz ve düzeltme modeli

1. Önce her `steady` pencerede SCT/PZEM akım oranı ve akım hatası hesaplanır.
2. PF, I_RMS, I_peak/crest factor, yük türü ve dalga biçimi birlikte değerlendirilir.
3. Benzer akım seviyesinde farklı PF noktaları; benzer PF seviyesinde farklı akım noktaları; aynı PF/akım civarında farklı yük türleri mümkün olduğunca karşılaştırılır.
4. PF tek başına neden kabul edilmez. Dimmerli akkor, LED sürücü ve motor yükleri ayrı ailelerde tutulur.
5. Ampirik fonksiyon yalnız test edilen PF/akım/yük/dalga biçimi aralığında geçerli aday sayılır.
6. Fonksiyonun kurulmasında kullanılan kayıtlarla doğrulama kayıtları ayrılır. En az bir tekrar veya eğitimde kullanılmamış çalışma noktasıyla kontrol yapılır.
7. Düzeltme modeli yalnız veri destekliyorsa kurulur; gereksiz çok değişkenli karmaşıklık eklenmez. Önce basit fonksiyon denenir.
8. Yeni yük tipi, motor kalkışı veya çamaşır makinesi evre geçişi otomatik olarak model kapsamında sayılmaz; ayrı doğrulama gerekir.
9. Kullanıcıya sunulan çıktı BERO'nun hesapladığı PF ve düzeltilmiş akım olur; iç katsayı/parametre kullanıcı çıktısı değildir.

## 12. Osiloskop ve ayrıntılı faz incelemesinin rolü

- Osiloskop ilk PF deneyinin ön koşulu değildir.
- 2D15P ile gerektiğinde düşük gerilimli sensör çıkışının görünümü, temel frekans, genlik, bozulma veya olası kırpılma kontrol edilir.
- İlk aşamada FFT, ayrıntılı harmonik tablosu veya osiloskop üzerinden faz açısı hesaplama zorunlu değildir.
- PF/akım sonucu pratik karşılaştırmayla açıklanamazsa ZMPT–SCT faz/zamanlama davranışı, analog ön uç ve ADC örnekleme gecikmesi daha ayrıntılı incelenir.
- 2D15P bataryalı olsa da giriş izolasyonu varsayılmaz; şebeke uçlarına bağlanmaz.

## 13. Başarı ve karar kapıları

| Kapı | Başarı koşulu | Sonraki işlem |
|---|---|---|
| G0 — Güvenlik | ZMPT kartı, bağlantı ve kapalı düzen uygunluğu incelendi | Güvenli düşük gerilim ön testi / uygun ise sonraki aşama |
| G1 — Gerilim ölçeği | ZMPT gerilim RMS değeri PZEM'e kararlı ve tekrarlanabilir biçimde yaklaştı | Trimpot ayarını kaydet ve sabitle |
| G2 — Gerçek yük verisi | 1/2/3 LED, vantilatör ve telefon şarjı için etiketli PZEM/BERO kayıtları alındı | Kararlı/dinamik pencereleri ayır |
| G3 — PF kanıtı | Ham v[n]/i[n], örnekleme hızı ve zaman eşlemesi gerçek PF hesabını destekliyor | BERO PF hesaplamasını karşılaştır |
| G4 — Düzeltme | Tekrarlanabilir hata örüntüsü ve bağımsız doğrulama var | Ayrı PF-akım düzeltme modeli adayı oluştur |
| G5 — Saha doğrulama | Yeni yük/evrelerde ayrı doğrulama yapıldı | Model kapsamını belgeleyip sürümle |

Bir kapı geçilemezse başarı ilan edilmez; hangi kanıtın eksik olduğu kayda alınır. PZEM'e tek noktada eşitlenmek tek başına doğrulama sayılmaz.

## 14. Deney oturumu sonunda saklanacak çıktılar

Her oturum için:
1. Değiştirilmemiş ham CSV/LOG.
2. Deney ayarları ve bağlantı özeti.
3. Kararlı pencere/dinamik pencere etiketli analiz CSV'si.
4. Grafik ve istatistikler.
5. Bulgular, sınırlamalar ve teknik yorum içeren Markdown raporu.
6. Kullanılan YAML/firmware/model sürümü ve Git commit bağlantısı.

Ham veri ile filtrelenmiş/yorumlanmış çıktı ayrı dosyalarda tutulur. Başarısız veya sonuçsuz denemeler de kaydedilir.

## 15. Bu planın başlangıç noktası

1. ZMPT101B kartının fiziksel tanıma ve güvenlik ön kontrolünü tamamla.
2. SCT013-030 doğrudan çıkış kısa DMM ön kontrolünü, mevcut 2D15P ile yap; UT61E+ teslim edildiğinde düşük mV ölçüm kontrolünü tekrar et.
3. Sabit dirençli yükte ZMPT gerilim ölçeğini PZEM'e yaklaştır ve trimpot ayarını sabitle.
4. İlk gerçek hayat serisini 1 → 2 → 3 LED ile başlat.
5. Her basamakta PZEM kararlılığını bekle, `settling/steady` etiketlerini uygula ve ham veriyi koru.
6. Ardından vantilatör, telefon şarjı ve son olarak dimmerli akkor testlerini uygula.
7. Mevcut ADS1115 ham örnekleme yeterliliğini ölç; gerçek BERO PF algoritması için yeterli değilse bunu açıkça raporla ve alternatif örnekleme kararını kanıta göre ver.

**Son durum:** Bu belge üzerinde anlaşılan deney planıdır. ZMPT trimpot ayarı, LED/vantilatör/şarj/dimmer deneyleri, ham eşzamanlı PF hesabı ve yeni düzeltme fonksiyonu henüz fiziksel olarak tamamlanmış değildir.
