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


## BERO'nun kapsamı: çoklu sensörlü ev gözlem sistemi

BERO tek bir akım ölçer veya yalnızca SCT013 projesi değildir. Hedef, farklı fiziksel değişkenleri ölçen sensörlerin ortak bir gözlem ve davranış çıkarımı çatısı altında bir araya gelmesidir. Akım ölçümü bu sensörlerden yalnızca biridir; AC akımın yanında uygun sensör ve ölçüm ön ucuyla DC akımın izlenmesi de olası kullanım alanıdır.

Kullanıcının belirttiği mevcut/planlanan sensör örnekleri:
- Su kuyusunda sıcaklık değişimini izleyen sensör.
- Kuyudaki basınçtan su seviyesini/su derinliğini çıkaran basınç sensörü.
- Evin girişinde şehir şebekesi su basıncını ölçen sensör.
- Elektriksel yüklerin AC akımını izleyen SCT tabanlı ölçüm; uygun donanımla DC akım ölçümü de.

Bu sensörler aynı fiziksel büyüklüğü ölçmez ve aynı algoritmayı kullanmaz. Her sensör kendi birimi, kalibrasyonu, örnekleme aralığı, geçerlilik kontrolü ve özellik çıkarma yöntemiyle ele alınır. Ortak BERO mimarisi, bu farklı ölçümleri zaman ve kaynak kimliği korunarak bir araya getirip daha üst düzey davranışlar hakkında çıkarım yapmayı hedefler.

## Geliştirme ortamı ile canlı kurulumun ayrımı

Şu anki SCT013-PZEM çalışması, kullanıcının diğer evde yürüttüğü hazırlık/geliştirme çalışmasıdır. Bu ortamda ölçüm zinciri, veri toplama, arşivleme ve analiz yöntemleri hazırlanıp doğrulanmaktadır. Kullanıcı açıkça belirtmiştir: şu anda canlı BERO kurulumunda çoklu sensörlerle birlikte çalışan bir uygulama yürütülmemektedir.

Dolayısıyla yukarıdaki çoklu sensör örnekleri BERO'nun sistem kapsamını ve hedeflenen sensör ailesini açıklar; mevcut canlı sistemde bu sensörlerin entegre olduğu veya ortak algoritmayla çalıştığı anlamına gelmez. Sensör entegrasyonları aşamalı ve ayrı ayrı doğrulanacaktır.
