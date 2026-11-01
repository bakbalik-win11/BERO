# ADR-024 — Python tarafında ON/OFF paket bütünlüğü doğrulaması

- **Tarih:** 2026-11-01
- **Durum:** KABUL EDİLDİ — kullanıcı kararı
- **İlişkili kararlar:** ADR-022, ADR-023
- **Kapsam:** Modül 2 SCT ve Modül 3 PZEM olay akışlarının Python tarafında paketlenmesi ve eğitim verisine kabulü

## Bağlam

Modül 3 SSR durum değişiminde BERO_EVT olayı üretir; aynı olayı kendi HA/PZEM akışına kaydeder ve UDP 4210 üzerinden Modül 2'ye gönderir. Modül 2 aldığı olayı kendi HA/SCT akışına kaydeder. Geçmiş log ve HA kayıtlarında Modül 3'te bulunan bazı EVENT_ID olaylarının Modül 2 kayıtlarında görünmediği gözlenmiştir. Her olayın iki tarafa eksiksiz ulaştığı varsayılamaz.

## Karar

1. Mevcut Modül 3 → UDP 4210 → Modül 2 olay aktarımı korunur. Bu karar UDP'yi kaldırmaz, HA merkezli yeni bir olay mimarisi kurmaz ve yeni HA helper gerektirmez.
2. Modül 3 kendi PZEM akışını; Modül 2 kendi SCT akışını, yalnızca kendi akışında kayıtlı olay işaretlerine göre bağımsız paketler.
3. Bir paket, ilgili akışta geçerli ON başlangıcı ve onu izleyen geçerli OFF bitişiyle sınırlandırılır. Başlangıç veya bitiş işareti eksikse, olay kimliği uyuşmuyorsa ya da sıra tutarsızsa o akış aralığı tamamlanmış paket sayılmaz.
4. Python, iki akışta oluşan paket aralıklarını yalnız BOOT_ID + EVENT_ID ile eşleştirir. İki tarafta da aynı paket aralığı doğrulanmadan SCT verisi PZEM etiketiyle eğitim örneğine alınmaz.
5. Eksik/uyuşmayan paketler tahminle tamamlanmaz ve sessizce atlanmaz; INCOMPLETE_EVENT, MISSING_ON, MISSING_OFF, EVENT_ID_GAP, DUPLICATE_EVENT, STATE_ORDER_ERROR, BOOT_CHANGED_WITH_OPEN_PACKET gibi tanı durumlarıyla raporlanır.
6. Bir akışta yeni ON olayı açık paket varken gelirse önceki aralık tamamlanmamış/bozuk olarak işaretlenir; yeni ON yeni paket başlangıcı olarak değerlendirilir. Bu kurtarma kuralı, önceki paketi geçerli kılmaz.
7. BOOT_ID değiştiğinde önceki boot oturumunda açık kalan paket tamamlanmamış olarak kapatılır. EVENT_ID boşlukları ayrıca olay dizisi eksikliği olarak raporlanır.
8. ON/OFF işaretlerinin bulunması paketin kararlı olduğu anlamına gelmez. PZEM ve SCT kararlılığı kendi ölçüm akışlarında bağımsız değerlendirilir; geçiş/yerleşme bölümleri eğitim alanından çıkarılır.

## Örnek davranış

- Modül 3 akışında 59 ON → 60 OFF → 61 ON → 62 OFF varsa iki tam olay aralığı kurulabilir.
- Modül 2 akışında 60 OFF yoksa Modül 2 tarafındaki 59 ON aralığı kapanmadığı için tamamlanmış paket sayılmaz. Sonraki 61 ON → 62 OFF aralığı kendi işaretleriyle tam kurulabiliyorsa bağımsız bir paket adayı olabilir.
- Bir tarafta tam paket bulunması, diğer tarafta aynı BOOT_ID + EVENT_ID paketinin mevcut olduğunu kanıtlamaz. İki akışın paketleri ayrı doğrulanır ve yalnız eşleşen kimlikli aralıklar eğitim adayı olur.

## Kapsam dışı / değişmeyenler

- UDP protokolü değişmez: BERO_EVT,BOOT_ID=<32 HEX>,EVENT_ID=N,STATE=ON|OFF.
- TIME alanı eklenmez; ADR-023 geçerlidir.
- Modül 2 ve Modül 3 firmware'ine bu ADR nedeniyle yeni paketleme mantığı eklenmez.
- HA helper, yeni event broker veya HA üzerinden merkezi paketleme kurulmaz.
- Timestamp iki sensörün ölçüm örneklerini eşleştirmek için kullanılmaz; yalnız kendi akışı içinde kaynak kayıt sırasını kurmak için kullanılabilir.

## Uygulama ve doğrulama durumu

Bu ADR Python tarafındaki kabul/ret kuralını tanımlar. Python uygulaması, gerçek HA export üzerinde test, test çıktısı/logu ve sonuç yorumu henüz yapılmamıştır. Bu kayıt yazılımın hazır veya doğrulanmış olduğu anlamına gelmez.
