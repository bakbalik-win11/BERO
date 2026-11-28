# FNIRSI SG-002 ile UT61E+ analog DC çıkış ve akım döngüsü kontrolü

- **Tarih / plan:** 2026-11-28
- **Görev:** MOD2-GRV002
- **Durum:** PLANLANDI — fiziksel deney ve ölçüm sonuçları henüz yok.
- **Kaynak cihaz:** FNIRSI SG-002, mevcut envanter varlığı.
- **Ölçü aleti:** UNI-T UT61E+ (satın alma adayı; teslim/çalışma durumu ayrıca kaydedilecek).
- **Amaç:** Sensör ADC zincirine geçmeden önce tezgâhtaki bağımsız multimetrenin DC analog gerilim ve endüstriyel akım döngüsü ölçümünü kontrollü bir kaynakla pratik olarak kontrol etmek.

## 1. SG-002'nin işlev sınırı

FNIRSI SG-002, ayarlanabilir analog **DC gerilim** ve **DC akım** kaynağı/simülatörüdür. Üretici kılavuzundaki temel teknik tanımlar:
- Gerilim çıkışı: model/menü sürümüne bağlı seçilebilir DC aralıklar; kılavuzda 0–10 V, 2–10 V, 0–5 V, 1–5 V ve 0–3,3 V seçenekleri listelenir.
- Akım çıkışı: model/menü sürümüne bağlı 0–20 mA, 4–20 mA veya 0–22 mA seçenekleri.
- Gerilim çıkışında azami yük akımı 20 mA olarak belirtilir.
- Akım çıkışında yük/örnekleme direnci 500 ohm'u aşmamalıdır.
- Ürün kılavuzunda ekranda iki ondalık basamak gösterimi vardır; gerçek çıkış değeri UT61E+ ile ayrıca okunmalıdır.

**Önemli ayrım:** SG-002'nin menüsündeki `50HZ` ifadesi kılavuzda bir *display mode / ekran gösterim modu* seçeneği olarak listelenir. Bu, SG-002'nin 50 Hz AC sinüs ürettiği anlamına gelmez. SG-002 bu deney planında AC dalga kaynağı olarak kullanılmayacaktır.

Üretici/kılavuz kaynakları:
- https://manuals.plus/fnirsi/sg002-0-10v-or-0-22m-voltage-and-current-source-signal-generator-manual.pdf
- https://www.fnirsi.com/ (model ve revizyon için cihazın kendi kılavuzu/etiketi esas alınır)

## 2. Test A — DC gerilim çıkışı

1. SG-002'nin fiziksel etiketi, terminal yazıları ve menüde gerçekten bulunan çıkış aralıkları fotoğraflanıp kaydedilir.
2. Gerilim modu seçilir; SG-002'nin terminal şemasına göre AVo ve GND çıkışı kullanılır. Kablo bağlantıları enerji kapalıyken yapılır.
3. Cihazın mevcut menüsünde bulunan uygun DC aralık seçilir. Mümkünse 0–3,3 V ve 0–10 V gibi BERO analog girişleriyle ilişkili aralıklar ayrı ayrı denenir.
4. Menüde erişilebilen birkaç kararlı setpoint belirlenir. Örnek hedefler, gerçek menü aralığına göre: 0,50 V, 1,00 V, 1,65 V, 2,50 V, 3,00 V, 3,30 V, 5,00 V ve 10,00 V. Aralıkta olmayan noktalar kullanılmaz.
5. Her noktada SG-002 ekran değeri ve UT61E+ DC gerilim okuması kaydedilir. Her nokta en az üç kez tekrarlanır.
6. UT61E+ girişi cihazın izin verilen ortak/mod farkı ve ölçüm aralığı içinde tutulur. SG-002'nin çıkışına başka besleme bağlanmaz.

Bu test bir kalibrasyon sertifikası üretmez. SG-002 bir test kaynağıdır; UT61E+ okumasıyla karşılaştırmalı davranış ve tekrarlanabilirlik değerlendirilir.

