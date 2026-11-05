# E13 — Yüksüz gürültü filtresi ve SCT örnekleme hızı

**Durum:** PLANLANDI — uygulama/firmware değişikliği yapılmadı  
**Tarih:** 2026-11-05  
**Faz:** Faz 2  
**İlişkili kayıtlar:** I007 yüksüz gürültü havuzu, E12 tepki süresi, T007 HA→PC, T008 kararlı alan analizi

## Amaç

Fiziksel akımın 0 A olduğu yüksüz durumda SCT'nin kısa süreli sıçramalarını, gerçek zamanlı davranışı kaybetmeden ayırt etmek ve SCT çıktısını yaklaşık 0,5 saniyede bir (2 Hz) üretme hedefinin mevcut donanım/yazılım düzeninde uygulanabilirliğini ölçmek.

Bu deney iki ayrı ama ilişkili soruyu inceler:
1. Ham ölçümleri koruyarak kısa süreli aykırı okumaları filtrelenmiş yüksüz akışta bastırabilir miyiz?
2. SCT başına 500 ms çıktı aralığı (2 Hz) sürdürülebilir mi; tek kanal ve üç kanal durumlarında gerçek hız nedir?

## Kullanıcı kararları ve ilk gözlem dayanağı

- I007 fiziksel sıfır akım havuzu ayrı tutulur; ON kalibrasyon/eğitim verisine karıştırılmaz.
- Ham kaynak veri değişmez biçimde korunur. Filtreli/türetilmiş akış ikinci bir veri katmanıdır; ham kaydın yerine geçmez.
- Kısa süreli tekil sıçramalar filtreli akışta bastırılabilir/işaretlenebilir; yeterli süre devam eden yükseliş gerçek durum değişimi adayı olarak korunmalıdır.
- Filtre penceresi, sapma sınırı ve devam süresi henüz belirlenmedi.
- Kullanıcının hedefi SCT'den yaklaşık her 0,5 saniyede bir yeni çıktı, yani 2 Hz almaktır. Bu henüz ölçülmüş veya uygulanmış değildir.

I007 ilk CSV'sinde iki uzun fiziksel sıfır-akım aralığı analiz edildi. Bu aralıklardaki SCT akım entity'lerinin medyanları yaklaşık 0,157–0,170 A; P95 değerleri yaklaşık 0,255–0,333 A aralığındadır. SCT1 maksimumu 0,506 A, SCT2 maksimumu 0,655 A olarak kaydedilmiştir. Bu maksimumlar tekil uç değerlerdir; süreklilikleri ve nedenleri ayrıca analiz edilmeden eşik olarak kullanılamaz. Önceki çevrimsel HA History kaydında bu iki maksimumun her biri tek kayıt örneği olarak görünmüş, önceki/sonraki değerler daha düşük seviyeye dönmüştür. History örnekleme aralığı, gerçek elektriksel sıçramanın tam süresini kanıtlamaz.

## Mevcut firmware referansı — değişiklik yapılmadan önce

Kaynak: firmware/bero-modul2-esp32d1.yaml

- Üç SCT kanalı sıralı okunur: SCT1 → SCT2 → SCT3.
- Her kanalın ct_clamp sample_duration değeri 200 ms.
- Kanal geçişleri arasında 250 ms bekleme vardır.
- Sıralı okuma script'i 2 saniyede bir çağrılır.
- Dolayısıyla her kanal için mevcut nominal yeni çıktı hızı yaklaşık 0,5 Hz'dir (kanal başına 2 saniyede bir).
- K=24.22.
- Kanallar eşzamanlı örneklenmiş kabul edilemez.

Yalnızca 2 saniyelik çağrı aralığını 500 ms yapmak üç kanalın her birine 2 Hz sağlayamaz. Mevcut sıralı yapıdaki üç adet 200 ms ölçüm ve gecikmeler zaten 500 ms toplam bütçeyi aşar. Üç kanalın her birinde 2 Hz isteniyorsa edinim mimarisi/kanal sıralaması/örnek süresi yeniden ele alınmalıdır. Tek öncelikli kanala 2 Hz sağlamak ayrı ve daha dar bir hedeftir.

