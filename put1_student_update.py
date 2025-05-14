#Put: utilizado para atualizar dados de um servidor

import requests
from status_obtain import status_verify
from get_token import token

url = 'http://127.0.0.1:3001/alunos/1'

headers =  {
    'Authorization': token
}

# No caso abaixo, vemos que ao passar somente um dado que queira atualizar ele atualiza com sucesso, ao contrário do post.
student_data = {
    "nome": "Fulaninho",
    "sobrenome": "Ousado",
    # "email": "fulanodetal@email.com",
    # "idade": "26",
    # "peso": "72.4",
    # "altura": "1.76"
}

response = requests.put(url=url, json=student_data, headers=headers)

status_verify(response)