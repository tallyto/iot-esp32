import machine
import time
import dht

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

while True:
    d.measure()
    t = d.temperature()
    h = d.humidity()
    
    if(t >= 30 and h >= 70):
        r.value(1)
    else:
        r.value(0)
      
    
    print("Temperatura = {}".format(t))
    print("Umidade = {}".format(h))
    

    
    time.sleep(5)
