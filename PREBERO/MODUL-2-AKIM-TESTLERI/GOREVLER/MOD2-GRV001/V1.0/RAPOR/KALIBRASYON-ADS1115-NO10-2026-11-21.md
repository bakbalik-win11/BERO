# MOD2-GRV001 V1.0 – Yeni ADS1115 No.10 katsayı tespiti ve doğrulama

Tarih: 2026-11-21  
Durum: Aşama 1 tamamlandı; Aşama 2 ölçümü bekleniyor.

## Çalışma çevriminin doğru sırası

Bu kayıt önceki ADS1115 deneyiyle karıştırılmamalıdır. Bu çalışma çevrimi, akım okuma kodunun yeniden oluşturulması ve yeni fiziksel ADS1115 No.10 modülünün kalibrasyonunun bulunması üzerine kuruludur.

### Aşama 1 – Kod 0'ın yeniden oluşturulması ve başlangıç ölçümü

- Akım okuma işlevi UDP/paket dinleme bölümlerinden ayrılarak yeniden oluşturuldu ve `KOD/MOD2-GRV001_KOD-0.yaml` konumunda temel sürüm olarak korundu.
- Bu aşamada ADS1115 fiziksel modül numarası **10** kullanıldı.
- Kod 0 ile 100 W ve 150 W yüklerde kararlı ölçüm pencereleri kaydedildi.
- Başlangıç katsayısı 27.60 iken PZEM/SCT kararlı okumaları karşılaştırıldı.
- Bu karşılaştırmadan ADS1115 No.10 için geçici katsayı 30.66 hesaplandı.

### Aşama 1 veri analizi – kararlı pencereler

Kaynak: kullanıcının aynı oturumda sağladığı `history.csv`. Yük geçişleri, sıfır durumları ve geçiş sıçramaları kararlı ortalamalara dahil edilmedi.

| Yük / pencere | PZEM akım ort. | SCT akım ort. | K = 27.60 × PZEM/SCT |
|---|---:|---:|---:|
| 150 W, 15:57:00–15:57:38 | 0.65050 A | 0.58537 A | 30.67 |
| 150 W, 15:58:33–15:59:58 | 0.65043 A | 0.58507 A | 30.68 |
| 100 W, 16:00:53–16:02:35 | 0.47450 A | 0.42759 A | 30.63 |

Üç pencerenin katsayılarının aritmetik ortalaması yaklaşık 30.6607'dir. V1.0 deneme YAML'inde 30.66 kullanılmıştır.

### Aşama 2 – Yeni katsayıyla tekrar ölçüm (şu anki adım)

- V1.0 YAML, Aşama 1'de bulunan **30.66** katsayısını uygular.
- Aynı 100 W ve 150 W yüklerde yeni ölçüm alınacaktır.
- Yeni PZEM ve SCT kararlı pencereleri ayrı ayrı kaydedilecek; yük geçişleri ve ilk sıçramalar dışarıda bırakılacaktır.
- Aşama 2 sonuçları Aşama 1 verileriyle karşılaştırılarak katsayının ölçüm hatasını ne ölçüde azalttığı değerlendirilecektir.
- Aşama 2 henüz yapılmadı; sonucu veya başarı durumu varsayılmayacaktır.

## Değerlendirme

- Aşama 1'de üç kararlı pencere 30.63–30.68 aralığında katsayı verdi.
- 30.66 yalnızca ADS1115 No.10 için geçici katsayıdır.
- PZEM karşılaştırma referansıdır; kusursuz ground truth olarak kabul edilmez.
- Bu katsayı başka ADS1115 modüllerine aktarılmayacaktır.

## Yazılım sürümleri ve koruma

- Temel kod: `KOD/MOD2-GRV001_KOD-0.yaml`
- Yeni katsayıyla deneme kodu: `V1.0/MOD2-GRV001_V1.0.yaml`
- Kod 0 değiştirilmemiştir; V1.0 ayrı dosyadır.
- V1.0 içindeki tek işlevsel değişiklik kalibrasyon katsayısının 27.60'tan 30.66'ya alınmasıdır. Diğer ESPHome ölçüm ayarları korunmuştur.

## Doğrulama durumu

| İş | Durum |
|---|---|
| Kod 0'ın yeniden oluşturulması ve temel dosya olarak saklanması | Yapıldı |
| ADS1115 No.10 ile başlangıç ölçümleri | Yapıldı |
| Kararlı pencerelerden 30.66 katsayısının hesaplanması | Yapıldı |
| V1.0 YAML hazırlanması ve depoya kaydı | Yapıldı |
| V1.0 derleme / cihaza yükleme | Kullanıcı testi bekleniyor |
| 30.66 ile 100 W ve 150 W tekrar ölçümü | Bekleniyor |
| Yeni katsayının doğrulanması | Bekleniyor |

## Sonraki kayıt

Aşama 2'de alınacak gerçek log/CSV ve yorumlar yalnızca bu sürümün `V1.0/LOG/` ve `V1.0/RAPOR/` klasörlerine eklenecektir. Ölçüm alınmadan başarı veya kesin kalibrasyon kararı verilmeyecektir.
