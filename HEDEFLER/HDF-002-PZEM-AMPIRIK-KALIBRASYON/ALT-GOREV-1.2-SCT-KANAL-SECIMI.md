# HDF-002 — Alt Görev 1.2
## SCT kanal seçimi ve iki katmanlı prototip mimarisi

### Karar

Prototipte kullanılacak üç SCT kanalı:

- **ESP32D #1 → 1T SCT**
- **ESP32D #2 → 2T SCT**
- **ESP32E → 4T SCT**

3T SCT okumalarında yaşanan sorun nedeniyle mevcut prototipte 4T SCT kullanılacaktır. Bu, geçici seçim olarak değil, prototipin güncel sensör eşlemesi için alınmış yeni karar olarak kaydedilir. 3T ile ilgili geçmiş sorun ve deneyimler korunur; bu karar 3T sorununun çözüldüğü anlamına gelmez.

### İki katmanlı mimari

Bu düzen aynı zamanda iki katmanlı bir yapı oluşturur:

1. **Ölçüm katmanı:** Üç ayrı ESP kendi SCT sensörünü ve o kanala ait BIAS değerini okur. Ham kayıtlar sensör ve cihaz kimliğiyle korunur.
2. **Referans ve deney kontrol katmanı:** PZEM ESP yalnızca kendi PZEM cihazını okur; ayrı SSR kontrol ESP'si yükün deney döngüsünü yönetir. Bu işlevler SCT ESP'lerinin ölçüm görevini üstlenmez.

SSR için 55 saniye açık + 5 saniye kapalı döngüsü başlangıç zamanlama adayı olarak ayrıca kaydedilmiştir; optimum olduğu henüz doğrulanmış değildir.

### Kayıt ve kanıt sınırı

- 3T SCT'nin eski sorun kayıtları korunur ve 4T kayıtlarıyla karıştırılmaz.
- Her SCT kanalının kendi BIAS değerinin ölçülmesi yeni donanım modifikasyonu gerektirir; bu modifikasyon ayrı alt görevde takip edilir.
- Bu kayıt mimari ve sensör seçimi kararını tanımlar. Yeni düzenin kurulduğu veya üç sensörün başarıyla okunduğu iddia edilmez.
