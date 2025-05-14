#Post: utilizado para enviar dados a um servidor

import requests
from status_obtain import status_verify

url = 'http://127.0.0.1:3001/users'

user_data = {
    "nome": "Circrano Desconhecido",
    "password": "1234567",
    "email": "cicranotal@gmail.com"
}

response = requests.post(url=url, json=user_data)

status_verify(response)