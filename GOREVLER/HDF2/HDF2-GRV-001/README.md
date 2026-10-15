# HDF2-GRV-001 — Hedef 2 Test Donanımının Kurulması

**Amaç:** Hedef 2 kapsamında kullanılacak test donanımını fiziksel olarak kurmak, bağlantılarını düzenlemek ve ilk veri toplama testine hazır olduğunu belgelemek.

**Durum:** Açık — donanım kurulumu ve kontroller bekleniyor.  
**Kanıt durumu:** Klasör ve görev tanımı oluşturuldu; fiziksel kurulum veya testin yapıldığı iddia edilmiyor.

## Görev kapsamı

1. Testte kullanılacak donanımı masada belirlemek ve envanterini kaydetmek.
2. ESP32-WROOM tabanlı test düzeneğini, SCT sinyal girişini ve BIAS ölçüm noktasını hazırlamak.
3. Mevcut GRV-008.2 adayındaki bağlantı planıyla fiziksel bağlantıları karşılaştırmak: SCT ADC GPIO34, BIAS ADC GPIO35.
4. Besleme, ortak referans/GND, USB-seri bağlantısı ve kablo düzenini kontrol etmek.
5. Enerji vermeden önce bağlantıları gözden geçirmek; ilk enerjilendirmede anormal ısınma, kısa devre ve beklenmeyen davranış olmadığını kontrol etmek.
6. Kullanılan donanımın fotoğrafını/bağlantı notlarını ve kontrol sonuçlarını RAPOR/LOG altında kaydetmek.
7. Donanım hazır olduğunda bir sonraki aşama olan mevcut kodun derlenmesi ve TEST-001'e geçiş için hazır olma kararını vermek.

## Sınırlar

- Bu görev yeni bir örnekleme mimarisi veya yeni kod geliştirme görevi değildir.
- GRV-Freeze-1 gereği, önce mevcut aday ve test hattı kullanılacaktır.
- GRV-008.2 adayının derlenmiş olduğu varsayılmayacaktır.
- Fiziksel donanım kurulumu tamamlanmadan veya kanıtı kaydedilmeden PASS verilmeyecektir.
- Henüz gerçek akım/yük testi yapılmış gibi rapor yazılmayacaktır.

## Kabul ölçütleri

- [ ] Kullanılan donanım ve kablolar listelenmiş.
- [ ] SCT ve BIAS bağlantıları GPIO34/GPIO35 planıyla karşılaştırılıp kaydedilmiş.
- [ ] Besleme ve GND/referans bağlantıları kontrol edilmiş.
- [ ] USB-seri bağlantısı ve Mac Mini tarafındaki port tespiti için hazırlık yapılmış.
- [ ] Kurulum fotoğrafı veya eşdeğer bağlantı kaydı eklenmiş.
- [ ] Açık kalan riskler ve sonraki adım raporlanmış.

## Klasörler

- `KOD/` — mevcut aday kodun referansı ve kodla ilgili notlar; bu görevde yeni kod üretmek için değil.
- `RAPOR/` — donanım kurulum raporu ve kontrol listesi.
- `LOG/` — kurulum sırasında alınan gerçek kayıtlar.

## Sonraki adım

Donanım kurulumunu ve bağlantı kontrollerini kaydet. Ardından mevcut `GRV-008.2_candidate.ino` dosyasını ESP32-WROOM hedefi için derle. Derleme PASS olmadan cihaza yükleme veya fiziksel veri testi yapıldığını belirtme.
