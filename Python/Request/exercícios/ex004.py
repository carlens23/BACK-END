import requests

try:
    # Tentando fazer uma requisição GET para um URL inválido
    response = requests.get('https://example.com/invalid')
    response.raise_for_status()  # Lançando uma exceção se a requisição não for bem-sucedida

    print(response.text) 

except requests.HTTPError as err:
    print('Erro HTTP:', err)
except requests.ConnectionError as err:
    print('Erro de conexão:', err)
except requests.RequestException as err:
    print('Erro durante a requisição:', err)
