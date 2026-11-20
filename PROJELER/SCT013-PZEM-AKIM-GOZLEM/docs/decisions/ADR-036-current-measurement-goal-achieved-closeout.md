# ADR-036 — Akım okuma hedefinin kapatılması

- **Tarih:** 2026-11-20
- **Durum:** KABUL EDİLDİ — eski çalışma kapatıldı
- **Karar sahibi:** Kullanıcı

## Karar
Önceki SCT013/PZEM akım okuma çalışması **KAPATILDI — HEDEFE ULAŞILDI**. Pratik hedef, SCT + ADS1115 ölçüm zinciriyle hedeflenen ev içi yük koşullarında akım okuyabilmekti. E19 kapsamında 18 W, 42 W, 57 W ve 150 W sabit yük karşılaştırmaları kaydedildi; raporlanan ortalama farklar ±%4 hedefinin içindedir. 100 W bağımsız doğrulama sayılmamıştır.

## Sınırlar
- PZEM karşılaştırma kaynağıdır; mutlak ground truth değildir.
- Sonuç tüm akım aralığına veya bütün sensör/ADC kartlarına genellenmez.
- ADS1115 analog giriş common-mode/GND–VDD güvenliği ve bias gerekliliği bu kapanışın kabul kapsamı değildir.
- Eski PZEM eğitim hattı, çok kanallı SCT, SSR/UDP olay mimarisi, 12 kanal genişleme ve eski Modül 5/6/7 tasarımları yeni aşamanın aktif hedefi değildir.

Eski deney, kod, log ve kararlar silinmez. Yeni geliştirme [PREBERO](../../PREBERO/README.md) altında baştan başlar.
