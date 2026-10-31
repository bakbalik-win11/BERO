# BERO — Mimari

Bu klasör, BERO'nun tek bir sensör veya deneyden bağımsız, tekrar kullanılabilir mimari ilkelerini tutar.

## Ana mimari

- [Pencereli sensör analizi ve davranış çıkarımı](PENCERELI-SENSOR-ANALIZI/README.md) — veri toplama, özellik çıkarma ve davranış çıkarımı katmanları; veri sözleşmesi, pencere türleri, sensör adaptörleri ve uygulama kuralları.

## Mimari ile uygulama arasındaki sınır

- **MIMARI/**: Sensörlerden bağımsız ilkeler, ortak veri akışı, arayüzler ve tasarım kararları.
- **PROJELER/**: Bu ilkelerin belirli donanım ve kullanım senaryolarında uygulandığı projeler.
- **DONANIM/** ve **ENVANTER/**: Fiziksel donanım ve stok kayıtları.

Mimari belgelerde bir sensöre ait pin, katsayı veya özel algoritma evrensel kural olarak tanımlanmaz. Uygulama kanıtları kendi proje klasörlerinde tutulur; mimari belge bunlara bağlantı verir.

## İlk uygulama

[SCT013 + PZEM akım gözlem sistemi](../PROJELER/SCT013-PZEM-AKIM-GOZLEM/README.md), pencereli sensör analizinin ilk somut uygulamasıdır. Buradaki deneyler mimariyi besler; ancak SCT'ye özgü sonuçlar diğer sensörlere doğrudan genellenmez.

## Durum

Bu klasör mimari tasarım ve yönlendirme kaydıdır. Burada tanımlanan genel davranış sınıflandırma sistemi henüz tamamlanmış/çalışan bir ürün değildir. Her uygulama, kod, derleme ve gerçek donanım kanıtıyla ayrı doğrulanır.
