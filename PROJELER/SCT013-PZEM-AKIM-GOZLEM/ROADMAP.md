# Güncel yol haritası

## Şu anki iş

BERO akım gözlem alt projesinde şu an tek odak, masaüstündeki **Modül 4 (ESP32D2 + ADS1115 + SCT)** ölçüm düzeneğidir.

İstenen akım aralığında ölçüm alabildiğimizi gösteren önceki deney kayıtları mevcut. Bu, masaüstü ölçüm zincirinin sonraki kullanım için yeterli olup olmadığını değerlendirmemize imkân veriyor; bütün koşulların veya nihai kurulumun doğrulandığı anlamına gelmiyor.

## Sıra

1. Modül 4'te bias'lı ve bias'sız ölçümü karşılaştır.
2. İki bağlantı yapısının sinyalini osiloskopta birlikte incele.
3. Gözlemlere dayanarak bias gerekli mi karar ver.
4. Bias gerekiyorsa PREBERO Modül 5/6/7 için bias besleme seçeneklerini karşılaştır:
   - ESP'nin beslemesinden bias üretmek.
   - Modül 1'deki trafo/güç kutusu yapısının ikizlerini üretmek.
5. Ölçüm zinciri yeterliyse PREBERO dönemindeki saha gözlemlerine geç.

## Henüz karara bağlanmayanlar

- Bias'ın gerekli olup olmadığı.
- Bias gerekiyorsa hangi besleme mimarisinin kullanılacağı.
- PREBERO modüllerinin ayrıntılı donanım/bağlantı tasarımı.

Bu başlıklar deney ve inceleme yapılmadan karara bağlanmış sayılmaz.

## PREBERO kapsamı

- **Modül 5:** Çamaşır makinesi gözlemi.
- **Modül 6:** Bulaşık makinesi gözlemi.
- **Modül 7:** Ana hat + PZEM gözlemi.

PREBERO, BERO'nun kurulacağı eve taşınma gerçekleşene kadar Sarıyer'deki mevcut evde yürütülecek hazırlık ve veri toplama dönemidir. Üç modül de PREBERO kapsamındadır.

## Tarihsel kayıtlar

Bu yol haritasının önceki sürümlerinde yer alan E19/E20/E21/E22/E23/E24 ve T006/T007/T008/T009/T010 planları, kendi tarihleri ve sonuçlarıyla depoda korunur. Eski planlar güncel aktif iş sırası olarak okunmamalıdır. Ayrıntılı karar: [ADR-034](docs/decisions/ADR-034-module4-bias-comparison-and-prebero-bias-supply.md).
