# BERO — Ölçüm İmkânları Kataloğu

**Amaç:** BERO çalışmaları sırasında fiziksel kontrol gerektiğinde, kullanıcıya hangi ölçü aletini hangi fonksiyonda/kademede kullanacağı, probları veya pensi nereye uygulayacağı ve hangi sonucu beklediğimiz açıkça söylenebilsin.

Bu katalog yalnız cihaz listesi değildir. Her ölçüm talimatı; cihaz + mod/fonksiyon + kademe + ölçüm noktası/bağlantı + beklenen değer/aralık + yorum ölçütü içerir.

## 1. Cihaz ve ölçüm imkânları

### UNI-T UT33D+ — dijital multimetre

| Fonksiyon | Kullanılabilir mod/kademe | BERO'daki olası kontrol | Beklenen sonuç nasıl tanımlanır? |
|---|---|---|---|
| DC gerilim | DC V; 200 mV, 2 V, 20 V, 200 V, 600 V | Bias regülatör çıkışı, bias orta noktası, düşük gerilim beslemeleri | Devre şeması/hedef gerilime göre sayısal değer veya tolerans aralığı |
| AC gerilim | AC V; 200 V, 600 V | Yalnız uygun ve güvenli koşullarda AC gerilim kontrolü | Kaynak gerilimi ve ölçüm noktası belirtilerek |
| DC akım | DC A; 2 mA, 20 mA, 200 mA, 10 A kademeleri | Düşük gerilim devresinin DC akım tüketimi; seri bağlantı gerektirir | Devre beklenen tüketimi biliniyorsa değer/aralık |
| Direnç | Ω kademeleri; 200 Ω'dan 200 MΩ'a | Enerjisiz devrede direnç, direnç ağı ve süreklilik ön kontrolü | Şema/renk kodu/parça toleransından hesaplanan değer |
| Diyot | Diyot test modu | Diyot ve köprü doğrultucu elemanlarının enerjisiz ön kontrolü | İlgili yarı iletkenin beklenen ileri yön düşümü; parça/veri sayfasına göre |
| Süreklilik | Buzzer | Enerjisiz kablo, hat ve bağlantı sürekliliği | İletişim/süreklilik var-yok; buzzer eşik değeri cihaz kılavuzuna bağlı |
| NCV | Temassız gerilim algılama | Yalnız ön tarama | Kesin gerilim yokluğu kanıtı değildir |

**Sınırlar:** UT33D+ AC akım ölçmez. Direnç, diyot ve süreklilik ölçümleri devre enerjisizken ve kondansatörler güvenli biçimde boşaltıldıktan sonra yapılır. Akım ölçümü devreye seri bağlanmayı gerektirir; yanlış soket/mod kullanımı kısa devre ve cihaz hasarı riski taşır. Şebeke tarafında ölçüm talimatı ayrıca güvenlik değerlendirmesi olmadan verilmez.

### UNI-T UT200B+ — pens ampermetre

| Fonksiyon | Kullanılabilir mod/kademe | BERO'daki olası kontrol | Beklenen sonuç nasıl tanımlanır? |
|---|---|---|---|
| AC akım | AC A; kullanıcının belirttiği 3 A kademesi ve cihazın diğer uygun kademeleri | PZEM/SCT akımını bağımsız fiziksel ölçümle karşılaştırma | Aynı yük ve zaman aralığında PZEM/SCT ile karşılaştırılacak A değeri/aralığı |

**Uygulama notu:** Pens yalnız tek bir akım taşıyan iletkeni çevrelemeli; faz ve nötr birlikte pens içine alınmamalıdır. Düşük akım ölçümünde 3 A kademesi, cihazın kılavuzundaki aralık ve doğruluk koşulları kontrol edilerek seçilir. Pensin iletken çevresindeki konumu ve ölçüm kararlılığı not edilir.

**Kayıt sınırı:** 3 A kademesi kullanıcı tarafından bildirildi. Bu katalogda henüz BERO'ya ait UT200B+ ile alınmış sayısal bir ölçüm sonucu yoktur.

## 2. Ölçüm talimatı standardı

Kullanıcıdan ölçüm istenirken aşağıdaki sırayla açık talimat ver:

