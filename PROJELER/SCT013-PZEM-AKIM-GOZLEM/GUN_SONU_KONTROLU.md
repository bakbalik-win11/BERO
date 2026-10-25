# Gün sonu kontrolü — teknik bilgi gerektirmeyen sürüm

**Amaç:** Günün işi gerçekten yapıldı mı, neyin kaldığı doğru kaydedildi mi, bunu birkaç dakika içinde kontrol etmek. Kodları veya ölçüm denklemlerini anlamanız beklenmiyor.

Her günün sonunda aşağıdaki üç kontrolü yapmanız yeterli. Asistan, cevap verirken bu bağlantıları kendisi sağlamalıdır.

## 1. Durum kaydına bakın

[STATUS.md dosyasını açın](STATUS.md).

Şu üç şeyi kontrol edin:
- **Son güncelleme** bugünün tarihi mi? Bugün depoda anlamlı iş yapılmadıysa bunun nedeni açıkça belirtilmiş mi?
- **Aktif faz** ve **sıradaki üç iş** gerçek çalışmayla uyumlu mu?
- Yapılmadığı halde tamamlandı denilen deney veya kalibrasyon var mı?

Teknik içeriğin doğruluğunu siz belirlemek zorunda değilsiniz. Şüpheli bir cümleyi görünce “Bu hangi kanıtla doğrulandı?” diye sorabilirsiniz.

## 2. Oturum günlüğüne bakın

[HISTORY/SESSION_LOG.md dosyasını açın](HISTORY/SESSION_LOG.md) ve en üstteki/en yeni tarihli oturum bölümünü bulun.

Şu alanların var olduğunu kontrol edin:
- **Durum**
- **Hedef ve kabul ölçütü**
- **Yapılan**
- **Doğrulama**
- **Açık kalanlar**
- **Sonraki adım**
- **Kanıt**

En önemli iki soru:
1. “Yapılan” bölümündeki işler gerçekten yapılmış mı, yoksa yalnızca önerilmiş mi?
2. “Doğrulama” bölümünde doğrudan açabileceğiniz bağlantı veya açıkça belirtilmiş test sonucu var mı?

Eski bir kayıt güncel gerçekle çelişiyorsa sessizce üstünü kapatmayın. Yeni bir düzeltme kaydıyla neyin eski kaldığı açıklanmalı.

## 3. Değişiklik varsa GitHub durumunu kontrol edin

Asistandan günün PR/commit ve test bağlantılarını isteyin. Ardından ilgili bağlantıyı açın.

- **PR açık:** Değişiklik önerilmiş ama henüz ana dala alınmamış olabilir. Asistan “main'e eklendi” dememeli.
- **PR birleştirildi:** Değişikliğin ana dalda olduğunu proje dosyasını açarak doğrulayın.
- **Action / kontrol başarılı:** Yalnızca o otomatik kontrolün geçtiği anlamına gelir; bütün teknik iddiaların doğru olduğunu kanıtlamaz.
- **Action başarısız veya hiç çalışmamış:** Bu durum gizlenmemeli; iş doğrulandı olarak raporlanmamalı.

Bugün depo değişikliği yapılmadıysa sırf günlük dolsun diye hayali commit veya sonuç üretilmemeli. Günlüğe neden değişiklik yapılmadığı ve bir sonraki adım yazılabilir.

## Günün sonunda asistanın sunması gereken kısa rapor

Asistan şu dört satırı net biçimde vermeli:

1. **Uygulandı:** Hedef ortamda gerçekten değişenler.
2. **Doğrulandı:** Kontrol edilen sonuçlar ve doğrudan bağlantılar.
3. **Bekliyor / engellendi:** Yapılmayan işler ve nedeni.
4. **Sonraki tek adım:** Bir sonraki oturumda başlayacağımız en küçük iş.

Bu dört satırın dayanağı yoksa “tamamlandı” kabul etmeyin. Teknik ayrıntıyı kendiniz çözmek zorunda değilsiniz; asistanın kanıt göstermesini isteyin.

## Durma işareti

Bir kayıtla GitHub'daki gerçek durum çelişiyorsa, sonuç verilmiş ama veri/kanıt yoksa veya PR birleştirilmeden “main'de” deniyorsa, kontrolü durdurun ve şu cümleyi kullanın:

> **Kapanışı durdur. Kayıt ile gerçek durumu karşılaştır, farkı düzelt ve doğrulamadan tamamlandı deme.**

Bu bir başarısızlık değil; yöntemin hatayı yakaladığı anlamına gelir.
