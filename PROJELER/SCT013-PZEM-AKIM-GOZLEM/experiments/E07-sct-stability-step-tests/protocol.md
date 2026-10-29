# E07 — SCT kararlılık gözlemi: basamaklı yükler ve örnekleme hızı

## Amaç
Sadece SCT örneklerinden kararlı bölgeleri belirlemek için hangi istatistiklerin işe yaradığını gözlemlemek. Bu deneyin amacı PZEM ile alan eşleştirmek değildir.

## Temel ilke
> Henüz kararlılık eşiği veya gereken pencere sayısı belirlemeyelim. Bunlar deney sonuçlarından çıkarmamız gereken kararlar; baştan varsaymamız gereken değerler değil.

Deney, kararlılık eşiği veya gerekli ardışık pencere sayısı için önceden değer dayatmaz. Sonuçlar bilgisayarda/Python'da incelenir; yeni deney ancak mevcut verinin cevaplayamadığı önemli bir soru kalırsa düşünülür. Bu planın sınırı üç turdur; otomatik olarak yeni turlar eklenmez.

## Planlanan düzen
- Öncelikli SCT: SCT013-030 (30 A / 1 V).
- ADC: seçilecek ESP32 kartının dahili ADC'si; kart modeli ve GPIO uygulama öncesinde kaydedilir.
- Her pencere için ilk tasarım varsayımı: 200 ms. Bu süre bu deneyde optimize edilmeyecek.
- Aynı örnek kümesinden hesaplanacak sonuçlar:
  - RMS
  - Peak (bias çıkarılmış sinyalin en büyük mutlak genliği)
  - Peak-to-Peak
  - Ortalama ve standart sapma
  - Min/max, örnek sayısı ve ölçülen gerçek örnekleme hızı
- İstatistikler aynı pencere kimliği ve zaman aralığıyla tek kayıtta tutulur. Sürekli ham ADC arşivi oluşturulmaz; gerekiyorsa yalnız olay çevresinde kısa kesit saklanır.

## Üç tur ve basamaklar
Her turda aynı dört durum sırayla gözlemlenir:
1. Boşta: SCT bağlı, ölçülen hattan akım geçmiyor.
2. 100 W akkor ampul.
3. 150 W akkor ampul.
4. 8,5 W LED ampul.

Örnekleme hızı turdan tura basamaklı değişir; başlangıç planı:
- Tur 1: 1 kS/s hedef
- Tur 2: 2 kS/s hedef
- Tur 3: 2,5 kS/s hedef

Bunlar hedef ayarlardır; ölçülen gerçek hız ve sapma her kayıtta ayrı tutulur. Her yük basamağında geçiş ve ardından oluşan sinyal davranışı kaydedilir. Yük basamaklarının bekleme süresi ve analizde kullanılacak kararlı aralık, ölçüm verisi görülmeden kesin kararlılık kuralı olarak sabitlenmez. Güvenli ve uygulanabilir kayıt süresi deney sırasında metadata'ya yazılır.

## İncelenecek sorular
- RMS, Peak, Peak-to-Peak ve diğer istatistikler basamak geçişlerinde ve sabit görünen bölümlerde nasıl değişiyor?
- Hangi istatistikler gürültü sıçramalarına veya dalga şekli değişimlerine daha duyarlı?
- 1, 2 ve 2,5 kS/s hedefleri arasında SCT kararlılık bölgelerini ayırt etmede gözle görülür bir fark var mı?
- Üç turdaki benzer yük durumları tekrarlanabilir sonuç veriyor mu?

Korelasyon, dağılım, ardışık pencere farkları ve görselleştirme Python'da yapılır. Korelasyon tek başına doğruluk veya kararlılık kanıtı sayılmaz.

## Sınırlar
- Bu deney PZEM eşleştirmesi, PF hesabı, FFT/THD veya laboratuvar düzeyinde doğruluk testi değildir.
- Peak/RMS oranı PF olarak yorumlanmaz.
- Kararlılık eşiği ve gerekli ardışık pencere sayısı sonuçlar görülmeden seçilmez.
- Üç tur tamamlandığında mevcut veri değerlendirilir; yeni tur yalnız somut, cevaplanmamış bir soru varsa önerilir.
- Şebeke yükleriyle çalışma yalnız güvenlik kontrolü ve uygun muhafaza/koruma koşulları altında yapılır.

## Kabul ölçütü
Üç tur ve her turdaki dört durum için yapılandırma ve zaman bilgisi kaydedilmiş olmalı; gerçek örnekleme hızı, pencere istatistikleri ve yük basamakları ayırt edilebilir olmalı. Python incelemesi, SCT kararlılık ölçütü seçmek için eldeki verinin yeterli olup olmadığını ve bir sonraki kararın ne olduğunu açıkça raporlamalı.

## Durum
PLANLANDI. Donanım kurulumu, firmware ve ölçüm henüz yapılmadı.
