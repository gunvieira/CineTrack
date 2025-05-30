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

        self.frameMenu.grid(row=0, column=0, sticky="nsew", padx=50, pady=30)
        self.frameAdicionar.grid(row=0, column=0, sticky="nsew", padx=50, pady=30)

        self.telaMenu()
        self.telaAdicionar()

        self.showTelamenu()

        self.root.mainloop()

    def showTelamenu(self):

        self.frameMenu.tkraise()

    def showTelaAdicionar(self):

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
                                      command=self.showTelaAdicionar)
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

        # ---------------Adicionar novo titulo--------------------

    def telaAdicionar(self):


        self.tituloAdicionar()
        self.radioTipoAdicionar()
        self.inputAdicionar()
        self.botoes()




    def tituloAdicionar(self):
        self.frameTituloAdicionar = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        self.frameTituloAdicionar.pack(pady=10, anchor='w')

        titulo = ctk.CTkLabel(self.frameTituloAdicionar,
                              text="Adicionar Novo Título",
                              font=ctk.CTkFont("Inter", 24, weight="bold"))
        titulo.pack(anchor='e')

    def radioTipoAdicionar(self):
        self.frameRadioTipo = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        self.frameRadioTipo.pack(pady=5, anchor='w')

        tipo_label = ctk.CTkLabel(self.frameRadioTipo,
                                  text="O que deseja adicionar:",
                                  font=ctk.CTkFont("Inter", 16))

        tipo_label.pack(anchor="w", pady=(0,6))

        tipoVar = ctk.StringVar(value="Filme")

        radioFilme = ctk.CTkRadioButton(self.frameRadioTipo,
                                        text="Filme",
                                        variable=tipoVar,
                                        radiobutton_width=20,
                                        radiobutton_height=20,
                                        border_width_unchecked=3,
                                        border_width_checked=7,
                                        fg_color="#414141",
                                        hover_color="#6F6F83",
                                        border_color="grey",
                                        font=ctk.CTkFont("Inter", 15),
                                        value="Filme")
        radioFilme.pack(side="left", padx=6)

        radioSerie = ctk.CTkRadioButton(self.frameRadioTipo,
                                        text="Série",
                                        variable=tipoVar,
                                        radiobutton_width=20,
                                        radiobutton_height=20,
                                        border_width_unchecked=3,
                                        border_width_checked=7,
                                        fg_color="#414141",
                                        hover_color="#6F6F83",
                                        border_color="grey",
                                        font=ctk.CTkFont("Inter", 15),
                                        value="Série")
        radioSerie.pack(side="left")

    def botoes(self):
        frameBotoesAdicionar = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        frameBotoesAdicionar.pack(anchor='w', pady=(10,0))


        voltar_btn = ctk.CTkButton(frameBotoesAdicionar, text="Voltar", command=self.showTelamenu, width=30)
        voltar_btn.pack(side="left", padx=10)

        limpar_btn = ctk.CTkButton(frameBotoesAdicionar, text="Limpar", width=30, command=lambda: print("Limpar"))
        limpar_btn.pack(side="left", padx=10)

        salvar_btn = ctk.CTkButton(frameBotoesAdicionar, text="Salvar", width=30, command=lambda: print("Salvar"))
        salvar_btn.pack(side="left", padx=10)

    def inputAdicionar(self):
        frameInputsAdicionar = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        frameInputsAdicionar.pack(anchor='w')

        frameNomeAdicionar = ctk.CTkFrame(frameInputsAdicionar, fg_color="transparent")
        frameNomeAdicionar.pack(anchor='w', pady=(0,10))

        # Nome
        nomeLabel = ctk.CTkLabel(frameNomeAdicionar,
                                  text="Nome",
                                  font=ctk.CTkFont("Inter", 16))
        nomeLabel.pack(anchor="w", pady=(10, 0))

        nomeEntry = ctk.CTkEntry(frameNomeAdicionar,
                                  width=270,
                                  height=30,
                                  font=ctk.CTkFont("Inter", 12))
        nomeEntry.pack(anchor="w")

        # Gênero e Ano
        frameGeneroAno = ctk.CTkFrame(frameInputsAdicionar, fg_color="transparent")
        frameGeneroAno.pack(anchor="w", pady=(0,15))

        frameGenero = ctk.CTkFrame(frameGeneroAno, fg_color="transparent")
        frameGenero.pack(anchor="w",side="left")

        genero_label = ctk.CTkLabel(frameGenero,
                                    text="Gênero",
                                    font=ctk.CTkFont("Inter", 16))
        genero_label.pack(anchor="w")

        generos = [
            "Ação",
            "Aventura",
            "Comédia",
            "Documentário",
            "Drama",
            "Terror",
            "Suspense",
            "Sci-fi",
            "Romance",
            "Musical"
        ]

        genero_menu = ctk.CTkOptionMenu(frameGenero,
                                        values=generos,
                                        dropdown_font=ctk.CTkFont("Inter", 12),
                                        font=ctk.CTkFont("Inter", 12, weight="bold"),
                                        fg_color="grey",
                                        button_color="#656565",
                                        button_hover_color="#414141",
                                        dropdown_fg_color="#AFB4BC",
                                        dropdown_hover_color="#414141",
                                        dropdown_text_color="white"
                                        )
        genero_menu.pack()

        frameAno = ctk.CTkFrame(frameGeneroAno, fg_color="transparent")
        frameAno.pack(side="left", anchor="w")

        anoLabel = ctk.CTkLabel(frameAno,
                                    text="Ano",
                                    font=ctk.CTkFont("Inter", 16))
        anoLabel.pack(anchor="w", padx=(60,0))

        anoEntry = ctk.CTkEntry(frameAno,
                                  width=70,
                                  height=30,
                                  font=ctk.CTkFont("Inter", 12))
        anoEntry.pack(anchor="w", padx=(60,0))


        # Gênero e Ano

        # Temporadas e Episódios
        frameTempEpi = ctk.CTkFrame(frameInputsAdicionar, fg_color="transparent")
        frameTempEpi.pack(pady=(5,10),anchor="w")

        frameTemp = ctk.CTkFrame(frameTempEpi, fg_color="transparent")
        frameTemp.pack(side="left")

        labelTemp = ctk.CTkLabel(frameTemp,
                                  text="Temp.",
                                  font=ctk.CTkFont("Inter", 16))
        labelTemp.pack(side="left", anchor="w")

        entryTemp = ctk.CTkEntry(frameTemp,
                                  width=50,
                                  height=30,
                                  font=ctk.CTkFont("Inter", 12)
                                  )
        entryTemp.pack(side="left", padx=(5,0))

        frameEpi = ctk.CTkFrame(frameTempEpi, fg_color="transparent")
        frameEpi.pack(side="left", padx=(41,0))

        labelEpi = ctk.CTkLabel(frameEpi,
                                 text="Ep./Temp.",
                                 font=ctk.CTkFont("Inter", 16))
        labelEpi.pack(side="left", anchor="w")
        entryEpi = ctk.CTkEntry(frameEpi,
                                 width=50,
                                 height=30,
                                 font=ctk.CTkFont("Inter", 12)
                                 )
        entryEpi.pack(side="left", padx=(5,0))

 # Streaming

        streamings = [
            "Alugar",
            "Apple TV +",
            "Disney +",
            "Globoplay",
            "Max",
            "Netflix",
            "Paramount +",
            "Prime Video",
            "Youtube"
        ]

        frameStreaming = ctk.CTkFrame(frameInputsAdicionar, fg_color="transparent")
        frameStreaming.pack(pady=(5,10), anchor="w")

        streaming_label = ctk.CTkLabel(frameStreaming,
                                       text="Streaming",
                                       font=ctk.CTkFont("Inter", 16))
        streaming_label.pack(anchor="w")

        streaming_menu = ctk.CTkOptionMenu(frameStreaming,
                                        values=streamings,
                                        dropdown_font=ctk.CTkFont("Inter", 12),
                                        font=ctk.CTkFont("Inter", 12, weight="bold"),
                                        fg_color="grey",
                                        button_color="#656565",
                                        button_hover_color="#414141",
                                        dropdown_fg_color="#AFB4BC",
                                        dropdown_hover_color="#414141",
                                        dropdown_text_color="white"
                                        )
        streaming_menu.pack()


        # Status
        frameStatus = ctk.CTkFrame(frameInputsAdicionar, fg_color="transparent")
        frameStatus.pack(pady=(10, 0), anchor="w")

        labelStatus = ctk.CTkLabel(frameStatus,
                                    text="Status",
                                    font=ctk.CTkFont("Inter", 16))
        labelStatus.pack(anchor="w")

        statusVar = ctk.StringVar(value="")
        btnQuero = ctk.CTkRadioButton(frameStatus,
                                      text="Quero Assistir",
                                      variable=statusVar,
                                      radiobutton_width=20,
                                      radiobutton_height=20,
                                      border_width_unchecked=3,
                                      border_width_checked=7,
                                      fg_color="#414141",
                                      hover_color="#6F6F83",
                                      border_color="grey",
                                      font=ctk.CTkFont("Inter", 12),
                                      value="Quero Assistir")
        btnQuero.pack(side="left", padx=5)

        btnAssis = ctk.CTkRadioButton(frameStatus,
                                      text="Assistindo",
                                      variable=statusVar,
                                      radiobutton_width=20,
                                      radiobutton_height=20,
                                      border_width_unchecked=3,
                                      border_width_checked=7,
                                      fg_color="#414141",
                                      hover_color="#6F6F83",
                                      border_color="grey",
                                      font=ctk.CTkFont("Inter", 12),
                                      value="Assistindo")
        btnAssis.pack(side="left", padx=5)

        btnConc = ctk.CTkRadioButton(frameStatus,
                                     text="Concluído",
                                     variable=statusVar,
                                     radiobutton_width=20,
                                     radiobutton_height=20,
                                     border_width_unchecked=3,
                                     border_width_checked=7,
                                     fg_color="#414141",
                                     hover_color="#6F6F83",
                                     border_color="grey",
                                     font=ctk.CTkFont("Inter", 12),
                                     value="Concluído")
        btnConc.pack(side="left")

        # Avaliação
        frameNota = ctk.CTkFrame(frameInputsAdicionar, fg_color="transparent")
        frameNota.pack(pady=(10, 0), anchor="w")

        nota_label = ctk.CTkLabel(frameNota,
                                  text="Avalie esse título",
                                  font=ctk.CTkFont("Inter", 16),
                                  )
        nota_label.pack(anchor="w")

        spin_var = tk.IntVar(value=1)

        # Cria o widget Spinbox
        spinbox = tk.Spinbox(
            frameNota,
            from_=1,
            to=10,
            textvariable=spin_var,
            width=2,
            font=("Inter", 12),
            justify="center",
            relief="groove"

        )
        spinbox.pack(anchor="w")






if __name__ == "__main__":
    View()

