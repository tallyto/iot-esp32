import time
import network

def connection(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    attempt = 0 
    while attempt < 30:
        print("Tentativa: ", attempt)
        if station.isconnected():
            print("Conectado!!!")
            break
        print("Desconectado")
        time.sleep(1)
        attempt += 1
    return station

