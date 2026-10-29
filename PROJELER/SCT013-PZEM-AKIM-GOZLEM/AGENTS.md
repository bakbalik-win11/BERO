# Proje çalışma protokolü

## Oturum başlangıcı — atlanamaz
Kullanıcı için kısa kontrol listesi: [Gün sonu kontrolü](GUN_SONU_KONTROLU.md). Kullanıcıdan teknik diff/JSON/test ayrıntılarını kendi başına denetlemesini bekleme; gerekli kanıtları asistan sunmalı.

1. Mevcut GitHub `main` dalını ve son commit'i kontrol et.
2. Bu dosyayı, `STATUS.md`, `ROADMAP.md`, `docs/open-questions.md` ve ilgili görev/deney dosyasını bu oturumda gerçekten oku.
3. Bir önceki durum kaydıyla depodaki gerçek dosya/PR durumunu karşılaştır.
4. Kullanıcıya işin başlangıç durumunu, hedefini ve kabul ölçütünü kısa biçimde belirt.
5. Bu dosyalar okunamadıysa okumuş gibi davranma; bunu engel olarak belirt.
6. Başlangıç raporunda okunan dosyaları, aktif görevi, son günlük girdisini ve karşılaştırılan dal/commit bilgisini kısa kanıtla belirt.
7. Daha önce cevaplanmış bilgi için soru sormadan önce envanter, teknik belge, görev kartı, açık sorular ve günlükte ara; kayıtla çelişki varsa önce farkı çöz.

## Depo tutarlılığı ve kullanıcı önceliği
- Depo kayıtları kullanıcı için kritik çalışma çıktısıdır. Anlamlı bir değişiklikte yalnız ana dosyayı değil, o bilgiye bağlı görev kartı, `STATUS.md`, `ROADMAP.md`, `docs/open-questions.md`, ilgili envanter/teknik belge ve `HISTORY/SESSION_LOG.md` kayıtlarını da kontrol et.
- Her dosyayı gereksiz yere değiştirme; ancak ilgili dosyalarda durum/bağlantı/karar tutarsızlığı varsa aynı oturumda düzelt.
- Başarıyı yalnızca commit cevabına dayanarak raporlama: yazılan dosyaları yeniden oku, commit SHA'larını ve bağlantıları doğrula; yapılmayan fiziksel testleri açıkça ayır.

## Kapsam
Proje, SCT ADC edinimi, akım özellikleri çıkarımı ve PZEM okumalarıyla zaman eşleştirmesidir. PF hesabı, FFT/THD, harmonik çözümleme, güç kalitesi analizi veya enerji analizörü geliştirme işi önermeyin.

## Değişmez veri kuralları
- PZEM kusursuz ground truth değildir; davranışı ve gecikmesi ölçülecek referans akışıdır.
- -1.0 gibi sentinel değerler, NaN, timeout ve parse hataları geçerli ölçüm gibi ortalamaya girmez.
- Şüpheli sıfır okumalarını doğrulamadan otomatik silme; gerçek elektrik kesintisi de olabilir.
- Sürekli ham ADC arşivi tutma. Normal kayıtta özet, olay çevresinde kısa ham kesit sakla.
- Birden fazla RMS penceresini doğrudan aritmetik ortalamayla birleştirme; örnek sayısı biliniyorsa kareler üzerinden birleştir.
- Her SCT pencere kaydında calibration_id bulunmalı. Kalibrasyon yapılmadıysa uydurma kimlik üretme.
- İstenen örnekleme hızı ile ölçülen gerçek hızı ayrı kaydet.
- Üretici belgesi, kullanıcı beyanı/raporu, hipotez, hesap ve bu projede ölçülen sonucu birbirinden ayır.
- Kullanıcının açıkça verdiği proje bilgilerini uygun kaynak etiketiyle kaydet; bağımsız doğrulanmadıysa ölçüm/bağımsız doğrulama gibi sunma.
- Daha önce kaydedilmiş ve hâlâ geçerli kullanıcı bilgilerini tekrar isteme; yalnız gerçekten eksik veya çelişkili alanı sor.

## Kanıt etiketleri
- **ÖLÇÜLDÜ:** Bu proje protokolü ve veri kaydıyla gösterilmiş sonuç.
- **ÜRETİCİ BELGESİ:** Üretici/kılavuzda açıkça belirtilmiş.
- **KULLANICI RAPORU:** Forum veya issue gözlemi.
- **HİPOTEZ:** Doğrulanmamış açıklama.
- **HESAP:** Belirtilen varsayımlardan matematiksel olarak türetilmiş.

Etiketsiz teknik iddia yazma.

