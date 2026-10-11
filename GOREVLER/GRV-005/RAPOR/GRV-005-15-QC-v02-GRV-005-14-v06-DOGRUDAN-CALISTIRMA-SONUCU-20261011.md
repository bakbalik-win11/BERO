# PROJE BERO — GRV-005-15 doğrudan çalıştırma sonucu — v06 CSV

**Durum:** Çalıştırma doğrulaması bekliyor  
**Girdi CSV:** `GOREVLER/GRV-005/RAPOR/GRV-005-14-v06-QC-GIRDİSİ-20261011.csv`  
**Script:** `GOREVLER/GRV-005/KOD/GRV-005-15-PYTHON-QC-v02.py`

## Neden henüz sonuç yazılmadı?

Bu oturumda GitHub'daki script ve CSV içeriği geri okundu. Ancak bu çalışma ortamında GitHub'dan indirilen dosyaları doğrudan çalıştıracak dosya aktarımı/çalıştırma bağlantısı bulunmadığından, **depo scriptinin gerçek doğrudan çalıştırılması tamamlanamadı**. Bu rapor PASS veya FAIL iddiası taşımaz.

Önceki raporda yer alan **14/14 PASS**, aynı QC ölçütlerini bağımsız uygulamayla kontrol etmenin sonucudur; doğrudan script çalıştırma sonucu değildir. Bu iki kanıt türü birbirine karıştırılmayacaktır.

## Depodan geri okuma kontrolleri

- Script dosyası bulundu: `GOREVLER/GRV-005/KOD/GRV-005-15-PYTHON-QC-v02.py`
- Script blob SHA: `1c455032af877e8898c6043a9bab97c8a38e7746`
- CSV girdisi bulundu: `GOREVLER/GRV-005/RAPOR/GRV-005-14-v06-QC-GIRDİSİ-20261011.csv`
- CSV blob SHA: `a71c03adb10cb8ba5264f7f8f1abb486900d0183`
- CSV başlığında 41 alan ve dört veri satırı olduğu içerikten kontrol edildi.

## Sıradaki tek adım

Script ve CSV'yi çalıştırılabilir bir ortama indirip şu komutu çalıştır:

```bash
python3 GOREVLER/GRV-005/KOD/GRV-005-15-PYTHON-QC-v02.py GOREVLER/GRV-005/RAPOR/GRV-005-14-v06-QC-GIRDİSİ-20261011.csv
```

Sonra gerçek terminal çıktısını bu rapora ekle. Scriptin exit code değeri 0 ve tüm 14 kontrol PASS ise doğrudan çalıştırma doğrulaması PASS sayılır. Aksi hâlde gerçek başarısız sonuç korunur ve neden incelenir. Sentetik öz-test bunun yerine geçmez.

## Sınır

Bu rapor yalnızca çalıştırma doğrulama adımının açık durumunu kaydeder. Firmware, CSV girdisi ve önceki bağımsız QC raporu değiştirilmemiştir.