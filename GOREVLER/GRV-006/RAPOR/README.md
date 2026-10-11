# GRV-006 — Python Veri Kümesi ve Home Assistant Üzerinden Veri Aktarım Zinciri

**Durum:** Açık — görev tanımı oluşturuldu; kodlama ve deney henüz yapılmadı.  
**Açılış tarihi:** 2026-10-11  
**Öncelik:** Önce veri dosyası üretme/okuma zincirini kanıtlamak; SCT ölçüm doğruluğunu bu görevin ilk kabul ölçütü yapmamak.

## 1. Amaç

Copilot ile Python'a verilecek bir veri kümesini üreten kodu hazırlamak, çıktıyı Home Assistant (HA) tarafında kaydetmek ve verinin HA'dan Mac'e taşınmasını uçtan uca doğrulamak. Mac'te veri işlenecek, tekrar okunacak, sonuç bağımsız olarak kontrol edilecek ve iyileştirilmiş sonuç yeniden işlenerek karşılaştırılacaktır.

Bu görev, önceki GRV-005 çalışmalarının yerine geçmez ve onların kayıtlarını değiştirmez. Yeni, ayrı bir görevdir. GRV-005'teki paket kontrolü veya QC öz-testinin geçmesi bu görevin başarı kanıtı sayılmaz.

## 2. Kullanıcının tarif ettiği akış

1. **Veri üretimi:** Copilot ile Python'a verilecek açık, küçük ve tanımlı bir data seti üret.
2. **Üretici kod:** Veri kümesini belirli bir şemayla dosyaya/çıktıya yazan kodu oluştur.
3. **HA kaydı:** Üretilen veriyi Home Assistant üzerinde sakla. Kaydedilen içeriğin gerçekten mevcut olduğunu, kaydın kendisini okuyarak doğrula.
4. **HA → Mac aktarımı:** Sonraki adımda veriyi HA'dan Mac'e al; Mac'e başarıyla kaydedilip okunduğu doğrulanmadan HA'daki kopyayı silme. Başarılı doğrulama sonrasında, görev kapsamı gereği HA'daki geçici kopyayı sil ve silindiğini ayrıca doğrula.
5. **Mac okuma testi:** Mac'teki dosyayı yeniden aç; şema, satır/sütun sayısı, veri türleri ve beklenen değerleri doğrula.
6. **Python işlemesi:** Veriyi Python ile işle. İşleme öncesi ve sonrası veriyi ayrı dosya/çıktı olarak koru; kaynak verinin üzerine yazma.
7. **Bağımsız teyit:** En az bir beklenen sonuç, ana işleme fonksiyonundan bağımsız bir yöntemle elle hesaplanabilir/denetlenebilir olmalı.
8. **İyileştirme turu:** İlk sonuç ve bağımsız kontrol karşılaştırıldıktan sonra gerekliyse tek bir somut iyileştirme yap. Aynı veri üzerinde tekrar çalıştır ve farkı ölç.
9. **Durdurma kararı:** İyileştirme ölçülebilir bir fayda sağlamıyorsa yeni döngü açma. Ek döngü yalnızca açık bir hata, karşılanmamış kabul ölçütü veya ölçülebilir iyileştirme hedefi varsa gerekçelendirilir.

## 3. İlk veri kümesi için sınırlar

- İlk deneme küçük, sentetik ve deterministik bir veri kümesi olabilir; donanım ölçümü gerektirmez.
- Şema, birim, veri türleri, beklenen satır sayısı ve beklenen işlem sonucu görev raporunda açıkça yazılmalıdır.
- Ham veri, işlenmiş veri ve doğrulama sonucu birbirinden ayrı tutulmalıdır.
- Zaman damgası veya sıra numarası gibi alanlar gerekiyorsa biçimleri sabitlenmelidir.
- Veri kaynağı, aktarım yönü ve dosya yolu her aşamada görünür olmalıdır.
- Bir test aracının kendi öz-testi, gerçek dosyanın yazılıp tekrar okunduğunun kanıtı değildir.

## 4. Kabul ölçütleri

