import requests
from status_obtain import status_verify
from get_token import token
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes

mimetypes = MimeTypes()

file_name = 'python_logo.png'
mimetype_file = mimetypes.guess_type(file_name)[0]

multipart = MultipartEncoder(fields={
    "foto": (file_name, open(file_name, 'rb'), mimetype_file),
    "aluno_id": "1"
})

url = 'http://127.0.0.1:3001/fotos'

headers =  {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

response = requests.post(url=url, headers=headers, data=multipart)
status_verify(response)