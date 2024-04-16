import machine
import time
import dht
import urequests
from internet_connection import connection

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

def sendTemperatureAndHumidityToThingSpeak(api_key, temperature, humidity):
    url = 'https://api.thingspeak.com/update?api_key={}&field1={}&field2={}'.format(api_key, temperature, humidity)
    response = urequests.get(url)
    print(response.text)
    response.close()

station = connection("KAMILA", '12345678')
if not station.isconnected():
    print("Erro de conexão com a rede WIFI! Tente novamente.")
else:
    print("Conexão realizada com sucesso!")
#     station.disconnect()


while True:
    d.measure()
    t = d.temperature()
    h = d.humidity()
    
    sendTemperatureAndHumidityToThingSpeak('EZBXXRD6C0TDBHO4', t,h)
      
    print("Disciplina: Cloud, IoT e Indústria 4.0 - 2024/1º")
    print("Professor: Valmir Moro")
    print("-" * 50)
    print("Equipe")
    print("Aluno: Tállyto Sousa Rodrigues")
    print("-" * 50)
    print("Climate Season")
    print("Temperatura Atual: {}°C".format(t))
    print("Umidade Relativa do Ar Atual: {}%".format(h))
    print("-" * 50)
    print("Condições de Acionamento do Relé")
    print("Temperatura > 31°C.")
    print("Umidade Relativa do Ar > 70%.")
    print()
   
    if(t >= 31 or h >= 70):
        r.value(1)
        print("Rele ligado")
    else:
        r.value(0)
        print("Rele desligado")

    
    time.sleep(5)


