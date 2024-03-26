import machine
import time
import dht

d = dht.DHT11(machine.Pin(4))

while True:
    d.measure()
    print("Temperatura = {}".format(d.temperature()))
    print("Umidade = {}".format(d.humidity()))
    time.sleep(5)
