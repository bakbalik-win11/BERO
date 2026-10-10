# GRV-004 — ALT-GÖREV-04: ORT hesabının bağımsız doğrulanması

- Tarih: 2026-10-10
- Durum: Açık — henüz uygulanmadı
- Önceki kayıt: [Sürekli ADC sonuçları, STD öncesi sürüm](ALT-GOREV-03-MIN-MAX-ORT-LOG-20261010.md)

## Amaç

Dört kanalın ORTALAMA (aritmetik ortalama) değerini ham örneklerden bilgisayarda bağımsız hesaplamak ve önceki ESPHome logundaki `avg` değerleriyle karşılaştırmak.

## Kapsam ve sınırlar

- ESP adı ve pinler değiştirilmez.
- Bu alt görevde ESP32'ye yeni ortalama/RMS algoritması eklenmesi hedeflenmez.
- Önceki kod ve log değiştirilmez; bu yeni, ayrı bir alt görevdir.
- Ham örnek verisi mevcut değil. `esp32d1-logs (11).txt` dosyası yalnızca tur başına özet değerleri içeriyor. Bu nedenle bağımsız ORT hesabı henüz yapılamaz.

## İş sırası

1. Dört kanalın ham örneklerini ve zaman damgalarını ayrı bir deney çıktısı olarak dışarı aktar.
2. Ham veriyi bilgisayarda CSV olarak sakla.
3. Her kanal için `ORT = toplam örnek değeri / örnek sayısı` hesabını bağımsız yap.
4. Her kanalın örnek sayısını da raporla; hedef kanal başına 1000 örnektir.
5. Bilgisayarda bulunan ORT ile ESPHome logundaki avg değerlerini karşılaştır.
6. Farkları ve kullanılan veri/kod sürümlerini rapora yaz.

## Kabul ölçütleri

- Her kanal için ham örnek sayısı açıkça görülür.
- ORT hesabı ham örneklerden bilgisayarda yeniden üretilebilir.
- Önceki cihaz logundaki avg ile karşılaştırma yapılır.
- Önceki deney kayıtlarının üzerine yazılmaz.

## İlk durum

**Bekleyen girdi:** Ham örnekler ve zaman damgaları. Mevcut özet logdan ham veriler geri üretilemez.
