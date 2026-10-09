# Proje BERO — Ana Pusula ve Süreklilik Kaydı

> Bu belge, günlük deney ayrıntılarının yerine geçmez. Projenin genel yönünü, nereden geldiğimizi, şu anda nerede olduğumuzu ve sıradaki adımı takip eden ana çerçevedir.

## 1. Bu belgenin görevi

Bu dosya, yeni bir çalışma oturumuna veya sohbete geçildiğinde BERO'nun bağlamını yeniden kurmak için ilk bakılacak yönlendirme kaydıdır.

- **Ana çerçeve burada:** proje amacı, ana mimari, aktif hedef, güncel durum ve sıradaki adım.
- **Görev ayrıntıları GOREVLER altında:** test planı, kod sürümleri, ölçümler, loglar ve görev deneyimi.
- **Ana hedefler HEDEFLER altında:** hedef tanımı, hedefe bağlı görev silsilesi ve hedefin sonuçlandırılması.
- **Fikir havuzu TODO altında:** henüz resmî göreve dönüşmemiş fikirler ve küçük yapılacaklar.
- **Kalıcı kararlar ve süreklilik ilkeleri** kendi belgelerinde korunur.
- Bu belge ayrıntılı kayıtların yerine geçmez; ilgili kayıtlara yönlendirir.

## 2. BERO'nun genel yönü

Proje BERO, ev otomasyonu ve ölçüm/denetim sistemini modüler, ölçülebilir, doğrulanabilir ve zaman içinde sürdürülebilir biçimde kurmayı hedefler.

Bilinen ana mimari çerçeve:
- **Home Assistant:** üst seviye otomasyon ve karar katmanı.
- **Aqara ve mevcut akıllı ev cihazları:** yaşam otomasyonunun mevcut bileşenleri.
- **ESP32 düğümleri:** özel ölçüm, sensör ve yerel kontrol işleri.
- **Saha I/O ve haberleşme:** RS485/Modbus ve Ethernet tabanlı modüler bağlantıların araştırılması.
- **Mini Node yaklaşımı:** işlevleri ayrıştırılmış ve bağımsız doğrulanabilir modüller.
- **Ölçüm disiplini:** ham veriyi, test koşullarını, yorumu ve doğrulanmış sonucu birbirinden ayırmak.

Bu bölüm ana resmi özetler. Ayrıntılı elektrik, HVAC, donanım ve bağlantı kararları kendi kayıtlarında tutulmalıdır; bu dosya onların yerine geçmez.

## 3. Aktif ana hedef

**[HDF-001 — Akımı Okuma](HEDEFLER/HDF-001-AKIMI-OKUMA/HEDEF.md)**

Hedef: akım ölçüm zincirini çalıştırmak, davranışını ölçümlerle doğrulamak ve kullanılan yöntemi sınırlarıyla birlikte tekrarlanabilir biçimde belgelemek.

Başlangıç görevi:
- **[GRV-001 — ESP32-D ile SCT-013 Akım Okuması](GOREVLER/GRV-001/RAPOR/README.md)**

Bu görevde amaç, ESP32-D ve SCT-013 ile akım okuma davranışını incelemektir. MCP3208/SPI zamanlama konusu bu görevin kapsamına kendiliğinden eklenmez; gerekirse ayrı görev olarak açılır.

## 4. Şu anki kayıtlı durum

- Hedef/görev yapısı GitHub'da oluşturuldu.
- GRV-001'in adı ve kapsamı ESP32-D + SCT-013 akım okuması olarak düzeltildi.
- Görev klasörlerinde RAPOR ve KOD alanları tanımlandı.
- Kayıt, sürümleme ve süreklilik politikası oluşturuldu.
- TODO fikir havuzu oluşturuldu. İlk fikir — ESP32-D ile SCT-013 30A/1V akım okuma — GRV-001 görevine dönüştürüldü ve TODO'da “Göreve dönüşenler — açık görevler” bölümünde açık `[ ]` olarak tutuluyor. Durum akışı açık fikir → göreve dönüşen açık kayıt → sonuçlanan kayıt biçiminde işliyor.
- **Deney sonucu veya derleme başarısı bu dosyada varsayılmayacak.** İlgili test kaydı ve kullanıcı doğrulaması bulunmadan kod başarılı/çalışıyor kabul edilmeyecek.
- GRV-001 henüz sonuçlandırılmış sayılmıyor.

