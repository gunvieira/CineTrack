import customtkinter as ctk
import tkinter as tk
from controller import Controller

class View:

    def __init__(self):
        ctk.set_appearance_mode("Light")  # Opções: "Dark", "Light", "System"
        ctk.set_default_color_theme("blue")  # Você pode mudar o tema aqui
        self.root = ctk.CTk()


        self.root.title("Cine Track")

        self.container = ctk.CTkFrame(self.root)
        self.container.pack(fill="both", expand=True)

        self.frameMenu = ctk.CTkFrame(self.container, fg_color="transparent")
        self.frameAdicionar = ctk.CTkFrame(self.container, fg_color="transparent")

        self.frameMenu.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)
        self.frameAdicionar.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

        self.telaMenu()
        self.telaAdicionar()

        self.showTelamenu()

        self.root.mainloop()

    def showTelamenu(self):

        self.frameMenu.tkraise()

    def showAdicionar(self):

        self.frameAdicionar.tkraise()


    # ---------------MENU--------------------

    def telaMenu(self):
        self.tituloMenu()
        self.botoesMenu()
        self.citacao()

    def tituloMenu(self):
        self.frameBemvindo = ctk.CTkFrame(self.frameMenu, fg_color="transparent")
        self.frameBemvindo.pack(pady=3)

        labelBemvindo = ctk.CTkLabel(self.frameBemvindo,
                                     text="Bem vindo ao",
                                     font=ctk.CTkFont("Inter", 24),
                                     text_color="#747474")
        labelBemvindo.pack(anchor="w", padx=3)

        labelCineTrack = ctk.CTkLabel(self.frameBemvindo,
                                      text="CineTrack",
                                      font=ctk.CTkFont("Inter", 64, weight="bold"))
        labelCineTrack.pack(anchor="w")

    def botoesMenu(self):
        self.frameBotoesMenu = ctk.CTkFrame(self.frameMenu, fg_color="transparent")
        self.frameBotoesMenu.pack(pady=3)

        btnNovoTitulo = ctk.CTkButton(self.frameBotoesMenu,
                                      text="Adicionar Novo Título",
                                      font=ctk.CTkFont("Inter", 20),
                                      width=300,
                                      height=50,
                                      text_color="#000000",
                                      fg_color="#C7C7D7",
                                      hover_color="#BDBDC9",
                                      cursor="hand2",
                                      command=self.showAdicionar)
        btnNovoTitulo.pack(pady=10)

        btnAtualize = ctk.CTkButton(self.frameBotoesMenu,
                                      text="Atualize seu Progresso",
                                      font=ctk.CTkFont("Inter", 20),
                                      width=300,
                                      height=50,
                                      text_color="#000000",
                                      fg_color="#C7C7D7",
                                      hover_color="#BDBDC9",
                                      cursor="hand2")
        btnAtualize.pack(pady=10)

        btnGeral = ctk.CTkButton(self.frameBotoesMenu,
                                      text="Visão Geral",
                                      font=ctk.CTkFont("Inter", 20),
                                      width=300,
                                      height=50,
                                      text_color="#000000",
                                      fg_color="#C7C7D7",
                                      hover_color="#BDBDC9",
                                      cursor="hand2")
        btnGeral.pack(pady=10)

    def citacao(self):
        self.frameCitacao = ctk.CTkFrame(self.frameMenu, fg_color="transparent")
        self.frameCitacao.pack(pady=10)

        labelCitacao = ctk.CTkLabel(self.frameCitacao,
                                    text='"Your imagination can create a reality."',
                                    font=ctk.CTkFont("Segoe UI", 15, slant="italic"))
        labelCitacao.pack()

        labelAutorCitacao = ctk.CTkLabel(self.frameCitacao,
                                         text="James Cameron",
                                         font=ctk.CTkFont("Segoe UI", 12, slant="italic"))
        labelAutorCitacao.pack(anchor='e')

        # ---------------MENU--------------------

    def telaAdicionar(self):


        self.tituloAdicionar()
        self.botoes()


    def tituloAdicionar(self):

        titulo = ctk.CTkLabel(self.frameAdicionar, text="Adicionar Novo Título", font=ctk.CTkFont(size=22, weight="bold"))
        titulo.pack()



    def botoes(self):


        voltar_btn = ctk.CTkButton(self.frameAdicionar, text="Voltar", command=self.showTelamenu)
        voltar_btn.pack(side="left", padx=10)

        limpar_btn = ctk.CTkButton(self.frameAdicionar, text="Limpar", command=lambda: print("Limpar"))
        limpar_btn.pack(side="left", padx=10)

        salvar_btn = ctk.CTkButton(self.frameAdicionar, text="Salvar", command=lambda: print("Salvar"))
        salvar_btn.pack(side="left", padx=10)


