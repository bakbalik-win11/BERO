# ADR-028 — Kararlı alanın SCT başlangıç/bitiş sınır kuralı

- **Tarih:** 2026-11-06
- **Durum:** KABUL EDİLDİ — kullanıcı kararı
- **İlişkili kararlar:** ADR-010, ADR-022, ADR-027
- **İlişkili deney:** E12 — SCT kararlı alan tespiti, PZEM örtüşmesi ve tepki süresi

## Bağlam

SCT ve PZEM farklı ölçüm/güncelleme davranışlarına sahiptir. Kullanıcının gözlemine göre yük OFF olduğunda PZEM akımı gecikmeli göstermeye devam edebilir; SCT yük değişimini daha erken yakalar. Bu nedenle kararlı alanın hem başlangıcını hem bitişini PZEM kararlılığına bağlamak, OFF geçişinin sınırını geciktirebilir.

ADR-010 ve ADR-022'deki bağımsız akış ve olay paketi ilkeleri korunur. Bu ADR, kararlı alanın mantıksal başlangıç/bitiş kuralını daha açık ve öncelikli biçimde tanımlar.

## Karar

1. **Başlangıç koşulu:** Aynı ON paketi içinde SCT kendi ölçüm akışında kararlı ve PZEM kendi ölçüm akışında kararlı olma koşullarını birlikte sağladığında kararlı alan açılır.
2. **Bitiş koşulu:** SCT kendi ölçüm akışında kararlılığını kaybettiğinde kararlı alan kapanır.
3. **PZEM'in rolü:** PZEM kararlılığı yalnızca alanın açılması için başlangıç koşuludur. PZEM'in sonradan kararsızlaşması, gecikmeli güncellenmesi veya OFF akımını geç göstermesi alanı kapatmaz.
4. **OFF olayı:** OFF olay işareti ADR-022 uyarınca ON paketini kapatmak ve paket bütünlüğünü doğrulamak için kullanılır. OFF olayının gelmesi tek başına kararlı alan bitiş algoritmasının yerine geçmez; alanın bitişi SCT kararlılık kaybıyla belirlenir.
5. **Akış bağımsızlığı:** SCT kararlılığı yalnız SCT ölçümlerinden, PZEM kararlılığı yalnız PZEM ölçümlerinden değerlendirilir. İki akışın tekil örnekleri timestamp üzerinden birebir eşleştirilmez.
6. **PZEM referansı:** Başlangıç koşulu sağlandıktan sonra PZEM proje referansı/etiket kaynağıdır. PZEM'in gecikmeli geçiş davranışı analizde görünür tutulmalı; geçişe ait gecikmeli değerler sessizce kararlı referans gibi kabul edilmemelidir.

## Gerekçe

PZEM'in OFF geçişini geç göstermesi, SCT'nin daha erken algıladığı yük değişiminin pencere bitişini geciktirmemelidir. Başlangıçta iki kaynağın birlikte kararlı olması, karşılaştırmanın aynı yük durumunda başladığını güvenceye alan kapıdır. Bitişte SCT'nin kullanılması ise yükün fiziksel değişimini daha erken yakalayan akışın sınır belirlemesini sağlar.

## Henüz belirlenmeyen uygulama parametreleri

Bu ADR yalnızca mantıksal sınır kuralını karara bağlar. Aşağıdakiler henüz belirlenmemiştir:
- SCT kararlılık kaybının istatistiksel tanımı,
- pencere boyu ve örnek sayısı,
- dağılım/standart sapma sınırı,
- ardışık pencere ortalamaları için mutlak veya bağıl değişim sınırı,
- kararlılık kaybının kabulü için gereken devam süresi,
- PZEM'in başlangıç kararlılığı için kullanılacak sayısal ölçütler.

Bu parametreler gerçek HA History verisi üzerinde incelenerek belirlenecektir. Sayısal eşik varsayılmayacaktır.

## Uygulama ve kanıt durumu

- E12 deney belgesine bu sınır kuralı işlendi.
- Python kararlılık tespit/eşleştirme kodu henüz yazılmadı.
- Firmware/YAML değişikliği, derleme veya OTA yapılmadı.
- E12 tamamlanmış değildir; gerçek veride algoritma ve farklı yük doğrulaması beklemektedir.
