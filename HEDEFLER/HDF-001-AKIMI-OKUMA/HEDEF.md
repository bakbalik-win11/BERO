# HDF-001 — Akımı Okuma

## Hedef

Proje BERO kapsamında akımın ölçüm zinciri üzerinden okunmasını, davranışının ölçümlerle doğrulanmasını ve elde edilen yöntemin sınırlarıyla birlikte tekrarlanabilir biçimde belgelenmesini sağlamak.

Bu ana hedef, tek bir kod denemesinden ibaret değildir. Sonuca ulaşmak için gereken görevler sırayla yürütülür; görev sırası, önceki görevlerden elde edilen ölçüm ve bulgulara göre netleştirilebilir. Her görev kendi kimliği ve kayıt alanıyla yürütülür; kapanmış görevlerin geçmişi korunur.

## Görev silsilesi

| Görev | Amaç | Durum |
|---|---|---|
| [GRV-001 — ESP32-D ile SCT-013 Akım Okuması](../../GOREVLER/GRV-001/RAPOR/README.md) | ESP32-D ve SCT-013 ile okuma zincirinin davranışını incelemek ve ölçüm sonuçlarını kaydetmek | Başlangıç / sonuç bekleniyor |

Yeni görevler, önceki görevdeki bulgulara göre bu tabloya yeni satır olarak eklenir. Eski görevlerin kayıtları yeni görev için yeniden yazılmaz.

GRV-001'in odağı ESP32-D ve SCT-013 ile akım okuma zincirini incelemek ve ölçüm davranışını kaydetmektir. MCP3208/SPI zamanlama doğrulaması bu görevin kapsamına dahil değildir; gerekirse ayrı bir görev olarak tanımlanır.

## Tamamlanma yaklaşımı

Ana hedefin tamamlandığı ancak sonuçlar ve kanıtlar değerlendirildikten sonra ilan edilir. Sonuç değerlendirmesi en az şunları kapsar:

- Hedeflenen ve fiilen elde edilen sonuç
- Kullanılan donanım, bağlantı ve test koşulları
- Ölçüm kayıtları ve bunların desteklediği bulgular
- Derlendiği ve test edildiği doğrulanmış kod sürümü ile bağlantısı
- Doğrulanmış noktalar, belirsizlikler ve sınırlar
- Öğrenilenler ve açık kalan işler

Test edilmemiş veya ölçümle doğrulanmamış noktalar başarılı sonuç olarak sunulmaz. Sonuç raporu hedef tamamlanırken hazırlanır; henüz sonuçlanmamış bir hedef için başarı iddiası oluşturulmaz.

## Süreklilik kuralı

Bu hedefe ait rapor, ölçüm ve kod geçmişi sessizce üzerine yazılarak değiştirilmez. Yeni bulgu yeni görev, yeni kod sürümü veya ek kayıt olarak tutulur. Ayrıntı: [Kayıt, Sürümleme ve Süreklilik Politikası](../../KAYIT_VE_SUREKLILIK.md).

## Durum

**DONDURULDU — yarım kaldı.** Veri okuma testlerinden işe yarar ESP yetenekleri ve deneyim kazanıldı; ancak bu verilerden güvenilir akım hesabına geçiş tamamlanmadı. HDF-001 tamamlanmış hedef olarak gösterilmez.


---

## 2026-10-12 — Dondurulma gerekçesi: veri okuma kazanıldı, F(x) felsefesi başarısız kaldı

**Durum:** Donduruldu; geçmiş kayıtları korunur. Bu karar, bütün deneylerin başarısız olduğu anlamına gelmez.

### Korunan kazanım

HDF-001 sırasında ESP'nin veri okuma yeteneklerini inceleyen testler yapıldı. Örnek toplama, kanal davranışı, zamanlama, veri aktarımı ve istatistik üretimi üzerine edinilen işe yarar bilgi HDF-002'de yeniden kullanılabilir. Bu testlerin değeri kaybolmadı; aynı testleri gereksiz yere baştan yapmak hedef değildir.

### Neden akım hesabına geçilemedi?

Hedef 1'deki F(x) yaklaşımı, SCT/MCP ölçüm zincirinin ürettiği entegre veya işlenmiş çıktıyı, ayrı PZEM ölçüm zincirinin hesaplanmış akım çıktısıyla zaman odaklı ilişkilendirmeye çalıştı. Ancak bu çıktılar aynı türden veri değildir: ölçüm zincirleri örnekleme, kümülasyon/entegrasyon ve matematiksel işleme gibi süreçlerden geçmiş olabilir. PZEM'in yayınladığı değer de ham SCT sinyalinin tek bir anlık davranışına doğrudan eşdeğer kabul edilemez.

Bu nedenle aynı veya yakın zaman damgaları, iki çıktının **aynı fiziksel akım olayını ve karşılaştırılabilir ölçüm niteliğini temsil ettiğini** kanıtlamıyordu. Sayısal veriler üzerinde istatistik hesaplamak mümkün olsa da, fiziksel anlamı ve eşleşmesi yeterince kurulmamış verilerden güvenilir F(x) elde etmek için kullanılan yöntem sağlam bir temel sunmadı.

Son testlerde istatistiksel sonuçların beklenen biçimde tutturulamaması, yalnızca parametre ayarı yapmaya devam etmek yerine yaklaşımın temel varsayımını sorgulamamız gerektiğini gösteren işaret oldu. Hata, ESP'nin okuma kabiliyetinin bütünüyle işe yaramaz olması değil; bu okumaları F(x)'e bağlamak için seçilen eşleştirme felsefesiydi.

### HDF-002'ye devredilen ilke

- İşe yarar ESP veri okuma testleri ve deney kayıtları korunur; uygun olanlar yeniden kullanılır.
- Zaman odaklı eşleştirme, aynı fiziksel olayın kanıtı olarak kullanılmaz.
- Önce aynı akım alanını/olayını temsil eden bölgeler belirlenir; PZEM'in sabit referans alanları (I, V, PF) bu bölgeleri gerekçeli biçimde etiketlemek için kullanılır.
- Etiketli veri kümesi oluşturmak, F(x)'ten önce gelen başlı başına bir kazanımdır.
- Etiketlenmiş veriden optimum paket/okuma yapısını seçme ve paket testleri sonraki aşamada yapılır.
- Ardından F(x) hesaplanır; hata görülür, değerlendirilir ve yöntem iyileştirilir.

**Sonuç:** HDF-001, veri okuma testleri bakımından değerli kazanımlar üretmiş; fakat zaman merkezli ve ölçüm zincirleri arasındaki temsil farkını gözetmeyen F(x) yaklaşımı nedeniyle akım hesaplama hedefine ulaşamamıştır. Bu yöntemle devam etmek yerine HDF-001 dondurulmuş, teknik kazanımlar HDF-002'ye aktarılmıştır.
