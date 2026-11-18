# BERO — Cihaz Davranışını Öğrenme ve Akım Tabanlı Tahmin Fikri

**Durum:** Fikir / araştırma yönü. Henüz deney planı, doğrulanmış yöntem veya ürün kararı değildir.

## Fikir

İki eş donanımlı veri toplama modülüyle farklı ev cihazlarının uzun süreli ses ve titreşim kayıtları alınması; bu kayıtların harici PC'de Python kullanılarak işlenmesi, öğrenme ve tahmin deneylerinde kullanılması.

## Modüller

- **Modül 4 — Çamaşır makinesi:** Mikrofon ve titreşim verisiyle uzun süreli kayıt.
- **Modül 5 — Bulaşık makinesi:** Modül 4'ün ikizi; mikrofon ve titreşimle uzun süreli kayıt.
- ESP'ler veri toplama, zaman damgası ve dosyaya yazma görevlerini yürütür. Home Assistant geçmişi kayıt kaynağı olarak kullanılmak zorunda değildir.
- Öğrenme, veri analizi, model geliştirme, tahmin ve doğrulama harici PC'de Python ile yapılır.

## Araştırma hedefi

Ses ve titreşim gibi daha zengin sensör verilerinden cihaz davranış örüntülerini öğrenmek; daha sonra yalnızca SCT/akım verisinin bu davranışları tanımaya veya durum tahmin etmeye ne ölçüde yeterli olduğunu araştırmak.

## Modül 6 — BERO ana ev panosu fikri

Modül 6, yalnızca SCT/akım verisi kullanarak davranış gözlemi, öğrenilmiş örüntülerden sapma tespiti veya durum tahmini yapabilecek bir ESP tabanlı saha uygulaması adayıdır.

Modül 4 ve 5'teki ses/titreşim kayıtları eğitim ve araştırma verisi olarak düşünülür. Modül 6'nın doğrudan mikrofon veya titreşim sensörüne sahip olması öngörülmüyor; hedef akım verisiyle çalışmaktır.

## Önerilen araştırma akışı

1. Modül 4 ve 5 ile uzun süreli ses/titreşim verisi toplamak.
2. Kayıtları PC/Python ortamında düzenlemek ve incelemek.
3. Cihaz çalışma davranışlarını ve olası aşamaları tanımlamak.
4. Öğrenme ve tahmin yöntemlerini veriler üzerinde denemek.
5. Akım verisinin tek başına ne kadar bilgi taşıyabileceğini araştırmak.
6. Sonuçları doğrulamadan Modül 6'ya aktarılabilir kabul etmemek.

## Sınırlar

- Bu fikir henüz arıza teşhisi veya güvenilir arıza tahmini iddiası değildir.
- Modül 4/5 ve Modül 6 arasında veri/öğrenme aktarımının mümkün olup olmadığı deneylerle gösterilmelidir.
- Sensör seçimi, örnekleme hızı, dosya biçimi, model türü ve alarm mantığı henüz belirlenmemiştir.
- Bu kayıt bir fikir notudur; kesin mimari veya uygulama kararı içermez.
