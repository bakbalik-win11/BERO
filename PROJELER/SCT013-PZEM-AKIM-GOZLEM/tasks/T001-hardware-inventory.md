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
1. **Sensör önceliği belirlenmiştir:** bu projede önce SCT013-030 (30 A / 1 V) kullanılacak. SCT013-100A-1V stokta alternatif olarak kalacak. Yeniden sensör seçimi sorma; kullanıcı tarafından bildirilen stok miktarlarını `hardware/inventory.md` içinde kaynak türüyle birlikte tut. Bu oturumdaki sensör görseli depo içinde kalıcı fotoğraf dosyası değildir; T001 tamamlanmadan önce gerçek parçayı gösteren kanıt varsa onu bağla, yoksa fotoğrafı `hardware/photos/` altına ekle.
2. PZEM referans belgesini kullan. Bu projedeki modülün 10 A dahili şöntlü mü yoksa 100 A harici CT'li mi olduğunu ve harici CT modelini mevcut kayıtlarla doğrula. Eksikse bilinmiyor olarak işaretle; genel kılavuzu tekrar araştırma.
3. MCU kartı ile ADC modelini/revizyonunu ve VREF değerini mevcut BERO kayıtlarından bu fiziksel düzeneğe kadar izlenebiliyor mu diye kontrol et. Proje için kanıt yoksa bilinmiyor olarak bırak.
4. Burden, bias bölücüsü, filtre ve kablolama değerlerini önceki devre kaydı varsa ona bağla; bu kurulumun farklı olabileceği durumda ölçülmemiş değerleri aktarma.
5. “Bias trafosu” alt devresini envantere kaydet: RN130421 6 V AC / 2,0 VA trafo + KBU6M 6 A / 1000 V köprü doğrultucu + L78L33 TO-92 korunaklı kutuda; 2 × 10 kΩ ile yaklaşık 1,65 V bias bölücü ayrı breadboardda. Bu yerleşim kullanıcı beyanıdır; fiziksel şema/fotoğrafla doğrulanmış gibi sunma.
6. KBU6M köprüsünden L78L33 girişine kadar kullanılan filtre kondansatörünün değerini/konumunu ve regülatör giriş/çıkış bypass kondansatörlerini varsa kaydet. Ardından 3,3 V/GND’nin ayrı breadboarddaki bölücüye nasıl taşındığını ve SCT sinyalinin bias düğümüne hangi bağlantıyla eklendiğini netleştir. “Şebeke dalgalanmasını biasa aynı motifle yansıtma” niyetini, şema ve ölçüm olmadan doğrulanmış sonuç olarak yazma.
7. Stokta bulunduğu bildirilen 100 nF / 50 V seramik kondansatörlerin adedini envanterde tut. Gerçek devrede yeri ve amacı belirlenmeden analog filtre veya bypass elemanı olarak atanmış sayma.
8. True-RMS referans cihazını ve en az üç yük seviyesi adayını kaydetmek için mevcut önceki kayıtları kullan; bilgi yoksa bunu T003'e bırak.
9. `hardware/inventory.md` içindeki her alan için kanıt yolu ve doğrulama tarihini yaz. Bulunamayan alanı “BİLİNMİYOR” veya “HENÜZ BULUNAMADI” diye işaretle ve sıradaki kanıt adımını belirt.

## Kabul ölçütü
Her envanter satırı ya önceki/var olan kanıta bağlanmıştır ya da neden hâlâ bilinmediği ve sıradaki somut kanıt adımı açıkça yazılmıştır. Kullanıcı tarafından bildirilen parça değerleri/yerleşimi, tam şema veya ölçüm kanıtı olmadan fiziksel bağlantı ve performans doğrulaması sayılmaz.

## Çıktı / dokunulacak dosyalar
- hardware/inventory.md
- Gerekiyorsa hardware/photos/
- Gerekirse docs/open-questions.md

## Güvenlik
Bu görev yalnızca mevcut kayıt incelemesi ve görsel envanter işidir. Şebeke bağlantısını sökme, kabloyu ayırma veya sisteme enerji verme.
