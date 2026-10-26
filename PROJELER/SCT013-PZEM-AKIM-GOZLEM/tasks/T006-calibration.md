# T006 — SCT kalibrasyonu

- **Durum:** PLANLANDI
- **Faz:** 1.3
- **Bağımlılık:** T005 ve T003
- **Hedef:** Ölçülmüş referans değerlerine dayanarak SCT amper dönüşüm katsayısını hesaplamak ve izlenebilir bir calibration_id kaydı oluşturmak.

## Yapılacak
1. calibration/PROCEDURE.md prosedürünü ve önceden belirlenmiş hata hedeflerini uygula.
2. En az üç uygun akım seviyesinde referans ölçümü ve SCT verisini eşleştir.
3. Her ölçümün donanım kimliğini, tarihini, yük senaryosunu, ham veri konumunu ve kullanılan hesap yöntemini kaydet.
4. Kalibrasyon sonucunu calibration/calibrations.csv içine yeni bir calibration_id ile ekle; eski girdilerin üzerine yazma.
5. Hata hedefi ve clipping durumunu değerlendir; hedef sağlanmadıysa katsayıyı başarılı kalibrasyon olarak sunma.
6. G1 kapısını yalnızca ROADMAP.md ve STATUS.md içindeki ölçütler kanıtla karşılandığında işaretle.

## Kabul ölçütü
En az üç seviyede SCT–referans farkı T003'te önceden onaylanan hedefler içindedir; clipping yoktur; calibration_id ve kanıt bağlantıları kayıtlıdır.

## Çıktı / dokunulacak dosyalar
- calibration/calibrations.csv
- calibration/PROCEDURE.md
- STATUS.md ve ROADMAP.md (G1 için tüm koşullar sağlanırsa)
