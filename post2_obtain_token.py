import requests
from status_obtain import status_verify

url = 'http://127.0.0.1:3001/tokens'

user_data = {
    "password": "1234567",
    "email": "cicranotal@gmail.com"
}

response = requests.post(url=url, json=user_data)

status_verify(response)

#NÃO FAÇA ISSO EM NUM PROGRAMA REAL!!! SOMENTE PARA FINS DIDÁTICOS
response_data = response.json()
token = response_data['token']

with open('token.txt', 'w') as file:
    file.write(token)