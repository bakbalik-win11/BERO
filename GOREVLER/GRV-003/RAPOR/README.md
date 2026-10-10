# GRV-003 — Trafo Bias Yapısının Kurulması ve Doğrulanması

## Amaç

SCT013 akım ölçüm zincirinde kullanılan trafo bias yapısını ayrı bir görev olarak tanımlamak; devre yapısını, fiziksel bağlantıları ve ölçüm sonuçlarını diğer sensör testlerinden önce açıklığa kavuşturmak.

## Neden ayrı görev?

GRV-004 kapsamındaki ESP32D1 + PZEM + SCT013 birleşik deneyi, bias yöntemine bağlıdır. Bu nedenle bias kaynağı ve fiziksel uygulaması önce ayrı olarak belgelenmeli ve doğrulanmalıdır.

## Mevcut bilgi

- Bias yöntemi: Trafo bias kullanılıyor.
- ESP32 GPIO32, GPIO33 ve GPIO34 üzerinde fiziksel olarak 1,65 V okunduğu bildirildi.
- PZEM ve SCT013 sensörleri enerjiyi ESP32'den almıyor.

## Alt görevler

1. Trafo bias devresinin şema ve bağlantılarını belgelemek.
2. Bias seviyesini ölçmek ve kullanılan ölçüm noktasını kaydetmek.
3. Sonuçları ölçüm/log kanıtıyla doğrulamak.

## Durum

**Açık — belgeleme ve doğrulama sürüyor.** 1,65 V ölçüm bilgisi ön bulgudur; devre şeması ve ölçüm ayrıntıları henüz bu kayıtta bulunmuyor.
