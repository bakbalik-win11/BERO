# T004 — Analog ön uç

- **Durum:** TAMAMLANDI
- **Faz:** 1.1
- **Bağımlılık:** T002 ve T003
- **Hedef:** Kullanılan SCT bağlantısını ve breadboard bias devresini hobi projesi için yeterli ayrıntıda kaydetmek.

## Tamamlananlar
- `hardware/frontend.md` içinde mevcut breadboard bias devresi ve ESP32 dahili ADC yaklaşımı belgelendi.
- Bias seviyesi yaklaşık **1,65 V** kabul edildi. Bu aşamada ayrıca ölçülüp doğrulanması gerekmiyor.
- Bias'ın testler başladığında SCT ham ölçümünden ayrı bir kanal/kayıt alanı olarak tutulacağı not edildi. Bu, yazılım ve veri kaydı aşamasında yapılacak; T004 ön koşulu değil.
- Envanterdeki SCT013-030 ve SCT013-100A-1V modelleri belgelendi. Kullanılacak model test bazında belirtilecek; tüm testler için tek model önceden sabitlenmedi.
- ESP32'nin dahili ADC'si kullanılacak; harici ADC ve MCP3208 sonraki aşamaya ayrıldı.

## Kabul ölçütü
Hobi projesi için mevcut bias devresi, ADC yaklaşımı ve eldeki SCT modelleri belgelendi. Laboratuvar düzeyinde bias ölçümü, ADC aralığı/clipping hesabı, tolerans analizi veya gürültü ölçümü bu görevin kapanış şartı değildir.

## Çıktı
- `hardware/frontend.md`

## Güvenlik
Hobi düzeyinde temel elektrik güvenliği ve sağduyulu bağlantı kontrolü uygulanır. Enerjili devrede bağlantı değiştirilmez ve açık iletkenlere dokunulmaz.
