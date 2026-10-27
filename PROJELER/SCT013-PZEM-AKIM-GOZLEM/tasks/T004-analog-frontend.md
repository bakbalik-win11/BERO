# T004 — Analog ön uç

- **Durum:** PLANLANDI
- **Faz:** 1.1
- **Bağımlılık:** T002 ve T003
- **Hedef:** Kullanılan SCT bağlantısını ve breadboard bias devresini hobi projesi için yeterli ayrıntıda kaydetmek.

## Yapılacak
1. hardware/frontend.md içinde kullanılan SCT modelini/çıkış türünü ve mevcut breadboard bias devresini kaydet.
2. Bias seviyesi yaklaşık **1,65 V** kabul edilir. Kullanıcı bu seviyeyi yaygın ve tecrübeyle bilinen bir uygulama olarak belirtti; bias seviyesini ayrıca ölçüp doğrulamak bu aşamanın şartı değildir.
3. Testler başladığında bias, SCT ham ölçümünden ayrı bir kanal/kayıt alanı olarak kaydedilecek. Bu, yazılım ve veri kaydı aşamasında yapılır; T004 ön koşulu değildir.
4. Bu aşamada ESP32'nin dahili ADC'si kullanılacak; harici ADC ve MCP3208 sonraki aşamaya ayrılmıştır. ADC çözünürlüğü ve VREF kaydı bu görevin şartı değildir.
5. Belirgin bağlantı sorunu görülürse not et. Beklenen maksimum sinyal, clipping payı, toleranslar ve ADC giriş aralığı için laboratuvar düzeyinde hesap/ölçüm bu görevin kapanış şartı değildir.

## Kabul ölçütü
Kullanılan SCT modeli ve breadboard bias devresi kaydedilmiş, bias'ın testlerde ayrı kanal/kayıt alanı olarak tutulacağı not edilmiş olmalıdır. Laboratuvar düzeyinde bias ölçümü veya ADC aralığı/clipping hesabı gerekmiyor.

## Çıktı
- hardware/frontend.md

## Güvenlik
Hobi düzeyinde temel elektrik güvenliği ve sağduyulu bağlantı kontrolü uygulanır. Enerjili devrede bağlantı değiştirme veya açık iletkenlere dokunma.
