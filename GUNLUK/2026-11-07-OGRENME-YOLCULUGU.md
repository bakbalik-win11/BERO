# 7 Kasım 2026 — Öğrenme yolculuğu için yeni sayfa

## Bugünün konuşmasından kalan

Bugün BERO'nun yanında, merak için sürdürülecek yeni öğrenme alanları üzerinde anlaştık.

Bu çalışmaların amacı para kazanmak, yeni bir kariyer kurmak veya sınav yetiştirmek değil. Emeklilik döneminde zamanı nitelikli değerlendirmek; merak etmek, öğrenmek, denemek ve küçük ilerlemelerden keyif almak.

**Temel ilke: Hedefe giden her küçük adım bir ilerlemedir.**

Bir konuyu bitirmek zorunda değiliz. Bir gün 10 dakika, başka bir gün daha uzun çalışabiliriz. Sıkılırsak konu değiştirir, merak ettiğimiz başka bir alana geçeriz. Başarı ölçümüz hız veya tamamlanan görev sayısı değil; anladığımız, denediğimiz ve keşfettiğimiz küçük şeylerdir.

## BERO devam ediyor

BERO unutulmuyor ve rafa kaldırılmıyor. O bizim uygulama ve keşif atölyemiz olmaya devam edecek.

- Home Assistant merkezli veri toplama ve yönetim yaklaşımı korunacak.
- ESP32/ESPHome düğümleri yerel algılama ve kontrol görevlerini sürdürecek.
- Python ile gerçek sensör verileri okunacak, temizlenecek, arşivlenecek, analiz edilecek ve grafiklerle incelenecek.
- KNIME ve Power BI gibi araçlar zamanla bu verileri farklı biçimlerde anlamlandırmak için kullanılabilecek.
- BERO yalnızca teknik sonuçların değil; denemelerin, hataların, keşiflerin ve öğrenme sürecinin de kaydı olacak.

### SCT düşük akım konusu

SCT ile 0,5 A altındaki alanı zorlamaya şimdilik ara verildi. Bu bir proje başarısızlığı olarak görülmüyor. Gerekirse ileride başka bir sensörle ele alınabilir; birkaç gün sonra yeniden denemek de serbest. Mevcut gözlemler korunacak, fakat bu konu BERO'nun bütün gündemini işgal etmeyecek.

### Python'a geçiş

Bir sonraki uygulamalı adımlardan biri veri Pythonları olacak:

- Home Assistant geçmişinden dışa alınan CSV dosyalarını okumak,
- veriyi doğrulamak ve düzenlemek,
- güvenli biçimde arşivlemek,
- arşivlenmiş veriden analiz ve grafik üretmek.

Veriyi içeri alan/koruyan kodlarla analiz ve eğitim kodları birbirinden ayrılacak. Analiz kodları ham veriyi değiştirmeyecek. İlk hedef büyük bir yapay zekâ modeli değil; gerçek bir dosyayı okuyup anlayabilmek, doğru grafikler çizmek ve veriye doğru soruları sorabilmek.

Grafikler özellikle önemli. SCT/PZEM çalışmalarında zaman serisi, dağılım, histogram, ortalama ve standart sapma gibi görsellerden çok şey öğrendik. Bu öğrenme biçimini sürdüreceğiz: her grafik bir soruya cevap arayacak.

## Yeni öğrenme alanları

Yarın ayrı depoların ana başlıklarını ve başlangıç planlarını açacağız. Bugün yeni depoları oluşturma veya derslere başlama işi yapılmadı; yalnızca yön ve çalışma biçimi üzerinde anlaşıldı.

### 1. IFRS — Finansal raporlama

Amaç, Uluslararası Finansal Raporlama Standartlarını (IFRS) küçük parçalar hâlinde anlamak. Standartların mantığı, muhasebeleştirme, finansal tablo etkileri ve örnek işlemler üzerinden ilerleyeceğiz. IFRS metinlerinin İngilizcesini de okuyacağız; Türkçe açıklama, İngilizce terim ve standart ifadeleri birlikte kullanılacak.

