import customtkinter as ctk

# Configuração global de tema do aplicativo
ctk.set_appearance_mode("dark")  # Opções: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Temas padrão: "blue", "green", "dark-blue"

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Matchday Mood ⚽🎵")
        self.geometry("750x500")
        self.minsize(600, 400) # Evita que a janela fique pequena demais e quebre o layout

        # ==========================================
        # 1. MENU LATERAL (Sidebar)
        # ==========================================
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y") # Preenche todo o eixo Y (vertical)

        # Título da Sidebar
        self.logo_label = ctk.CTkLabel(
            self.sidebar,
            text="Matchday Mood",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.logo_label.pack(padx=20, pady=(20, 30))

        # Botões de Navegação
        self.btn_dashboard = ctk.CTkButton(self.sidebar, text="🏠 Painel do Jogo")
        self.btn_dashboard.pack(padx=20, pady=10)

        # Botão do Spotify (Com as cores reais da marca)
        self.btn_spotify = ctk.CTkButton(
            self.sidebar,
            text="🎵 Conectar Spotify",
            fg_color="#1DB954",
            hover_color="#1ED760",
            text_color="black",
            font=ctk.CTkFont(weight="bold")
        )
        self.btn_spotify.pack(padx=20, pady=10)

        # ==========================================
        # 2. ÁREA PRINCIPAL (Conteúdo)
        # ==========================================
        # Criamos um frame transparente para agrupar o conteúdo da direita
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        # Título da Seção
        self.titulo_main = ctk.CTkLabel(
            self.main_frame,
            text="Próximo Jogo",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.titulo_main.pack(anchor="w", pady=(0, 20)) # anchor="w" alinha à esquerda (West)

        # Card que vai receber os dados da API
        self.card_jogo = ctk.CTkFrame(self.main_frame, corner_radius=15, fg_color="#1E1E1E")
        self.card_jogo.pack(fill="x", ipady=30) # ipady dá um preenchimento interno vertical

        # Texto temporário (Placeholder)
        self.info_status = ctk.CTkLabel(
            self.card_jogo,
            text="Aguardando conexão com a API de Futebol...",
            text_color="gray",
            font=ctk.CTkFont(size=14)
        )
        self.info_status.pack(pady=40)

# Bloco de execução isolada
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()