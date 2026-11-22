# ZMPT101B / ZMPT107 – Kullanım Kılavuzu İnceleme Kaydı

## Kaynak
- Kullanıcının sağladığı dosya: `ZMPT101B.PDF`
- Belge başlığı: **ZMPT101B (ZMPT107) voltage transformer operating guide**
- Uzunluk: 4 sayfa
- Belge türü: ZMPT101B/ZMPT107 gerilim trafosu için bağlantı ve tasarım/örnekleme kılavuzu.
- Kapsam notu: Bu belge, satın alınan potansiyometreli PCB modülünün eksiksiz şeması veya modül performans sertifikası olarak değerlendirilmemelidir.

## Belgeden çıkarılan teknik bilgiler

### 1. Bağlantı seçenekleri – Sayfa 1
Belge iki bağlantı yaklaşımı gösterir:
- **Figure I:** Op-amp içeren aktif çıkış yaklaşımı.
- **Figure II:** Pasif çıkış yaklaşımı.

Şemalar, transformatörün tek başına analog ölçüm zinciri olmadığını; akım sınırlama ve örnekleme dirençlerinin/analog ön ucun tasarımın parçası olduğunu gösterir.

### 2. ADC girişine göre maksimum çıkış RMS değeri – Sayfa 1–2
Belge, maksimum çıkış RMS değerini ADC'nin izin verdiği tepe giriş gerilimine göre sınırlar.

Verilen formüller:
- Bipolar ADC: (U_{max}=V_{peak}/\sqrt{2})
- Unipolar ADC: (U_{max}=V_{peak}/(2\sqrt{2}))

Belgedeki örnekler:
- ±5 V bipolar ADC için: 3,53 V RMS.
- 0–3,3 V unipolar ADC için: 1,16 V RMS.

Bu değerler, örnekleme girişindeki AC bileşeninin izin verilen tepe gerilimine göre verilen kılavuz örnekleridir. Hazır kartın OUT pininde ölçülmüş değerler değildir.

### 3. Primer akım sınırlama direnci R′ – Sayfa 2
Belge, ZMPT101B/ZMPT107 elemanının tipik çalışma akımını 1–2 mA olarak belirtir.
- Giriş gerilimi 100 V veya altındaysa örnek seçim olarak 2 mA verilir.
- 220 V ve üzeri için direnç gücünü azaltmak amacıyla 1–2 mA aralığı önerilir.
- Örnek: 100 V / 2 mA = 50 kΩ.
- Örnek: 220 V / 1,1 mA ≈ 200 kΩ.

Belge ayrıca seçilen direncin güç dayanımının yeterli payla belirlenmesini ve yüksek sıcaklık katsayılı metal film direnç kullanılmasını tavsiye eder.

**Uygulama sınırı:** Bu hesaplar çıplak trafo/ön uç tasarımı içindir. Satın alınan hazır modülün primer dirençleri bilinmeden bu değerler karta harici olarak eklenmeyecek veya kart üzerinde değişiklik yapılmayacaktır.

### 4. Sekonder örnekleme direnci R – Sayfa 3
Belge, örnekleme direncini hedeflenen maksimum çıkış gerilimi, maksimum giriş gerilimi ve primer akım sınırlama direnci ile ilişkilendirir.
Verilen örnek:
- (V_{output,max}=3,53 V)
- (V_{input,max}=120 V)
- (R′=50 kΩ)
- Hesaplanan (R≈1,471 kΩ)

Belge, direnç seçiminin belirtilen üst sınırı aşmaması gerektiğini not eder.

### 5. Aktif ve pasif çıkış karşılaştırması – Sayfa 3–4
Belgenin nitel değerlendirmesi:

**Aktif çıkış**
- Daha yüksek hassasiyet.
- Daha küçük faz hatası.
- Daha yüksek çıkış gerilimi.
- Daha güçlü yük sürme kapasitesi.
- Devre daha karmaşıktır.
- Tek kutuplu ADC için op-amp pozitif girişine sabit referans gerilimi eklenebileceği belirtilir.
- Faz kompanzasyonu gerekirse C/R elemanları veya yazılım yöntemi değerlendirilebilir.

**Pasif çıkış**
- Daha basit devre.
- Belgeye göre yüksek hassasiyet.
- Çıkış gerilimi sınırlıdır.
- Yük direnci arttıkça faz farkı artar.

Bu karşılaştırma belgedeki genel tasarım açıklamasıdır; satın alınan hazır modülün ölçülmüş faz hatasını belirtmez.

## BERO / PF araştırması için uygulanacak yorum

1. Satın alınan parça potansiyometreli ZMPT101B PCB modülüdür. Bu kılavuzun şemaları, modülün gerçek PCB şemasıyla aynı kabul edilmeyecektir.
2. Kartın OUT sinyalinin DC ofseti, tepe genliği, kırpılma payı ve 50 Hz dalga şekli fiziksel kart geldikten sonra ölçülecektir.
3. Kartın 50 Hz faz gecikmesi, SCT013 akım kanalına göre ayrıca karakterize edilmelidir.
4. Gerçek aktif güç ve gerçek PF için gerilim ve akım örnekleri ortak zaman tabanında alınmalıdır. Yalnızca RMS gerilim ve RMS akımı çarpmak aktif gücü vermez.
5. ADC giriş sınırları aşılmamalıdır. Kılavuzdaki 0–3,3 V örneği, kart OUT sinyalinin doğrudan her ESP32 ADC girişine güvenle bağlanabileceği anlamına gelmez.
6. Kılavuzdaki çıplak eleman direnç hesapları, hazır modüle uygulanmadan önce kart devresi incelenmelidir.
7. 4000 V izolasyon gibi modül tanıtım değerleri, tamamlanmış ölçüm düzeneğinin şebeke güvenliği onayı yerine geçmez.

## Deney öncesi doğrulama listesi
- [ ] Kartın gerçek pin sırası ve PCB revizyonu fotoğraf/ölçümle doğrulandı.
- [ ] Besleme gerilimi üretici/kart baskısı ve ölçümle doğrulandı.
- [ ] OUT DC ofseti ölçüldü.
- [ ] OUT tepe-tepe genliği ve kırpılma kontrol edildi.
- [ ] 50 Hz dalga şekli gözlendi.
- [ ] 50 Hz faz gecikmesi ölçüldü.
- [ ] SCT013 akım örnekleriyle zaman hizalaması doğrulandı.
- [ ] ADC giriş koruması ve örnekleme mimarisi doğrulandı.

## Durum
- Kılavuz incelendi ve teknik içerik bu kayıt dosyasına işlendi.
- Hazır ZMPT101B modülü henüz kargoda; fiziksel kart ölçümleri yapılmadı.
- PF ölçümü uygulanmış veya doğrulanmış değildir.
- Bu kayıt imalat/onay belgesi değildir.

## Kaynak dosya durumu
Bu kayıt, konuşmada kullanıcı tarafından yüklenen `ZMPT101B.PDF` dosyasının incelenmesiyle hazırlanmıştır. GitHub metin dosyası olarak kılavuzun teknik özeti ve deney notları kaydedilmiştir; orijinal PDF ikili dosyası bu işlemde GitHub deposuna yüklenmemiştir.