- [ ] Üretici kod çalıştırılmış ve gerçek bir çıktı dosyası/HA kaydı oluşmuştur.
- [ ] Oluşan veri, aynı kaynaktan yeniden okunmuş; şema ve kayıt sayısı doğrulanmıştır.
- [ ] HA'da kayıt bulunduğu doğrudan okunarak gösterilmiştir.
- [ ] Veri HA'dan Mac'e aktarılmış, Mac'te yeniden açılmış ve içerik eşleşmesi doğrulanmıştır.
- [ ] Mac kopyası doğrulanmadan HA kopyası silinmemiştir.
- [ ] Mac'te dosya okuma, Python işleme ve işlenmiş sonucu yeniden okuma testleri geçmiştir.
- [ ] En az bir işlenmiş sonuç bağımsız olarak doğrulanmıştır.
- [ ] İlk sonuç ile varsa iyileştirilmiş sonuç ölçülebilir biçimde karşılaştırılmıştır.
- [ ] Sonuçlar, komutlar ve dosyalar raporlanmıştır; yalnızca öz-test çıktısı başarı kanıtı olarak sunulmamıştır.

## 5. Görev sırası ve sınırlar

### GRV-006-01 — Veri kümesi ve üretici kod
Copilot için açık görev tanımı hazırla; küçük veri kümesini ve beklenen sonuçları belirle; kodun dosya/çıktı üretmesini sağla. Önce yerel yazma ve aynı dosyayı okuma kanıtlanır. Ardından aynı veri HA'ya kaydedilir ve HA'dan okunarak doğrulanır.

### GRV-006-02 — HA'dan Mac'e taşıma ve temizleme
HA'daki kaydı Mac'e aktar. Mac dosyasını yeniden açıp içerik eşleşmesini doğrula. Ancak bu doğrulamadan sonra HA'daki geçici kaydı sil ve silinme durumunu kontrol et.

### GRV-006-03 — Mac'te işleme ve bağımsız teyit
Mac'te veriyi Python ile işle; sonucu ayrı çıktı olarak kaydet ve tekrar oku. Beklenen sonucu bağımsız hesapla/kontrol et.

### GRV-006-04 — Tek iyileştirme ve durdurma kararı
Gerekliyse bir iyileştirme uygula ve önce/sonra sonuçlarını kıyasla. Ek döngü gerekip gerekmediğini kanıta göre kararlaştır; sırf süreci sürdürmek için yeni kontrol üretme.

Alt görevler ayrı kanıt ve rapor gerektirebilir; fakat sırf klasör/rapor üretmek ilerleme sayılmaz. İlk öncelik çalışan veri akışıdır.

## 6. Çalışma ilkeleri

- Kullanıcı test elemanı değildir; gereksiz komutları ve sonucu olmayan teşhis döngülerini kullanıcıya yükleme.
- Bir sonraki adıma geçmeden önce mevcut adımın somut çıktısını göster.
- Hata durumunda yeni testler eklemeden önce mevcut dosya, kod ve gerçek çıktı incelenir.
- Aynı testi gerekçesiz tekrarlama; önceki kanıtı yeniden kullan.
- Eski görev ve deneyim kayıtlarının üzerine yazma. Bu görev ayrı tutulur.
- Donanım/SCT arızası varsayma; bu görev öncelikle veri üretme, taşıma, okuma ve işleme zincirini sınar.
- Durum etiketleri: **Tanımlandı**, **Çalışılıyor**, **Kanıtlandı**, **Engellendi**. Kodun yazılmış olması tek başına **Kanıtlandı** anlamına gelmez.

## 7. İlk yapılacak somut iş

Copilot'a verilecek üretici kod görevini, veri şemasını ve bağımsız beklenen sonucu tek bir küçük örnek üzerinde netleştir. İlk kanıt: dosyanın gerçekten yazılması, aynı dosyanın tekrar açılması ve içerik/sonuç doğrulamasıdır. Bu kanıt olmadan paket kontrolü, ek test altyapısı veya yeni döngü ekleme.

## 8. Başlangıç durumu

Bu dosya yalnızca görev tanımıdır. Henüz kod üretildiği, HA kaydı oluşturulduğu, Mac'e aktarım yapıldığı veya herhangi bir testin geçtiği iddia edilmemektedir.
