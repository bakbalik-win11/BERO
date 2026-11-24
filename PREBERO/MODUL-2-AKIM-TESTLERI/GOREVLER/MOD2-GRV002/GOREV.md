# MOD2-GRV002 – BERO bağımsız PF ve PF etkili akım ölçümü

- **Açılış tarihi:** 2026-11-24
- **Durum:** AÇIK – çerçeve ve deney adımları tanımlandı; bu kayıtta yeni fiziksel deney yapılmadı.
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

## 3. İki aşamalı yaklaşım

### Aşama A – PZEM referansıyla grafik ve ampirik akım düzeltmesi

İlk aşamada ZMPT101B ile PF hesaplamayı beklemeden, PZEM'in yayınladığı akım ve PF değerleri eğitim/referans etiketi olarak kullanılacaktır. EXP akımının PZEM akımına göre sapması grafiklerle incelenecektir. EXP formülünün geliştirilmesinde izlenen pratik yol tekrar edilecektir: veri toplama → grafikleme → eğilimi gözleme → uygun basit fonksiyonu deneme → bağımsız kayıtla kontrol.

İlk karşılaştırma değişkenleri:
- PZEM akımı (`I_PZEM`)
- PZEM PF (`PF_PZEM`)
- EXP akımı (`I_EXP`)
- Hata: `error_A = I_PZEM - I_EXP`
- Oran: `ratio = I_PZEM / I_EXP` (yalnızca oran için uygun, sıfıra yakın olmayan akım değerlerinde)
- Zaman damgası ve kararlı pencere kimliği
- Varsa PZEM gerilimi/aktif gücü ve yük/çalışma modu notu

İlk grafikler:
1. X=PF_PZEM, Y=I_PZEM/I_EXP.
2. X=PF_PZEM, Y=I_PZEM-I_EXP.
3. X=I_EXP, Y=I_PZEM/I_EXP.
4. PF ve akım seviyesini birlikte gösteren hata grafiği.

Başlangıç hipotezi: PF 1'den uzaklaştıkça EXP akımını aşağı yönde düzeltmek gerekebilir. Bu yalnızca hipotezdir; grafikler tersini veya akım/yük türüne bağlı daha karmaşık bir davranışı gösterirse veri esas alınır.

İlk aday ifade, yalnızca grafikler böyle bir eğriyi desteklerse kullanılmak üzere:
`I_corr = I_EXP × C(PF)`.
Gerekirse akım seviyesini de içeren `C(PF, I_EXP)` değerlendirilir. İlk aşamada karmaşık model veya makine öğrenmesi zorunlu değildir.

### Aşama B – ZMPT101B ile BERO'nun kendi PF hesabı

İkinci aşamada ZMPT101B gerilim dalga biçimi, SCT013 akım dalga biçimiyle ortak zaman tabanında örneklenerek BERO'nun kendi gerçek PF hesabı geliştirilir:

- `P = mean(v_ac[n] × i_ac[n])`
- `Vrms = sqrt(mean(v_ac[n]^2))`
- `Irms = sqrt(mean(i_ac[n]^2))`
- `S = Vrms × Irms`
- `PF = P / S`

Yalnızca faz açısı ve cos(phi) hesabı, sinüzoidal olmayan yüklerde gerçek PF yerine kullanılmaz. Zaman hizası, sensör/analog ön uç faz etkisi, ADC örnekleme aralığı ve jitter ölçülmeden PF sonucu doğrulanmış sayılmaz.

Aşama A'da PZEM PF ile bulunan ampirik düzeltme, Aşama B'de BERO'nun kendi PF ölçümüyle denenebilir. PZEM'e göre kalibrasyon ile bağımsız PF ölçümü ayrı doğrulama başlıkları olarak raporlanacaktır.

## 4. Deney adımları ve ilerleme

| Adım | İş | Durum |
|---|---|---|
| 0 | Proje hedefini ve V1.6'yı koruma kararını tanımlama | TAMAMLANDI – kullanıcı kararı, 2026-11-24 |
| 1 | Mevcut çamaşır makinesi ve düşük PF kayıtlarını yeniden grafikleme; PF-akım-hata eğilimini görme | BEKLİYOR |
| 2 | Aynı zaman penceresinde PZEM I/PF ve EXP akımı içeren yeni pratik yük kayıtları toplama | BEKLİYOR |
| 3 | Grafiklerden basit düzeltme fonksiyonu adayı çıkarma; gerekirse farklı akım bantlarını ayırma | BEKLİYOR |
| 4 | Fonksiyonu eğitimde kullanılmayan tekrar/yük kaydıyla kontrol etme | BEKLİYOR |
| 5 | ZMPT101B kartını güvenli düşük gerilimli izole AC ile tanıma: kart revizyonu, besleme, OUT ofseti, genlik ve kırpılma | BEKLİYOR |
| 6 | SCT ve ZMPT örnekleme zamanlamasını ve faz davranışını ölçme; BERO PF hesabını geliştirme | BEKLİYOR |
| 7 | BERO PF değeriyle akım düzeltmesini deneme; PZEM olmadan çalışma davranışını doğrulama | BEKLİYOR |
| 8 | Sonuç, hata aralığı, tepki davranışı ve kullanım sınırlarını raporlama; gerekirse yeni sürüm açma | BEKLİYOR |

Adım sırası deneyde elde edilen sonuca göre güncellenebilir. Her adımın sonucu, kullanılan ham veri, grafik, log ve kısa yorumuyla kaydedilir. Başarısız veya sonuçsuz deneyler de korunur.

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
`timestamp,window_id,I_pzem,PF_pzem,V_pzem,P_pzem,I_raw,I_EXP,error_A,ratio,load_state,notes`

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

Bu görevde henüz yeni fonksiyon, firmware veya donanım doğrulaması üretilmemiştir. İlk sıradaki iş mevcut verilerin grafiklenmesidir.