## Deney A — yüksüz filtre yaklaşımı (önce çevrimdışı)

1. I007 ham oturumunu salt okunur kaynak olarak kullan.
2. Ham değer dizisini ve timestamp'leri değiştirmeden tut.
3. Kayan pencere üzerinde merkez ve saçılım hesapla. Medyan ve MAD gibi sağlam istatistikleri basit ortalamaya alternatif olarak karşılaştır.
4. Merkezden sapma büyüklüğü ile ardışık örneklerde devam süresini birlikte kullan.
5. Tekil kısa sıçramayı işaretle veya filtreli seride bastır; devam eden yükselişi otomatik olarak silme.
6. Çıktıda en az şu alanları koru: timestamp, entity_id, raw_value, filtered_value, outlier_flag, window_id/parameter_id.
7. Farklı pencere uzunlukları ve devam sürelerini aynı ham oturum üzerinde karşılaştır; sonuçları ham/filtreli grafik ve istatistiklerle raporla.

Kabul ölçütü:
- Ham kayıt birebir korunmalı.
- Filtreli seri tekil kısa sıçramaları azaltmalı.
- Süreklilik gösteren kontrollü ON geçişini bastırmamalı.
- Filtre gecikmesi ve yanlış bastırma oranı raporlanmalı.
- Eşikler tek I007 oturumuna bakılarak nihai seçilmemeli; 7–10 günlük havuz biriktikçe yeniden değerlendirilmelidir.

## Deney B — 2 Hz örnekleme

Aşamalar:
1. Mevcut düzenin gerçek kanal başına çıktı aralığını History timestamp'lerinden ölç ve referansla.
2. Önce SCT1 tek kanalında 500 ms hedefli prototipin sürdürülebilirliğini ölç.
3. Ardından üç kanal açıkken her kanalın timestamp aralıklarını, sıra kaymasını ve eksik/tekrarlı güncellemeleri ölç.
4. Aynı kararlı yükte (başlangıçta uygun bir rezistif yük) mevcut 2 saniyelik referans ile daha hızlı akışı karşılaştır.
5. Gürültü dağılımı, kararlı alan medyanı, standart sapma, tepki gecikmesi ve örnek kaybını raporla.

Sabit tutulacaklar:
- İlk karşılaştırmada K=24.22.
- Mümkünse sample_duration=200 ms.
- Aynı CT, sarım, kablo yerleşimi ve yük.
- Değişen tek unsur örnek çıktı hızı/edinim düzeni olmalı.

Kabul ölçütü:
- Kanal başına gerçek 500 ms civarı çıktı aralığı timestamp'lerle kanıtlanmalı.
- Tekrarlanabilirlik ve kararlı yük seviyesi kabul edilemez ölçüde bozulmamalı.
- Üç kanalın eşzamanlı olduğu varsayılmamalı; gerçek örnekleme zamanları korunmalı.
- Hedef üç kanalda sağlanamıyorsa tek kanal 2 Hz veya farklı kanal önceliği açıkça raporlanmalı.

## Güvenlik ve uygulama sınırı

Bu belge yalnız deney planıdır. Firmware YAML henüz değiştirilmedi, derleme/OTA yapılmadı. Kullanıcı onayı ve kontrollü test olmadan mevcut çalışan firmware'e müdahale edilmeyecek. I007 ham yüksüz veri havuzu filtreleme denemesi nedeniyle değiştirilmez.

## Açık işler

