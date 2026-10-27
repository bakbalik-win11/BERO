# T003 — PZEM tabanlı model hata hedefi

- **Durum:** TAMAMLANDI — kullanıcı, PZEM'e göre ±4% sapmayı yeterli kabul etti; Python değerlendirmesinde geçerli aralık içinde kalan sonuçlar `OK` olarak işaretlenecek.
- **Faz:** 0.3
- **Bağımlılık:** T001; fiziksel deney öncesinde T002
- **Hedef:** SCT verisinden Python ile oluşturulan modelin PZEM okumalarına uyumunu değerlendirmek için kabul hedefini belirlemek.

## Kararlar
1. **Eğitim/etiket referansı:** PZEM-004T V3.0. SCT verisi PZEM okumalarıyla etiketleme/eğitim amacıyla kullanılacaktır.
2. **Kabul hedefi:** Model tahmini, karşılık gelen geçerli PZEM akım okumasından **±%4 bağıl sapma** içinde kalırsa sonuç `OK` sayılır.
3. **Python kararı:** Her geçerli değerlendirme örneğinde bağıl sapma hesaplanır; `abs(prediction - pzem_current) / abs(pzem_current) <= 0.04` ise `OK`, değilse `OUT_OF_RANGE` olarak işaretlenir. Eşik dâhildir; tam %4 sapma `OK` olur.
4. **Geçerli aralık:** PZEM okuması geçerli olmalı ve yüzde hesabında payda sıfır olmamalıdır. Geçersiz PZEM okumaları veya sıfır akım değeri bu yüzde kuralıyla sınıflandırılmaz; ayrı geçersiz/hesaplanamaz durum olarak tutulur.
5. Bu hedef, modelin PZEM okumalarına uyumunu ölçer; mutlak ölçüm doğruluğu veya PZEM'in kusursuz referans olduğu iddiası değildir.
6. Kararlı alanları bulma, SCT istatistiklerini çıkarma ve PZEM/SCT alanlarını eşleştirme bu görevin kapsamında değildir; ilgili görev ve deneylerde ele alınır.

## Kabul ölçütü
±%4 hedefi, `OK` karar kuralı ve geçersiz/sıfır referans değerlerinin ele alınışı dokümante edilmiştir.

## İlgili dosyalar
- [Proje kapsamı](../docs/00-scope.md)
- [Hedef mimari](../docs/architecture/sct-pzem-labeling-and-calibration.md)
