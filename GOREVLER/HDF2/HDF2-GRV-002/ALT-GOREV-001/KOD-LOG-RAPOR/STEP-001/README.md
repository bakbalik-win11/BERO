# STEP-001 — ADC yöntemi, kod adayı ve derleme

**Durum:** AÇIK — kod adayı bulundu; derleme bekliyor.

## Yapılacaklar
1. GRV-008.2 ESP32-WROOM aday kodunu ve Arduino-ESP32/ESPHome hedef uyumunu incele.
2. Frame yapısı, binary paket boyu, ADC kanal sırası, tampon sahipliği ve overflow davranışını kontrol et.
3. ESP32-WROOM hedefinde derle; sonucu ve kullanılan sürümleri logla.
4. Derleme hatası varsa yalnızca kanıtlanan hataları düzelt; eski adayı koru ve yeni sürüm oluştur.

İlgili kod: `../KOD/GRV-008.2_candidate.ino` ve `../KOD/grv008_test_receiver.py`.

Başarı kanıtı: derleme sonucu ve sürüm bilgileri. Fiziksel test bu step'in tamamlanma kanıtı değildir; ayrıca kaydedilir.