"""
     def botoesAdicionar(self):
        # Tipo (Filme ou Série)
        tipo_frame = ctk.CTkFrame(janela, fg_color="transparent")
        tipo_frame.pack(fill="x", padx=20)

        tipo_label = ctk.CTkLabel(tipo_frame, text="O que deseja adicionar:")
        tipo_label.pack(anchor="w")

        tipo_var = ctk.StringVar(value="Série")
        ctk.CTkRadioButton(tipo_frame, text="Filme", variable=tipo_var, value="Filme").pack(side="left", padx=10)
        ctk.CTkRadioButton(tipo_frame, text="Série", variable=tipo_var, value="Série").pack(side="left")

        # Nome
        nome_label = ctk.CTkLabel(janela, text="Nome:")
        nome_label.pack(anchor="w", padx=20, pady=(15, 0))
        nome_entry = ctk.CTkEntry(janela)
        nome_entry.pack(fill="x", padx=20)

        # Gênero e Ano
        genero_ano_frame = ctk.CTkFrame(janela, fg_color="transparent")
        genero_ano_frame.pack(fill="x", padx=20, pady=(10, 0))

        genero_frame = ctk.CTkFrame(genero_ano_frame, fg_color="transparent")
        genero_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
        genero_label = ctk.CTkLabel(genero_frame, text="Gênero")
        genero_label.pack(anchor="w")
        genero_menu = ctk.CTkOptionMenu(genero_frame, values=["Ação", "Comédia", "Drama", "Terror", "Ficção"])
        genero_menu.pack(fill="x")

        ano_frame = ctk.CTkFrame(genero_ano_frame, fg_color="transparent")
        ano_frame.pack(side="left", fill="x", expand=True, padx=(5, 0))
        ano_label = ctk.CTkLabel(ano_frame, text="Ano")
        ano_label.pack(anchor="w")
        ano_entry = ctk.CTkEntry(ano_frame)
        ano_entry.pack(fill="x")

        # Temporadas e Episódios
        temp_epi_frame = ctk.CTkFrame(janela, fg_color="transparent")
        temp_epi_frame.pack(fill="x", padx=20, pady=(10, 0))

        temp_frame = ctk.CTkFrame(temp_epi_frame, fg_color="transparent")
        temp_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
        temp_label = ctk.CTkLabel(temp_frame, text="Temporadas")
        temp_label.pack(anchor="w")
        temp_entry = ctk.CTkEntry(temp_frame)
        temp_entry.pack(fill="x")

        epi_frame = ctk.CTkFrame(temp_epi_frame, fg_color="transparent")
        epi_frame.pack(side="left", fill="x", expand=True, padx=(5, 0))
        epi_label = ctk.CTkLabel(epi_frame, text="Episódios por Temporada")
        epi_label.pack(anchor="w")
        epi_entry = ctk.CTkEntry(epi_frame)
        epi_entry.pack(fill="x")

        # Streaming
        streaming_label = ctk.CTkLabel(janela, text="Streaming:")
        streaming_label.pack(anchor="w", padx=20, pady=(10, 0))
        streaming_menu = ctk.CTkOptionMenu(janela, values=["Netflix", "Amazon Prime", "HBO", "Disney+", "Outro"])
        streaming_menu.pack(fill="x", padx=20)

        # Status
        status_frame = ctk.CTkFrame(janela, fg_color="transparent")
        status_frame.pack(fill="x", padx=20, pady=(10, 0))

        status_label = ctk.CTkLabel(status_frame, text="Status:")
        status_label.pack(anchor="w")

        status_var = ctk.StringVar(value="Concluído")
        ctk.CTkRadioButton(status_frame, text="Quero Assistir", variable=status_var, value="Quero Assistir").pack(side="left", padx=5)
        ctk.CTkRadioButton(status_frame, text="Assistindo", variable=status_var, value="Assistindo").pack(side="left", padx=5)
        ctk.CTkRadioButton(status_frame, text="Concluído", variable=status_var, value="Concluído").pack(side="left", padx=5)

        # Avaliação
        nota_label = ctk.CTkLabel(janela, text="Avalie esse título!")
        nota_label.pack(anchor="w", padx=20, pady=(10, 0))
        nota_menu = ctk.CTkOptionMenu(janela, values=[str(i) for i in range(1, 11)])
        nota_menu.pack(fill="x", padx=20)

        spin_var = tk.StringVar(value="1")
        spinbox = tk.Spinbox(janela, from_=1, to=10, textvariable=spin_var, width=10, font=("Arial", 14))
        spinbox.pack()

"""




if __name__ == "__main__":
    View()

