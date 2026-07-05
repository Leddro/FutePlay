import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env para não expor suas chaves
load_dotenv()

def buscar_info_time(nome_time="Flamengo"):
    """
    Busca informações de um time específico na API de Futebol.
    """
    # ATENÇÃO: Pegue a URL exata do endpoint (ex: /teams ou /search) lá no painel do RapidAPI
    url = "https://free-api-live-football-data.p.rapidapi.com/football-get-team"

    # Busca a chave que você salvou no arquivo .env
    api_key = os.getenv("RAPIDAPI_KEY")

    if not api_key:
        print("Erro: Chave da API não encontrada no arquivo .env!")
        return None

    # Parâmetros da busca (pode variar conforme a documentação da API)
    querystring = {"search": nome_time}

    # Cabeçalhos obrigatórios do RapidAPI
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "free-api-live-football-data.p.rapidapi.com"
    }

    try:
        print(f"Buscando dados do {nome_time}...")
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Levanta um erro se a requisição falhar (ex: erro 401 ou 404)

        # Converte a resposta em formato JSON para um dicionário Python
        dados = response.json()
        return dados

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao conectar com a API: {e}")
        return None

# Bloco de teste: só roda se você executar este arquivo diretamente
if __name__ == "__main__":
    resultado = buscar_info_time()

    if resultado:
        print("\n=== Dados Recebidos da API ===")
        print(resultado)