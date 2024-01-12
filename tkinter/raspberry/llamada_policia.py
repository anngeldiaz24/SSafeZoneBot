import os
import time # para la medición y espera de tiempo
from netmiko import ConnectHandler # para facilitar la automatización de dispositivos de red a través de SSH
from dotenv import load_dotenv # para cargar las variables del .env

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Accedemos a las variables de entorno
HOST = os.getenv('HOST')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

def llamarPolicia():
    # Configuramos las credenciales del celular para poder conectarnos a través de SSH
    celular = {
        'device_type': 'linux',
        'host': HOST,
        'username': USERNAME,
        'password': PASSWORD,
        'port': 8022,
    }

    # Establecemos la conexión SSH
    ssh = ConnectHandler(**celular)
    # Enviamos el comando que utiliza termux para interactuar con el celular y hacer la llamada
    ssh.send_command("termux-telephony-call +523310906952")
    # Esperamos 30 segundos mientras se hace la llamada
    time.sleep(30)

    # Cerramos la conexión SSH
    ssh.disconnect()