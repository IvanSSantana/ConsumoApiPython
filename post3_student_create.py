import requests
from status_obtain import status_verify
from get_token import token

url = 'http://127.0.0.1:3001/alunos'

headers =  {
    'Authorization': token
}

student_data = {
    "nome": "Fulano",
    "sobrenome": "Siclano",
    "email": "fulanodetal@email.com",
    "idade": "26",
    "peso": "72.4",
    "altura": "1.76"
}

response = requests.post(url=url, json=student_data, headers=headers)

status_verify(response)