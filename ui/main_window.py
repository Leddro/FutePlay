import customtkinter as ctk
# 1. IMPORTANTE: Importamos a nossa função da API aqui no topo!
from core.football_api import buscar_proximo_jogo

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Matchday Mood ⚽🎵")
        self.geometry("750x500")
        self.minsize(600, 400)

        # ==========================================
        # MENU LATERAL (Mantido igual)
        # ==========================================
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        self.logo_label = ctk.CTkLabel(self.sidebar, text="Matchday Mood", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(padx=20, pady=(20, 30))

        self.btn_dashboard = ctk.CTkButton(self.sidebar, text="🏠 Painel do Jogo")
        self.btn_dashboard.pack(padx=20, pady=10)

        self.btn_spotify = ctk.CTkButton(self.sidebar, text="🎵 Conectar Spotify", fg_color="#1DB954", hover_color="#1ED760", text_color="black", font=ctk.CTkFont(weight="bold"))
        self.btn_spotify.pack(padx=20, pady=10)

        # ==========================================
        # ÁREA PRINCIPAL
        # ==========================================
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.titulo_main = ctk.CTkLabel(self.main_frame, text="Próximo Jogo", font=ctk.CTkFont(size=28, weight="bold"))
        self.titulo_main.pack(anchor="w", pady=(0, 20))

        self.card_jogo = ctk.CTkFrame(self.main_frame, corner_radius=15, fg_color="#1E1E1E")
        self.card_jogo.pack(fill="x", ipady=30)

        self.info_status = ctk.CTkLabel(self.card_jogo, text="Aguardando conexão com a API de Futebol...", text_color="gray", font=ctk.CTkFont(size=14))
        self.info_status.pack(pady=20) # Diminuí o pady para caber o botão

        # 2. NOVO: Botão para carregar os dados
        # O parâmetro 'command' diz qual função deve rodar ao clicar no botão
        self.btn_atualizar = ctk.CTkButton(self.card_jogo, text="🔄 Buscar Jogo", command=self.carregar_dados_api)
        self.btn_atualizar.pack(pady=10)

    # ==========================================
    # MÉTODOS DA INTERFACE (Ação dos Botões)
    # ==========================================

    def carregar_dados_api(self):
        """
        Função acionada quando o botão 'Buscar Jogo' é clicado.
        """
        self.info_status.configure(text="Procurando próximo confronto...", text_color="white")
        self.update()

        # Chama a função que criamos
        dados = buscar_proximo_jogo()

        if "erro" in dados:
            self.info_status.configure(text=f"Erro: {dados['erro']}", text_color="red")
        else:
            # Exibe o texto formatado no meio do card, com fonte maior e na cor de destaque
            self.info_status.configure(
                text=dados["sucesso"],
                text_color="#1DB954", # Verde combinando com o botão do Spotify
                font=ctk.CTkFont(size=22, weight="bold")
            )