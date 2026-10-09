# Hesaplama-3 — DC ortalama ve AC RMS ayrımı

ACS758 hem AC hem DC akım ölçebilir. Hesaplama yöntemi ölçülen akım türüne göre seçilmelidir.

## DC akım

Örneklerin ortalama çıkış gerilimi:
`Vmean = sum(V[i]) / N`

Ofset farkı:
`deltaV = Vmean - V0`

050B için:
`I_DC ≈ deltaV / 0.040`

050U için:
`I_DC ≈ deltaV / 0.060`

İşaret, çift yönlü 050B'de akım yönünü gösterir. Tek yönlü 050U'da negatif akım ölçümü desteklenen aralık dışında olabilir.

## AC akım

Önce DC ofseti kaldır, sonra RMS:
`V_AC_RMS = sqrt(sum((V[i] - Vmean)^2) / N)`

Ardından nominal duyarlılıkla:
`I_AC_RMS ≈ V_AC_RMS / S`

Burada Vmean, pencere ortalamasıdır; DC akım bileşeni varsa bu işlem AC bileşeni ondan ayırır. Toplam AC+DC RMS isteniyorsa tanımı ve hesap yöntemi ayrıca belirlenmelidir.

## Örnek

050B, S=0.040 V/A, V0=2.500 V varsayalım:
- DC çıkış ortalaması 2.700 V ise I ≈ +5 A.
- Sinüzoidal AC çıkışın ofset çıkarılmış RMS'i 0.400 V ise I_AC,RMS ≈ 10 A.

Bunlar ideal nominal duyarlılıkla hesap örnekleridir; gerçek sensör ofseti ve hassasiyeti kalibrasyonla belirlenir.

## Örnekleme notu

Örnek sayısı tek başına örnekleme hızı değildir. Her örneğin zaman damgası ve gerçek aralığı kaydedilmeli. AC dalga biçiminde yetersiz örnekleme, aliasing, düzensiz örnek aralığı ve analog kırpılma RMS sonucunu bozar.
