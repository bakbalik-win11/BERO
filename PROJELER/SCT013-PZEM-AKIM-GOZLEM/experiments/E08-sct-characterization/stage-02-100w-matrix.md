# Aşama 2 — 100 W akkor ampul karşılaştırma matrisi

Neden: 100 W akkor ampul, yük altında ilk kontrollü karşılaştırmadır. Yük sabitken örnekleme hızı ve kablo turu etkisini incelememizi sağlar.

Matris: 1, 2 ve 4 kablo turunun her birinde 1, 2 ve 2,5 kS/s hedeflerini dene. Her penceredeki aynı örnek kümesinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesapla. Ortalama, standart sapma, min/max, örnek sayısı ve gerçek hızı da kaydet.

Sorular: Hız değişince aynı yöntemin pencere değişkenliği değişiyor mu? Tur sayısı artınca sonuçlar nasıl değişiyor? Tur etkisi farklı hızlarda aynı mı? Yöntemlerin her biri tekrarlı pencerelerde ne kadar tutarlı? Ham sonuçları yöntemler arasında doğrudan sıralama; her yöntemin kendi değişkenliğini karşılaştır.


## Test durumu — 2026-10-30

<badge>TEST AÇILDI — HAZIRLIK</badge>

### HEDEF
100 W akkor yük altında SCT013-030 çıkışının ADC örnek davranışını ölçmek; tur sayısı ve örnekleme hızı etkilerini karşılaştırmak.

### Donanım ve bağlantı
- Sensör: SCT013-030 (30 A / 1 V); E00B'deki bias ağı yaklaşımı korunur.
- ADC: ESP32 dahili ADC. Gerçek kart modeli ve pinout test öncesinde doğrulanıp kayda yazılacak.
- CT, ampul devresinin yalnızca tek yalıtılmış akım taşıyan iletkenini çevrelemelidir; faz ve nötr birlikte CT içinden geçirilmez. Tur sayısı, aynı tek iletkenin CT penceresinden kaç kez geçirildiğidir.
- CT sekonderini primer akım varken açık devre bırakma; SCT modelinin üretici bağlantı talimatına uy. Şebeke devresi üzerinde bağlantı/yer değiştirme yalnız yetkin kişi tarafından, enerji kesilerek ve uygun muhafaza/koruma ile yapılır.
- ESP32/bias beslemesi ölçülen şebeke hattından ayrı tutulur.

### Deney matrisi
| İletken turu | 1.000 örnek/s | 2.000 örnek/s | 2.500 örnek/s |
|---:|---|---|---|
| 1 | İlk koşul | Planlandı | Planlandı |
| 2 | Planlandı | Planlandı | Planlandı |
| 4 | Planlandı | Planlandı | Planlandı |

- İlk koşul 1 tur × 1.000 örnek/s olarak belirlendi. Her koşulda 100 W akkor yük sabit tutulur.
- Başlangıç pencere uzunluğu 200 ms'dir; optimum olduğu varsayılmaz.
- Aynı pencere örneklerinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanır. Ortalama, standart sapma, minimum, maksimum, örnek sayısı ve gerçekleşen örnekleme hızı da saklanır.
- Her koşul için kayıt süresi ve tekrar sayısı, ilk edinim yazılımı/örnek verisi görüldükten sonra kararlaştırılacak; kararlılık eşiği baştan sabitlenmeyecek.

### Firmware ve veri
Mevcut [E00B firmware'i](../E00B-sct-connected-no-current/firmware/esp32d2-e00b-sct-no-current.yaml) dört kanalı 1 saniyelik aralıkla Home Assistant'a yayımlar; bu yüksek hızlı ADC örneklemesi değildir. E08 için ayrı firmware hazırlanacaktır. Firmware; örnekleme hedefini, gerçek örnek sayısını/süreyi ve pencere özetlerini raporlamalıdır. YAML/deney planı firmware tarafından otomatik okunmuyorsa ayarlar kod içinde açıkça eşlenmelidir.

### HEDEF / LOG / SONUÇ
- **HEDEF:** 100 W yük altında ilk kontrollü SCT sinyalini almak ve hız/tur matrisine başlamak.
- **LOG:** Test açıldı. İlk koşul 1 tur × 1.000 örnek/s. Firmware henüz hazırlanmadı; derleme, cihaza yükleme, fiziksel test ve log yok.
- **SONUÇ:** Henüz ölçülmedi. Mevcut E00B YAML bu testi gerçekleştirmek için yeterli değil. Sonraki adım E08 yüksek hızlı edinim firmware'ini hazırlamak.