## İş durumu sözlüğü
- **PLANLANDI:** kapsam ve kabul koşulu belirlendi.
- **HAZIRLANDI:** taslak veya değişiklik hazır, hedefe uygulanmış/aktarılmış olmayabilir.
- **UYGULANDI:** değişiklik hedef dalda/ortamda mevcut.
- **DOĞRULANDI:** ilgili kontroller çalıştırılmış ve kanıt kaydedilmiş.
- **TAMAMLANDI:** bütün kabul ölçütleri karşılanmış ve sonuç kanıtla doğrulanmış.
- **ENGELLENDİ:** gereken erişim, donanım, karar veya test yok.

Yalnızca dosyanın var olması ya da bir komutun başarılı dönmesi işi **TAMAMLANDI** yapmaz.

## Görev kartları
- İş sırası ve bağımlılıklar [tasks/README.md](tasks/README.md) içinde tutulur.
- Bir oturumda yalnızca STATUS.md içindeki **Aktif görev** üzerinde çalış. Kapsam dışı fikirleri mevcut işe ekleme; sonraki uygun görev veya açık soru olarak kaydet.
- Görev kartının durumunu ancak kanıt destekliyorsa güncelle. Yazılmış belge, fiziksel donanımın doğrulandığı anlamına gelmez.
- Kabul ölçütleri karşılanmadan ROADMAP.md kutusunu veya karar kapısını işaretleme.

## Her adımın kayıt standardı — zorunlu
Her anlamlı çalışma/deney adımı için aynı üçlü korunur:
1. **HEDEF:** Bu adımda hangi soruyu cevaplayacağız, neden yapıyoruz ve başarıyı ne gösterecek?
2. **LOG:** Gerçekte ne yapıldı; kullanılan donanım/yazılım ve ayarlar nelerdi; hangi ham kayıtlar, zamanlar, örnek sayıları ve gözlemler elde edildi? Yapılmayan işlem açıkça belirtilir.
3. **SONUÇ:** Kanıt ne gösteriyor, hangi sınırlamalar var ve bir sonraki adım ne olacak? Veri yoksa sonuç uydurulmaz; sonuç “henüz ölçülmedi” olarak kaydedilir.

Bu üçlü deney protokolünde ve sonuç kaydında görünür olmalı; anlamlı depo çalışması sonunda oturum günlüğüne de hedef, yapılan iş, doğrulama ve açık kalanlar eklenir. Her yeni adımın hedefi ve önceki adımın sonucu görülmeden bir sonraki karmaşık adıma geçilmez. Kullanıcıya oturum sonunda hedef/log/sonuç özeti verilir.

## Görev sözleşmesi
Her anlamlı depo işi için başlamadan önce hedefi, dosya/alan kapsamını, kabul ölçütlerini ve doğrulama yöntemini tanımla. Çalışma sonunda her kabul ölçütünü tek tek sonuçlandır: geçti, kaldı veya uygulanamadı. Başarısız/çalıştırılmayan testi başarılı olarak sunma.

## Güvenlik ve deney etiği
- Deney yapılmadan sonuç yazma. Deney yapılmadıysa results.md bunu açıkça söylemeli.
- 220–240 V şebeke bağlantısını yalnız yetkin kişi, uygun muhafaza ve koruma ile kurmalı.
- CT sekonderini, üretici talimatı izin vermedikçe primer akım geçerken açık bırakma.
- Cihaz, ADC, analog ön uç veya kalibrasyon zinciri değişince yeni calibration_id oluştur.
- Karar değişirse yeni ADR aç; eski kararın tarihçesini silme.

## Oturum sonu — depo işi için zorunlu
Ayrıntılı adımlar [SESSION_PROTOCOL.md](SESSION_PROTOCOL.md) içindedir. Her anlamlı depo çalışmasında:
1. Gerçek değişiklikleri ve Git farkını incele.
2. İlgili testleri/bağlantıları/şemaları doğrula; çalıştırılmayan testleri belirt.
3. `STATUS.md` ve gerektiğinde `ROADMAP.md` / görev dosyalarını güncelle.
4. `HISTORY/SESSION_LOG.md` dosyasına [şablona](HISTORY/SESSION_TEMPLATE.md) uygun oturum kaydı ekle.
5. Dal, commit, PR ve doğrulama kanıtlarını kontrol et.
6. Bir koşul tamamlanmadıysa durumu tamamlandı gösterme; açıkça ENGELLENDİ veya DEVAM EDİYOR olarak bırak.

Bu protokol bir sohbetin kendi kendine başlamasını garanti etmez. Yeni oturumda dosyalar yeniden okunmalı. GitHub Actions, PR'da durum/günlük güncellemesinin yapılıp yapılmadığını kontrol eder; teknik doğruluğun tümünü otomatik kanıtlamaz.

## Oturum sonu
- Deney sonucu için protokol, ortam, cihaz kimlikleri ve veri yolunu kaydet.
- Kanıt yoksa başarı iddiası yazma.
- Depoda değişiklik yapıldıysa kullanıcıya kesin yolları ve PR/commit bağlantısını ver.
- Yalnız yerel dosya hazırlandıysa uzak depoya aktarılmış gibi sunma.

