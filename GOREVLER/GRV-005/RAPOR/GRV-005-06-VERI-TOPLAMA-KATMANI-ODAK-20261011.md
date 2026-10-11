# GRV-005-06 — Gerçek örnek toplama ve veri üretim katmanı

- Tarih: 2026-10-11
- Durum: İnceleme kapsamı tanımlandı; uygulama ve donanım doğrulaması henüz yapılmadı.
- Ön koşul: GRV-005-05 kontrollü matematik self-test logda `RESULT=PASS` verdi.
- Ana karar: Matematik formülleri mevcut kanıtla doğrulandı; yeni bulgu olmadan değiştirilmemeli. Hata arama odağı gerçek örnek toplama ve veri üretim katmanıdır.

## 1. Kanıtlanmış ve henüz kanıtlanmamış

### Kanıtlanan
- Sabit test girdisi `x={1,2,3,4}` için mean, örnek standart sapması, ham RMS ve bias çıkarılmış RMS beklenen tolerans içinde çıktı.
- Test başlangıç/bitiş kayıtları ve `RESULT=PASS` cihaz logunda gözlendi.

### Henüz kanıtlanmayan
- Gerçek ADC örneklerinin fiziksel kanaldan doğru okunması.
- Her kanal için tam 1000 deneme hedefinin uygulanması.
- Örneklerin kanal kimlikleriyle doğru eşleştirilmesi ve aynı çevrimdeki BIAS referansının doğru ilişkilendirilmesi.
- Örnekleme süresinin, aralıklarının ve pencere başlangıç/bitiş zamanlarının doğru kaydedilmesi.
- Başarısız okumaların API tarafından algılanıp `invalid_count` alanına doğru yansıtılması.
- ADC penceresi ile PZEM güncelleme işareti arasındaki zaman ilişkisinin doğru kaydedilmesi.
- Üretilen CSV satırlarının alan sırası, sayısal değerleri, eksik değerleri ve kimliklerinin sözleşmeye uyması.
- Gerçek SCT-013 akım ölçümünün doğruluğu.

## 2. İnceleme sırası

1. **Okuma mekanizması:** ADC sürücüsü/API okuma hatasını ayırt edebiliyor mu? Başarısız okuma ile gerçek sıfır kodu karıştırılıyor mu?
2. **Örnek sayacı:** Her kanal için deneme sayısı ve geçerli örnek sayısı ayrı tutuluyor mu? Döngü tam 1000 denemede duruyor mu?
3. **Kanal eşlemesi:** CH0/CH1/CH2/BIAS fiziksel bağlantı ve yazılım kanal kimlikleriyle tutarlı mı?
4. **Pencere yönetimi:** Başlangıç, bitiş, merkez ve geçen süre aynı pencerenin gerçek olaylarından hesaplanıyor mu?
5. **BIAS ilişkilendirmesi:** Aynı ölçüm çevriminin BIAS istatistikleri doğru CH kayıtlarına bağlanıyor mu?
6. **PZEM zaman referansı:** `pzem_update_millis` alanının `on_value` işareti olduğu korunuyor; bağımsız Modbus yanıt zamanı olduğu varsayılmıyor.
7. **Kayıt/CSV üretimi:** Her çevrim için beklenen kanal satırları, ortak `measurement_id`, doğru alanlar ve geçersiz değerlerin boş tutulması kontrol ediliyor.
8. **Bağımsız analiz:** Üretilen CSV, Python ile alan/kimlik/sayı tutarlılığı açısından denetleniyor; hedef `pzem_current` ise bu alan model girdilerine sızdırılmıyor.

## 3. Tanılama ilkeleri

- Ham ADC örnekleri seri loguna veya Home Assistant'a dökülmeyecek; yalnızca geçici RAM içinde tutulmaları ve özet istatistik üretmeleri planlanıyor.
- Her iddia için log, kod veya bağımsız veri kanıtı aranacak.
- API okuma hatasını gerçekten bildirmiyorsa `invalid_count` yapay olarak artırılmayacak; sınır açıkça kaydedilecek.
- Test sonucunda gerçek 0 A varsayılmayacak. Prototipin kendi tüketimi nedeniyle daha önce gözlenen 0.028 A pratik taban değeridir, fiziksel sıfır akım kanıtı değildir.
- Mevcut ESP32D1 yapılandırması, ALT09/ALT10, GRV-002/004 ve önceki raporlar üzerine yazılmayacak. Uygulama yeni ve sürümlenmiş dosyalarda yapılacak.
- Derleme, cihaza yükleme ve cihazda başarılı çalışma ayrı doğrulama seviyeleridir.

## 4. Sonraki somut adım

Gerçek veri toplama uygulamasını tasarlamadan önce, kullanılacak güncel ESPHome YAML'ı ve ADC okuma bileşeninin mevcut API'si incelenmeli. Ardından örnek toplama durum makinesi ve CSV satırı üretimi ayrı alt adımlar hâlinde planlanmalı. Bu kayıt tek başına donanımın test edildiği veya firmware uygulamasının tamamlandığı anlamına gelmez.
