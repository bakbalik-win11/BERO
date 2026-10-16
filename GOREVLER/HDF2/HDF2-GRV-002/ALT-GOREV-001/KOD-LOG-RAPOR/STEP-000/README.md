# STEP-000 — Görev ve kayıt yapısı

**Durum:** TAMAMLANDI

Bu step, Alt Görev 1'in kayıt klasörlerinin ve ilerleme raporu yapısının oluşturulmasını kapsar.

- `KOD/` — firmware ve Python kodları
- `LOG/` — derleme ve fiziksel test logları
- `RAPOR/` — step raporları ve ana ilerleme raporu

Kanıt: Alt görev klasörü ve kayıt dizini GitHub'da oluşturuldu.


# STEP-000 — Görev ve kayıt yapısı

**Durum:** TAMAMLANDI

## Amaç
Alt görev için step bazlı klasörleri ve ilerleme raporu bağlantılarını oluşturmak.

## Planlanan işler
1. KOD, LOG ve RAPOR kayıt düzenini belirle.
2. Step klasörlerini ve görev tanımlarını aç.
3. İlerleme raporunu step klasörlerine bağla.

## Tamamlanan işler
- [x] Step klasörleri oluşturuldu.
- [x] İlerleme raporu bağlantıları eklendi.

## Kapanış ölçütü
Kayıt düzeni ve step dizini mevcut.

## Çalışma kaydı
Her tamamlanan işin tarihi, kullanılan kod sürümü, test sonucu ve kanıt bağlantısı aşağıya alt alta eklenecek. Step ancak kapanış ölçütü kanıtlandığında kapatılacak.

## 2026-10-16 — PZEM / SSR / Home Assistant kayıtlarının doğrulanması

Öncelik, yüksek hızlı USB/ham veri testlerine geçmeden önce mevcut çalışan PZEM–SSR–Home Assistant zincirinin gerçek durumunu kanıtlamaktır. Kullanıcının sağlayacağı mevcut ESPHome YAML dosyaları ve loglar esas alınarak (1) PZEM ölçümlerinin Home Assistant'a ulaşıp güncellendiği, (2) SSR açma/kapama olaylarının nerede üretildiği ve nasıl kaydedildiği, (3) bu iki veri akışının ayrı ayrı zaman damgasıyla tutulup tutulmadığı, (4) SSR olayları ile PZEM ölçümlerinin aynı deney/olay kimliğiyle ilişkilendirilmeye uygunluğu ve (5) mevcut kayıtların kanıt olarak saklanması incelenecektir. Eksik kanıtlar varsayımla tamamlanmayacak; çalışan kodlar görülmeden değiştirilmeyecek. Gerekirse yalnızca doğrulanan eksik için kod değişikliği yapılacak; ilgili YAML/kod sürümü, test logu ve sonuç raporu STEP-000 altında saklanacaktır. Şu anki durum: YAML ve loglar kullanıcı tarafından henüz bu inceleme için sunulmadı; doğrulama yapılmış veya PASS alınmış sayılmaz.
