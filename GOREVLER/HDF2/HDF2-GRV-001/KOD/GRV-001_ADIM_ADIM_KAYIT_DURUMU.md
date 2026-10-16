# HDF2-GRV-001 — Adım Adım Kod ve Test Kaydı
**Güncelleme:** 2026-10-16  
**Kural:** Her adımın kodu, logu ve açıklaması bu görev altında tutulur. Kod adı ve dosya yolu geri okunup doğrulanmadan "depoya kaydedildi" denmez. Test yapılmadıysa PASS yazılmaz.

## Adımlar
| Adım | İçerik | Durum | Kayıt / not |
|---|---|---|---|
| 1.1 | ESP32 dahili ADC temel `analogRead` kontrolü | Bu kayıtta kanıt eksik | Kaynak kod ve gerçek log dosyası bulunup bağlanmalı |
| 1.2 | SCT + BIAS ham veri okuma | Bu kayıtta kanıt eksik | Kaynak kod ve gerçek log dosyası bulunup bağlanmalı |
| 1.3 | Timer, sabit örnekleme, ping-pong buffer | Tasarım konuşuldu; doğrulanmış test kaydı yok | Aday kod/log bulunup bağlanmalı |
| 1.4 | ADC Continuous + DMA | Copilot örneği/önerisi konuşuldu; kaynak ve test sonucu burada doğrulanmadı | Aday kod/log bulunup bağlanmalı |
| 1.5 | Paket numarası, sınırlar, örnek sayısı ve zaman bilgisi | Doğrulanmış kod/log bu klasörde yok | Kaynak kod ve log bulunup bağlanmalı |
| 1.6 | Gerçek dalga / osiloskop testi | Bugün test yapıldığına dair doğrulanmış kayıt yok | Osiloskop örnekleri ve gerçek test logu bulunup bağlanmalı |
| 1.7 | DS3231 / RTC sürekliliği | DS3231 iletişim/yazma sorunu açık | RTC test kodu ve logu ayrı kayıtlanmalı |

## İlgili mevcut dosya adları
- `GRV-008.2_candidate.ino` — önceki GRV-008 raporunda aday dosya olarak anılmıştır; bu klasörde kaynak içeriği doğrulanmadı.
- `grv008_test_receiver.py` — önceki GRV-008 raporunda aday dosya olarak anılmıştır; bu klasörde kaynak içeriği doğrulanmadı.

## Önemli ayrım
Bu indeks, eksik kayıtları görünür kılmak içindir; kayıp kodun yerine geçmez. Orijinal osiloskop örnekleri ve loglar bulunmadan yeni kaynak kod yazılmış veya test yapılmış gibi işaretlenmeyecektir. Her adım tamamlandığında aynı numara ile kaynak kod, açıklama, ham log ve test sonucu eklenmelidir.
