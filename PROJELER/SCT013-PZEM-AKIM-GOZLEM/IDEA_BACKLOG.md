# Fikir Havuzu ve Değişken Öncelikler

**Amaç:** Sohbet sırasında ortaya çıkan fikirleri, henüz görev olmadan kaybetmeden saklamak ve önceliklerini ihtiyaç değiştikçe güncelleyebilmek.

## Kullanım kuralları

- Yeni fikirler önce bu dosyaya girer; otomatik olarak aktif göreve dönüşmez.
- Her fikre kalıcı bir `I###` kimliği verilir. Durum veya öncelik değişse de kimlik değişmez.
- Öncelik sırası sabit değildir. Kullanıcı yeni bilgi verdiğinde sıralama güncellenir; değişiklik ve gerekçe karar geçmişine eklenir.
- Öncelik alanı boşsa henüz sıralama kararı verilmemiştir. Asistan kendi başına aciliyet varsaymaz.
- Bir fikir uygulanmaya hazır olduğunda görev listesine `T###` görevi olarak alınır; fikir kaydı silinmez, görev ID'sine bağlantı eklenir.
- Fikir ertelenirse veya önceliği düşerse silinmez. İptal edilirse nedenini kaydet.
- Bir fikir hakkında sohbet içinde yeni ayrıntı verilirse önce mevcut ID'li kaydı güncelle; aynı fikri tekrar tekrar yeni kayıt olarak açma.

## Alanlar

- **Öncelik:** P1 = şu an öne alınacak; P2 = sıradaki uygun fırsatta; P3 = düşük öncelik/ileride; boş = kararlaştırılmadı.
- **Durum:** FİKİR, DEĞERLENDİRİLİYOR, BEKLİYOR, GÖREVE ALINDI, ERTELENDİ, İPTAL.
- **Gerekçe / tetikleyici:** Önceliği değiştirebilecek ihtiyaç, bağımlılık veya yeni bilgi.
- **Görev bağlantısı:** Göreve dönüştürüldüyse ilgili T-ID.

## Fikirler

| Fikir ID | Fikir | Öncelik | Durum | Gerekçe / tetikleyici | Görev bağlantısı |
|---|---|---|---|---|---|
| I001 | Python programlarının sayısını, sorumluluklarını ve aralarındaki veri akışını ayrı mimaride tanımlamak | — | FİKİR | Kullanıcı programların nasıl oluşacağını aşamalı anlatacak; sayı ve görev dağılımı şimdiden sabitlenmeyecek. | T007 ile ilişkili |
| I002 | Home Assistant'taki verileri PC'ye taşıyacak Python aktarım akışını tanımlamak | — | FİKİR | Veri HA'da toplanacak, PC'ye aktarılacak ve PC'de işlenecek. Uygulama ayrıntıları sonraki açıklamalarla netleşecek. | T007 ile ilişkili |
| I003 | PZEM akışı ve üç SCT kanalının kararlı alanlarını deneylerle geliştirilecek kriterlerle Python'da etiketlemek | — | FİKİR | Kabul kriteri ve etikette tutulacak alanlar henüz kararlaştırılmadı. | — |


| I004 | Tek sayfalık ilerleme ağacı oluşturmak: fazlar, görevler, deneyler, durumlar ve sıradaki adımı tek görünümde bağlamak | — | GÖREVE ALINDI | Uygulandı: PROGRESS_TREE.md oluşturuldu ve STATUS.md ile ilişkilendirildi; ağaç güncel tutulacak. | PROGRESS_TREE.md |
| I005 | Hat bazında SCT birincil iletken tur sayısını belirlemek ve tur sayısını hat/sensör kalibrasyon kimliğiyle ilişkilendirmek | — | FİKİR | Kullanıcı ileride hatta özel tur kullanmanın muhtemel olduğunu belirtti. E08'de 1/2/4 tur matrisi zaten var; 5 tur yalnız dış AI önerisi ve henüz doğrulanmadı. E08 sonuçları ve gerçek hat yük profili görüldükten sonra yeniden değerlendirilir. | [Tur sayısı tasarım notu](docs/technical-reviews/2026-10-30-ct-primary-turn-count-design-note.md) |

## Öncelik / karar geçmişi

Henüz kayıtlı bir öncelik değişikliği yok.

Yeni kararları şu biçimde ekle:
- Tarih — Fikir ID — eski öncelik/durum → yeni öncelik/durum — gerekçe — kullanıcı kararı mı, öneri mi?

## Gözden geçirme

