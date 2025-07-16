import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables del archivo .env

def consultar_dni(dni):
    token = os.getenv("RENIEC_TOKEN")  # leer el token desde variable de entorno
    url = f"https://api.apis.net.pe/v1/dni?numero={dni}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return f"Nombre: {data['nombres']} {data['apellidoPaterno']} {data['apellidoMaterno']}"
    else:
        return f"❌ Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    dni = input("Ingrese número de DNI: ")
    print(consultar_dni(dni))