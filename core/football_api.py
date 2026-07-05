import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def buscar_jogador(nome_jogador="Arrascaeta"):
    """
    Busca informações de um jogador específico na API de Futebol.
    """
    # URL corrigida usando o endpoint exato que estava no seu painel do RapidAPI
    url = "https://free-api-live-football-data.p.rapidapi.com/football-players-search"

    api_key = os.getenv("RAPIDAPI_KEY")

    if not api_key:
        print("Erro: Chave da API não encontrada no arquivo .env!")
        return None

    # Parâmetro de busca
    querystring = {"search": nome_jogador}

    # Cabeçalhos obrigatórios do RapidAPI
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
    }

    try:
        print(f"Buscando dados de: {nome_jogador}...")
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()

        dados = response.json()
        return dados

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao conectar com a API: {e}")
        return None

# Bloco de teste
if __name__ == "__main__":
    resultado = buscar_jogador()

    if resultado:
        print("\n=== Dados Recebidos da API ===")
        print(resultado)