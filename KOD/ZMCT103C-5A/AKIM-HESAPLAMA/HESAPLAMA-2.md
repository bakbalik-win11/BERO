# Hesaplama-2 — Burden direnci ve primer akımı

ZMCT103C nominal oranı 1000:1'dir. 5 A primerde sekonder yaklaşık 5 mA olur.

V_burden_RMS = I_secondary_RMS × R_burden
I_primary_RMS ≈ (V_burden_RMS / R_burden) × 1000

| Burden | 5 mA ile ideal gerilim |
|---:|---:|
| 50 Ω | 0,25 V RMS |
| 100 Ω | 0,50 V RMS |
| 200 Ω | 1,00 V RMS |

Üretici datasheet'i 5 A test koşulunda 50 Ω belirtir. Burden değerini büyütmek sekonder gerilimini artırır ama doğruluk ve CT yük koşullarını değiştirebilir.

**Güvenlik:** Primer akım geçerken sekonderi açık devre bırakma. Bağlantıyı enerji kesikken yap; akım uygulanmadan önce burden'ın bağlı olduğunu doğrula. ADC'nin negatif AC yarım dalgasını doğrudan ölçemeyeceğini unutma.