import requests

url = 'https://upload.wikimedia.org/wikipedia/commons/9/99/Unofficial_JavaScript_logo_2.svg'
file_name = url.split('/')[-1]

response = requests.get(url)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucess
    print(response.status_code)
    print(response.reason)

    with open(file_name, 'wb') as file:
        file.write(response.content)
else:
    # Error
    print(response.status_code)
    print(response.reason)