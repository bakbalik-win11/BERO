# Oda İçi BERO Akım Gözlem Modülü — Fikir Kaydı

**Durum:** FİKİR / TASARIM ADAYI — prototip, devre veya ürün doğrulaması değildir.  
**Tarih:** 2026-11-13

## Amaç

BERO'nun akım gözlem kabiliyetini oda veya priz bazında çoğaltılabilir, küçük modüllere dönüştürmek. Her modül, bağlı olduğu hattın elektriksel davranışını Home Assistant/BERO'ya aktarır. Hedef yalnızca anlık akım göstermek değil, hattın ve bağlı cihazların zaman içindeki yük davranışını tanımaktır.

## Önerilen modül fikri

- **İşlemci:** Mini ESP32 kartı.
- **Ölçüm ön ucu:** ADS1115 ADC.
- **Akım sensörü:** SCT akım trafosu; sensörün modüle sökülüp takılabilmesi için jack bağlantısı düşünülüyor.
- **Muhafaza / kullanım biçimi:** Küçük oda içi modül. Bu elektroniklerin fiziksel olarak üçlü priz gövdesine sığabilecek kadar kompakt olması olası bir ürünleşme yönü olarak değerlendiriliyor.
- **Veri yolu:** İlk prototipte mevcut ESP/Home Assistant veri akışı; BERO'nun uzun vadeli haberleşme mimarisi ayrıca geçerlidir.

## Üçlü priz biçiminde olası uygulama

Üçlü priz gövdesine entegre bir BERO modülü veya BERO gözlem modüllü üçlü priz fikri ortaya atıldı. Bu biçimde her çıkışın ayrı ayrı mı, yoksa priz grubunun toplam akımının mı gözleneceği henüz kararlaştırılmadı. Ayrı çıkış gözlemi, her çıkışa ait iletkenin uygun CT yerleşimine fiziksel olarak erişilebilmesini gerektirir; yalnızca tek bir ortak CT ile üç çıkışın tüketimleri birbirinden ayrılamaz.

Alternatif olarak modül, üçlü prizden bağımsız küçük bir kutuda bulunabilir ve harici SCT sensörü jack üzerinden bağlanabilir. Bu, ilk prototip için daha esnek bir mekanik yaklaşım adayıdır; karar verilmiş değildir.

## Kullanım senaryoları

- TV / eğlence hattının bekleme ve çalışma davranışını ayırt etmek.
- Telefon şarj hattında şarj, dolum sonrası ve boşta bekleme davranışlarını incelemek.
- Oda bazında aydınlatma ve diğer cihazların çalışma profillerini izlemek.
- Hat bazında öğrenilen davranışlara dayanarak ileride otomasyon kararları üretmek.

Hatlar aynı eşikle veya aynı davranış modeliyle değerlendirilmek zorunda değildir. Her hattın normal tabanı ve cihaz karakteristiği kendi verisinden çıkarılmalıdır. 0,005 A (5 mA) altını sıfır kabul etme konusu bu görüşmede kullanım/işletim eşiği olarak tartışılmıştır; bütün hatlar için nihai ve değişmez mimari kural olarak tanımlanmamıştır.

## Açık tasarım soruları

1. Bir modül tek SCT mi, iki SCT mi destekleyecek?
2. ADS1115 kanalları ve SCT giriş jack'larının sayısı ne olacak?
3. Üçlü priz uygulamasında toplam akım mı, her priz çıkışının akımı mı izlenecek?
4. Modülün beslemesi, izolasyonu, koruması, sıcaklık yönetimi ve muhafaza ölçüleri nasıl çözülecek?
5. SCT jack pin dizilimi, giriş koruması ve yanlış bağlantı önlemleri nasıl tanımlanacak?
6. Modüller arası veri aktarımı uzun vadeli BERO haberleşme omurgasına nasıl bağlanacak?

## Güvenlik ve doğrulama sınırı

Üçlü priz içine şebeke gerilimiyle çalışan elektronik yerleştirmek, yalnızca kartların fiziksel olarak sığmasıyla güvenli hâle gelmez. İzolasyon mesafeleri, yalıtım sınıfı, sigorta/koruma, kablo kesitleri, ısınma, yangın muhafazası, mekanik dayanım ve ilgili elektrik güvenliği standartları tasarlanıp doğrulanmalıdır. Şebeke tarafı tasarımı ve montajı yetkin kişilerce yapılmalıdır. Bu fikir kaydı bir bağlantı şeması, üretim talimatı veya güvenli ürün onayı değildir.

## Kanıt / kaynak ayrımı

- **KULLANICI FİKRİ:** Mini ESP32 + ADS1115 + jack ile takılan SCT sensörlü küçük oda içi modül; elektroniklerin üçlü priz gövdesine sığabileceği düşüncesi.
- **TASARIM ÇIKARIMI:** Tek ortak CT üçlü prizin toplam akımını gözleyebilir; çıkışları birbirinden ayırmak için ayrı CT ölçüm noktaları gerekir.
- **HENÜZ DOĞRULANMADI:** Boyut, kanal sayısı, besleme, elektriksel güvenlik, mekanik yerleşim, haberleşme ve gerçek ürün uygulanabilirliği.

## Sonraki adım

Bu fikir, mevcut E21 çamaşır makinesi gözlem görevini değiştirmez. E21 tamamlandıktan veya ayrı bir donanım tasarım işi açıldığında gereksinimler netleştirilip önce düşük gerilimli masaüstü prototip olarak ele alınabilir.
