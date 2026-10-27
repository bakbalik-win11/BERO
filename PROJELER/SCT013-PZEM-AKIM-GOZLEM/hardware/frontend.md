# SCT analog ön uç kontrolü

**Durum: Ölçüm yapılmadı; breadboard bias alt devresi kullanıcı beyanıyla mevcut.** SCT013 jack üzerinden bu devreye bağlanacak ve ESP32'nin dahili ADC işleviyle okunacaktır. Bu aşamada harici ADC kullanılmayacak; MCP3208 sonraki aşamaya ayrılmıştır.

Breadboard bias alt devresi kullanıcı beyanına göre iki adet 10 kΩ dirençle orta nokta oluşturur; orta nokta ile GND arasına 104 kodlu (100 nF) kondansatör bağlanmıştır. Bu kayıt, SCT AC sinyalinin bias noktasına kuplaj yönteminin doğrulandığı anlamına gelmez.

Kaydedilecek / değerlendirilecek konular:
- Kullanılacak SCT model kodu ve çıkış türü.
- SCT modelinde dahili burden olup olmadığı; harici burden varsa değeri ve gücü.
- SCT AC sinyalinin breadboard bias devresinden ESP32 ADC girişine kuplaj yöntemi.
- Kullanılan analog filtre ve ek direnç değerleri (varsa).
- ESP32 ADC girişindeki DC seviyesi, beklenen maksimum sinyal ve güvenli giriş aralığı.
- Yüksüz ADC ortalaması, min/max ve gürültü metriği.
- En yüksek planlanan akımda clipping durumu.

SCT013-100A-1V gerilim çıkışlı varyant ile SCT013-000 akım çıkışlı varyant aynı değildir. Ölçülmemiş değerler ölçülmüş gibi yazılmayacaktır.