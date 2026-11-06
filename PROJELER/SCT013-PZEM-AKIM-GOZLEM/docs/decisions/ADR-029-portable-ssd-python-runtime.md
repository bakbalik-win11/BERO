# ADR-029 — Python çalışma ortamının taşınabilir SSD üzerinde tutulması

- **Durum:** KABUL EDİLDİ
- **Tarih:** 2026-11-06
- **Kapsam:** BERO Python-1 ve Python-2 çalışma ortamı, veri arşivi ve analiz çıktıları
- **İlgili görev:** [T007 — Home Assistant verisini PC'ye aktarma ve Python başlangıcı](../../tasks/T007-python-architecture.md)

## Bağlam

BERO Python programlarının iki farklı ARM64 bilgisayarda çalıştırılması hedeflenmektedir:
- Microsoft Surface 11 — Snapdragon X Elite, Windows.
- Mac mini 2024 — Apple M4, macOS.

Kullanıcının hedefi, BERO çalışma ortamını ve verilerini harici SSD üzerinde taşımak; SSD başka bilgisayara takıldığında o bilgisayarın işletim sistemine uygun başlatıcıyı çift tıklayarak programı çalıştırabilmektir.

## Karar

1. **SSD ana çalışma ve veri alanıdır.** Python kaynak kodları, çalışma paketleri/bağımlılıklar, yapılandırmalar, gelen-kutu, ham arşiv, işlenmiş veriler, eğitim çıktıları ve loglar SSD üzerinde tutulacaktır.
2. **İki işletim sistemi desteklenecektir:** Windows ARM64 (Snapdragon X Elite Surface) ve macOS ARM64 (Apple M4 Mac mini).
3. **İşletim sistemine özgü çalıştırma paketleri ayrı olacaktır.** Windows ve macOS için uygun ayrı başlatıcı/çalıştırma paketleri hazırlanır. Ortak Python kaynak kodu, veri sözleşmeleri ve proje veri yapısı mümkün olduğunca aynı tutulur. Tek bir işletim sistemi çalıştırılabilir dosyasının iki platformda da çalışacağı varsayılmaz.
4. **Performans istisnası kontrollüdür.** Bir işlem doğrudan SSD üzerinde yürütüldüğünde belirgin performans kaybı yaratıyorsa geçici çalışma verileri bilgisayarın RAM'inde veya yerel geçici alanında işlenebilir. İşlem çıktıları ve kalıcı kayıtlar SSD'ye yazılır. Yerel geçici alan kalıcı veri deposu olarak kullanılmaz.
5. **Taşınabilirlik hedefi:** Programlar sabit disk harfine, kullanıcı adına veya bilgisayara özgü mutlak klasör yoluna bağımlı tasarlanmayacaktır. SSD kökünden türetilen göreli yollar esas alınacaktır.
6. **Veri bütünlüğü:** RAW kaynak dosyalar değiştirilmeden korunur. İşlenmiş/normalize/etiketlenmiş/eğitim verileri ayrı türetilmiş alanlarda tutulur. Loglar ve işlem kayıtları SSD üzerinde saklanır.

## Henüz kararlaştırılmayan uygulama ayrıntıları

- SSD dosya sistemi ve Windows/macOS ortak yazma uyumluluğu.
- Python runtime/bağımlılık paketleme yöntemi (ör. platforma özel self-contained paket veya SSD üzerindeki taşınabilir runtime).
- Başlatıcıların biçimi ve çift tıklama akışı.
- Yerel geçici alanın kullanılacağı işlemler, sınırları ve temizleme politikası.
- SSD çıkarılmadan önce güvenli kapatma/doğrulama davranışı.
- Çevrimdışı çalışma ve ilk kurulum gereksinimleri.

Bu ADR bu teknik ayrıntıları peşinen seçmez. Gerçek dosya boyutları ve performans gözlemleriyle kararlaştırılacaktır.

## Kabul / doğrulama sınırı

Bu kayıt bir mimari karardır; SSD üzerinde klasörlerin oluşturulduğu, Python paketlerinin hazırlandığı veya iki bilgisayarda çalıştırma testinin yapıldığı anlamına gelmez. Uygulama ve platform testleri T007 kapsamında ayrıca doğrulanacaktır.
