# T001 — Fiziksel donanım envanteri

- **Durum:** PLANLANDI
- **Faz:** 0.1
- **Bağımlılık:** Yok
- **Hedef:** Bu projede gerçekten kullanılacak SCT, PZEM, MCU/ADC ve analog ön uç bileşenlerini fiziksel kanıtla tanımlamak.

## Yapılacak
1. Elimizdeki parçaları bir araya getir; şebeke bağlantısını sökme veya enerji verme.
2. SCT üzerindeki tam model ve çıkış etiketini fotoğraflandır. Akım çıkışlı SCT013-000 ile gerilim çıkışlı varyantları birbirinin yerine varsayma.
3. PZEM kartının model/revizyon bilgisini ve CT üzerindeki model/sınıf işaretini ayrı fotoğraflandır.
4. MCU kartının model/revizyonunu, varsa ADC çip işaretini ve bilinen VREF bilgisini kaydet.
5. Burden direnci, bias bölücüsü, filtre ve kablolamaya ait görülebilen parçaları fotoğraflandır; değerler fiziksel olarak okunamıyorsa ölçülmüş gibi yazma.
6. hardware/inventory.md içindeki her alanı kanıt yolu ve doğrulama tarihiyle güncelle. Bulunamayan alanı “BİLİNMİYOR” veya “HENÜZ BULUNAMADI” diye işaretle ve sıradaki kanıt adımını belirt.
7. Fotoğrafları hardware/photos/ altına, açıklayıcı dosya adlarıyla ekle. Fotoğraflarda kişisel/özel bilgi varsa yüklemeden önce kırp.

## Kabul ölçütü
Her envanter satırı ya fiziksel kanıtla doğrulanmıştır ya da bilinmediği ve neden henüz doğrulanamadığı açıkça yazılmıştır. Satıcı sayfası veya eski BERO kaydı tek başına mevcut fiziksel parçanın kimliğini kanıtlamaz.

## Çıktı / dokunulacak dosyalar
- hardware/inventory.md
- hardware/photos/
- İlgili soru kapandıysa docs/open-questions.md

## Güvenlik
Bu görev yalnız görsel envanter ve mevcut etiketleri kaydetme işidir. Şebeke tarafını açma, kabloyu sökme veya sisteme enerji verme.