Yeni fikirleri kaydet; yalnızca kullanıcı öncelik belirlediğinde veya yeni bilgi sıralamayı değiştirmeyi gerektirdiğinde öncelikleri değiştir. Aktif görev sayısını şişirme. Bu dosya fikirlerin geçmişini korur; `tasks/README.md` uygulanacak işlerin listesidir.


| I006 | SCT1 kararlı alan tespiti ve tepki süresi algoritması; PZEM ile bağımsız kararlı alan örtüşmesi ve kısa sample_duration değerlendirmesi | P1 | GÖREVE ALINDI | 2026-11-05 kullanıcı kararı: üç soru E12 deneyinde birlikte araştırılacak. İlk veri 20:07–20:37 100 W oturumu; tam log analizi sonrası Python fonksiyonu ve kısa pencere alt deneyi planlanacak. | E12 |


| I007 | Modül 2 üç SCT kanalından toplanan yüksüz/OFF kayıtlarıyla ayrı gürültü tabanı havuzu oluşturmak; fiziksel tur sayılarını dikkate alarak kanal bazlı dağılım ve eşik analizi yapmak | P2 | BEKLİYOR | 2026-11-05 kullanıcı kararı: bir sonraki oturumun ilk adımı bu gece alınan sistem yüksüz HA History CSV kaydını kullanıcıdan istemek. Her yeni yüksüz kayıt ayrı analiz edilip zaman içinde aynı havuzda biriktirilecek. SCT1 fiziksel 1 geçiş; SCT2 4 geçiş; SCT3 3 geçiş. Tur sayısına bölme yalnız yaklaşık normalize edilmiş karşılaştırma sağlar; kanal kazancı/K, hat yerleşimi ve örnekleme farkları nedeniyle ham ölçüm deima korunacak ve doğrudan tek bir gürültü eşiği varsayılmayacak. | ADR-025 / E11 |


**2026-11-05 — Kullanıcının uzun süreli toplama talimatı:** I007 tek gecelik bir test olarak değil, hedef süresi bir hafta/10 gün veya kullanıcı uygun gördükçe daha uzun tutulabilecek sürekli bir gözlem çalışması olarak yürütülecek. Kullanıcı her gün/oturum sonunda HA History CSV sağlayacak. Her dosya bağımsız kalite kontrolü ve kanal analizi alacak; doğrulanan kayıtlar aynı kümülatif yüksüz veri havuzuna eklenecek. Yeni ekleme öncesinde depodaki son kümülatif dosya okunacak, tekrar kayıtlar kontrol edilecek, yeni veri üzerine eklenecek ve güncellenmiş havuz depoya geri yazılacak. İlk gerçek CSV geldikten sonra kaynak CSV arşivleme ve kümülatif veri şeması kesinleştirilecek. Ölçüm hattında fiziksel olarak hiçbir yük yoktur ve ESP/PZEM/modül beslemeleri bu hattan alınmamaktadır; dolayısıyla gözlem koşulunun gerçek hat akımı 0 A'dır. SCT çıktıları bu fiziksel sıfır akım koşulundaki ölçüm tabanı/gürültü davranışıdır. Hedef eşik belirlemek değil, uzun dönem gürültü bandını ve oturumlar arası değişimi tanımaktır.


| I008 | Ekipmanların uzun dönem davranışından bakım/anomali uyarıları üretmek: hidrofor ve basınç tankı çevrim sıklığı, kat kaloriferi genleşme tankı/pompa davranışı, motor akım trendleri | — | FİKİR | 2026-11-05 kullanıcı vizyonu: BERO yalnızca cihaz programı tahmini yapmayacak; haftalık/aylık geçmişten normal davranış öğrenecek. Örneğin hidroforun normalden sık devreye girmesi için kullanıcının belirlediği koşulda bildirim üretilebilir. Sık çevrim tek başına tank/diyafram arızasını kanıtlamaz; kaçak, çekvalf, basınç şalteri ve kullanım değişimi gibi alternatif nedenler de uyarıda belirtilmeli. | — |

**2026-11-05 — I008 kapsam açıklaması:** Hedef yalnız anlık alarm değil, uzun dönemli davranış geçmişinden yeni türetilmiş göstergeler üretmektir: çevrim sıklığı, çalışma/duruş süresi, akım seviyesi ve eğilimi, normal banttan kalıcı sapma. Kullanıcı kendi uyarı koşulunu ve bildirim eşiğini tanımlayabilmelidir. İlk örnek hidrofor; aynı yaklaşım havalandırma motoru, kat kaloriferi ve diğer pompa/motor ekipmanlarına genişletilebilir. Bu henüz uygulanacak aktif görev değil, uzun vadeli ürün fikridir.