1. **Amaç:** Hangi arıza/hipotez/özelliği kontrol ediyoruz?
2. **Cihaz:** Tam model.
3. **Mod ve kademe:** Örn. UT33D+ → direnç (Ω) → uygun kademe.
4. **Bağlantı:** Probların iki ucu veya pensin çevreleyeceği tek iletken. Gerekirse enerjisiz bırakma koşulu.
5. **Beklenen:** Sayısal hedef, tolerans aralığı veya yalnız karşılaştırma beklentisi. Değer bilinmiyorsa uydurma; önce şema, parça kodu veya üretici belgesinden çıkar.
6. **Kullanıcıdan istenecek çıktı:** Ekran değeri, birim, seçili kademe ve ölçüm koşulu.
7. **Yorum:** Sonucun hangi aralıkta normal, şüpheli veya geçersiz sayılacağı; eşik kaynağı.

### Örnek talimat biçimi — henüz yapılmış test değildir

> **Kontrol:** Bias trafosu regülatör çıkışını doğrula.  
> **Cihaz/mod:** UT33D+ — DC V — 20 V kademesi.  
> **Bağlantı:** Siyah prob devre GND, kırmızı prob L78L33 çıkışı. Yalnız düşük gerilim DC tarafında ölç.  
> **Beklenti:** Kullanıcının daha önce bildirdiği ölçüm 3,31 V DC. Bu önceki gözlemi tekrar kontrol edeceğiz; kabul toleransı devre gereksinimi ve regülatör toleransı doğrulanmadan belirlenmiş sayılmaz.  
> **Bildir:** Ekran değeri, kademe ve ölçüm anındaki yük durumu.

> **Kontrol:** Bilinen direnç değerini doğrula.  
> **Cihaz/mod:** UT33D+ — Ω — ölçülen nominal değere uygun kademe.  
> **Bağlantı:** Devre enerjisiz; mümkünse direncin en az bir bacağı devreden ayrılmış; problar direncin iki ucunda.  
> **Beklenti:** Nominal direnç ve parça toleransından hesaplanır. Örneğin 10 kΩ ±%5 parça için 9,5–10,5 kΩ aralığı; bu yalnız örnek tolerans hesabıdır, BERO'da teyit edilmiş bir parça değeri değildir.

> **Kontrol:** Yük akımını bağımsız gözle.  
> **Cihaz/mod:** UT200B+ — AC A — uygun aralık; kullanıcı tarafından belirtilen 3 A kademesi düşük akım koşulunda değerlendirilebilir.  
> **Bağlantı:** Pens yalnız faz gibi tek akım taşıyan iletkeni çevreler.  
> **Beklenti:** Test yükü ve eşzamanlı PZEM ölçümü bilindikten sonra belirlenir; örnek bir yükün akımı varsayılarak ölçüm sonucu uydurulmaz.

## 3. Sonuç kaydı şablonu

Her gerçek ölçümden sonra şu alanları doldur:

- Tarih/saat ve saat dilimi:
- Kontrol edilen modül/devre:
- Kontrol amacı:
- Ölçü aleti/model:
- Fonksiyon/mod ve kademe:
- Ölçüm noktası veya pens konumu:
- Devre/yük koşulu:
- Beklenen değer ve dayanağı:
- Gerçek okuma ve birim:
- Tekrar sayısı/kararlılık:
- Sonuç: UYGUN / ŞÜPHELİ / UYGUN DEĞİL / SONUÇSUZ
- Kanıt sınıfı: ÖLÇÜLDÜ / ÜRETİCİ BELGESİ / HESAP / HİPOTEZ / KULLANICI BİLDİRİMİ
- Log/fotoğraf referansı ve yorum:

## 4. Katalog kapsamı ve güncelleme

Yeni ölçü aleti kullanıcı tarafından bildirildiğinde önce model ve fonksiyonları doğrulanır, sonra bu kataloğa eklenir. Yeni ölçüm imkânı ortaya çıktığında ilgili mod/kademe, güvenli bağlantı biçimi ve beklenen değer belirleme yöntemi eklenir.

**Önemli:** Katalogdaki örnek talimatlar geçmişte yapılmış testleri göstermez. Beklenen değer, gerçek devre ve ölçüm koşulu bilinmeden kesinleştirilmez. Ölçüm cihazı kapasitesi ile BERO'da fiilen ölçülmüş sonuç ayrı tutulur.
