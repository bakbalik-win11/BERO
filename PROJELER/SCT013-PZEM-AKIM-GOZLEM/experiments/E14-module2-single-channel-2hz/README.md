# E14 — Modül 2 tek SCT kanalında 2 Hz ölçüm denemesi

**Durum:** PLANLANDI — kısa oturum / öncelik kullanıcı tarafından esnek bırakıldı  
**Planlanan oturum:** 2026-11-06 akşamı (uygunluk ve veri durumuna bağlı)  
**Faz:** Faz 2  
**İlişkili kayıtlar:** E13 örnekleme hızı hedefi, E12 SCT tepki/kararlılık gözlemi, T010 Modül 2

## Amaç

Mevcut Modül 2'yi deney alanı olarak kullanarak üç kanallı sıralı okuma yerine tek SCT kanalını daha sık okumak ve yaklaşık her 500 ms'de bir yeni ölçüm sonucu (2 Hz) üretmenin pratikte mümkün olup olmadığını görmek.

Bu, gelecekteki tek kanallı canlı ESP hedefi için erken bir fizibilite denemesidir. Modül 2'nin kalıcı mimarisini veya canlı ESP firmware'ini tanımlamaz. Modül 2 deney amacıyla değiştirilebilir; mevcut çalışan YAML değişiklik öncesi Git'te korunur ve deney sürümü ayrı dosya/commit olarak saklanır. Deney sonunda gerekirse önceki çalışan sürüme geri dönülebilir.

## Deney kapsamı

- Yalnızca **SCT1 / sarı kanal / GPIO32** okunacak.
- Kullanıcının son fiziksel beyanına göre SCT1 primer iletkeninde **1 geçiş** vardır. YAML içindeki eski 2T adlandırması fiziksel sarım sayısı olarak kabul edilmeyecektir.
- SCT2 (yeşil/GPIO33) ve SCT3 (mavi/GPIO34) bu denemede ölçüm döngüsüne katılmayacaktır.
- Ortak bias GPIO35 mevcut bağlantısında kalır.
- İlk karşılaştırmada K=24.22 ve sample_duration=200 ms korunması hedeflenir. Değişken olarak yalnız ölçümün yeniden çağrılma/yayın aralığı ele alınır.
- Hedef: yeni SCT1 ölçüm sonucunun yaklaşık 500 ms aralıkla üretilmesi (2 Hz). Bu hedef henüz kanıtlanmış değildir.
- 4 saniye / 8 örnek kayan pencere bu deneyin zorunlu kapsamı değildir; filtreleme ayrı E13 değerlendirmesidir.

## Bağlantılar ve mevcut referans

| Kanal | Fiziksel bağlantı | E14 kullanımı |
|---|---|---|
| SCT1 | Sarı kablo, GPIO32, 1 fiziksel geçiş | Aktif |
| SCT2 | Yeşil kablo, GPIO33, 4 fiziksel geçiş | Devre dışı / okunmayacak |
| SCT3 | Mavi kablo, GPIO34, 3 fiziksel geçiş | Devre dışı / okunmayacak |
| Ortak bias | Turuncu kablo, GPIO35 | Mevcut bias devresi korunur |

Mevcut Modül 2 kodu üç kanalı sıralı okur; ct_clamp sample_duration 200 ms'dir ve SCT1→SCT2→SCT3 arasında 250 ms beklenir. Sıralı döngü 2 saniyede bir çağrıldığı için kanal başına mevcut nominal çıktı yaklaşık 0,5 Hz'dir. E14'te tek kanala geçilerek bu zaman bütçesi yeniden değerlendirilecektir.

## Deney yöntemi

