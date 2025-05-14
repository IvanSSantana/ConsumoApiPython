import requests

def status_verify(response: requests.models.Response):
    print(f'Status Code: {response.status_code}')
    print(f'Reason: {response.reason}')
    print(f'Text: {response.text}')
    print(f'JSON: {response.json()}')