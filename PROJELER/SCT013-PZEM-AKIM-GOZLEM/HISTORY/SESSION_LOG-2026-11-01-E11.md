# 2026-11-01 — E11 üç SCT sıralı log analizi / oturum eki

- **DEPO OKUMASI:** STATUS, ROADMAP, T010, ADR-018, E11 README/YAML, SESSION_LOG ve 100 W yük kaydı incelendi.
- **KAYNAK:** `esp32d1-logs (64).txt`; 2.795 satır / 208.718 bayt; SHA-256 `97a36071b8319625df5e717b358c8ec69fea609be928ba71e6e3a5153c081484`.
- **ANALİZ:** 176 çevrim; her SCT için 176 akım ve Raw AC yayını; 176 bias yayını. İlk çevrim açılış verisi olarak ayrıldı. Sonraki 175 çevrim ortalamaları SCT1 0.42141 A, SCT2 0.42283 A, SCT3 0.42686 A; CV %1.98 / %2.36 / %2.09.
- **BIAS:** Ortalama 1.66022 V; min–maks 1.642–1.682 V.
- **ZAMANLAMA:** 159/176 çevrimde sıra geçişleri 200–300 ms aralığında; 17 çevrimde sapma. 12:01:07 çevriminde 16/454/392 ms anomali. Gerçek pencere çakışmasızlığı kesin kabul edilmedi; 50 ms pay korunacak.
- **ESKİ DENEY KIYASI:** LOAD-100W-004 SCT1 0.425 A ortalama / 0.423 A medyan; yeni SCT1 0.42141/0.420 A. Yeni logda fiziksel yük ve besleme koşulu bağımsız etiketli olmadığından koşullu kıyas.
- **REFERANS:** PZEM yok; 0.427 A geçici UNIT beklentisidir. K=24.22 değişmedi; kalibrasyon/±%4 sonucu verilmedi.
- **DOSYALAR:** [Analiz](../logs/module2/2026-11-01-e11-three-sct-sequential-analysis.md), [kanıt](../logs/module2/2026-11-01-e11-three-sct-sequential-evidence.txt), [maskelenmiş tam log](../logs/module2/2026-11-01-e11-three-sct-sequential-full-sanitized.txt).
- **SONRAKİ:** Zamanlama anomalisini kontrollü tekrar loguyla incele; T010 kabul kapıları kapanmadan T007/T008/T006'ya geçme.

