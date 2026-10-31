# BERO Modülü — Bias Trafosu

**Modül kimliği:** BERO-BIAS-TRAFOSU-001  
**Adı:** Bias Trafosu  
**Proje:** SCT013 – PZEM Akım Gözlem  
**Durum:** Fiziksel modül mevcut; çıkış gerilimi ölçümü kullanıcı fotoğrafıyla destekleniyor. Tam devre bağlantı doğrulaması açık.

## 1. Amaç

Bias Trafosu, ESP32D2'nin SCT013 ölçüm devresinde kullanılan bias beslemesini sağlar. Kullanıcı, modülün ESP'ye bağlı olduğunu ve bias ürettiğini bildirmiştir.

Bu modül ESP32D2'nin ana beslemesi olarak tanımlanmamıştır; görevi SCT ölçüm devresinin bias beslemesini sağlamaktır.

## 2. Modül içeriği

| Bileşen | Model / değer | Modülde bulunan |
|---|---|---:|
| İzolasyon trafosu | RN130421, 230 V AC / 6 V AC, 2 VA, EI 30/15.5 | 1 |
| Köprü doğrultucu | KBU610, 1000 V / 6 A | 1 |
| Filtre kondansatörü | 2200 µF / 35 V, 16×25 mm | 1 |
| Pozitif voltaj regülatörü | L78L33, 3.3 V, TO-92 | 1 |

### Stok dağılımı — ilgili parçalar

| Parça | Toplam stok | Modülde | Serbest stok |
|---|---:|---:|---:|
| KBU610 | 5 | 1 | 4 |
| 2200 µF / 35 V kondansatör | 3 | 1 | 2 |
| L78L33 TO-92 | 3 | 1 | 2 |

## 3. Elektriksel yapı

**Bileşenlerden çıkarılan muhtemel güç zinciri (HİPOTEZ; kart izleri henüz takip edilmedi):**

230 V AC → RN130421 izolasyon trafosu → KBU610 köprü doğrultucu → 2200 µF filtre kondansatörü → L78L33 → 3.3 V DC bias beslemesi.

Bu zincir bileşen listesine dayanır; her bileşenin kart üzerindeki pin bağlantısı ve kondansatör polaritesi henüz fiziksel olarak doğrulanmış değildir.

## 4. Ölçüm ve kanıt

- **Ölçülen çıkış:** 3.31 V DC.
- **Kanıt türü:** Kullanıcının paylaştığı UNI-T UT33D+ multimetre fotoğrafı.
- **Yorum:** Fotoğrafta multimetre DC gerilim kademesinde 3.31 V göstermektedir. Ölçüm, modülün çıkışında bu anda 3.3 V seviyesinde gerilim bulunduğunu destekler.
- **Sınır:** Ölçümün yük koşulu ve ölçüm noktalarının devre şemasıyla eşleştirilmesi fotoğraftan kesinleştirilemiyor. Yük altında regülasyon/kararlılık testi yapılmış kabul edilmez.

## 5. Bağlantı ilişkisi

- **Modül çıkışı:** ESP32D2'nin SCT013 ölçüm devresindeki bias beslemesine bağlıdır (KULLANICI BİLDİRİMİ).
- **ESP32D2 ADC bias noktası:** Modülün 3.3 V çıkışıyla aynı nokta olduğu varsayılmaz; devredeki bölücü/orta nokta bağlantısı ayrıca izlenmelidir.
- **SCT013 sinyal bağlantısı:** Bu modülün güç/bias rolü ile SCT sinyalinin analog kuplaj yolu birbirinden ayrı tanımlanmalıdır. Tam bağlantı şeması henüz doğrulanmadı.

## 6. Güvenlik

Modülün primer tarafı şebeke gerilimiyle çalışır. Enerjiliyken kutu açılmaz veya bağlantı değiştirilmez. Şebeke tarafı inceleme ve ölçümleri yalnız yetkin kişi tarafından uygun koruma ve ölçüm prosedürleriyle yapılmalıdır. ESP32 bağlantısından önce düşük gerilim çıkışının doğru referansa ve polariteye sahip olduğu enerjisiz kontrollerle doğrulanmalıdır.

## 7. Açık kalan doğrulamalar

- KBU610, kondansatör ve L78L33 pin bağlantılarının kart üzerinde izlenmesi.
- Kondansatör polaritesinin ve gerçek bağlantı noktasının doğrulanması.
- 3.31 V ölçümünün tam ölçüm noktası ve yük koşulunun kaydı.
- ESP32D2 bias orta noktasının ayrıca ölçülmesi ve modül çıkışıyla ilişkisinin doğrulanması.
- Modülün ESP32D2'ye giden kablo/konnektör pin diziliminin belgelenmesi.

## 8. Kaynak ve kayıt ayrımı

- RN130421 elektriksel özellikleri: kullanıcının paylaştığı üretici teknik dokümanı.
- L78L ailesi özellikleri: kullanıcının paylaştığı ST L78L veri sayfası görseli; bu görsel L78L33'ün modüldeki gerçek bağlantısını kanıtlamaz.
- Parça adetleri ve modül içindeki yerleşimleri: kullanıcı bildirimi.
- 3.31 V DC: kullanıcı fotoğrafındaki multimetre ölçümü.
- Güç zinciri: bileşenlerden çıkarılan, fiziksel bağlantı takibi bekleyen hipotez.
