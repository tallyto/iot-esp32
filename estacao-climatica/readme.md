# Estação Climática

Este é um projeto de estação climática que utiliza um sensor DHT11 para medir a temperatura e umidade relativa do ar e envia os dados para o serviço ThingSpeak para visualização e análise. Além disso, o projeto inclui uma funcionalidade de controle de relé com base nas condições climáticas.

## Funcionalidades

- Mede temperatura e umidade relativa do ar com o sensor DHT11.
- Envia os dados para o serviço ThingSpeak.
- Controla um relé com base nas condições climáticas (temperatura e umidade relativa do ar).
- Suporta conexão à rede Wi-Fi para envio de dados.

## Requisitos

- Microcontrolador compatível com MicroPython.
- Sensor DHT11.
- Acesso à internet para enviar dados para o ThingSpeak.
- Conta no ThingSpeak com chave de API válida.

## Como Usar

1. Conecte o sensor DHT11 ao seu microcontrolador conforme as especificações do fabricante.
2. Certifique-se de que a biblioteca `internet_connection.py` esteja presente no seu ambiente de desenvolvimento. Esta biblioteca deve conter a lógica para conectar-se à rede Wi-Fi.
3. Substitua `SSID` e `senha_wifi` pelo SSID e senha da sua rede Wi-Fi, respectivamente.
4. Substitua `sua_chave_API_ThingSpeak` pela sua chave de API do ThingSpeak.
5. Carregue o código na placa microcontroladora.
6. Observa a saída da estação climática para monitorar a temperatura, umidade relativa do ar e o estado do relé.

## Visualização dos Dados

Os dados enviados pela estação climática podem ser visualizados no [ThingSpeak](https://thingspeak.com/channels/2502279).

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
