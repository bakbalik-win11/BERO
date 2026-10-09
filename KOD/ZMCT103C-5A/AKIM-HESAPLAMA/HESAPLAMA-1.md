# Hesaplama-1 — Bias çıkarma ve RMS

İdeal 12-bit MCP3208 yaklaşımı: VADC = raw × VREF / 4095. Gerçek VREF ve ADC aktarım hataları kalibrasyonda hesaba katılmalıdır.

Örnek gerilimlerinin ortalaması:
mean = sum(V[i]) / N

AC bileşen RMS:
V_AC_RMS = sqrt(sum((V[i] - mean)^2) / N)

Bu, ADC girişindeki AC bileşenidir. Giriş bölücü/op-amp varsa devre oranı uygulanmalıdır.

Çıplak CT ve bilinen dirençli burden için:
I_primary_RMS ≈ V_burden_RMS × 1000 / R_burden

Örnek: R=100 Ω ve burden üzerinde 0,50 V RMS ölçülürse I ≈ 0,50 × 1000 / 100 = 5 A. Nominal oran ve ideal burden varsayımıdır; gerçek devre yüklemesi ve kalibrasyon sonucu etkiler.