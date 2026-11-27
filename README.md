# BERO

BERO deposunun ana çalışma alanları:

- [DONANIM](DONANIM/): Ortak sensör, bileşen ve donanım kayıtları.
- [ENVANTER](ENVANTER/): Fiziksel bileşen ve modüllerin mevcut/yaşam döngüsü durumu.
- [PREBERO](PREBERO/): Hazırlık, masaüstü deneyleri, modül ve görev takibi.
- [OGRENME](OGRENME/): Ekipman ve teknik konularda bağımsız öğrenme kayıtları.
- [docs/decisions](docs/decisions/): Depo genelindeki karar kayıtları.

## Bilginin sensörden nihai modüle ilerlemesi

- Bir sensöre ait kalıcı tecrübe ve tekrar kullanılabilecek kod parçacıkları sensörün DONANIM klasöründe tutulur. Kod ve bilgi, denenmiş/doğrulanmış/başvuru niteliği gibi durumuyla etiketlenir.
- Sensörün deneyleri, bağlantı denemeleri, ham verisi, sürümleri ve olgunlaşma kayıtları ilgili PREBERO modül ve görevinde tutulur.
- Deneyle olgunlaşan bilgi nihai cihaz modülüne aktarılır; kaynak sensör ve deney kayıtları korunur, aktarım bağlantıyla gösterilir.
- Bir fiziksel modül devreden çıksa veya imha edilse bile modülün adı, amacı ve çalışma geçmişi depodan silinmez. Fiziksel durum ENVANTER'de, teknik geçmiş ilgili modül/görev kayıtlarında güncellenir.

## Devam noktası

PREBERO'da çalışmaya başlarken [DURUM.md](PREBERO/DURUM.md) okunur. Bu dosya güncel aşamayı, kısa geçmişi ve sonraki adımı gösterir; ayrıntılı deney kanıtlarına bağlantı verir.

Donanım ve envanter kayıtları merkezi tutulur; modüller bu bilgileri kopyalamak yerine ortak DONANIM ve ENVANTER kayıtlarına bağlanır.
