# STEP-003 — Mac'e aktarım ve veri bütünlüğü

**Durum:** BEKLİYOR

- Python alıcısını Mac Mini'deki gerçek seri porta göre yapılandır.
- Binary frame başlangıç/bitiş marker'larını ve beklenen frame boyunu doğrula.
- Frame sayısı, ID sırası, eksik/bozuk frame ve aktarım taşmalarını raporla.
- Ham örnekleri CSV olarak sakla; kaynak binary kaydı korunur.

Başarı kanıtı: gerçek cihazdan alınan kayıt, parser çıktısı ve bütünlük kontrolü.


# STEP-003 — Mac'e aktarım ve veri bütünlüğü

**Durum:** BEKLİYOR

## Amaç
ESP'den Mac Mini'ye gelen binary frame'leri doğrulayıp ham veriyi dosyaya almak.

## Planlanan işler
1. Python alıcısında gerçek seri portu seç.
2. Frame marker'larını, frame boyunu ve frame ID sırasını doğrula.
3. Eksik/bozuk frame ve taşma sayılarını raporla.
4. Ham veriyi CSV'ye çıkar; orijinal binary kaydı da koru.

## Tamamlanan işler
- Henüz tamamlanan iş kaydedilmedi.

## Kapanış ölçütü
Gerçek aktarım kaydı, parser çıktısı ve bütünlük sonucu saklanmış.

## Çalışma kaydı
Her tamamlanan işin tarihi, kullanılan kod sürümü, test sonucu ve kanıt bağlantısı aşağıya alt alta eklenecek. Step ancak kapanış ölçütü kanıtlandığında kapatılacak.

