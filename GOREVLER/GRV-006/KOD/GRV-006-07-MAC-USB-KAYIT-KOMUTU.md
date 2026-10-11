# GRV-006-07 — Mac USB canlı kayıt başlatma

Amaç: ESP32D1'i USB ile Mac'e bağlayınca logları elle kopyalamadan dosyaya almak.

## Bir defalık hazırlık

Masaüstünde Terminal aç ve şu komutları sırayla kopyala:

```bash
python3 -m pip install --user pyserial
cd ~/Desktop
curl -fL -o GRV-006-06-USB-serial-capture-v01.py https://raw.githubusercontent.com/bakbalik-win11/BERO/main/GOREVLER/GRV-006/KOD/GRV-006-06-USB-serial-capture-v01.py
python3 GRV-006-06-USB-serial-capture-v01.py --list
```

Listede görünen ESP32 seri portunu seç. Genellikle `/dev/cu.` ile başlar. Sonra:

```bash
python3 ~/Desktop/GRV-006-06-USB-serial-capture-v01.py --port /dev/cu.PORT_ADI --outdir ~/Desktop
```

`/dev/cu.PORT_ADI` kısmını listede görünen gerçek portla değiştir. Log akarken ölçüm satırları gelecektir; durdurmak için Ctrl-C. Ham log ve CSV Masaüstüne yazılır.

## Sonraki kontrol
Terminalde `CSV_COLUMN_MISMATCH` görülürse CSV'yi işleme zincirine verme; ham .log dosyası saklıdır ve kolon eşleşmesi ayrıca düzeltilmelidir. `CSV_ROWS: 0` veya başlık eksikse cihazın seri log biçimi incelenmelidir.

## Durum
Komut ve kod depoda belgelendi. Fiziksel USB portu bu ortamdan görülemediği için gerçek cihazda PASS iddiası yoktur. ESP firmware'i değiştirilmez.
