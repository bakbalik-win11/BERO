# E18 — CH1 SCT çıkarılmış, bias hattı üzerinden uzun süreli kontrol

**Durum: PLANLANDI — fiziksel bağlantı ve kayıt henüz yapılmadı.**

## HEDEF

CH1'de gözlenen sıçramaların SCT sensöründen/sensör bağlantısından mı, yoksa ESP ölçüm girişinden ve ortak ölçüm zincirinden mi kaynaklandığını ayırmaya yardımcı olacak kontrol kaydı almak.

Bu deney E17 düşük akım yük deneylerinden ayrıdır. 15 W ampul deneyi değildir; CH1'de SCT sensörü ölçümden çıkarılır ve kullanıcı kararına göre CH1 ölçüm noktası bias okuyan hatta bağlanır.

## Deney bağlantısı

- CH1'in SCT sensör bağlantısı çıkarılacak.
- CH1 ölçüm girişi, Modül 2'nin ortak bias okuyan hattına bağlanacak. Proje kayıtlarında ortak bias ölçüm noktası GPIO35 olarak tanımlanmıştır; fiziksel bağlantı yapılmadan önce kart üzerindeki gerçek hat/pin eşlemesi teyit edilecek.
- Bu, CH1 girişini boşta bırakma deneyi değildir.
- Bağlantı yalnızca düşük gerilimli ESP/bias tarafında yapılır. Şebeke tarafında bağlantı değişikliği yapılmaz.
- SCT sekonderi ve CT bağlantısı üretici talimatına uygun şekilde güvenli tutulur; primer akım varken sekonder açık bırakılmaz.

## Sabit tutulacaklar

- ESP ve mevcut firmware/YAML değiştirilmez.
- K, sample_duration, update_interval, pin yapılandırması ve diğer kanallar değiştirilmez.
- CH2/CH3 normal çalışıyorsa kontrol serileri olarak kayıtta tutulur.
- SSR olayları varsa ayrı metadata olarak korunur; CH1'in fiziksel yük durumu sayılmaz.
- Deney süresince CH1'e SCT sinyali uygulanmaz; CH1 bias hattı üzerinden gözlenir.

## Kayıt

- Home Assistant History üzerinden uzun süreli CH1 ham SCT ve hesaplanmış akım kaydı alınır.
- Mevcutsa ortak bias entity/okuması, CH2 ve CH3 serileri de aynı CSV'de korunur.
- Başlangıç/bitiş saati, gerçek bağlantı, kullanılan firmware/YAML sürümü ve CSV kolonları kayıt sonrasında eklenir.
- Ham CSV varsayılan olarak Git'e eklenmez; özet istatistikler, seçilmiş log örnekleri ve yorum saklanır.

## Analiz

1. CSV'deki gerçek entity_id, birim, timestamp ve güncelleme aralıkları doğrulanır.
2. CH1'in bias hattına bağlı olduğu süre ayrı bir deney aralığı olarak kesilir.
3. CH1 ham SCT ve hesaplanmış akım serilerinin merkez, dağılım, yüzdelik, minimum/maksimum ve sıçrama davranışı incelenir.
4. CH1 davranışı ortak bias serisiyle ve varsa CH2/CH3 kontrol serileriyle karşılaştırılır.
5. Tekil sıçramalar ham kayıttan silinmez; ayrıca işaretlenip sayılır.
6. Sonuç, sensör sinyali olmadan ölçüm zincirinde sıçrama görülüp görülmediği ve bias referansının davranışı açısından yorumlanır.

## Yorum sınırları

- CH1 bias hattına bağlıyken sıçrama görülmesi, SCT sensörünün o sıçramalar için gerekli olmadığını gösterir; tek başına ESP ADC'sinin kusurlu olduğunu kanıtlamaz. Bias hattı, kablolama, ortak empedans, parazit, ADC davranışı ve yazılım işleme birlikte olası kaynaklardır.
- Sıçrama görülmemesi de önceki sıçramaların kesinlikle SCT'den kaynaklandığını kanıtlamaz; deney koşulları ve bağlantı biçimi farklı olabilir.
- Bu deney CH1'e ait mevcut donanım/bağlantı düzeni için kontrol niteliğindedir; diğer kanallara genellenmez.
- Deney E17-A/E17-B düşük akım sonuçlarıyla birleştirilmez; kalibrasyon, K değişikliği veya eğitim etiketi üretmez.

## LOG / kullanıcı gözlemi

Kullanıcı, CH1'in bias hattı üzerinden yapılan gözleminde tekil sıçramalar dışında stabil seyrettiğini bildirdi. Bu gözlem, dalgalanmanın ana kaynağının bias hattı olmadığını ve yeni bir bias hattı araştırmasının mevcut proje hedefi açısından anlamlı olmadığını düşündürmektedir. Tekil sıçramaların fiziksel nedeni bu deneyle kesin olarak belirlenmiş değildir. Gerçek başlangıç/bitiş zamanı, süre, CSV örnek sayısı, istatistikler ve log örneği deney sonrasında eklenecek.

## SONUÇ

Henüz sonuç yok. Deney yalnızca planlandı.
\n\n## Kapanış — kullanıcı kararı\n\nE18, bias hattı gözleminin sıçramalar dışında stabil olması ve kalan düşük akım belirsizliğinin CH1 sensörünün ölçüm alt sınırı/ölü bölgesiyle ilgili kabul edilmesi nedeniyle kapatıldı. Bu sonuç ADC, kablolama veya tüm analog ölçüm zincirinin kusursuz olduğunu kanıtlamaz; yalnızca bias hattını ana şüpheli olarak araştırmayı sürdürmek için gerekçe kalmadığını belirtir. Yeni bir tekrarlı bias kontrolü planlanmayacaktır.\n\n**SONUÇ:** KAPATILDI — kullanıcı gözlemi esas alındı; ayrıca sayısal CSV istatistiği veya donanım arızası teşhisi iddia edilmez.\n