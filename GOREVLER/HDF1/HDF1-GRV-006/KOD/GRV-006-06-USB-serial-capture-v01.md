# GRV-006-06 — USB seri log yakalama

## Hedef
ESP32D1'in USB seri logunu Mac'e otomatik kaydetmek; firmware'in loga yazdığı CSV başlıklarını ve veri satırlarını ayrı bir CSV dosyasına çıkarmak. Böylece logu elle kopyalayıp CSV'yi elle oluşturma adımı kaldırılır.

## Donanım ve araç
- Mevcut ESP32D1; cihaz adı değiştirilmez.
- USB veri kablosu.
- Mac mini, Python 3 ve pyserial.

## Çalıştırma
```bash
python3 -m pip install pyserial
python3 GRV-006-06-USB-serial-capture-v01.py --list
python3 GRV-006-06-USB-serial-capture-v01.py --port /dev/cu.PORT_ADI --outdir ~/Desktop
```
`/dev/cu.PORT_ADI` yerine `--list` çıktısındaki gerçek ESP32 USB seri portunu yaz. Yakalama çalışırken cihazın açılış/ölçüm logları terminale akar; durdurmak için Ctrl-C kullanılır. İstersen `--seconds 60` ile 60 saniye sonra otomatik durdurulabilir.

## Üretilen dosyalar
- `GRV-006-06-USB-TARIH.log`: ham seri log; kaynak kanıtı korunur.
- `GRV-006-06-USB-TARIH.csv`: firmware logundan başlık parçaları ve veri satırları çıkarılabilirse üretilir.

## Güvenlik ve doğrulama
- Betik firmware yüklemez ve ESP adını/configürasyonunu değiştirmez.
- Ham log her zaman saklanır.
- İki başlık parçası alınmadan CSV satırı yazılmaz.
- Başlıkta beklenen sütun sayısıyla satır sütun sayısı uyuşmazsa satır CSV'ye eklenmez; `CSV_COLUMN_MISMATCH` uyarısı yazılır.
- ESP32'nin USB seri port adı Mac'te değişebilir; gerçek port `--list` ile bulunmalıdır.
- Bu betik depoda hazırlandı ancak fiziksel USB bağlantısı burada yapılamadığı için cihaz üzerinde çalıştığı iddia edilmez.

## Kabul ölçütü
Kullanıcı cihazı USB ile bağlayıp betiği çalıştırdığında:
1. Ham .log dosyası oluşmalı.
2. CSV başlığı ve satırlar ayrıştırılmalı.
3. Kolon uyuşmazlığı uyarıları incelenmeli.
4. Çıkan CSV mevcut GRV-006-04 Python → ESP echo akışına verilmeden önce doğrulanmalı.

## Durum
**Hazır; fiziksel USB yakalama henüz cihazda çalıştırılarak doğrulanmadı.** Mevcut GRV-006-05 log türevli CSV echo PASS sonucu değişmez. Bu adımın amacı canlı kayıt alımını otomatikleştirmek; sensörün amper doğruluğunu kanıtlamak değildir.
