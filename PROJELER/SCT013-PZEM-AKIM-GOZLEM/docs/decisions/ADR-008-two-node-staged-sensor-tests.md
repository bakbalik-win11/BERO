# ADR-008 — İki ölçüm düğümü ve aşamalı sensör testleri (tarihsel karar)

- **Tarih:** 2026-10-30
- **Durum:** TARİHSEL / FAZ 1 KAPANIŞIYLA AKTİF PLAN OLMAKTAN ÇIKTI
- **İlişkili karar:** ADR-011

## Tarihsel karar

Bu ADR, ESP-1'in SCT013 ana ölçüm kolu olarak ayrılması ve ESP-2 üzerinde PZEM-004T V3.0, ACS712-5A ve ZMCT103C-5A sensörlerinin aşamalı test edilmesi fikrini kayda almıştı. Testlerin fiziksel olarak yapıldığı anlamına gelmiyordu.

## Güncel durum

Faz 1'in ana hedefi dış kaynaklı çalışan kodla ±%4 sapma olarak sağlandığı için Faz 1 kapsamında kalan yapılmamış deney ve işler kapatıldı. Bu ADR'deki ESP-2 sensör test planı da aktif deney planı değildir ve uygulanmak üzere beklememektedir.

Donanım envanterindeki ACS712-5A ve ZMCT103C-5A kayıtları silinmez; bunların mevcut olması yeni test planı açıldığı anlamına gelmez. Faz 2, önce HA verisini PC'ye aktarma ve bulunan SCT kodunu PZEM ile eğitme işidir.

Eski teknik bağlam için [donanım envanteri](../../hardware/inventory.md) ve [Faz 1 deney arşivi](../../experiments/README.md) korunur. E09 açılmamış plan olduğu için kaldırılmıştır.
