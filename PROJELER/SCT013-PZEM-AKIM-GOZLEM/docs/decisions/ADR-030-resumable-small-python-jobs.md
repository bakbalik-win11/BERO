# ADR-030 — Küçük, bağımsız ve kaldığı yerden devam edebilen Python görevleri

- **Durum:** KABUL EDİLDİ
- **Tarih:** 2026-11-06
- **Kapsam:** BERO Python-1, Python-2 ve bunların alt işlem adımları
- **İlgili karar:** [ADR-029 — Taşınabilir SSD çalışma ortamı](ADR-029-portable-ssd-python-runtime.md)
- **İlgili görev:** [T007 — Home Assistant verisini PC'ye aktarma ve Python başlangıcı](../../tasks/T007-python-architecture.md)

## Bağlam

BERO veri işleme hattı tek ve uzun süre çalışan, çok sayıda işi tek seferde yapan kırılgan bir Python programına dönüşmemelidir. Bir adımda hata, kilitlenme, işletim sistemi/uygulama kapanması veya bilgisayarın yeniden başlaması bütün hattı durdurmamalı; daha önce başarıyla işlenmiş veri ve sonuçlar kaybolmamalıdır.

## Karar

1. **İşler küçük ve bağımsız görevlere bölünür.** Her Python görevi tek, açık bir sorumluluğa ve tanımlı girdi/çıktıya sahip olur. Bir görevin başarısızlığı diğer bağımsız görevlerin tamamlanmış çıktılarını geçersiz kılmaz.
2. **İşlem adımları yeniden başlatılabilir olur.** Program kapanır veya hata verirse, yeniden çalıştırıldığında daha önce başarıyla tamamlanmış işleri tanıyıp gereksiz yere baştan işlememeli; kaldığı yerden veya son güvenli kontrol noktasından devam edebilmelidir.
3. **İşlenmiş veri kaybolmaz.** Kaynak RAW dosyalar değiştirilmez. Her görev çıktısını ayrı, sürümlenebilir/tanımlanabilir türetilmiş dosya veya veri kümesi olarak üretir. Başarısız bir görev kaynak girdiyi veya önceki geçerli çıktıyı silmez.
4. **Yarım çıktı geçerli sonuç gibi sunulmaz.** Görev çıktısı önce geçici bir dosyaya/konuma yazılır; yazma ve doğrulama başarıyla bitince nihai çıktı olarak yayımlanır. Kesinti sırasında oluşan yarım çıktı tamamlanmış çıktı olarak kabul edilmez. Uygun dosya sistemi desteğiyle atomik yeniden adlandırma kullanılacaktır.
5. **Durum ve kontrol noktaları kalıcıdır.** Her görev; girdi kimliği/hash'i, görev adı ve sürümü, başlama/bitirme zamanı, durum, çıktı konumu/hash'i ve hata bilgisini SSD'deki işlem kayıtlarına yazar. Başarıyla tamamlanan adımların checkpoint bilgisi yeniden başlatmada kullanılabilir.
6. **Tekrar çalıştırma güvenlidir (idempotent tasarım).** Aynı girdi aynı görev sürümüyle yeniden işlendiğinde yinelenen arşiv veya çakışan çıktı üretmemeli; var olan sonucu doğrulamalı ya da yeni sürümü açıkça ayrı üretmelidir. Kaynak verinin üzerine yazılmaz.
7. **Hata izolasyonu uygulanır.** Bir dosyanın bozuk olması veya tek bir analiz görevinin kilitlenmesi diğer dosyaların ve görevlerin ilerlemesini engellememelidir. Hatalı girdi kaybolmadan hata/karantina alanında tutulur; hata nedeni loglanır.
8. **Görev akışı yönetilebilir olur.** Küçük görevleri sıraya koyan hafif bir çalıştırıcı/orkestrasyon katmanı olabilir; bu katman görevlerin iç mantığını tek bir büyük programa dönüştürmez. Bir görevin çıktısı sonraki görevin girdisi olarak açıkça tanımlanır.
9. **Kalıcı durum ve sonuç SSD'dedir.** ADR-029 uyarınca kod, veri, görev durumu, checkpoint, log ve nihai çıktılar SSD üzerinde tutulur. Performans için RAM veya yerel geçici alan kullanılabilir; kesinti sonrasında gerekli işi yeniden kurmaya yetecek kalıcı durum SSD'de bulunur.

## Uygulama ilkeleri

- Her görev küçük tutulur; örneğin dosya keşfi, CSV doğrulama, hash/tekrar kontrolü, ham arşivleme, veri inceleme, paket bütünlüğü kontrolü, SCT kararlı alan analizi, PZEM kararlı alan analizi, örtüşme/etiket üretimi ve raporlama ayrı görevler olarak ele alınabilir. Bu liste görev sınırlarını tasarlamak için örnektir; nihai görev listesi uygulama sırasında netleştirilir.
- Görevler arası veri sözleşmeleri ve çıktı şemaları açıkça tanımlanır.
- Bir görevin başarı ölçütü yalnızca süreç kodunun sıfırla kapanması değildir; çıktı bütünlüğü ve beklenen kayıtların varlığı kontrol edilir.
- Hata, zaman aşımı veya kullanıcı tarafından durdurma durumunda son başarılı checkpoint korunur.
- Kaynak ve önceki başarılı sonuçlar otomatik temizleme/yeniden deneme sırasında silinmez.
- Gerçek dosya boyutları ve iş yükleri görülmeden paralellik, zaman aşımı veya yeniden deneme sayısı gibi sayısal değerler sabitlenmez.

## Kabul / doğrulama sınırı

Bu ADR mimari kararıdır. Henüz görev çalıştırıcısı, checkpoint mekanizması, atomik çıktı akışı veya hata/kilitlenme kurtarma testi uygulanmış değildir. Bunlar T007 kapsamındaki Python uygulamasında tasarlanıp gerçek örnek dosyalarla doğrulanacaktır.
