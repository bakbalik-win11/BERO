# STEP-003 — Mac'e aktarım ve veri bütünlüğü

**Durum:** BEKLİYOR

- Python alıcısını Mac Mini'deki gerçek seri porta göre yapılandır.
- Binary frame başlangıç/bitiş marker'larını ve beklenen frame boyunu doğrula.
- Frame sayısı, ID sırası, eksik/bozuk frame ve aktarım taşmalarını raporla.
- Ham örnekleri CSV olarak sakla; kaynak binary kaydı korunur.

Başarı kanıtı: gerçek cihazdan alınan kayıt, parser çıktısı ve bütünlük kontrolü.
