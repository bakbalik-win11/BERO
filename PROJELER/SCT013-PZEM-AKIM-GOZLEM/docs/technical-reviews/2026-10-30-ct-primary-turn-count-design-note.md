# SCT birincil iletken tur sayısı — gelecekte hat bazında seçim notu

- **Kayıt tarihi:** 2026-10-30
- **Durum:** FİKİR / TASARIM NOTU — fiziksel test yapılmadı, tur sayısı seçilmedi, firmware veya kalibrasyon değiştirilmedi.
- **İlişki:** E08 SCT karakterizasyon deneyi ve ileride hat bazında sensör/kurulum seçimi.
- **Kullanıcı yönü:** Kullanıcı, ileride her hatta özel tur sayısı kullanmanın muhtemel olduğunu belirtti. Bu not, fikri kaybetmemek için tutulur; aktif deney sırasını değiştirmez.

## 1. Fikrin amacı

SCT'nin içinden geçirilen aynı akım taşıyan iletkenin tur sayısını, ölçülecek hattın beklenen akım aralığına göre seçebilmek.

Bu yaklaşımın olası amacı, düşük akımlarda CT çıkışını ve ADC girişindeki sinyal genliğini artırırken, hattın beklenen en yüksek akımında CT'nin nominal çalışma aralığını aşmamaktır.

Tur sayısı gerçek hat akımını artırmaz. CT çekirdeğinin gördüğü amper-tur değerini artırır.

## 2. Temel fiziksel ilişki

Birincil iletken CT penceresinden N kez geçirilirse, ideal ilk yaklaşımda:

`I_ampere-turn = I_primary × N`

Aynı primer akımında tur sayısının artırılması, CT çekirdeğinin gördüğü amper-tur değerini artırır. CT doğrusal bölgede kaldığı sürece sekonder/gerilim çıkışının tur sayısıyla yaklaşık orantılı artması beklenir.

Bu, ideal ve yaklaşık bir ilişkidir. Gerçek çıkış; CT çekirdeği, yük/burden, frekans, dalga şekli, kablo yerleşimi ve sensörün doğrusal çalışma aralığına bağlıdır. Her tur sayısı için ölçüm ve kalibrasyon gerekir.

## 3. SCT013-030 (30 A / 1 V) için yalnızca teorik ölçek

Aşağıdaki tablo, 30 A nominal tek-tur değerinden türetilen amper-tur ölçeğidir. Üreticinin çok turlu çalışma garantisi veya kesin doyum sınırı olarak okunmamalıdır.

| Birincil tur | 30 A nominal amper-tur değerine karşılık gelen teorik primer akımı |
|---:|---:|
| 1 | 30 A |
| 2 | 15 A |
| 3 | 10 A |
| 4 | 7,5 A |
| 5 | 6 A |

Örnek hesaplar:

- 0,04 A yük, 5 turda 0,20 A-tur oluşturur.
- 0,447 A yük, 5 turda 2,235 A-tur oluşturur.
- 0,616 A yük, 5 turda 3,08 A-tur oluşturur.
- 6,39 A yük, 5 turda 31,95 A-tur oluşturur.

Son örnek, 30 A nominal tek-tur amper-tur ölçeğinin biraz üzerindedir. Bu nedenle 5 tur, kettle gibi yüksek akım koşullarında varsayılan seçenek olamaz. Bununla birlikte 30 A/N hesabı kesin clipping veya doyum eşiği değildir; gerçek sınır deney ve üretici verisiyle ayrıca ele alınmalıdır.

## 4. BERO'daki mevcut deney planıyla ilişkisi

E08 — SCT karakterizasyon planında zaten şu matris bulunuyor:

- İletken turu: 1, 2 ve 4.
- Hedef örnekleme hızları: 1, 2 ve 2,5 kS/s.
- İlk kontrollü yük: 100 W akkor.
- Sonraki yük karşılaştırması: 150 W akkor ve 8,5 W LED.
- Aynı pencere örneklerinden bias çıkarılmış RMS, mutlak Peak ve Peak-to-Peak hesaplanması.

Bu mevcut E08 matrisi korunur. Bu not E08'e yeni koşul eklemez ve aktif deney sırasını değiştirmez.

**5 tur**, Gemini tarafından önerilmiş bir olasılık olarak kaydedilir; mevcut E08 matrisinde yoktur ve kullanıcı tarafından uygulanmış/kararlaştırılmış bir test değildir. 1/2/4 tur sonuçları görüldükten ve hat profili netleştikten sonra ayrıca değerlendirilir.

## 5. Hat bazında tur seçimi için ileride kaydedilecek bilgiler

Her sensör/hat kurulumu için en az şu bilgiler tutulmalıdır:

