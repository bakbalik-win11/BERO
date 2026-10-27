# T001 — Fiziksel donanım envanteri

- **Durum:** PLANLANDI
- **Faz:** 0.1
- **Bağımlılık:** Yok
- **Hedef:** Önceki BERO donanım kayıtlarını tekrar yazmadan kullanarak bu projede seçilen gerçek konfigürasyonu ve yalnızca eksik kalan proje-özel bilgileri kaydetmek.

## Önceden mevcut referanslar
- [SCT013-100A-1V teknik kayıt ve geçmiş notlar](../hardware/references/SCT013-100A-1V.md)
- [SCT013-30A-1V teknik kayıt ve geçmiş notlar](../hardware/references/SCT013-30A-1V.md)
- [PZEM-004T V3.0 teknik kayıt ve geçmiş haberleşme notu](../hardware/references/PZEM-004T-V3.0.md)
- [Referans kopyalarının kaynakları ve kullanım notu](../hardware/references/README.md)

Bu belgelerdeki genel teknik özellikleri yeniden yazma. Kaynak veya önceki proje kaydı mevcut bir bilgiyi gerçekten doğruluyorsa envanterde dosya/kanıt bağlantısını kullan. Genel ürün belgesi, yeni projede hangi fiziksel parçanın kullanıldığını tek başına göstermez.

## Yapılacak
1. Mevcut SCT referansları üzerinden bu projede kullanılacak varyantı belirle: SCT013-100A-1V mi, SCT013-30A-1V mi? Önceki proje kayıtlarında aynı fiziksel cihazın modelini doğrulayan kanıt varsa tekrar fotoğraf istemek yerine o kanıtı bağla. Kanıt yoksa yalnız model etiketini gösteren fotoğraf gerekebilir.
2. PZEM referans belgesini kullan. Bu projedeki modülün 10 A dahili şöntlü mü yoksa 100 A harici CT'li mi olduğunu ve harici CT modelini mevcut kayıtlarla doğrula. Eksikse bilinmiyor olarak işaretle; genel kılavuzu tekrar araştırma.
3. MCU kartı ile ADC modelini/revizyonunu ve VREF değerini mevcut BERO kayıtlarından bu fiziksel düzeneğe kadar izlenebiliyor mu diye kontrol et. Proje için kanıt yoksa bilinmiyor olarak bırak.
4. Burden, bias bölücüsü, filtre ve kablolama değerlerini önceki devre kaydı varsa ona bağla; bu kurulumun farklı olabileceği durumda ölçülmemiş değerleri aktarma.
5. True-RMS referans cihazını ve en az üç yük seviyesi adayını kaydetmek için mevcut önceki kayıtları kullan; bilgi yoksa bunu T003'e bırak.
6. `hardware/inventory.md` içindeki her alan için kanıt yolu ve doğrulama tarihini yaz. Bulunamayan alanı “BİLİNMİYOR” veya “HENÜZ BULUNAMADI” diye işaretle ve sıradaki kanıt adımını belirt.
7. Yalnızca mevcut kayıtlar belirli fiziksel parça kimliğini kanıtlamıyorsa yeni fotoğraf ekle. Fotoğrafları `hardware/photos/` altına, açıklayıcı dosya adlarıyla koy; kişisel/özel bilgiyi kırp.

## Kabul ölçütü
Her envanter satırı, ya önceki/var olan kanıta bağlanmıştır ya da neden hâlâ bilinmediği ve sıradaki somut kanıt adımı açıkça yazılmıştır. Genel teknik referansların kopyalanması fiziksel donanım doğrulaması sayılmaz.

## Çıktı / dokunulacak dosyalar
- hardware/inventory.md
- Gerekiyorsa hardware/photos/
- Gerekirse docs/open-questions.md

## Güvenlik
Bu görev yalnızca mevcut kayıt incelemesi ve görsel envanter işidir. Şebeke bağlantısını sökme, kabloyu ayırma veya sisteme enerji verme.
