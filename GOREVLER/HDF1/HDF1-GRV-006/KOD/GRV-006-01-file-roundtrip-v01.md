# PROJE BERO — GRV-006-01 — Dosya yazma, yeniden okuma ve Python işleme

## Hedef

Tek ve küçük bir CSV veri kümesini gerçek dosyaya yazmak, aynı dosyayı yeniden açmak, Python ile dönüştürmek, sonucu ayrı dosyaya yazıp yeniden okumak ve bağımsız bir hesapla kontrol etmek.

## Veri ve sınırlar

- Veri türü: açıkça sentetik/deterministik örnek veri.
- Ham girdi: `GRV-006-01-ham-veri.csv`
- İşlenmiş çıktı: `GRV-006-01-islenmis-veri.csv`
- İşlem: her `value` alanını ikiyle çarpıp `double_value` olarak yazmak.
- Bu basamak ESP iletişimini, SCT ölçümünü veya fiziksel doğruluğu test etmez.

## Gerçek çalıştırma sonucu

Script, çalışma ortamında çalıştırıldı. Konsol çıktısı:

```text
SOURCE_WRITTEN: GRV-006-01-ham-veri.csv (44 bytes)
OUTPUT_WRITTEN: GRV-006-01-islenmis-veri.csv (66 bytes)
SOURCE_REREAD: PASS (3 rows; values=10,20,30)
PROCESSING: PASS (double each value)
OUTPUT_REREAD: PASS (3 rows; doubled_values=20,40,60)
INDEPENDENT_CHECK: PASS (expected_sum=120; output_sum=120)
RESULT: PASS — GRV-006-01 file round-trip and Python processing demonstrated
LIMIT: synthetic data only; no ESP communication or sensor-accuracy claim
```

## Bağımsız kontrol

Beklenen toplam, dönüşüm satırlarını oluşturan liste işleminden ayrı olarak `2 × (10 + 20 + 30) = 120` biçiminde hesaplandı. İşlenmiş CSV dosyası yeniden açılarak okunan `double_value` toplamı da 120 bulundu; satırlar `[20, 40, 60]` ile eşleşti.

## Sonuç

**GRV-006-01'in dosya yazma → dosyadan yeniden okuma → Python işleme → işlenmiş dosyayı yeniden okuma → bağımsız toplam kontrolü basamağı PASS.** Bu, görev tanımının yalnızca ilk kısmıdır; Python→ESP→geri okuma henüz yapılmadı.

## Sonraki adım

GRV-006-02'de aynı çıktı için bağımsız hesap kanıtını koruyup ardından GRV-006-03 öncesinde depodaki mevcut ESP arayüzünü ve kodunu incelemek. Yeni haberleşme yöntemi varsaymamak.
