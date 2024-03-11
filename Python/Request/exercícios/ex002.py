import requests

data = {'title': 'foo', 'body': 'bar', 'userId': 1}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

if response.status_code == 201:
    print('Novo post criado com ID:', response.json()['id'])
else:
    print('Erro:', response.status_code)
