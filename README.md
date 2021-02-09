# Pulp discord bot

Buy and sell crypto fast and easy with a simple callback in discord

## Instalacion
Es una instalacion sencilla, como cualquier otro programa de python
```bash
git clone https://github.com/MysteriusFat/pulp-discord-bot.git
pip install requirements.txt
python3 run.py
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
channel_id = '807200314460602401'
cookie = '__cfduid=YOUR_DISCORD_COOKIE; locale=es-ES'
```

despues de seguir los pasos puedes ejecutar el programa y estaria listo para funcionar
de todas formas este programa es solo una prueba y el codigo deberia ser revisado cualquier mal funcionamento sera arreglado despues de las pruebas que se realizaran hoy a las 4pm
# HumpyPump.py
