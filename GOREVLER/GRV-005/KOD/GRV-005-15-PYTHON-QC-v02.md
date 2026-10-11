# GRV-005-15 — Python CSV QC v02

- Tarih: 2026-10-11
- Kaynak: v01 QC betiği, yeni sürüm olarak güncellendi.

## v02 değişikliği

BIAS satırında adc_rms_raw boş olabilir; CH0-1T, CH1-2T ve CH2-3T satırlarında ise bu alan zorunludur. Bu ayrım QC içinde açıkça kontrol edilir.

## Test durumu

- Sentetik pozitif/negatif öz test: 5/5 senaryo PASS.
- v03 hizalama şablonlarından log değerleriyle yeniden oluşturulan dört satır: 14/14 kontrol PASS.
- Bu, statik regresyon testidir; v03 firmware'den alınan gerçek cihaz CSV'si değildir.

## Çalıştırma

```bash
python3 GRV-005-15-PYTHON-QC-v02.py --self-test
python3 GRV-005-15-PYTHON-QC-v02.py cihazdan_alinan.csv
```
