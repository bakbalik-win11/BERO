# ADR-017 — Modül 2 taşınabilir tasarımında tek kablolu ortak bias

- **Tarih:** 2026-11-01
- **Durum:** KABUL EDİLDİ — uygulanmış donanım tasarımı
- **İlgili görev:** [T010](../../tasks/T010-module2-triple-sct-bringup.md)
- **İlgili modül:** BERO-SCT-OKUMA-TEST-002

## Bağlam

Modül 2, proje sahibi tarafından taşınabilir ve sade bir ölçüm modülü olarak tasarlanıp imal edildi. Üç SCT girişinin her biri ayrı sinyal yoluna sahip olmakla birlikte bias dağıtımının üç ayrı devreye bölünmesi istenmedi.

## Karar

Tek bias devresi kullanılır. Bias, tek kablo/ortak hat üzerinden üç SCT kanalına dağıtılır. Üç SCT için ayrı bias devresi veya ayrı bias kablosu kullanılmaz.

## Fiziksel uygulama

- Bias devresi breadboard üzerinde kurulmuştur; kullanıcı bu düzenin görüntüsünü daha önce paylaşmıştır.
- Ortak bias, modülün imalatı sırasında ölçülmüştür.
- SCT-1 sinyali sarı / GPIO32; SCT-2 sinyali yeşil / GPIO33; SCT-3 sinyali mavi / GPIO34.
- Ortak bias izleme bağlantısı turuncu / GPIO35.
- Üç SCT sinyal hattı bağımsızdır; bias referansı ortaktır.
- Tek ortak bias dağıtımı taşınabilirlik ve kablolama sadeliği için bilinçli seçilmiştir.

## Kabul ve sınırlar

Bu karar uygulanmış donanım mimarisini kaydeder. Üç ayrı bias devresi oluşturmak veya bias bağlantısını her SCT için yeniden test etmek gerekmemektedir. İlk imalat sırasında üç kanalın okuma kontrolleri ve ortak bias ölçümü yapılmıştır; Modül 2 ile yük testleri, derleme ve fiziksel çalışma kayıtları proje deposunda bulunmaktadır.

Bu ADR yeni fiziksel test yapıldığı anlamına gelmez. E10 pencere deneyi (200 → 500 → 1000 → 200 ms) ayrı ve henüz PLANLANDI durumundadır. Firmware YAML'ın mevcut kanal kapsamı bu donanım kararından ayrı takip edilir.

## Kaynak sınıfı

Proje sahibinin/imalatçının kendi üretimi ve ölçümü hakkındaki birinci el beyanı (USER REPORT). Bu, proje için birincil imalat kaydıdır.
