# MOD3-AKM001 – V1.6 uzun pamuklu program saha testi

- **Tarih:** 2026-11-22
- **Durum:** KAPANDI
- **Modül:** 3 – Çamaşır Makinesi
- **Testin ana amacı:** Modül 2'de geliştirilen V1.6 akım ölçüm kodunun gerçek çamaşır makinesinde çalışmasını ve PZEM akım referansıyla davranışını gözlemlemek.
- **Kapsam dışı:** PF ölçüm modülü geliştirmek, V1.6 katsayısını yeniden kalibre etmek, ses/titreşim entegrasyonu veya program aşamalarını otomatik sınıflandırmak.

## 1. Test düzeni ve kaynak

- Akım sensörü: SCT013 30A/1V ölçüm zinciri, ESP32D2 ve Modül 2'den devralınan V1.6 referans modeli.
- Karşılaştırma: Modül 3 WROOM üzerindeki PZEM akım ve güç kayıtları.
- Kaynak CSV: Kullanıcının sağladığı `çamaşır makinası uzun prg.csv`.
- Kaynak dosya satırı: 8.291 kayıt.
- Zaman aralığı: 2026-11-22 17:23:00 – 18:40:58 (Europe/Istanbul), yaklaşık 77 dakika 58 saniye.
- Kayıt sayıları: ESP32D2 akım 4.676; PZEM akım 900; PZEM aktif güç 911; PZEM gerilim 851; PZEM PF 541; PZEM enerji 264; PZEM frekans 147.
- Kullanıcının analizinde toplam enerji yaklaşık 0,530 kWh olarak raporlandı.

## 2. Sonuç – ana hedef

Yeni V1.6 kodu gerçek çamaşır makinesinin uzun pamuklu programı boyunca çalıştı ve kayıt üretti. Isıtma bloğunda ve programın sonraki motor/yıkama/sıkma davranışlarında ESP32D2 akım izi ile PZEM akım izi aynı genel çalışma motiflerini takip etti. Program sonundaki akımın sıfıra dönüşü de kayıtta görüldü.

**Karar:** Yeni kodun gerçek cihaz üzerinde uzun program boyunca çalışması ve karşılaştırmalı kayıt üretmesi hedefi yerine getirildi. MOD3-AKM001 kapatıldı. Bu kapanış, V1.6'nın tüm akım/PF koşullarında mutlak doğruluğunun kanıtlandığı anlamına gelmez.

## 3. Akım karşılaştırması

Kullanıcının sağladığı 1 saniyelik hizalanmış analizde:
- Isıtma bloğu: 17:24:12–17:38:56, yaklaşık 14 dakika 44 saniye.
- Isıtma gücü yaklaşık 1,81 kW, akım yaklaşık 8,28 A ve PF yaklaşık 1,00 bandında.
- Isıtma bloğunda ESP32D2 − PZEM ortalama farkı yaklaşık −0,109 A olarak raporlandı.
- Isıtma sonrası düşük akım bölümlerinde ESP32D2'nin PZEM'den ortalamada yaklaşık +0,16 ila +0,27 A yüksek okuduğu; tüm döngü için ortalama farkın +0,158 A ve MAE'nin 0,267 A olduğu kullanıcı analizinde bildirildi.

Bağımsız CSV kontrolünde, ESP32D2 örnekleri PZEM akım örneğiyle en yakın zamanlı kayıt üzerinden ±2,5 saniye toleransla eşleştirildi:
- Eşleşen çift: 4.496
- Ortalama fark (ESP32D2 − PZEM): +0,160 A
- Mutlak fark ortalaması (MAE): 0,240 A
- Isıtma aralığında eşleşmiş ortalama fark: −0,093 A; MAE: 0,138 A
- Isıtma sonrası aralıkta eşleşmiş ortalama fark: +0,225 A; MAE: 0,264 A

