# ADR-026 — PZEM kararlı-alan eğitimi hedefinin kapatılması ve çamaşır makinesi davranış analizine geçiş

- **Tarih:** 2026-11-13
- **Durum:** KABUL EDİLDİ — kullanıcı kararı
- **Kapsam:** SCT-013 + ADS1115 akım gözlem zincirinin mevcut ayarlarla yük davranışını izleme yaklaşımı

## Bağlam

13 Kasım 2026 oturumunda aynı SCT-013 + ADS1115 ölçüm zinciri; düşük akım yükleri, fanlar, ütü, tost makinesi ve kettle'ın ısı koruma/kaynatma modlarında gözlendi. Kullanıcı tarafından paylaşılan grafikler ve CSV analizleri, kararlı çalışma alanlarında ADS1115 ile PZEM arasındaki farkın bu oturum örneklerinde yaklaşık yüzde 1 mertebesinde kaldığını; ADS1115 eğrisinin yük değişimlerini PZEM'den önce ve daha düzenli gösterdiğini destekledi.

Örnek oturum sonuçları:
- Ütü, yaklaşık 10.6 A: ortak kararlı alanda yaklaşık +%1.29.
- Tost makinesi, yaklaşık 8.2 A: iki çevrimde yaklaşık +%1.2.
- Kettle ısı koruma, yaklaşık 0.69 A: dört çevrimde yaklaşık +%0.2 ila +%0.6.
- Kettle kaynatma, yaklaşık 6.9 A: iki çevrimde yaklaşık +%1.2.

Bu değerler ilgili oturumların karşılaştırma sonuçlarıdır; tüm cihazlar, tüm akım aralıkları veya bağımsız laboratuvar doğruluğu için genel garanti değildir. PZEM proje karşılaştırma kaynağıdır, kusursuz ground truth değildir. PZEM'in iki basamaklı görüntü çözünürlüğü ve daha seyrek/basamaklı güncellemesi karşılaştırma yorumunda dikkate alınır.

## Karar

1. **Önceki ana hedef kapatıldı:** PZEM ve SCT'nin bağımsız kararlı alanlarını bulup örtüştürerek eğitim/etiketleme verisi üretmek ve bu süreç için aç/kapa deneylerini zorunlu kılmak, mevcut BERO hedefi için artık gerekli bir ön koşul değildir. Kullanıcı mevcut ölçüm zincirinin pratik ihtiyacı karşıladığını belirterek bu iş akışını kapattı.
2. **E20 kapatıldı:** 18 W fiziksel aç/kapa tepki protokolü plan aşamasındaydı. Yeni hedef için gerekli olmadığına karar verildi; yapılmamış fiziksel deney tamamlandı sayılmaz. E20 belgeleri tarihsel plan olarak korunur.
3. **Geçmiş silinmez:** E19/E20, T008/T006, ADR'ler, eski kararlı-alan eğitim tasarımı, loglar ve CSV analizleri tarihsel kayıt olarak kalır. Firmware, YAML, katsayılar ve ham veriler bu kararla silinmez veya değiştirilmez.
4. **Yeni hedef:** Çamaşır makinesinin bir programı boyunca SCT-013 + ADS1115 akım davranışını izleyerek program evrelerini ve evreler arası geçişleri tanımak. Yeni çalışma [E21 — Çamaşır makinesi program davranışı analizi](../experiments/E21-washing-machine-program-analysis/README.md) altında yürütülür.
5. **PZEM'in rolü:** Yeni hedefte PZEM kararlı-alan eğitim etiketi üretmek için zorunlu değildir. Varsa yardımcı karşılaştırma/kayıt kaynağı olarak saklanabilir; ADS/SCT davranış analizinin yerine geçmez.
6. **Ölçüm ayarları korunur:** Bu karar firmware veya katsayı değişikliği değildir. Yeni program gözlemi öncesinde kullanılan gerçek YAML/binary ve ayarlar kayda alınır; kullanıcı onayı olmadan gain, örnekleme, pencere, filtre veya katsayı değiştirilmez.
7. **Güvenlik ön koşulu:** ADS1115 A0/A1 ortak-mod ve GND–VDD giriş sınırlarının fiziksel doğrulaması açık konudur. Yüksek akımda düzgün grafik görülmesi elektriksel giriş güvenliğini kanıtlamaz. Şebeke tarafı testleri uygun koruma ve yetkin kurulumla yapılmalıdır.

## Sonraki iş

E21 kapsamında önce çamaşır makinesinin tek bir seçilmiş programı, kullanıcı tarafından bildirilen program/ayar ve yük koşullarıyla baştan sona kaydedilir. Ham Home Assistant geçmişi korunur. Sonra akım zaman serisinden gözlenen evreler, süreler, seviyeler, geçişler ve tekrar eden örüntüler çıkarılır. Makinenin gerçek program evreleri veri ve kullanıcı gözlemiyle desteklenmeden isimlendirilmez; yalnız akım grafiğinden su seviyesi, tambur yönü veya ısıtıcı durumu kesin kabul edilmez.

## Kanıt sınırı

Bu ADR, yeni hedefin seçildiğini ve önceki eğitim iş akışının kapatıldığını kaydeder. Çamaşır makinesi programı henüz analiz edilmiş değildir; E21 başlangıçta PLANLANDI durumundadır.