Bu durum bölümü, yeni kanıt elde edildiğinde güncellenebilir bir anlık görüntüdür. Değişiklik önemli bir karar veya önceki durumu etkiliyorsa aşağıdaki kronolojiye ayrıca kayıt eklenir.

## 5. Sıradaki adım

1. GRV-001 için kullanılacak mevcut ESP32-D + SCT-013 kodunu ve donanım/bağlantı durumunu belirlemek; mevcut çalışan sürümü korumak.
2. Test koşullarını ve ölçüm beklentisini görev raporuna kaydetmek.
3. Tek değişkenli deneylerle ölçüm almak; ham veriyi ve logları saklamak.
4. Bulgulara göre sonraki görev gerekip gerekmediğine karar vermek.
5. Derleme gerektiren kod, kullanıcı başarılı derlemeyi doğrulamadan görev klasörüne taşınmamalıdır.
6. Ana hedef ancak kabul ölçütleri ve kanıtlar değerlendirildikten sonra kapatılmalıdır.

Bu liste, yeni test sonucu geldikçe güncellenir; sonuçlar önceden varsayılmaz.

## 6. Oturum devri — en son nerede kaldık?

Yeni bir oturuma geçerken bu bölümü kısa ve somut biçimde güncelle:
- **Son tamamlanan iş:** Hangi belge, kod veya deney tamamlandı?
- **Son doğrulanmış durum:** Hangi sonuç kullanıcı/ölçüm/log tarafından doğrulandı?
- **Açık soru:** Hangi belirsizlik hâlâ çözülmedi?
- **Sıradaki tek adım:** Devam etmek için ilk yapılacak somut işlem nedir?
- **İlgili kayıtlar:** Görev raporu, kod sürümü, log veya karar bağlantıları.

Bir sonuç doğrulanmadıysa “bekliyor” yaz; tahminle doldurma.

### Mevcut devir notu

- **Son tamamlanan iş:** İlk TODO fikri, ESP32-D + SCT-013 30A/1V akım okuma olarak GRV-001 görevine bağlandı; TODO, görev raporu ve HISTORY kaydı güncellendi.
- **Son doğrulanmış teknik sonuç:** Bu güncelleme kayıt/organizasyon işidir; yeni bir teknik ölçüm veya derleme sonucu yok.
- **Açık soru:** GRV-001 için kullanılacak mevcut ESP32-D kod sürümü, bağlantı düzeni ve test koşulları henüz doğrulanmadı.
- **Sıradaki adım:** Mevcut çalışan kodu ve donanım/bağlantı durumunu tespit edip test başlangıç koşullarını görev raporuna kaydetmek.

## 7. Önemli kararların kronolojisi

Bu bölüm **eklemeli kayıt** içindir. Yeni kararlar yeni tarihli maddeler olarak eklenir; eski maddeler sessizce değiştirilmez.

- **2026-10-09:** Ana hedef/görev ilişkisi kuruldu. HDF-001 “Akımı Okuma”; GRV-001 “ESP32-D ile SCT-013 Akım Okuması” olarak tanımlandı.
- **2026-10-09:** Geçmiş deneyimin üzerine yazmama, kod sürümlerini ve raporları koruma, her kod için eşlik eden Markdown belgesi bulundurma ve doğrulanmamış sonuçları doğrulanmış gibi sunmama ilkeleri kayıt altına alındı.
- **2026-10-09:** Henüz resmî göreve dönüşmemiş fikirler ve küçük yapılacaklar için tarihli, tamamlanma tikli ve yeni maddeleri üstte tutan TODO listesi oluşturuldu.
- **2026-10-09:** TODO sonuç durumları tanımlandı: “Tamamlandı”, “Vazgeçildi” ve “Göreve dönüştü”. Göreve dönüşen fikir, bağlı resmî görev tamamlanana kadar açık kalacak; sonuçlanmış maddeler ayrı bölüme taşınacak.

Yeni karar kaydında tarih, karar, gerekçe ve etkilediği dosyalar belirtilir.

- **2026-10-09:** Yeni süreklilik ilkesi: anlamlı görev basamakları görev raporunda tarihli izlenecek; tekrar kullanılabilir donanım/sensör tecrübesi kaynak görev ve kanıt bağlantısıyla donanımın Markdown notuna aktarılacak; doğrulanmış kod sürümleri koşulları ve test belgeleriyle ayrı korunacak. İlkenin uygulama ayrıntıları [Asistan İşletim Protokolü](ASISTAN_ISLETIM_PROTOKOLU.md) ve [Kayıt, Sürümleme ve Süreklilik Politikası](KAYIT_VE_SUREKLILIK.md) içindedir.

