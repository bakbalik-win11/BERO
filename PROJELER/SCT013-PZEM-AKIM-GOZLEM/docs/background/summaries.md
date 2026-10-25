# Özet istatistikler

## Zorunlu
- Ofseti giderilmiş ve kalibre edilmiş AC RMS akım.
- Pencere start/end, sample_rate_actual_hz ve sample_count.
- calibration_id.
- ADC ortalaması, min/max ve clipping sayısı.

## Önerilen
- Her 200 ms pencerede RMS; gerekirse alt pencere RMS min/max.
- Olay algılanınca kısa ham örnek kesiti.
- Peak saklanıyorsa crest factor türetilebilir; min/max varsa peak-to-peak türetilebilir.

## Varsayılan olarak saklanmayan / türetilebilen
- Standart sapma aynı ofset giderme tanımıyla AC RMS'e çok yakın/eşdeğer olabilir; ikisini birden tutma gerekçesi varsa yaz.
- Crest factor = peak / RMS.
- Peak-to-peak = max - min.
- Zero crossing ana alan değildir; ancak frekans veya örnekleme teşhisi ihtiyacı doğarsa eklenebilir.

## RMS pencerelerini birleştirme
RMS_toplam = √(Σ(Nᵢ × RMSᵢ²) / ΣNᵢ)

Örnek sayıları farklıysa ağırlıklandırmayı ihmal etme. Ofset giderme yöntemini tutarlı uygula. Küçük bir istatistik kümesi ham dalga biçimini eksiksiz korumaz; deney yapılmadan “%95 bilgi korunur” türü genel bir yüzde verme.