1. Deney öncesinde depodaki çalışan bero-modul2-esp32d1.yaml sürümünü ve SHA/commit bilgisini kaydet; bu dosyanın üzerine doğrudan deney sonucu yazma.
2. Deney firmware'ini ayrı bir E14 dosyası veya açıkça tanımlanmış deney commit'i olarak hazırla.
3. Ölçüm script'inde yalnız SCT1 component.update çağrısını çalıştır; SCT2/SCT3 çağrılarını bu deney döngüsünden çıkar.
4. Hedef çağrı aralığını 500 ms yap. sample_duration=200ms, K=24.22 ve fiziksel düzeni ilk denemede sabit tut.
5. Derleme ve OTA/cihaz yükleme öncesinde YAML kontrolü yap; donanım değişikliği kullanıcı onayıyla uygulanır.
6. Home Assistant History veya eşdeğer timestamp'li kayıtla gerçek SCT1 güncelleme aralıklarını ölç. Yalnız ayar değerine bakarak 2 Hz gerçekleştiğini kabul etme.
7. Kısa yüksüz gözlem ve kullanıcı tarafından seçilen sabit yük koşulunda kayıt al. Yük, başlangıç/bitiş zamanı ve fiziksel düzen log notuna yazılır.
8. Mevcut 2 saniyelik referansla karşılaştırma gerekiyorsa aynı SCT, aynı sarım, aynı K, aynı sample_duration ve aynı yük korunur; mümkün olduğunca yalnız çağrı aralığı değişir.

## Ölçülecek göstergeler

- SCT1 ardışık kayıt timestamp farklarının medyanı, dağılımı ve uç değerleri.
- 500 ms hedefinden sapma; eksik, tekrarlı veya düzensiz güncelleme olup olmadığı.
- Yüksek/kararlı yük koşulunda ölçüm medyanı ve standart sapması.
- Yüksüz koşulda ölçüm dağılımı; I007 ham yüksüz veri havuzuyla karıştırmadan ayrı raporlama.
- Başlangıç ve yük geçişi gözlenirse ilk tepki zamanı ve kararlı seviyeye yerleşme.
- ESP loglarında script çakışması, atlanan çevrim veya hata olup olmadığı.

## Kabul / değerlendirme

- 2 Hz hedefi ancak HA/cihaz timestamp'leri yaklaşık 500 ms yeni ölçüm aralığını gösterirse sağlanmış sayılır.
- Kısa oturumda elde edilen sonuç ön fizibilite bulgusudur; uzun süreli sürdürülebilirlik kanıtı değildir.
- Ölçüm dağılımı veya kararlı yük merkezi belirgin biçimde bozulursa daha sık güncelleme tek başına başarı sayılmaz.
- Başarısızlık da sonuçtur: gerçek aralık, sınırlayıcı neden ve sonraki deneme önerisi kaydedilir.
- Bu deneme E13'teki filtre algoritmasını seçmez; 4 saniye/8 örnek pencereyi veya herhangi bir eşik değerini onaylamaz.

## Güvenlik ve geri dönüş

- Yalnız düşük gerilimli ESP/SCT analog tarafında yazılım değişikliği yapılır; şebeke bağlantısına müdahale edilmez.
- OTA/firmware değişikliği öncesi mevcut çalışan YAML ve geri dönüş sürümü korunur.
- Deney bitince Modül 2'nin önceki çalışan üç kanallı firmware'ine dönülebilir.
- E14 sonucu görülmeden kalıcı canlı ESP mimarisi veya yeni varsayılan ölçüm ayarı ilan edilmez.

## Sonuç ve kanıt

Henüz deney yapılmadı. Firmware değişikliği, derleme, OTA ve fiziksel test gerçekleşmiş değildir. Sonuçlar; kullanılan YAML/commit, HA CSV veya log örneği, timestamp analizi ve yorumla birlikte bu dosyaya eklenecektir.

## Açık işler

- [ ] Deney öncesi çalışan Modül 2 YAML sürümünü SHA/commit ile sabitle.
- [ ] SCT1 tek kanallı deney YAML'ını ayrı dosyada hazırla.
- [ ] Derleme ve OTA öncesi kullanıcıyla ayarları doğrula.
- [ ] SCT1 için 500 ms çağrı aralığını dene.
- [ ] HA timestamp'lerinden gerçek çıktı hızını ve kayıp/tekrarları hesapla.
- [ ] Kısa yüksüz ve uygun sabit yük gözlemlerini karşılaştır.
- [ ] Sonuç, gerçek log örneği ve yorumunu depoya ekle.

**Durum notu:** E14 kısa akşam oturumu için adaydır; Cumartesi planlanan uzun çalışmanın önüne geçmez. Kullanıcı, deneyler arasında önceliği o günkü veri/donanım durumuna göre değiştirebilir.
