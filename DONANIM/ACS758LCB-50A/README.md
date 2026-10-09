# ACS758LCB — 50 A Lineer Hall Akım Sensörü

## 1. Amaç ve model ayrımı

Bu klasör, BERO'da kullanılacak/incelemesi yapılan **ACS758LCB 50 A lineer Hall akım sensörü** için üretici verilerini, bağlantıyı, analog çıkışı ve güvenli test sırasını toplar.

**Önemli parça kodu ayrımı:** “ACS758LCB 50A” ifadesi tek başına hassasiyeti belirlemek için yeterli değildir. Allegro seçim tablosunda:
- **ACS758LCB-050B**: çift yönlü ±50 A, tipik **40 mV/A**.
- **ACS758LCB-050U**: tek yönlü 0…50 A, tipik **60 mV/A**.

Satın alınan modülün üzerindeki entegre işaretlemesini veya üretici/satıcı parça kodunu doğrulamadan 40 mV/A sabitini kesin kabul etme. Bu belgede örnek hesaplar **050B çift yönlü varyant** üzerinden anlatılır.

## 2. Teknik özet (ACS758LCB-050B)

| Özellik | Değer | Not |
|---|---:|---|
| Üretici | Allegro MicroSystems | Üretici veri sayfası |
| Ölçüm aralığı | −50 A…+50 A | 050B çift yönlü varyant |
| Tipik hassasiyet | 40 mV/A | VCC ve sıcaklıkla değişebilir |
| Besleme | 3,0…5,5 V | Tek besleme |
| Çıkış | Analog, ratiometrik | AC ve DC ölçebilir |
| Tipik bant genişliği | 120 kHz | Uygulama filtresiyle sınırlanabilir |
| Basamak yanıtı yükselme süresi | 3 µs tipik | Veri sayfası ailesi bilgisi |
| Primer iletken direnci | 100 µΩ tipik | Bakır akım yolu |
| Çalışma sıcaklığı | −40…150 °C | LCB varyantı seçim tablosu |
| İzolasyon | Akım yolu ile sinyal pinleri arasında galvanik izolasyon | Montaj/PCB/terminal güvenliğini tek başına garanti etmez |

