import requests

# Cabeçalhos personalizados
headers = {'User-Agent': 'MeuScript/1.0'}

response = requests.get('https://api.github.com/user', headers=headers)

if response.status_code == 200:
    print(response.json())  # Imprimindo informações do usuário do GitHub
else:
    print('Erro:', response.status_code)
