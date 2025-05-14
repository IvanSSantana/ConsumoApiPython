#Delete: utilizado para deletar dados de um servidor

import requests
from status_obtain import status_verify
from get_token import token

url = 'http://127.0.0.1:3001/alunos/2'

headers =  {
    'Authorization': token
}

response = requests.delete(url=url, headers=headers)

status_verify(response)