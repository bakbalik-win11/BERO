# Yüksüz ofset ve gürültü tabanı

## Amaç
Yük yokken ADC bias/ofseti, gürültü RMS'i ve clipping'i ölç.

## Başlangıç hipotezi
HİPOTEZ — bu projede deneyle doğrulanmadı; sonuç gibi raporlanamaz.

## Prosedür
1) Güvenlik ve analog bağlantıyı doğrula. 2) Sabit ayarlarda en az 30 s veri al. 3) sample_count, ortalama, min/max ve ofset giderilmiş gürültü RMS'ini çıkar.

## Güvenlik
hardware/safety-checklist.md tamamlanmadan şebeke deneyi yapılmaz.

## Kabul ölçütü
Tekrarlı ofset/gürültü ölçümleri ve donanım kimlikleri kayıtlı.