## 8. Süreklilik ilkesi

**Bir sonraki adımı bulurken önceki adımları kaybetme.** Yeni oturumda önce bu pusula, sonra ilgili ana hedef, sonra aktif görev raporu ve en son kod/log kayıtları okunur.

Ayrıntılı kayıt politikası: [KAYIT_VE_SUREKLILIK.md](KAYIT_VE_SUREKLILIK.md).

## 9. Asistanın komut tetikleyicileri

- **“Ara rapor”** verildiğinde [ASISTAN_ISLETIM_PROTOKOLU.md](ASISTAN_ISLETIM_PROTOKOLU.md) içindeki ara rapor kontrol listesi otomatik uygulanır.
- **“Günü kapa”** verildiğinde ara rapor adımlarına ek olarak gün sonu kaydı ve yeni oturum devri hazırlanır.
- Bu komutlar yalnızca sohbet yanıtı üretmek anlamına gelmez: uygun olduğunda kaynak kayıtlar ve bu pusula güncellenir; başarısız araç işlemleri açıkça bildirilir.

Komutların ayrıntılı kontrol listesi: [ASISTAN_ISLETIM_PROTOKOLU.md](ASISTAN_ISLETIM_PROTOKOLU.md).

## 10. Tarihli proje geçmişi

Projenin nereden nereye ilerlediğini tarih sırasıyla görmek için [HISTORY/](HISTORY/README.md) günlüğü kullanılır. “Ara rapor” ve “günü kapa” komutlarında yalnızca bu pusula güncellenmez; ilgili tarihin HISTORY dosyasına da yeni bir kayıt eklenir. Günlük geçmiş eklemeli tutulur ve eski girdiler silinmez.

## 11. TODO — fikir havuzu

[TODO/README.md](TODO/README.md), henüz resmî göreve dönüşmemiş fikirlerin ve küçük yapılacakların ortak listesidir. Yeni fikirler bölümün en üstüne eklenir; ilk kayıt tarihi korunur. Tamamlanan veya vazgeçilen fikirler silinmez, sonuç ve tarihleriyle “Sonuçlananlar” bölümüne taşınır. Bir fikir resmî göreve dönüşürse “Göreve dönüşenler — açık görevler” bölümüne alınır ve bağlı görev tamamlanana kadar açık kalır. Görev tamamlandığında sonuç “Görev tamamlandı” olarak kaydedilir.


## 12. Günlük kontrol listesi ve süreklilik

[GUNLUK/README.md](GUNLUK/README.md) günlük tik listesinin dizinidir. Her gün için `GUNLUK/YYYY/YYYY-MM-DD.md` dosyası tutulur; [GitHub Actions iş akışı](.github/workflows/daily-bero-checklist.yml) Türkiye saatiyle yaklaşık 03.05'te yeni günlük dosyası oluşturmaya ayarlanmıştır.

- “Ara rapor” ve “günü kapa” sırasında günlük kontrol listesi, TODO yaşam döngüsü, HISTORY, aktif görev raporu ve bu pusula birlikte gözden geçirilir.
- Kutular yalnızca ilgili işlem tamamlanıp GitHub kaydı geri okunarak doğrulandığında işaretlenir.
- Günlük otomasyonun zamanlanmış ilk çalışması henüz doğrulanmış değildir.


## 13. Süreklilik denetimi — 2026-10-09

- **Denetim bulgusu:** Günlük otomasyonun yeni dosyayı `GUNLUK/README.md` indeksine eklememesi düzeltildi.
- **Asistan sorumluluğu:** Günlük liste, TODO yaşam döngüsü, HISTORY, görev raporu, pusula, bağlantılar ve GitHub geri-okuma doğrulaması.
- **Kullanıcı sorumluluğu:** Yalnızca teknik kanıt ve kararlar — deney koşulları/ham loglar, derleme sonucu, gerektiğinde donanım veya çalışan yapılandırma değişikliği onayı.
- **Henüz doğrulanmayan:** GitHub Actions iş akışının gerçek çalıştırması. İlk başarılı çalıştırma görülene kadar günlük otomasyonun çalıştığı varsayılmayacak.
- **Sıradaki adım:** GitHub Actions durumunu doğrulamak; ardından GRV-001 için mevcut kod, bağlantı ve test koşullarını belirlemek.
- **Ayrıntılı kayıt:** [HISTORY Kayıt 007](HISTORY/2026/2026-10-09.md).
