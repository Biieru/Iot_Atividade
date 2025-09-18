import requests
import json

# Configurações do canal ThingSpeak
CHANNEL_ID = "2943258"  # ID do canal fornecido
READ_API_KEY = "G3BDQS6I5PRGFEWR"  # Chave de leitura fornecida
RESULTS = 5  # Quantos registros obter

# URL da API do ThingSpeak
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results={RESULTS}"

print("Extraindo dados do ThingSpeak...")

try:
    # Faz a requisição para a API
    response = requests.get(url, timeout=10)
    
    if response.status_code == 200:
        # Converte a resposta para JSON
        data = response.json()
        
        print("\n=== DADOS EXTRAÍDOS ===")
        print(f"Canal: {data['channel']['name']}")
        print(f"Total de registros: {len(data['feeds'])}")
        print("-" * 40)
        
        # Exibe cada registro
        for i, feed in enumerate(data['feeds'], 1):
            print(f"Registro {i}:")
            print(f"  Data/Hora: {feed['created_at']}")
            print(f"  Temperatura: {feed['field1']} °C")
            print(f"  Umidade: {feed['field2']} %")
            print("-" * 30)
            
    else:
        print(f"Erro: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}")