### 2. Python — Programlama ve veri analizi

Sıfırdan veya mevcut bilgiyi yoklayarak küçük adımlarla ilerleyeceğiz. Önce temel Python, sonra dosya okuma, veri düzenleme, grafikler, istatistik ve analiz. Uygulama örnekleri mümkün oldukça BERO'nun gerçek verilerinden seçilecek.

### 3. KNIME — Görsel veri iş akışları

KNIME küçük ve anlaşılır uygulamalarla öğrenilecek. Veri okuma, filtreleme, birleştirme, gruplama, görselleştirme ve zamanla modelleme gibi konulara geçilecek. Depo öncelikle öğrenme planı, denemeler ve notlar için kullanılacak.

### 4. İngilizce — Teknik ve mesleki okuduğunu anlama

Hedef konuşma becerisi değil. Öncelik okuduğunu anlama: temel cümle yapıları, sık kullanılan kelimeler, teknik terimler, yönergeler, dokümantasyon ve sınav sorularını çözümleme. IFRS ve Power BI metinleri de İngilizce okuma pratiğinin parçası olacak. Küçük metinler, kelime notları ve tekrarlarla ilerleyeceğiz.

### 5. Power BI — Analiz ve raporlama ekranları

Amaç yalnızca PL-300 sertifikası değil; finansal ve operasyonel verilerden anlamlı analizler ve kullanışlı ekranlar tasarlayabilmek. PL-300 ileride girilebilecek bir sınav hedefi olarak durabilir; zorunluluk veya takvim baskısı olmayacak.

## Öğrenme alanları birbirini besleyecek

- BERO gerçek veri ve uygulama alanı sağlayacak.
- Python veriyi işlememize ve analiz etmemize yardım edecek.
- KNIME görsel veri akışları kurmayı öğretecek.
- Power BI analizleri etkileşimli raporlara ve ekranlara dönüştürecek.
- İngilizce, IFRS ve teknoloji alanlarındaki kaynakları kendi dilinde okuyabilmemizi sağlayacak.
- IFRS finansal raporlama bilgisini geliştirecek.

Bu alanlar birbirinden kopuk yarışlar değil. Birinde öğrenilen şey diğerinde kullanılabilir.

## Birlikte çalışma biçimi

- Sohbet ederek öğrenme; açıklama, örnek, soru-cevap ve gerektiğinde tekrar.
- Kısa ve anlaşılır oturumlar; sabit günlük hedef yok.
- Sınav, teslim tarihi veya gelir elde etme baskısı yok.
- Bilinmeyen veya tamamlanmamış işler açıkça belirtilecek.
- Öğrenilenler, küçük uygulamalar ve işe yarayan örnekler ilgili depoda saklanacak.
- Depolar öncelikle yol haritası, öğrenme günlüğü, kaynaklar ve ilerleme kaydı olacak; her küçük etkinlik ağır bir prosedüre dönüştürülmeyecek.
- BERO'nun mevcut teknik kayıtları ve kanıtları korunacak; daha kişisel ve okunabilir öğrenme notları bunların yanında yer alacak.

## Yarın için başlangıç

1. BERO'yu unutmadan mevcut durumunu ve Python veri işleme adımını ele almak.
2. IFRS, Python, KNIME, İngilizce ve Power BI için ayrı öğrenme depolarının ana başlıklarını planlamak.
3. Her alanda yalnızca ilk küçük adımı belirlemek; hepsine aynı anda yüklenmemek.

---

**Günün cümlesi**

> Hedefe her küçük adım bir ilerlemedir.

Bu kayıt bir bitiş veya büyük bir taahhüt değil. Merak ederek, acele etmeden sürdürülecek bir öğrenme döneminin başlangıç notudur.
