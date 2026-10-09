# Hesaplama-2 — VIOUT geriliminden amper

## Temel denklem

`I = (VOUT - V0) / S`

- VOUT: sensörün o andaki çıkış gerilimi.
- V0: gerçek sıfır akım ofseti.
- S: hassasiyet (V/A).

### ACS758LCB-050B

Üretici seçim tablosunda tipik 40 mV/A:
`I ≈ (VOUT - V0) / 0.040`

Örnek: V0=2.500 V ve VOUT=2.900 V ise:
`I ≈ (2.900 - 2.500) / 0.040 = +10 A`

### ACS758LCB-050U

Üretici seçim tablosunda tipik 60 mV/A ve tek yönlü 0…50 A:
`I ≈ (VOUT - V0) / 0.060`

**Varyantı doğrulamadan 0.040 veya 0.060 seçme.** Ofsetin tam olarak 2.500 V olduğu varsayılmamalı; gerçek V0 sıfır akımda ölçülmelidir.

## ADC raw kodundan gerilim

İdeal 12-bit ADC yaklaşımı:
`VADC ≈ raw × VREF / 4095`

Bu MCP3208 için yalnızca ilk yaklaşımdır. VREF ölçülmeli, ADC aktarım hatası kalibrasyonda değerlendirilmelidir. Sensör ile ADC arasında bölücü varsa:
`VOUT = VADC × (Rtop + Rbottom) / Rbottom`
bu denklem, Rtop'ın sensör çıkışından ADC düğümüne; Rbottom'ın ADC düğümünden GND'ye bağlı olduğu basit bölücü içindir. Gerçek devrede yükleme ve toleransları hesaba kat.

## Kalibrasyon

Sıfır akım ofsetini kaydet. Ardından birden çok bilinen akım noktasında referans ampermetreyle karşılaştır. İdeal doğrunun eğimi ve kesişimi ölçüm zinciri dahil belirlenebilir; nominal hassasiyet tek başına doğruluk garantisi değildir.
