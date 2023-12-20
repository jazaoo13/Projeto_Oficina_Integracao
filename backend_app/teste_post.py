import requests

# URL da rota
url = 'http://192.168.1.25:5000/update_database'  # Atualize com o seu URL real

# Dados para a solicitação POST (se necessário)
data = {'cod_barra': '78969954434', 'peso': '6666'}

# Realiza 5 solicitações POST de teste
for _ in range(5):
    try:
        response = requests.post(url, json=data)

        # Verifica o código de status da resposta
        if response.status_code == 200:
            print('POST bem-sucedido!')
            print(response.json())
        else:
            print(f'Erro no POST. Código de status: {response.status_code}')
            print(response.json())
    
    except Exception as e:
        print(f'Erro na solicitação POST: {e}')
