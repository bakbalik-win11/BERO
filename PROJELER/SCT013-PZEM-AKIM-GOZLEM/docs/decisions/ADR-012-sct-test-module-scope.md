> **Sonraki karar / güncel uygulama:** ADR-012 ilk taslakta ESP32D2 ve ESP besleme yöntemini açık bırakmıştı. 2026-10-31 tarihli [ADR-015](ADR-015-module2-esp32d1-triple-sct.md) ile Modül 2'nin gömülü ESPHome kimliği `esp32d1`, harici 5 V besleme ve PC USB erişimi olarak güncellendi. ADR-012 tarihsel kapsam kararını korur; ESP kimliği ve besleme bakımından ADR-015 geçerlidir.

# ADR-012 — SCT Okuma Test Modülü kutu kapsamını sadeleştirme

- **Tarih:** 2026-10-31
- **Durum:** KABUL EDİLDİ
- **Karar sahibi:** Kullanıcı
- **Karar:** Modül 2 kutusu yalnızca üç SCT girişi, ESP32D2 ve bias mini breadboard içerecek.

## Bağlam

Modül 2 için daha önce 220 V AC girişi, PZEM beslemesi, ESP'yi besleyecek 5 V güç kaynağı, SSR güç devresi ve anahtarlanan 220 V AC çıkışı konuşulmuştu. Kullanıcı bu kapsamdan vazgeçti ve kutuyu SCT okuma birimi olarak sadeleştirdi.

## Karar

Modül 2 kutusunda yalnızca şu bileşenler bulunur:
1. Üç adet 3,5 mm dişi SCT girişi.
2. ESP32D2.
3. Ortak bias devresini taşıyan mini breadboard.

Bu kutuda 220 V AC giriş/çıkış, PZEM, SSR veya ESP için kutu içi 220 V → 5 V güç kaynağı bulunmaz. PZEM ve SSR BERO sisteminin diğer bölümlerinde ayrı ele alınacaktır.

Bias devresi ayrı BERO-BIAS-TRAFOSU-001 modülünden beslenecektir. ESP32D2'nin besleme yöntemi ve kutu dışı düşük gerilim bağlantısı henüz kararlaştırılmamıştır.

## Sonuç ve sınırlar

- Önceki Modül 2 taslağındaki şebeke, PZEM ve SSR bölümleri bu kutu için geçersiz kılındı; tarihçe bu ADR ile korunur.
- Üç SCT girişinin eşzamanlı kullanımı veya ilk testte kullanılacak kanal sayısı kararlaştırılmış değildir.
- Fiziksel kablolama, jack pin eşlemesi ve besleme bağlantıları doğrulanmış değildir.
- Bu karar diğer BERO modüllerinin PZEM/SSR kapsamını iptal etmez.