- [ ] I007 ham CSV oturumunu kaynak olarak doğrula ve hash'ini kaydet.
- [ ] HA History timestamp aralıklarından mevcut SCT kanal başına gerçek güncelleme hızını çıkar.
- [ ] Çevrimdışı kayan pencere/robust outlier filtre prototipini hazırla.
- [ ] Tekil sıçrama ve kontrollü kalıcı ON geçişi üzerinde filtre gecikmesini/yanlış bastırmayı test et.
- [ ] SCT1 tek kanal 2 Hz prototipini ayrı kontrollü test olarak planla.
- [ ] Üç kanal 2 Hz fizibilitesini gerçek timestamp ve örnek kaybıyla değerlendir.
- [ ] Deney sonuçlarını ve gerçek log örneklerini depoya ekle.

**Sonuç:** Henüz yok. E13 tamamlanmış değildir.


## 2026-11-05 — Canlı ESP mimarisi netleştirildi: tek kanal, 2 Hz

Kullanıcı açıklamasıyla hedef mimari kesinleştirildi:
- Eğitim/veri toplama aşamasında üç SCT kanalının okunması yararlıdır; mevcut Modül 2 bu amaçla kullanılabilir.
- Canlı çalışacak eğitilmiş ESP üç kanalı okumayacak. Tek bir SCT kanalından her 500 ms'de bir yeni ölçüm alacak: 2 Hz.
- Dolayısıyla canlı ESP için üç kanalın her birinde 2 Hz sağlama gereksinimi yoktur. E13'ün canlı örnekleme fizibilitesi tek kanal odağına indirgenmiştir.
- Mevcut Modül 2 üç kanallı eğitim firmware'i olduğu gibi kalır; bu hedef nedeniyle değiştirilmez. Tek kanallı canlı ESP ayrı hedef mimaridir ve henüz uygulanmış değildir.

## 4 saniyelik kayan filtre penceresi — ilk tasarım adayı

Kullanıcı, 2 Hz canlı ölçüm akışında yaklaşık 4 saniyelik kayan pencere kullanmayı önerdi. 2 Hz'de pencere başına 8 örnek bulunur. Amaç tekil kısa süreli sıçramaları karakterize edip yüksüz durum kararını daha kararlı hale getirmektir.

Bu değer **ilk test adayıdır; onaylanmış nihai parametre değildir**. Filtre tasarımında:
- Ham ölçüm her zaman ayrı ve değişmez tutulur.
- Sekiz örnekli kayan pencereden sağlam merkez/dağılım (ör. medyan ve MAD) çıkarılır.
- Tekil aykırı örnek ham akıştan silinmez; türetilmiş akışta işaretlenir veya filtreli durum değerine katılmaz.
- Ardışık örneklerde devam eden yükseliş, gerçek yük başlangıcı olabileceğinden otomatik olarak bastırılmaz.
- Pencere dolum süresi, filtre gecikmesi ve yük başlangıcını algılama gecikmesi ayrıca raporlanır.

4 saniye pencere ile sekiz örnek olması, sistemin mutlaka 4 saniye gecikmeli karar vereceği anlamına gelmez. Kayan pencere her 500 ms'de güncellenebilir; ancak hangi kararın ne zaman kesinleşeceği seçilen süre/ardışıklık mantığına bağlıdır. Bu davranış kontrollü ON/OFF geçişiyle test edilmelidir.

## E13 kapsam düzeltmesi

- Deney A: I007 ham yüksüz kayıtları üzerinde çevrimdışı filtre karşılaştırması; ham veriyi değiştirmez.
- Deney B: canlı hedef ESP için tek SCT kanalında 500 ms çıktı aralığının (2 Hz) sağlanması. Üç kanal hız testi canlı hedef için gerekli değildir; üç kanallı Modül 2 yalnız eğitim/veri toplama düzeni olarak kalır.
- Tek kanallı canlı ESP'de 4 saniyelik / 8 örnekli kayan filtre adayı, tekil sıçramayı bastırırken gerçek ON başlangıcını geciktirmeme açısından değerlendirilecek.

Açık işler ve kabul ölçütleri buna göre revize edilmelidir. Firmware henüz değiştirilmedi; 2 Hz ve filtre uygulaması test bekliyor.
