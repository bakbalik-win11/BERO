# STEP-001 — ADC yöntemi, kod adayı ve derleme

**Durum:** AÇIK — kod adayı bulundu; derleme bekliyor.

## Yapılacaklar
1. GRV-008.2 ESP32-WROOM aday kodunu ve Arduino-ESP32/ESPHome hedef uyumunu incele.
2. Frame yapısı, binary paket boyu, ADC kanal sırası, tampon sahipliği ve overflow davranışını kontrol et.
3. ESP32-WROOM hedefinde derle; sonucu ve kullanılan sürümleri logla.
4. Derleme hatası varsa yalnızca kanıtlanan hataları düzelt; eski adayı koru ve yeni sürüm oluştur.

İlgili kod: `../KOD/GRV-008.2_candidate.ino` ve `../KOD/grv008_test_receiver.py`.

Başarı kanıtı: derleme sonucu ve sürüm bilgileri. Fiziksel test bu step'in tamamlanma kanıtı değildir; ayrıca kaydedilir.


# STEP-001 — ADC yöntemi, kod adayı ve derleme

**Durum:** AÇIK

## Amaç
Mevcut GRV-008.2 adayını kullanarak tek ESP32-WROOM için ADC yakalama yolunu ve derlenebilir firmware'i doğrulamak.

## Planlanan işler
1. Mevcut aday kodunu ve hedef kart/Arduino-ESP32 sürümünü kontrol et.
2. ADC Continuous yapılandırmasını, kanal sırasını ve örnek sayısını incele.
3. DMA/callback, buffer sahipliği, frame ID/marker ve overflow sayacı davranışını incele.
4. ESP32-WROOM hedefinde derle; tam derleme çıktısını LOG'a kaydet.
5. Gerekirse yalnızca doğrulanmış hataları düzelt; eski sürümü koruyup yeni sürüm oluştur.

## Tamamlanan işler
- Henüz tamamlanan iş kaydedilmedi.

## Kapanış ölçütü
Derleme sonucu ve kullanılan sürümler kaydedilmiş; başarılı derleme kanıtlanmış. Bu tek başına donanım testi değildir.

## Çalışma kaydı
Her tamamlanan işin tarihi, kullanılan kod sürümü, test sonucu ve kanıt bağlantısı aşağıya alt alta eklenecek. Step ancak kapanış ölçütü kanıtlandığında kapatılacak.

