# Güncel yol haritası

## Ana mimari karar

**PREBERO Modül 5/6/7'den önce Modül 4 tasarlanacak ve imal edilecek.** Modül 4, masaüstünde geçici olarak çalışan ESP32D2 + ADS1115 + SCT düzeneğinin kalıcı, sabit ve tekrarlanabilir donanım hâline getirilmiş sürümü olacaktır. PREBERO modüllerinin akım ölçüm yapısı için referans oluşturacaktır.

Mevcut masaüstü düzenek çalışılan/deney yapılan prototiptir; imal edilmiş nihai Modül 4 değildir.

## Güncel çalışma sırası

1. **ADS1115 hobi düzeyinde teknik raporu:** Entegrenin çalışma mantığı, giriş türleri, 16 bit, PGA, örnekleme hızı, besleme ve giriş gerilimi sınırları. BERO/SCT kullanımı için gereken bilgiyle sınırlı.
2. **Masaüstü bağlantı incelemesi:** SCT, ön uç/burden, AIN0/AIN1, ADS1115 beslemesi ve yazılım ayarlarını gerçek bağlantı üzerinden belirle.
3. **Biaslı/bias'sız karşılaştırma:** Ölçüm koşullarını ve logları kaydet.
4. **Osiloskop gözlemi:** Bias'sız ve bias'lı sinyal yapılarını güvenli düşük gerilim tarafında gözlemle; girişlerin GND'ye göre ve diferansiyel davranışını incele.
5. **Modül 4 tasarım kararı:** Bias, besleme, bağlantılar, kablolama, konektörler ve fiziksel yerleşimi kanıta göre belirle.
6. **Modül 4 imalatı ve doğrulaması:** Geçici masaüstü prototipinden bağımsız, sabit modülü kur ve gerçek donanımda test et.
7. **PREBERO Modül 5/6/7:** Modül 4 kabul kontrollerinden sonra çamaşır, bulaşık ve ana hat + PZEM modüllerine geç.

## Açık kararlar

- Bias gerekli mi?
- Bias gerekiyorsa Modül 5/6/7 için ESP beslemesinden bias mı, Modül 1'in ikiz bias kutuları mı?
- Modül 4'ün nihai bağlantı ve fiziksel yerleşim ayrıntıları.

Bu kararlar rapor, gerçek bağlantı incelemesi ve deney kanıtı olmadan verilmiş sayılmaz.

## Kapsam düzeyi

Bu bir hobi/araştırma projesidir. ADS1115'in tüm olası elektriksel karakteristiklerini laboratuvar düzeyinde ölçmek hedeflenmez. BERO'da doğru ve güvenli kullanım için gereken veri sayfası bilgisi, temel hesaplar ve osiloskop gözlemleri yeterlidir. Üreticinin elektriksel sınırları ve güvenlik koşulları ise mutlaka gözetilir.

## PREBERO kapsamı

- **Modül 5:** Çamaşır makinesi gözlemi.
- **Modül 6:** Bulaşık makinesi gözlemi.
- **Modül 7:** Ana hat + PZEM gözlemi.

Üç modülün tamamı PREBERO kapsamındadır. Bu modüllerin imalatına Modül 4 tasarımı ve imalatı doğrulandıktan sonra başlanır.

## Tarihsel kayıtlar

E19/E20/E21/E22/E23/E24 ve T006/T007/T008/T009/T010 kayıtları kendi tarihleri ve sonuçlarıyla korunur. Eski planlar güncel aktif iş sırası olarak okunmamalıdır.

Ayrıntı: [ADR-035 — Modül 4 tasarım kapısı ve PREBERO ön koşulu](docs/decisions/ADR-035-module4-design-gate-before-prebero.md).
