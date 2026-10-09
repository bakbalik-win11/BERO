# Örnek Kod-1 — Python + USB–RS485 + Modbus RTU

## Kurulum
~~~bash
python -m pip install pymodbus pyserial
~~~

## Python başlangıç örneği
Pymodbus API'si sürümler arasında değişebildiğinden aşağıdaki örnek yaygın 3.x API'sini hedefler; kurulu sürümün belgeleriyle doğrula.

~~~python
from pymodbus.client import ModbusSerialClient

PORT = "COM3"       # Windows örneği; gerçek portla değiştir
SLAVE_ID = 1
client = ModbusSerialClient(
    port=PORT, baudrate=9600, bytesize=8,
    parity="N", stopbits=1, timeout=1
)
if not client.connect():
    raise RuntimeError(f"Serial port could not open: {PORT}")
try:
    result = client.read_input_registers(address=0, count=10, slave=SLAVE_ID)
    if result.isError():
        print("Modbus read failed:", result)
    else:
        print("Raw input registers:", result.registers)
finally:
    client.close()
~~~

Örnek ham input register'ları okur; mühendislik birimine dönüşüm ayrı belgede ele alınır. Bazı Pymodbus sürümlerinde slave parametresinin adı değişebilir. İlk testte yalnızca okuma işlevi kullan; 0x42 enerji sıfırlama ve 0x41 kalibrasyon komutlarını deneme.

**Durum:** Örnek taslak; USB adaptörü ve gerçek PZEM ile test edilmedi.