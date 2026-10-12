# HDF-002 — Alt Görev 1.2
## Prototip için geçici SCT kanal seçimi

### Karar

3T SCT okumaları problemli olduğu için, prototip yeniden düzenlenirken 3T SCT geçici olarak kullanılmayacaktır. Prototipte mevcut durumda bağlı olan 4T SCT, 3T yerine geçici olarak okunacaktır.

Üç ölçüm ESP'sinin sensör eşlemesi bu aşamada şöyledir:

- **ESP32D #1 → 1T SCT**
- **ESP32D #2 → 2T SCT**
- **ESP32E → 4T SCT (3T yerine geçici seçim)**

Bu, prototip aşamasına ait geçici bir donanım/sensör seçimi kararıdır. 3T SCT'nin sorununun çözüldüğü veya 4T SCT'nin kalıcı seçim olduğu anlamına gelmez.

### Kayıt ve koruma

- 3T SCT ile ilgili mevcut sorun ve geçmiş deneyim kayıtları korunur; üzerine yazılmaz.
- 4T SCT ile alınacak veriler 3T kayıtlarıyla karıştırılmaz; sensör kimliği her kayıtta açıkça tutulur.
- Daha sonra 3T SCT sorunu incelenebilir ve sensör seçimi yeni kanıta göre tekrar değerlendirilebilir.

**Kanıt sınırı:** Bu dosya geçici seçim kararını kaydeder. 1T, 2T ve 4T sensörlerinin yeni prototipte başarıyla okunduğu henüz iddia edilmez.
