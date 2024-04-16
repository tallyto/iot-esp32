import time
from internet_connection import connection


while True:
    print("Conectando com a rede WIFI...")
    time.sleep(2)
    station = connection("Aluno-Estacio", None)
    if not station.isconnected():
        print("Erro de conexão com a rede WIFI! Tente novamente.")
    else:
        print("Conexão realizada com sucesso!")
    station.disconnect()
    
    time.sleep(10)

