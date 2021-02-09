# Humpy Pump.py

Buy and sell crypto fast and easy with a simple callback in discord

## Instalacion
Es una instalacion sencilla, como cualquier otro programa de python
```bash
git clone https://github.com/MysteriusFat/pulp-discord-bot.git
pip install requirements.txt
```
## Uso

Es muy simple solo declaras el channel_id donde se manda la senal de compra, el separador de la moneda y el profit
```bash 
python humpypump.py -h
usage: humpypump.py [-h] [-id CHANNEL_ID] [-s SEPARATOR] [-p PROFIT] [--fee FEE]

HumpyPump.py is a fast pump bot for buy and sell cryptos

optional arguments:
  -h, --help      show this help message and exit
  -id CHANNEL_ID  ID of discord channel where the buy signal is trigger
  -s SEPARATOR    Is the trigger signal of buying coin. Example: Buy $SKY in coinbase
  -p PROFIT       Is the multiplicator value of next sell of the cryptos what you buy. Example: if you put 2.00 in this variable and you buy $DOGE at 0.5 $ you sell your $DOGE in 1.00$. A high value
                  incremet the risk of lose your invertion.
  --fee FEE       Is the fee of binance sometimes this changes and you can update
```

Ejemplo:
```bash 
python humpypump.py id=321321321 -s=$ -p=2.00
```

## Configuracion

Esta parte es importante para que el programa funcione correctamente. Antes de iniciar el programa se necesita abrir el archivo config.py y poner tus propias api keys y cookies

Binance auth:
  - Ir a https://www.binance.com/es/my/settings/api-management y crear una nueva api 
  - Cuando tengas tu api_key y secret_key copiarla en el archivo config.py

deveria quedar algo como esto:

```python
# Binance config
apy_key = "YOUR_API_KEY"
secret_key = "YOUR_SECRET_KEY"
```

Dicord cookie y channel_id:
  - Primero tienen que activar el modo desarollador de discord el cual se encuentra en configuracion > apariencia
  - Cuando ya este activo apretas ```ctrl + shift + I```
  - ahora al igual que el impeccionar elemento vas a buscar la cookie llamada ```__cfduid``` y la copias en el archivo config.py
  - Para conseguir el ```channel_id``` solamante vamos al discord del pulp y hacemos click derecho en el canal donde se avisara la crypto que se va a comprar 
  - apretamos en copiar channel id para ponerlo en el archivo config.py

deberia quedar algo asi:
```python
# Discord config
cookie = '__cfduid=YOUR_DISCORD_COOKIE; locale=es-ES'
```