- `sensor_id` veya sensörün fiziksel envanter kimliği.
- CT modeli ve nominal çıkış tipi (ör. SCT013-030, 30 A / 1 V).
- `line_profile`: hattın gerçek kullanım profili; yalnız cihaz isimlerinden varsayılmaz.
- `turn_count`: CT penceresinden geçirilen aynı tek akım taşıyan iletkenin tur sayısı.
- Beklenen normal akım ve mümkünse eşzamanlı yükte beklenen en yüksek akım.
- Başlangıç akımı/inrush gibi kısa süreli yüksek akım koşulları biliniyorsa notu.
- Analog ön uç/bias ve ADC yapılandırması.
- Kullanılan firmware/yapılandırma sürümü.
- Tur sayısı ve donanım düzeniyle ilişkili ayrı `calibration_id`.
- Referans ölçüm ve her tur koşulunun ölçüm sonuçları.

Bir sensör/hat/tur/analog ön uç düzeninden diğerine geçildiğinde önceki kalibrasyon kimliği otomatik olarak yeniden kullanılmamalıdır.

## 6. İlerideki seçim ilkesi

Tur sayısı yalnızca düşük akım sinyalini büyütmek amacıyla seçilmemelidir. Seçim, hattın gerçek en yüksek sürekli akımı ve geçici akım koşulları ile CT'nin doğrusal çalışma aralığı birlikte değerlendirilerek yapılmalıdır.

- Küçük yüklerin bulunduğu hatlarda daha fazla tur araştırılabilir.
- Karma priz hatlarında eşzamanlı yüklerin toplamı dikkate alınmalıdır.
- Kettle, ısıtıcı, fırın gibi yüksek akım yükleri beklenen hatlarda tur sayısı daha düşük tutulabilir.
- Hat profili bilinmiyorsa çok turlu konfigürasyon varsayılmamalı; önce güvenli ve tanımlı bir referans kurulumla karakterizasyon yapılmalıdır.

Bu maddeler henüz seçim standardı değildir; gelecekteki tasarım kararına girdi olacak ilkelerdir.

## 7. Fiziksel bağlantı ve güvenlik notları

- Tur, aynı tek akım taşıyan iletkenin CT penceresinden birden fazla kez geçirilmesiyle oluşturulur.
- Faz ve nötr birlikte CT penceresinden geçirilmez; aksi durumda manyetik etkiler birbirini büyük ölçüde götürebilir.
- İletkenin yalıtımı, kesiti, bükülme yarıçapı, mekanik sabitlemesi ve CT penceresine uygunluğu korunmalıdır.
- Şebeke hattında iletkeni yerinden çıkarma veya yeniden yönlendirme yalnız enerji kesilmişken, uygun muhafaza/koruma ve yetkin kişi tarafından yapılmalıdır.
- CT sekonder bağlantısı, üretici talimatı izin vermedikçe primer akım varken açık bırakılmamalıdır.
- Bu not fiziksel montaj talimatı veya güvenlik onayı değildir.

## 8. Kanıt ve belirsizlik sınıfları

- **KULLANICI YÖNÜ:** Hat bazında özel tur sayısı kullanılması muhtemel bir gelecek yaklaşımı olarak kullanıcı tarafından belirtildi.
- **MEVCUT DEPO PLANI:** E08'de 1/2/4 tur matrisi zaten tanımlı; henüz fiziksel test sonucu değildir.
- **DIŞ AI ÖNERİSİ:** Gemini 5 turu düşük akım için popüler/uygun bir seçenek olarak önerdi. Bu öneri bağımsız üretici doğrulaması veya BERO ölçümü değildir.
- **HESAP:** Amper-tur örnekleri, primer akım × tur sayısı hesabıdır.
- **HİPOTEZ:** Çıkışın doğrusal bölgede tur sayısıyla yaklaşık orantılı artması ve ADC sinyalinin büyümesi beklenir; BERO düzeninde ölçülmelidir.
- **HENÜZ BİLİNMİYOR:** Her SCT örneğinin çok turlu doğrusal aralığı, gerçek doyum noktası, hat başına en uygun tur sayısı ve her tur için kalibrasyon katsayısı.

## 9. HEDEF / LOG / SONUÇ

- **HEDEF:** Hat bazında CT tur sayısı seçimi fikrini, teorik hesabı, E08 ile ilişkisini ve güvenlik sınırlarını ileride bulunabilecek şekilde saklamak.
- **LOG:** 2026-10-30 tarihinde kullanıcı hat bazında özel tur yaklaşımını gündeme getirdi. E08 stage-02 ve E08 protokolü incelendi; 1/2/4 tur matrisinin zaten mevcut olduğu doğrulandı. Gemini'nin 5 tur önerisi ayrıca değerlendirildi.
- **SONUÇ:** Fikir depoya park edildi. E08 matrisi, aktif görev ve firmware değiştirilmedi. 5 tur onaylanmadı; fiziksel test, ölçüm, kalibrasyon veya doyum doğrulaması yapılmadı.
- **Sonraki adım:** E08'in mevcut 1/2/4 tur sonuçları elde edildikten ve hedef hattın gerçek yük profili belirlendikten sonra, gerekirse ayrı hat konfigürasyonu/kalibrasyon kararı aç.
