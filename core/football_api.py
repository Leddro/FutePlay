import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()

# Horário de Brasília (UTC-3; o Brasil não tem horário de verão desde 2019)
FUSO_BRASILIA = timezone(timedelta(hours=-3), "BRT")

def buscar_proximo_jogo():
    """
    Busca a agenda completa e usa a inteligência do Python para
    filtrar e retornar apenas o jogo mais próximo.
    """
    # Endpoint de busca geral (retorna times e partidas)
    url = "https://free-api-live-football-data.p.rapidapi.com/football-all-search"

    api_key = os.getenv("RAPIDAPI_KEY")
    if not api_key:
        return {"erro": "Chave da API não encontrada no .env"}

    # Parâmetro de busca
    querystring = {"search": "Flamengo"}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        dados = response.json()

        # Entrando nas chaves do JSON para pegar a lista de sugestões
        sugestoes = dados.get("response", {}).get("suggestions", [])
        jogos_futuros = []

        for item in sugestoes:
            # Garante que estamos olhando para uma partida (match)
            if item.get("type") == "match":
                status = item.get("status", {})

                # Se o jogo ainda não começou e não terminou, é um jogo futuro!
                if status.get("started") == False and status.get("finished") == False:

                    # A API retorna a data em UTC (ex: 2026-07-11T10:00:00Z); converte para o horário de Brasília
                    data_utc = datetime.fromisoformat(item["matchDate"].replace("Z", "+00:00"))
                    data_jogo = data_utc.astimezone(FUSO_BRASILIA)

                    # Guarda as informações essenciais na nossa lista
                    jogos_futuros.append({
                        "mandante": item["homeTeamName"],
                        "visitante": item["awayTeamName"],
                        "data": data_jogo,
                        "campeonato": item["leagueName"]
                    })

        if not jogos_futuros:
            return {"erro": "Nenhum jogo futuro encontrado."}

        # O Pulo do Gato: Ordena a lista de jogos futuros pela data (do mais perto ao mais longe)
        jogos_futuros.sort(key=lambda x: x["data"])

        # Pega o primeiro item da lista ordenada (o próximo jogo!)
        proximo = jogos_futuros[0]

        # Formata a data para o padrão brasileiro (Dia/Mês/Ano às Hora:Minuto)
        data_formatada = proximo["data"].strftime("%d/%m/%Y às %H:%M")

        # Monta um texto limpo e direto para enviar para a tela
        texto_final = f"🏆 {proximo['campeonato']}\n\n⚽ {proximo['mandante']} x {proximo['visitante']}\n📅 {data_formatada}"

        return {"sucesso": texto_final}

    except Exception as e:
        return {"erro": f"Falha na API: {str(e)}"}