## Orantılı doğrulama
- Bu hobi projesinde laboratuvar veya endüstriyel sertifikasyon düzeyinde testler varsayılan değildir.
- Somut sorun, güvenlik gereği veya görev kabul ölçütü gerektirmedikçe ayrıntılı tolerans/hata bütçesi, ADC doğrusallık ya da clipping marjı testleri ekleme.
- Normal test sırasında belirgin anormallik görülürse yalnız ilgili noktayı incele ve kaydet.
- Kabul ölçütleri karşılandıysa yeni şartlar uydurup görevi tekrar açma.
- Temel güvenlik önlemlerini koru; yapılmayan kontrolü yapılmış gibi yazma.


## Her adımın kaydı
Her anlamlı çalışma veya deney adımında üç bölüm bulunmalı:

1. **HEDEF:** Hangi soruya cevap aranıyor ve kabul ölçütü nedir?
2. **LOG:** Gerçekte ne yapıldı; donanım/yazılım ayarları, süre, örnek sayısı, ham kayıt yolu, gözlemler ve sapmalar nelerdir? Yapılmayan işlem açıkça belirtilir.
3. **SONUÇ:** Kanıt neyi destekliyor, hangi belirsizlikler kaldı ve sıradaki adım nedir? Ölçüm yapılmadıysa sonuç uydurulmaz; henüz ölçülmediği yazılır.

Bu üç bölüm ilgili deney protokolü/sonuç kaydında ve oturum günlüğünde yer alır. Önceki adımın sonucu değerlendirilmeden gereksiz karmaşıklığa geçilmez. Oturum sonunda kullanıcıya hedef, log ve sonuç özeti verilir.


## Deney koşulları için açıklamalı YAML
Her deney için, deney koşulları ve yapılandırma parametreleri uygunsa açıklamalı bir YAML dosyasında tutulur. YAML; deney kimliği/durumu, HEDEF, donanım ve bağlantı bilgileri, planlanan örnekleme ve kayıt ayarları, koşul listesi, kaydedilecek çıktılar ile LOG/SONUÇ alanlarını içerebilir. Her parametreye kısa açıklama eklenir; bilinmeyen değerler tahmin edilmez, `null` veya açık bir “henüz belirlenmedi” notuyla gösterilir. Planlanan ayarlar ile gerçekte kullanılan ayarlar birbirinden ayrılır. YAML tek başına ölçüm kanıtı değildir; gerçek çalışma LOG'a, yorum SONUÇ'a kaydedilir. Firmware bu YAML'ı gerçekten okumuyorsa YAML'ın kod tarafından otomatik uygulandığı iddia edilmez.


## Deney YAML ve kod koşulları — atlanamaz
Bu, BERO için zorunlu çalışma kuralıdır; kullanıcı yeniden hatırlatmasa da her ilgili adımda uygulanır.

1. Deney kodu/firmware'i hazırlamadan önce deney koşullarını açıklamalı bir `experiment.yaml` dosyasında tanımla veya mevcut dosyayı güncelle.
2. YAML en azından deney kimliği ve hedefi, donanım/bağlantı, pinler (bilinmiyorsa açıkça belirtilir), planlanan ayarlar, her deney koşulu, kaydedilecek çıktılar ve durum alanlarını içersin. Her önemli alanın yanında ne anlama geldiğini açıklayan yorum bulunsun.
3. Kodun başında veya ilgili yapılandırma bölümünde deney kimliği, hangi YAML/koşullara karşılık geldiği, kullanılan gerçek ayarlar ve deneyin amacı açıklansın. Kod YAML'ı çalışma anında okumuyorsa YAML'dan otomatik yapılandırılıyor gibi gösterilmesin; kod ve YAML arasındaki eşleşme açıkça belgelenir.
4. Planlanan ayarlar ile gerçekten kullanılan ayarları karıştırma. Gerçek kart/GPIO, örnekleme hızı, süre ve bağlantı durumu doğrulanmadıysa uydurma; bilinmeyen alanı `null` veya “henüz belirlenmedi” olarak bırak.
5. Her adımda **HEDEF / LOG / SONUÇ** zorunludur. LOG'a gerçekten yapılan işlemi, koşulları, ham veri yolunu ve sapmaları yaz; SONUÇ'a yalnız kanıtın desteklediği yorumu ekle. Deney yapılmadıysa bunu açıkça belirt.
6. Her anlamlı değişiklikte YAML, kod açıklamaları, deney protokolü/sonuç kaydı ve oturum günlüğü arasında tutarlılığı kontrol et. Yazılan dosyaları yeniden oku.

Bu kuralın amacı yalnızca dokümantasyon üretmek değil; kodun hangi deney koşulunda çalıştığını anlaşılır ve yeniden kurulabilir kılmaktır. Uygun YAML veya HEDEF/LOG/SONUÇ kaydı olmadan deney kodu işi tamamlanmış sayılmaz.
