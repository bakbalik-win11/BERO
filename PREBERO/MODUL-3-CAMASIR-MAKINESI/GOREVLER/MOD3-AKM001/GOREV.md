# MOD3-AKM001 – V1.6 uzun pamuklu program saha testi

- **Durum:** KAPANDI
- **Tarih:** 2026-11-22
- **Amaç:** Modül 2'den devralınan V1.6 akım ölçüm kodunun gerçek çamaşır makinesinde uzun program boyunca çalışmasını ve PZEM akım referansıyla karşılaştırmalı kayıt üretmesini doğrulamak.

## Kapsam

- ESP32D2 / SCT013 / V1.6 akım kaydı.
- Modül 3 WROOM / PZEM akım, aktif güç, gerilim ve PF kayıtları.
- Uzun pamuklu programın başlangıçtan bitişe gözlemi.

PF sensörü geliştirme, ZMPT101B entegrasyonu, ses/titreşim entegrasyonu ve otomatik program sınıflandırması bu görevin kapsamında değildir.

## Sonuç

V1.6 kodu yaklaşık 78 dakikalık gerçek program boyunca çalıştı ve veri kaydetti. Isıtma bloğunda PZEM ile yakın akım takibi; ısıtma sonrası düşük akım bölümlerinde pozitif fark gözlendi. Ayrıntılı sonuç ve yöntem sınırları:

`RAPOR/MOD3-AKM001-V1.6-UZUN-PAMUKLU-SAHA-TESTI-2026-11-22.md`

## Kapanış kararı

Görevin ana amacı yerine getirildiği için MOD3-AKM001 kapatıldı. V1.6 değiştirilmedi. PF farkının nedeni bu deneyle kanıtlanmadı. ZMPT101B fikri ayrı ve geleceğe dönük araştırma olarak kaldı.
