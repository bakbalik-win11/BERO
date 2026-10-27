# Çalışma Kaydı ve Yeniden Üretilebilirlik Protokolü

Bu protokol, depodaki tüm projeler ve konular için geçerlidir. Amaç yalnızca işi tamamlamak değil; yapılan işi, kanıtını ve nasıl yeniden bulunacağını kalıcı biçimde korumaktır.

## Değişmez öncelik

**Önce yapılan işi doğru yere kaydet ve kaydı doğrula; sonra yeni işe geç.** Kayıt işi erteleniyorsa bunu açıkça belirt. Depoya yazılmamış bir işi kaydedilmiş gibi sunma.

## Testler, sonuçlar, kodlar ve loglar

Her anlamlı test veya deney için, işin niteliğine uygun olarak:

- **Test tanımı/protokolü:** Amaç, tarih, koşullar, donanım, yazılım/firmware sürümü, yapılandırma, adımlar ve kabul ölçütleri.
- **Sonuç:** Ham veri ve ölçümler, beklenen-gerçekleşen karşılaştırması, geçme/kalma veya belirsiz sonuç; yorumları ham veriden ayrı tut.
- **Kod ve yapılandırma:** Gerçekte kullanılan dosya/sürüm ve mümkünse commit SHA; test sonrası değişen kodu testte kullanılan kodla karıştırma.
- **Loglar:** Zaman damgası, komut/işlem, ilgili çıktı ve hata mesajları; bağlamı yeniden kurmaya yetecek bilgiler.
- **Veri ve grafikler:** Kaynak veriyi koru; türetilmiş tablo/grafiğin hangi dosya ve işlemden üretildiğini kaydet.
- **Durum ve bağlantılar:** Proje durum dosyası, görev/deney kaydı ve oturum günlüğünde birbirine giden açık yollar/bağlantılar bulunsun.

Her proje için tüm maddeler zorunlu dosyalar anlamına gelmez; ilgili olmayanı uydurmak yerine uygulanamaz olarak belirt. Ham veri varsa onu yalnızca grafik veya özetle değiştirme.

## Kanıt durumunu doğru etiketle

Kayıtlarda şu durumları birbirinden ayır:

1. **Planlandı** — henüz çalıştırılmadı.
2. **Çalıştırıldı** — işlem yapıldı, ancak sonuç ayrıca doğrulanmamış olabilir.
3. **Sonuç kaydedildi** — çıktı/veri depoda mevcut.
4. **Doğrulandı** — belirtilen kontrol gerçekten yapıldı; hangi kontrolün yapıldığı yazılı.
5. **Başarısız / belirsiz / engellendi** — sonucu sakla, nedeni ve sonraki adımı belirt.

Kullanıcı beyanı, doküman bilgisi, hesaplama, varsayım ve doğrudan ölçüm aynı kanıt türü gibi sunulmaz. Yapılmamış test, ölçüm, derleme veya CI çalıştırması yapılmış gibi yazılmaz.

## Kayıt ve doğrulama sırası

1. İşe başlamadan önce ilgili depo ve klasörlerde önceki kodu, testleri, sonuçları ve logları ara.
2. Çıktıyı doğru proje/deney/görev konumuna kaydet; dosya adını ve ilişkilendirmeleri anlaşılır seç.
3. İlgili indeks, README, durum kaydı veya oturum günlüğünü güncelle ki dosya sonradan bulunabilsin.
4. Değişiklikten sonra depodaki dosyayı yeniden oku; içeriği, bağlantıları ve commit'i doğrula.
5. Son raporda **Uygulandı**, **Doğrulandı**, **Bekliyor/engellendi** ve **Sonraki tek adım** başlıklarını kullan. Gerçekten kontrol edilmeyen hususları açıkça belirt.

## Bulunabilirlik

Bir iş yalnızca sohbet içinde kalmamalıdır. Sonraki oturumda başka biri veya aynı kullanıcı; ne yapıldığını, hangi kodun kullanıldığını, testin çalışıp çalışmadığını, sonucu ve ilgili log/veriyi depo içinden bulabilmelidir. Her oturumda tek bir oturum günlüğü kaydı ve ilgili kalıcı dosyalara yollar bırakılması tercih edilir.

Bu protokol, projeye özgü talimatların yerine geçmez; onlarla birlikte uygulanır.