# Bağımsız Ölçüm Ekipmanları

**Sınıflandırma:** Sistem modülü değil; bağımsız ölçüm ve kontrol ekipmanı.

Bu cihazlar ESP/HA telemetri hattına veri sağlamaz. PZEM, Faz 2'de SCT verisini etiketlemek ve karşılaştırmak için proje referansıdır. Bağımsız ölçüm cihazları, gerektiğinde sonuçları harici olarak kontrol etmek için kullanılır; otomatik etiket kaynağı değildir.

## UNI-T UT200B+

- **Tür:** Pens ampermetre.
- **BERO rolü:** Akım ölçümlerinde bağımsız karşılaştırma/kontrol.
- **Kullanıcı tarafından belirtilen imkân:** 3 A akım kademesi; düşük akım gözlemlerinde daha uygun kademe seçimi sağlayabilir.
- **Kayıt sınırı:** Gerçek ölçüm sonuçları henüz bu envanter girdisiyle iddia edilmez. Her ölçümde kademe, iletken yerleşimi, yük ve gösterge değeri kaydedilmelidir.

## UNI-T UT33D+

- **Tür:** Dijital multimetre.
- **BERO rolü:** Gerilim, DC akım, direnç, diyot ve süreklilik kontrolleri; özellikle bias beslemesi ve düşük gerilim noktalarının bağımsız kontrolü.
- **Üretici teknik özellikleri:**
  - DC gerilim: 200 mV / 2 V / 20 V / 200 V / 600 V; ±(%0,5 + 2 digit).
  - AC gerilim: 200 V / 600 V; ±(%1,2 + 3 digit).
  - DC akım: 2.000 µA / 20 mA / 200 mA / 10 A; ±(%1 + 2 digit).
  - Direnç: 200 Ω–200 MΩ kademeleri; ±(%0,8 + 2 digit).
  - Diyot testi, süreklilik buzzeri ve NCV; manuel kademe seçimi.
- **Önemli sınır:** UT33D+ AC akım ölçmez. AC akım ölçümü için kullanılmamalıdır.
- **Üretici kaynağı:** [UNI-T UT33+ Series — UT33D+ teknik özellikleri](https://meters.uni-trend.com/product/ut33plus-series/).
- **Önceki kullanım kaydı:** Kullanıcı, Bias Trafosu çıkışındaki 3,31 V DC ölçümünü UT33D+ ekran fotoğrafıyla paylaşmıştı. Ölçüm yükü ve tam prob noktaları ayrıca doğrulanmış değildir.

## Kayıt protokolü

Bağımsız ölçüm sonuçları kaydedilirken en az şu bilgiler tutulur: tarih/saat ve saat dilimi, cihaz/model, seçilen kademe, ölçüm noktası veya pensin çevrelediği tek iletken, yük koşulu, ekrandaki değer ve varsa ölçüm süresi. Bu cihazların sonuçları PZEM verisiyle aynı koşulda alınsa bile PZEM etiketinin yerine sessizce geçirilmez.
