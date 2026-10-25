# Örnekleme hızı

**Etiket: kaynak özeti + tasarım hipotezi; BERO'da ölçülmedi.**

50 Hz temel bileşenin nominal periyodu 20 ms'dir. 100 örnek/s Nyquist hesabı teorik sınırı açıklar; RMS, tepe veya darbeli akım dalga biçimi için pratik doğruluk garantisi değildir.

OpenEnergyMonitor emonLib tartışmasında yaklaşık 5.588 akım örneği/s (calcIrms) ve 2.535 gerilim-akım örnek çifti/s (calcVI) bildirilmiştir. Bunlar belirli yazılım/donanım uygulamalarının değerleridir, evrensel minimum değildir.

## Başlangıç seçimi
- **2 kS/s:** başlangıç hedefi; nominal 50 Hz'de 40 örnek/çevrim.
- **1 kS/s:** düşük işlem yükü alternatifi.
- **2,5 kS/s:** karşılaştırma noktası.
- **500 S/s:** yalnızca kaba RMS gözlemi için opsiyonel alt test.

200 ms ve 2 kS/s yaklaşık 400 örnek verir. Şebeke tam 50,000 Hz olmayabileceğinden sabit 200 ms her zaman tam 10 çevrime oturmaz. Pencere dalgalanması sorun olursa çevrime senkron pencereyi deneyle.

## Deney gereksinimi
Aynı yük dizisini farklı hızlarda ölç. İstenen hızı değil sample_count / gerçek süre oranını raporla. RMS tutarlılığı ile tepe yakalama başarısını ayrı değerlendir.

## Kaynaklar
- OpenEnergyMonitor: https://community.openenergymonitor.org/t/sampling-rate-of-emonlib/4383
- emonLib kaynak kodu: https://github.com/openenergymonitor/EmonLib/blob/master/EmonLib.cpp