## 3. Test B — 4–20 mA DC akım döngüsü

1. SG-002'nin fiziksel kılavuzundaki aktif/pasif akım bağlantı tipi ve terminal eşleşmesi doğrulanır; model/revizyon teyit edilmeden terminal bağlantısı varsayılmaz.
2. Akım çıkışının izin verdiği yük sınırı 500 ohm altında tutulur.
3. Öncelikli güvenli yöntem olarak uygun toleranslı bir akım algılama direnci üzerinden gerilim ölçümü yapılabilir. Örnek 250 ohm dirençte:
   - 4 mA → 1,00 V
   - 8 mA → 2,00 V
   - 12 mA → 3,00 V
   - 16 mA → 4,00 V
   - 20 mA → 5,00 V
4. Direnç gücü, toleransı ve bağlantı şeması deneyden önce doğrulanır. 250 ohm üzerinde 20 mA akımda 0,1 W güç oluşacağından uygun güç sınıfı ve güvenlik payı seçilir.
5. Alternatif doğrudan mA ölçümünde UT61E+ akım girişine seri bağlanır; doğru mA girişi, kademe ve sigorta kontrol edilmeden bağlantı yapılmaz. Akım çıkışı veya loop enerjiliyken multimetre voltaj girişinin akım yoluna paralel bağlanmasıyla kısa devre oluşturulmaz.
6. 4, 8, 12, 16 ve 20 mA hedefleri (SG-002'nin gerçek menüsünün desteklediği değerler içinden) ayarlanır. SG-002 gösterimi, direnç üstündeki gerilimden hesaplanan akım ve/veya seri mA ölçümü kaydedilir.

SG-002'nin kendi çıkış doğruluğu ve UT61E+ doğruluğu ayrı hata kaynaklarıdır. SG-002 ekranı mutlak referans standardı kabul edilmez.

## 4. Beklenen kullanım ve BERO bağlantısı

Bu deney, 4–20 mA transmitter, endüstriyel analog giriş ve 0–10 V/0–3,3 V analog girişlerin BERO tarafında karakterizasyonuna yardımcı olur. Gerçek sensör testinden ayrıdır:
- SG-002, sensörün fiziksel olayı algılamasını test etmez.
- SG-002, sensörün AC dalga biçimini veya fazını simüle etmez.
- SG-002 ile doğrulanan DC giriş zinciri, SCT013 AC akım transformatörü veya ZMPT101B AC dalga ölçümünü doğrulamış sayılmaz.
- ADC/ESP32/MODBUS analog giriş karşılaştırması yapılacaksa aynı DC setpoint ve aynı zaman penceresi kaydedilir; ham ADC kodu ve UT61E+ ölçümü ayrı tutulur.

## 5. Kaydedilecek veriler

`timestamp,sg002_mode,sg002_range,sg002_setpoint,ut61e_reading,measurement_range,sense_resistor_ohm,calculated_current_mA,repeat_index,notes`

- Cihazın model/PCB/firmware revizyonu bilinmiyorsa bilinmiyor olarak yazılır.
- Üretici kılavuzu ile fiili menü farklıysa fiziksel cihaz davranışı ayrıca kaydedilir.
- Ham gözlem değiştirilmez; hesaplanan fark/lineerlik ayrı raporda değerlendirilir.

## 6. Sonuç durumu

Bu dosya yalnızca deney planıdır. SG-002 çıkışı veya UT61E+ ile fiziksel ölçüm henüz yapılmamıştır. Başarılı, doğrulanmış veya kalibre edilmiş sonucu olduğu iddia edilmez.

## 7. Kaynaklar

- FNIRSI SG-002 kullanım kılavuzu: https://manuals.plus/fnirsi/sg002-0-10v-or-0-22m-voltage-and-current-source-signal-generator-manual.pdf
- BERO envanteri: `ENVANTER/README.md`
