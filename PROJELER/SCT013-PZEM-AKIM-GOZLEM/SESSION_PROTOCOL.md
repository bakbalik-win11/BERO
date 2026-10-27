# Oturum protokolü: kayıt değil, kanıt

## Amaç
Bu dosya, proje kurallarının sadece yazılı kalmasını değil, her anlamlı depo çalışmasında uygulanıp uygulanmadığının görünür olmasını sağlar. Kullanıcıdan Git ayrıntılarını denetlemesini beklemek yerine, çalışma raporunda denetimin kanıtı gösterilir.

## A. Başlangıç kontrolü
Her anlamlı çalışma oturumunda:
1. GitHub'daki `main` dalının güncel SHA'sını kontrol et.
2. `AGENTS.md`, `STATUS.md`, `ROADMAP.md`, `docs/open-questions.md` ve ilgili görev/deney dosyasını oku.
3. Son `HISTORY/SESSION_LOG.md` girdisiyle mevcut deponun durumunu karşılaştır.
4. Çıktı olarak üç bilgi üret: **mevcut durum**, **bu oturumun hedefi**, **kabul ölçütleri**.
5. Gerekli dosyalara/araçlara erişilemiyorsa başlangıç kontrolü tamamlanmış sayılmaz.
6. Başlangıç raporunda gerçekten okunan dosyaları ve son commit/branch bilgisini kısaca belirt; okunmayan dosyaları açıkça bildir.
7. Daha önce yanıtlanmış bir bilgiyi yeniden sormadan önce ilgili envanter, teknik kayıt, görev, açık sorular ve günlükte ara. Kayıtlar çelişiyorsa varsayım yapmak yerine çelişkiyi çöz.

## B. Uygulama ve doğrulama
- Kapsam dışındaki dosyaları değiştirme.
- Her kabul ölçütünü bir test, diff, dosya içeriği veya dış sistem sonucu ile eşleştir.
- Kaynak taraması ile donanımda ölçüm yapmayı ayır.
- Sentetik örnekleri sentetik olarak işaretle.
- Başarısız testleri düzeltmeden veya istisnasını belgeleyip açıkça bildirmeden işi tamamlandı sayma.
- Dış sisteme yazma yaptıysan, sonrasında aynı konumu yeniden oku ve sonucu doğrula.
- Teknik iddialarda kaynağı görünür tut: kullanıcı beyanı, üretici belgesi, hipotez, hesap ve ölçülmüş sonuç farklı kategorilerdir.
- Kullanıcı tarafından bildirilen bir test/olgu, kullanıcı beyanı olarak kaydedilebilir; bağımsız ölçüm yapılmış gibi etiketlenemez.

## C. Kapatma kontrolü
Her anlamlı depo işi için:
- [ ] Değiştirilen dosyalar/diff yeniden incelendi.
- [ ] Kabul ölçütleri tek tek sonuçlandırıldı.
- [ ] İlgili testler çalıştırıldı; çalıştırılamayan testler isimleriyle belirtildi.
- [ ] `STATUS.md` güncel.
- [ ] Faz/ölçüt değiştiyse `ROADMAP.md` güncel.
- [ ] `HISTORY/SESSION_LOG.md` içinde bu oturuma ait yeni kayıt var.
- [ ] Dal/commit/PR'nin gerçek durumu yeniden okundu.
- [ ] Başlangıçta okunan kaynaklar ve commit/branch, raporda doğrulanabilir biçimde belirtildi.
- [ ] Önceden verilmiş proje bilgileri yeniden sorulmadan önce depodaki kayıtlar kontrol edildi.
- [ ] Kullanıcı beyanı, üretici bilgisi, hipotez, hesap ve ölçüm sonuçlarının etiketleri doğru kullanıldı.
- [ ] Kullanıcıya uygulanan, doğrulanan, bekleyen ve engellenen işler ayrı raporlandı.

Bir kontrol yapılamıyorsa kutuyu tamamlanmış gibi işaretleme. Günlükte engeli ve sonraki somut adımı belirt.

## D. İş bitiş tanımı
- **Hazırlandı:** içerik hazırlanmış, fakat hedef ortama uygulanmamış olabilir.
- **Uygulandı:** hedef ortamda mevcut olduğu gözlemlendi.
- **Doğrulandı:** önceden tanımlı doğrulamalar çalıştı ve sonuçları kaydedildi.
- **Tamamlandı:** bütün kabul koşulları doğrulandı.
- **Engellendi:** erişim/karar/donanım/test eksiği nedeniyle koşul karşılanamadı.

Bir PR açmak, PR'ı birleştirmekle aynı şey değildir. Dosya üretmek, depoya yazmakla aynı şey değildir. JSON'u okumak, şemaya uygun olduğunu test etmekle aynı şey değildir.

## E. Otomatik kontrolün kapsamı ve sınırı
`.github/workflows/sct-pzem-session-close.yml`, bu proje klasörüne dokunan PR'larda `STATUS.md` ve `HISTORY/SESSION_LOG.md` değişikliklerinin bulunmasını ve yeni günlük kaydının gerekli başlıkları taşımasını denetler.

Bu CI kontrolü dosya/düzen disiplinini kontrol eder; bir ölçüm iddiasının doğru olup olmadığını veya her sohbetin bu dosyaları okuduğunu kanıtlayamaz. Bu nedenle başlangıçta dosyaları gerçekten okumak ve sonunda dış sistemi yeniden kontrol etmek hâlâ gereklidir.
