# Hesaplama-1 — ADC raw → VIOUT → amper (5A)

İdeal 12-bit MCP3208 dönüşümü:

- V_ADC ≈ raw × VREF / 4095
- Basit direnç bölücüde k = R_alt/(R_üst + R_alt); VIOUT ≈ V_ADC/k
- I ≈ (VIOUT − V0) / 0.185

**Örnek (yalnızca ideal hesap):** V0=2,500 V, VIOUT=2.685 V ise I≈+1 A.

**Önemli:** V0 gerçek sıfır akımda ölçülmelidir. k=1 ancak güvenli ve gerçekten bölücüsüz bir ADC arayüzünde geçerlidir; ACS712'nin 5 V OUT'unu 3,3 V ADC'ye doğrudan bağlama. ADC VREF'i, kazanç/ofset hataları ve analog filtre ayrıca kalibre edilmelidir.
