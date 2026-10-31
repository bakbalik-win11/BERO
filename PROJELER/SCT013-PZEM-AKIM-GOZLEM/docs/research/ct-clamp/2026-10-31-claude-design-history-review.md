# Claude ct_clamp tasarım tarihçesi — BERO değerlendirmesi

**Kaynak:** Kullanıcının sağladığı Word belgesinin Markdown aktarımı.  
**Durum:** Yardımcı araştırma kaynağı; bağımsız doğrulama değildir.

## Değerlendirme

Belge BERO için yararlıdır. İlk PR (#559), Jesse Hills ve Otto Winter katkıları, CTL-10-CLS / D1 Mini test düzeneği, asenkron örnekleme gerekçesi, 200 ms ve 60 s varsayılanlarının kanıt durumu ve #2283 tekrar filtresinin amacı hakkında araştırma özeti sağlar.

Mevcut [tasarım tarihçesi](2026-10-31-design-history.md), [üç kaynaklı sentez](2026-10-31-synthesis-copilot-claude-independent.md) ve [bağımsız teknik inceleme](2026-10-31-independent-technical-review.md) ile birlikte okunmalıdır. Bu belge onların yerine geçmez.

## Mevcut BERO araştırmasıyla uyumlu bulgular

- PR #559 / 2019, ilk CT clamp bileşen kaydıdır.
- İlk geliştirici düzeneği CTL-10-CLS ve D1 Mini A0 içerir; bileşen SCT013 modeline özel değildir.
- Örneklemenin `loop()` içinde asenkron yürütülmesi ESPHome ana döngüsünü bloke etmemek içindir.
- 200 ms, 50 Hz'de 10 tam çevrime karşılık gelir; 10 çevrimin neden seçildiğine dair özel tarihsel gerekçe bulunamamıştır.
- 60 s, genel polling varsayılanı olarak değerlendirilmiştir; ct_clamp'e özel bir tasarım gerekçesi kanıtlanmamıştır.
- PR #2283, tekrar eden değerlerin istatistiğe yeniden katılmasını önleyerek doğruluğu iyileştirmeyi hedefler. Kaynakta ADC sample çağrısı eşitlik kontrolünden önce yapıldığı için bu filtre ADC çağrısını durdurmaz.

## Temkin gerektiren çıkarımlar

### ESP32 ve last_value filtresi

Word belgesi, #2283'ün ESP8266 + ADS1115 bağlamında olduğunu ve ESP32 yerleşik ADC için gerekçenin aynı şekilde geçerli olmayabileceğini öne sürüyor. Bu, rapor yazarının kaynak koddan çıkardığı bir yorumdur; PR açıklaması ESP32'de filtrenin gereksiz olduğunu söylemez.

Aynı sayısal ADC değerinin yeni bir dönüşümde tekrar oluşması da mümkündür. Bu nedenle filtreyi BERO ESP32 ADC'sinde etkisiz veya zararlı ilan etmiyoruz. Etkisi ancak kontrollü karşılaştırmayla değerlendirilebilir.

### Düşük akım hedefi

Tarihsel belgelerde düşük akım için doğruluk sınıfı veya garanti bulunmaması, bileşenin düşük akımda kesinlikle başarısız olduğu anlamına gelmez. BERO'nun kendi çalışma aralığı, kendi donanım ve loglarıyla değerlendirilmelidir.

### Özel bileşen önerisi

Ayrı özel bileşen geliştirme, Claude raporunun önerisidir; BERO kararı değildir. Önce E10 ve gerekirse tekrar filtresini izole eden testler tamamlanmalıdır.

### PR #647 ve issue #457

Offset başlangıç davranışı ile #647 arasındaki ilişki raporda kaynak kod karşılaştırmasına dayalı çıkarım olarak sunulmuştur. Doğrudan PR açıklamasıyla kanıtlanmadığı notu korunmalıdır.

## BERO mimarisine aktarılabilecek dersler

1. Uzun örnekleme işi ana uygulama döngüsünü bloke etmemelidir.
2. Kaynak adaptörü ile sinyal işleme algoritması birbirinden ayrılmalıdır.
3. Örnekleme penceresi ile yeni pencerenin başlama aralığı farklı parametrelerdir.
4. İstenen okuma sayısı, ADC dönüşüm sayısı ve istatistiğe kabul edilen örnek sayısı aynı kavram değildir.
5. Bugünkü kod davranışı ile ilk geliştiricinin tarihsel niyeti ayrı kanıtlanmalıdır.
6. Bir PR'ın test donanımı ve ADC türü başka MCU/ADC kombinasyonuna doğrudan genellenmemelidir.

Bu dersler sensörden bağımsız BERO mimarisine taşınabilir. CT'ye özgü RMS ve offset işleme ise SCT/AC uygulamasında kalır.

## Proje kararına etkisi

- E10 (200 → 500 → 1000 → 200 ms) planı geçerlidir.
- 2 s yayın aralığı, K=24.22 ve mevcut pin ayarları bu rapor nedeniyle değiştirilmez.
- E10 bir pencere süresi gözlemidir; kalibrasyon veya ±%4 doğruluk testi değildir.
- T010 ve Faz 2 görev sırası değişmez.

## Sonuç

Claude Word belgesi, ct_clamp tasarım tarihçesi için ek kaynak olarak arşivlenmelidir. ESP32 filtresinin gereksiz olduğu, belirli bir ölçüm hatasına yol açtığı, düşük akımın desteklenmediği veya özel bileşen yazmanın zorunlu olduğu bu belgeyle kanıtlanmış değildir.

**Yapılmayanlar:** Firmware/YAML değişikliği, derleme, OTA ve fiziksel test yapılmadı.
