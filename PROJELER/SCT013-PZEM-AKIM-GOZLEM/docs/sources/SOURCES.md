# Kaynak listesi ve doğrulama durumu

Bu başlangıç listesidir. Hiçbir kaynak bu donanımda deney yapıldığı anlamına gelmez.

| Kaynak | Tür | Kullanım | Sınırlama |
|---|---|---|---|
| https://community.openenergymonitor.org/t/sampling-rate-of-emonlib/4383 | Topluluk tartışması | emonLib uygulamalarında örnekleme hızları | BERO deney sonucu değil |
| https://github.com/openenergymonitor/EmonLib/blob/master/EmonLib.cpp | Açık kaynak kod | RMS hesaplama yaklaşımı | Kod uygulaması, doğruluk garantisi değil |
| https://docs.openenergymonitor.org/electricity-monitoring/ct-sensors/yhdc-sct-013-000-ct-sensor-report.html | Teknik inceleme | SCT-013-000 varyantı | SCT-013-100 ile karıştırma |
| https://mathieu.carbou.me/MycilaPZEM/PZEM-004T-V3.0-Datasheet-User-Manual.pdf | Kılavuz kopyası | PZEM alanları ve yayınlanan özellikler | Fiziksel varyant ayrıca doğrulanmalı |
| https://esphome.io/components/sensor/ct_clamp/ | Açık kaynak dokümantasyonu | CT penceresi / örnekleme uygulaması | Sürüme göre değişebilir |
| https://esphome.io/components/sensor/pzemac/ | Açık kaynak dokümantasyonu | PZEM entegrasyonu | Polling ayarı, iç yenileme hızı değildir |
| https://github.com/olehs/PZEM004T/issues/22 | Kullanıcı hata raporu | Hata okumaları / anormal değer | Tekil kullanıcı raporu |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC10422426/ | Akademik çalışma | NILM özellikleri ve dalga biçimi analizi | Amaç bu projeden farklı |

## Kanıt etiketleri
- **ÖLÇÜLDÜ:** Protokol, cihaz kimliği, tarih ve veri dosyasıyla.
- **ÜRETİCİ BELGESİ:** Üretici/kılavuzda açıkça yazılı.
- **KULLANICI RAPORU:** Forum veya issue.
- **HİPOTEZ:** Doğrulanmamış açıklama.
- **HESAP:** Açık varsayımlardan matematiksel sonuç.

Bir kaynağa atıf yaparken hangi iddiayı desteklediğini belirtin; kaynakçaya eklenmiş olması tek başına yeterli değildir.