Kaynak: [Allegro ACS758xCB üretici veri sayfası](https://www.allegromicro.com/~/media/Files/Datasheets/ACS758-Datasheet.ashx?la=en). Ürün satıcısının modül kartına eklediği devre, kondansatör veya çıkış filtresi üretici IC'sinden farklı olabilir.

## 3. Pinler ve bağlantı

Üretici veri sayfasındaki 5-CB paket pin işlevleri:

| Pin | İşlev | Bağlantı notu |
|---|---|---|
| 1 | VCC | 3,0…5,5 V; modülün gerçek gereksinimini doğrula |
| 2 | GND | MCU/ADC referans GND'si |
| 3 | VIOUT | Analog gerilim çıkışı |
| 4 | IP+ | Primer akım yolu terminali |
| 5 | IP− | Primer akım yolu terminali |

IP+ → IP− yönünde artan pozitif akım, VIOUT'u yükseltir. Akım yönü ters çevrilirse çift yönlü 050B için çıkış orta noktadan aşağıya kayar. **Kart üzerindeki pin sırasını fotoğrafa veya klemens yerleşimine bakarak varsayma; kart üzerindeki yazıyı ve üretici çizimini kontrol et.**

## 4. Sıfır akım ofseti ve çıkış aralığı

Bu sensör akım yokken ideal olarak beslemenin yaklaşık yarısı civarında çıkış verir. Bu, kesin 2,500 V olduğu anlamına gelmez: gerçek sıfır akım ofsetini kurulumda ölç ve yazılımda kalibre et.

050B, 40 mV/A tipik hassasiyet varsayımıyla:
- 0 A: yaklaşık VCC/2
- +10 A: sıfır noktası + yaklaşık 0,400 V
- −10 A: sıfır noktası − yaklaşık 0,400 V
- ±50 A: sıfır noktasından yaklaşık ±2,000 V

Örneğin VCC=5,0 V ve orta nokta=2,5 V varsayımıyla ideal uçlar yaklaşık 0,5…4,5 V olur. Bunlar **tipik, hesaplanmış** değerlerdir; garanti edilen çıkış sınırları veya kalibrasyon sonucu değildir.

## 5. ESP32 ve MCP3208 ile kullanım

- ESP32 GPIO ADC girişi ve MCP3208 analog girişleri besleme/reference sınırlarını aşmamalıdır.
- Sensör 5 V ile besleniyorsa VIOUT 3,3 V'u aşabilir. ESP32 ADC veya 3,3 V referanslı MCP3208'e doğrudan bağlamadan önce tüm akım aralığındaki çıkış aralığını hesapla/ölç ve gerekirse uygun hassasiyetli bölücü veya tampon katı kullan.
- MCP3208 için VREF ≤ VDD olmalı; VDD, VREF, analog GND ve dijital GND veri sayfasına uygun bağlanmalıdır.
- Sensörün 5 V beslemesi ve ADC'nin 3,3 V referansı ayrı olabilir; ancak sinyal aralığı ADC sınırlarıyla uyumlu olmalı ve ortak referans bağlantısı doğru kurulmalıdır.
- Çıkış üzerindeki kondansatör/filtre bant genişliğini düşürür. AC/RMS ölçümünde filtre değeri, örnekleme hızı ve anti-alias gereksinimi birlikte seçilmelidir.
- 50 A yüksek akımdır. Primer yol, kablo kesiti, terminal sıkılığı, sıcaklık artışı ve sigorta/koruma devresi tasarlanmalıdır. Sensörün galvanik izolasyonu, tüm modülün şebeke güvenli olduğu anlamına gelmez.

## 6. Test sırası

1. Enerjisizken kartın parça kodunu, pin işaretlerini ve PCB izlerini kontrol et.
2. Primer akım hattı bağlı değilken VCC ve GND'yi doğrula.
3. VIOUT'u yüksek empedanslı multimetreyle ölç; gerçek sıfır akım ofsetini kaydet.
4. ADC'ye bağlamadan önce VIOUT'un beklenen minimum/maksimum aralığını belirle.
5. Önce düşük, güvenli ve bilinen DC akımla yön ve ölçek testi yap; referans ampermetreyle karşılaştır.
6. AC/RMS testinde gerçek örnek aralıklarını zaman damgasıyla kaydet, ofseti çıkar ve dalga biçiminin kırpılmadığını doğrula.
7. Birden fazla akım noktasında kalibrasyon yap; tek noktayı bütün aralık için doğruluk kanıtı sayma.

## 7. Kaynaklar

- Allegro MicroSystems — [ACS758xCB datasheet (PDF)](https://www.allegromicro.com/~/media/Files/Datasheets/ACS758-Datasheet.ashx?la=en)
- Allegro MicroSystems — [ACS758 datasheet alternatif bağlantı](https://www.allegromicro.com/-/media/files/datasheets/acs758-datasheet.pdf)
- DigiKey — [ACS758LCB-050B-PFF-T ürün ve özellikleri](https://www.digikey.com/en/products/detail/allegro-microsystems/ACS758LCB-050B-PFF-T/2042745)
- Meon Otomasyon — [ACS758LCB 50A modül açıklaması](https://www.meonotomasyon.com/urun/acs758lcb-50a-lineer-hall-akim-sensoru-modulu)
- Motorobit — [ACS758LCB 50A modül](https://www.motorobit.com/acs758lcb-50a-lineer-hall-akim-sensoru-modulu)

**Doğrulama durumu:** Üretici IC veri sayfası araştırıldı. BERO'daki gerçek modülün parça kodu, PCB filtresi, pin yerleşimi ve kalibrasyonu fiziksel cihazla doğrulanmış değildir.
