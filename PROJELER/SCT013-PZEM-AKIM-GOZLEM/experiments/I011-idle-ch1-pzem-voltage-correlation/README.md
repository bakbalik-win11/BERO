# I011 — Uzun süreli yüksüz CH1–PZEM gerilim korelasyonu

## Amaç

Fiziksel yük kesildikten sonra K=24.22 uygulanmış CH1 akım çıktısında gözlenen sinüzoidal görünümlü dalgalanmanın, PZEM'in ölçtüğü şebeke gerilimi (yaklaşık 220–230 V aralığı) ile zamansal/istatistiksel ilişkisi olup olmadığını incelemek.

Bu deney bir **korelasyon testi**dir. Gerilim ile CH1 arasında ilişki bulunması tek başına nedensellik veya gerçek akım kanıtı değildir.

## Deney koşulu ve durum

- Fiziksel test yükü devreden çıkarılmış olacak; sistem uzun süre yüksüz/boşta çalışacak.
- Ölçüm sistemi ve PZEM açık kalacak; test boyunca başka yük eklenmeyecek.
- Kullanıcının son gözlemi: güç kesildikten sonra K uygulanmış CH1 çıktısında sinüzoidal görünümlü bir dalgalanma bulunuyor.
- PZEM gerilim gözlem aralığı: kullanıcının belirttiği yaklaşık **220–230 V**.
- Deneyin başlangıç/bitiş zamanı ve CSV henüz bekleniyor.
- Bu deney 18 W I010 yük deneyinden ayrıdır; yük yokken yapılacak bağımsız boşta kayıt olarak tutulur.

## Kaydedilecek seriler

Aynı zaman aralığında ve timestamp korunarak:
1. CH1 K öncesi katsayısız ct_clamp çıktısı.
2. CH1 K uygulanmış çıktı (K=24.22).
3. PZEM gerilim (V).
4. Varsa PZEM akım (A) ve aktif güç (W), yalnızca yardımcı kontrol serileri olarak.
5. Varsa SSR/olay işaretleri; ancak fiziksel yüksüz koşulun kanıtı olarak tek başına kullanılmayacak.

Her serinin kendi örnek sayısı, güncelleme aralığı, eksik veri ve timestamp farkları ayrı raporlanacak. Farklı hızdaki seriler yapay biçimde bire bir örnek eşleştirmeye zorlanmayacak.

## Analiz planı

- Önce zaman ekseni, veri boşlukları, güncelleme aralıkları ve sensör değerlerinin tekrar/hold davranışı kontrol edilecek.
- CH1 K öncesi ve K sonrası seriler matematiksel tutarlılık açısından karşılaştırılacak.
- CH1 ile PZEM gerilimi için zaman hizalı pencere özetleri oluşturulacak; 5, 10, 20, 30 ve 60 saniye aday pencereler kullanılabilir.
- Pearson ve Spearman korelasyonları, zaman serisi otokorelasyonu ve olası gecikmeler dikkate alınarak yorumlanacak.
- Ortak zaman eğilimi korelasyonu yapay olarak yükseltebileceğinden, ham seri korelasyonuna ek olarak pencere merkezli/detrend edilmiş değişimlerin ilişkisi incelenecek.
- Gerekirse çapraz korelasyon ve gecikme analizi yapılacak; PZEM gerilim güncelleme hızı bu analizin çözünürlüğünü sınırlar.
- Sinüzoidal görünümün periyodu, genliği ve kararlılığı yalnızca yeterli örnekleme/timestamp çözünürlüğü varsa tahmin edilecek. PZEM gerilim serisi 50 Hz dalga biçimi değildir; RMS gerilim telemetrisi olarak ele alınacak.
- Tekil sıçramalar korelasyon sonucu sayılmayacak. Süreklilik, pencere medyanı/MAD ve zaman davranışı esas alınacak.
- Korelasyon bulunmaması da gerilim etkisini kesin dışlamaz; ölçüm hızları ve veri çözünürlüğü raporda belirtilecek.

## Beklenen yanıt

Bu kayıt sonunda şu sorular yanıtlanacak:
1. CH1 boşta dalgalanması PZEM gerilim değişimleriyle aynı yönde/zamanda hareket ediyor mu?
2. İlişki pencere bazında ve detrend edilmiş değişimlerde de korunuyor mu?
3. Olası gecikme ve veri güncelleme hızları ilişkiyi değerlendirmeye elverişli mi?
4. Dalgalanma, PZEM geriliminden bağımsız bir CH1/ADC/ölçüm zinciri davranışı gibi mi görünüyor?

**Durum: TEST PLANI HAZIR / UZUN SÜRELİ BOŞTA KAYIT BEKLENİYOR.**


## Ek ölçüm serisi — Bias korelasyonu

Kullanıcının ek talebiyle aynı uzun süreli yüksüz testte **bias gerilimi** de CH1 ve PZEM gerilimiyle birlikte incelenecek.

Kaydedilecek ek seri:
- CH1 ADC girişinin ortak bias noktasındaki gerçek gerilim ölçümü (V), timestamp ile.
- Bias ölçümü ayrı bir HA sensörü/telemetri olarak mevcut değilse, bu seri varmış gibi kabul edilmeyecek; test öncesinde hangi entity'nin gerçek bias voltajını temsil ettiği doğrulanacak. Katsayısız ct_clamp akım çıktısı bias gerilimi değildir ve onun yerine kullanılamaz.

Genişletilmiş analiz:
1. Bias seviyesi ve değişimi ile CH1 katsayısız ct_clamp çıktısı arasındaki ilişki.
2. Bias ile K uygulanmış CH1 çıktısı arasındaki ilişki.
3. PZEM RMS gerilimi ile bias değişimi arasındaki ilişki.
4. Üç seri için ortak zaman pencerelerinde Pearson/Spearman, detrend edilmiş değişim korelasyonu, gecikme ve kararlılık analizi.
5. Bias'ın DC merkez seviyesi ile dalgalanma/genlik davranışı ayrı ele alınacak; sabit bias seviyesi ile bias dalgalanması birbirine karıştırılmayacak.

**Önemli:** Bias, ADC sinyalinin merkezleme gerilimidir. Bias–CH1 korelasyonu görülmesi tek başına şebeke kaynaklı girişim veya fiziksel akım kanıtı değildir; yalnızca olası bağlantıyı gösterir. Sensörün hangi elektriksel noktayı ölçtüğü ve örnekleme/güncelleme hızı raporlanacaktır.