**Metodoloji notu:** Kullanıcı analizindeki 1 saniyelik hizalama ile bu rapordaki ±2,5 saniye en yakın örnek eşleştirmesi aynı yöntem değildir. Bu nedenle +0,267 A ve +0,240 A MAE değerleri birbirinin yerine kullanılmamalıdır. PZEM karşılaştırma referansıdır; mutlak ground truth değildir.

## 4. Program davranışından gözlemler

- Isıtma bloğunda yüksek ve görece sabit akım bölgesi görüldü.
- Isıtma sonrasında yıkama/durulama/motor hareketleri düşük akım bölgesinde tekrar eden darbeler oluşturdu.
- Kullanıcının işaretlediği ara sıkma rampaları yaklaşık 17:58, 18:08, 18:15 ve 18:28:52 civarında görüldü.
- Final sıkma yaklaşık 18:36–18:40 aralığında daha uzun bir yüksek akım platosu oluşturdu.
- Kullanıcı, merdane durma ve yön değiştirme anlarını fiziksel olarak işitebildiğini; akım grafiğindeki çukurların bu motiflerle örtüştüğünü belirtti.

Bu kayıt, program aşamalarının otomatik sınıflandırıldığını göstermez. Yalnızca daha sonraki analiz için elektriksel davranış izlerinin kaydedildiğini gösterir.

## 5. PF gözlemi ve sınırlar

PZEM PF kayıtları bu oturumda mevcuttur (541 örnek). Kullanıcının analizinde düşük/orta akım çalışma bölümlerinde PF yaklaşık 0,53–0,73; ısıtma bloğunda yaklaşık 1,00 olarak tanımlandı. Bu gözlem, V1.6 akım farkının yalnızca PF'den kaynaklandığını kanıtlamaz; akım seviyesi ve makinenin çalışma modu da aynı anda değişmektedir.

Bu görev PF ölçüm sistemi geliştirmemiştir. ZMPT101B + SCT013 ile ayrı PF ölçüm modülü fikri, ileriye dönük araştırma olarak kalır.

## 6. Teknik kararlar

1. V1.6 kodu ve kalibrasyon modeli bu test sonucuyla değiştirilmez.
2. MOD3-AKM001 – V1.6 uzun pamuklu program saha testi kapatılır.
3. Bu testin ana amacı yeni kodun gerçek cihazda çalışmasını doğrulamak ve saha kaydı almaktı; amaç yerine getirilmiştir.
4. PF kaynaklı olası akım sapması bu testte kesin neden olarak gösterilmemiştir. Gerekirse ayrı Step 2 araştırmasında ele alınır.
5. ZMPT101B ekleme fikri Modül 3'ün mevcut test kapsamına dahil değildir. Kullanıcı isterse daha sonra ayrı donanım/deney görevi olarak açılır.
6. Ses ve titreşim kanalları bu deneyde kullanılmadı; bu testin kapsamı değildi.

## 7. Kapanış

**MOD3-AKM001 KAPANDI.** V1.6 yeni koduyla çamaşır makinesinin uzun pamuklu programından yaklaşık 78 dakikalık gerçek saha kaydı alındı. Kodun gerçek cihazda çalışması doğrulandı; çalışma koşullarına göre PZEM ile farkın yön değiştirdiği gözlendi. Mutlak ölçüm doğruluğu ve farkın PF kaynaklı olup olmadığı bu görevin kabul kriteri değildi ve kanıtlanmış sayılmaz.

## 8. Kaynaklar

- Ham kaynak CSV: Kullanıcının bu oturumda yüklediği `çamaşır makinası uzun prg.csv` (8.291 satır; 653.385 bayt).
- Kullanıcının 1 saniyelik hizalanmış analiz grafiği ve ekran görüntüsü: 2026-11-22 tarihli konuşma ekleri.
- Bu rapordaki bağımsız eşleştirme: CSV'deki zaman damgaları Europe/Istanbul saatine çevrildi; her ESP32D2 akım örneği için en yakın PZEM akım örneği ±2,5 saniye içinde eşleştirildi.
