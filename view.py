import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk


class View:

    # atualizar nome de funçoes tudo minusculo com _

    def __init__(self):
        ctk.set_appearance_mode("Light")  # Opções: "Dark", "Light", "System"
        ctk.set_default_color_theme("blue")  # Você pode mudar o tema aqui
        self.root = ctk.CTk()


        self.root.title("Cine Track")

        self.container = ctk.CTkFrame(self.root)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frameMenu = ctk.CTkFrame(self.container, fg_color="transparent")
        self.frameAdicionar = ctk.CTkFrame(self.container, fg_color="transparent")
        self.frameAtualizar = ctk.CTkFrame(self.container, fg_color="transparent")
        self.frameVisaoGeral = ctk.CTkFrame(self.container, fg_color="transparent")

        self.frameMenu.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)
        self.frameAdicionar.grid(row=0, column=0, sticky="nswe", padx=30, pady=10)
        self.frameAtualizar.grid(row=0, column=0, sticky="nswe", padx=20, pady=10)
        self.frameVisaoGeral.grid(row=0, column=0, sticky="nswe", padx=20, pady=10)

        self.telaMenu()
        self.telaAdicionar()
        self.telaAtualizar()
        self.telaGeral()

        self.showTelamenu()

        self.root.mainloop()

    def showTelamenu(self):

        self.frameMenu.tkraise()
        self.root.geometry("450x500")

    def showTelaAdicionar(self):

        self.frameAdicionar.tkraise()
        self.root.geometry("450x510")

    def showTelaAtualizar(self):

        self.frameAtualizar.tkraise()
        self.root.geometry("400x415")

    def showTelaVisaoGeral(self):

        self.frameVisaoGeral.tkraise()
        self.root.geometry("900x400")


    # ---------------Menu--------------------

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
                                      text_color="black",
                                      fg_color="grey",
                                      hover_color="#9A9A9A",
                                      cursor="hand2",
                                      command=self.showTelaAdicionar)
        btnNovoTitulo.pack(pady=10)

        btnAtualize = ctk.CTkButton(self.frameBotoesMenu,
                                      text="Atualize seu Progresso",
                                      font=ctk.CTkFont("Inter", 20),
                                      width=300,
                                      height=50,
                                      text_color="black",
                                      fg_color="grey",
                                      hover_color="#9A9A9A",
                                      cursor="hand2",
                                      command=self.showTelaAtualizar)
        btnAtualize.pack(pady=10)

        btnGeral = ctk.CTkButton(self.frameBotoesMenu,
                                      text="Visão Geral",
                                      font=ctk.CTkFont("Inter", 20),
                                      width=300,
                                      height=50,
                                      text_color="black",
                                      fg_color="grey",
                                      hover_color="#9A9A9A",
                                      cursor="hand2",
                                      command=self.showTelaVisaoGeral)
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

    # ---------------Adicionar Novo Título--------------------

    def telaAdicionar(self):
        self.tituloAdicionar()
        self.radioTipoAdicionar()
        self.nomeGeneroAdicionar()
        self.anoStreamingAdicionar()
        self.tempEpiAdicionar()
        self.statusAdicionar()
        self.spinAdicionar()
        self.botoesAdicionar()

    def tituloAdicionar(self):
        self.frameTituloAdicionar = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        self.frameTituloAdicionar.pack(pady=(5,10), anchor='w')

        titulo = ctk.CTkLabel(self.frameTituloAdicionar,
                              text="Adicionar Novo Título",
                              font=ctk.CTkFont("Inter", 24, weight="bold"))
        titulo.pack(anchor='w')

    def radioTipoAdicionar(self):
        frameRadioTipo = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        frameRadioTipo.pack(pady=(5,10), anchor='w')

        tipo_label = ctk.CTkLabel(frameRadioTipo,
                                  text="O que deseja adicionar:",
                                  font=ctk.CTkFont("Inter", 16))

        tipo_label.pack(anchor="w")

        self.tipoAdicionarVar = ctk.StringVar(value="Filme")

        radioFilme = ctk.CTkRadioButton(frameRadioTipo,
                                        text="Filme",
                                        variable=self.tipoAdicionarVar,
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

        radioSerie = ctk.CTkRadioButton(frameRadioTipo,
                                        text="Série",
                                        variable=self.tipoAdicionarVar,
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

    def nomeGeneroAdicionar(self):
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

        frameNomeGenero = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        frameNomeGenero.pack(anchor='w', fill="x", pady=(5,10))

        frameNomeAdicionar = ctk.CTkFrame(frameNomeGenero, fg_color="transparent")
        frameNomeAdicionar.pack( anchor='w', side="left")

        frameGenero = ctk.CTkFrame(frameNomeGenero, fg_color="transparent")
        frameGenero.pack(anchor="w", side="right")

        nomeLabel = ctk.CTkLabel(frameNomeAdicionar,
                                 text="Nome:",
                                 font=ctk.CTkFont("Inter", 16))
        nomeLabel.pack(anchor="w")

        self.entryNome = ctk.CTkEntry(frameNomeAdicionar,
                                 width=200,
                                 height=30,
                                 font=ctk.CTkFont("Inter", 12))
        self.entryNome.pack()

        labelGenero = ctk.CTkLabel(frameGenero,
                                   text="Gênero:",
                                   font=ctk.CTkFont("Inter", 16))
        labelGenero.pack(anchor="w")

        self.comboboxGeneroAdicionar = ctk.CTkOptionMenu(frameGenero,
                                            values=generos,
                                            dropdown_font=ctk.CTkFont("Inter", 12),
                                            font=ctk.CTkFont("Inter", 12, weight="bold"),
                                            fg_color="grey",
                                            button_color="#656565",
                                            button_hover_color="#414141",
                                            dropdown_fg_color="#AFB4BC",
                                            dropdown_hover_color="grey",
                                            dropdown_text_color="black",
                                            width=130,
                                            height=30)
        self.comboboxGeneroAdicionar.pack()

    def anoStreamingAdicionar(self):
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

        frameStremingAno = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        frameStremingAno.pack(anchor="w", fill="x", pady=(5,10))

        frameStreaming = ctk.CTkFrame(frameStremingAno, fg_color="transparent")
        frameStreaming.pack(anchor="w", side="left")

        frameAno = ctk.CTkFrame(frameStremingAno, fg_color="transparent")
        frameAno.pack(anchor="w", side="right")

        labelAno = ctk.CTkLabel(frameAno,
                                text="Ano:",
                                font=ctk.CTkFont("Inter", 16))
        labelAno.pack(anchor="w")

        self.entryAno = ctk.CTkEntry(frameAno,
                                width=100,
                                height=30,
                                font=ctk.CTkFont("Inter", 12))
        self.entryAno.pack()

        labelStraming = ctk.CTkLabel(frameStreaming,
                                       text="Streaming:",
                                       font=ctk.CTkFont("Inter", 16))
        labelStraming.pack(anchor="w")

        self.comboboxStreamingAdicionar = ctk.CTkOptionMenu(frameStreaming,
                                           values=streamings,
                                           dropdown_font=ctk.CTkFont("Inter", 12),
                                           font=ctk.CTkFont("Inter", 12, weight="bold"),
                                           fg_color="grey",
                                           button_color="#656565",
                                           button_hover_color="#414141",
                                           dropdown_fg_color="#AFB4BC",
                                           dropdown_hover_color="grey",
                                           dropdown_text_color="black"
                                           )
        self.comboboxStreamingAdicionar.pack()

    def tempEpiAdicionar(self):
        frameTempEpi = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        frameTempEpi.pack(anchor="w", fill="x", pady=(10, 10))

        frameTemp = ctk.CTkFrame(frameTempEpi, fg_color="transparent")
        frameTemp.pack(side="left")

        frameEpi = ctk.CTkFrame(frameTempEpi, fg_color="transparent")
        frameEpi.pack(side="right")

        labelTemp = ctk.CTkLabel(frameTemp,
                                 text="Temporadas:",
                                 font=ctk.CTkFont("Inter", 16))
        labelTemp.pack(side="left", anchor="w")

        self.entryTempAdicionar = ctk.CTkEntry(frameTemp,
                                 width=60,
                                 height=30,
                                 font=ctk.CTkFont("Inter", 12))
        self.entryTempAdicionar.pack(side="left", padx=(5, 0))

        labelEpi = ctk.CTkLabel(frameEpi,
                                text="Ep./Temp.:",
                                font=ctk.CTkFont("Inter", 16))
        labelEpi.pack(side="left", anchor="w")

        self.entryEpiAdicionar = ctk.CTkEntry(frameEpi,
                                width=60,
                                height=30,
                                font=ctk.CTkFont("Inter", 12))
        self.entryEpiAdicionar.pack(side="left")

    def statusAdicionar(self):
        frameStatus = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        frameStatus.pack(anchor="w", fill="x", pady=(0, 10))

        labelStatus = ctk.CTkLabel(frameStatus,
                                   text="Status",
                                   font=ctk.CTkFont("Inter", 16))
        labelStatus.pack(anchor="w")

        self.statusAdicionarVar = ctk.StringVar(value="")

        radioQuero = ctk.CTkRadioButton(frameStatus,
                                      text="Quero Assistir",
                                      variable=self.statusAdicionarVar,
                                      radiobutton_width=20,
                                      radiobutton_height=20,
                                      border_width_unchecked=3,
                                      border_width_checked=7,
                                      fg_color="#414141",
                                      hover_color="#6F6F83",
                                      border_color="grey",
                                      font=ctk.CTkFont("Inter", 14),
                                      value="Quero Assistir")
        radioQuero.pack(side="left", padx=(0,20))

        radioAssis = ctk.CTkRadioButton(frameStatus,
                                      text="Assistindo",
                                      variable=self.statusAdicionarVar,
                                      radiobutton_width=20,
                                      radiobutton_height=20,
                                      border_width_unchecked=3,
                                      border_width_checked=7,
                                      fg_color="#414141",
                                      hover_color="#6F6F83",
                                      border_color="grey",
                                      font=ctk.CTkFont("Inter", 14),
                                      value="Assistindo")
        radioAssis.pack(side="left", padx=(0,20))

        radioConc = ctk.CTkRadioButton(frameStatus,
                                     text="Concluído",
                                     variable=self.statusAdicionarVar,
                                     radiobutton_width=20,
                                     radiobutton_height=20,
                                     border_width_unchecked=3,
                                     border_width_checked=7,
                                     fg_color="#414141",
                                     hover_color="#6F6F83",
                                     border_color="grey",
                                     font=ctk.CTkFont("Inter", 14),
                                     value="Concluído")
        radioConc.pack(side="left")

    def spinAdicionar(self):
        frameNota = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        frameNota.pack(anchor="w", fill="x", pady=(5, 10))

        labelAvalie = ctk.CTkLabel(frameNota,
                                  text="Avalie esse título:",
                                  font=ctk.CTkFont("Inter", 16),
                                  )
        labelAvalie.pack(anchor="w", side="left", padx=(0, 5))

        self.spinNotaAdicionarVar = tk.IntVar(value=10)

        spinNota = tk.Spinbox(
                        frameNota,
                        from_=1,
                        to=10,
                        textvariable=self.spinNotaAdicionarVar,
                        width=2,
                        fg="black",
                        bg="#AFB4BC",
                        font=("Inter", 12),
                        justify="center",
                        text="Sua nota",
                        relief="groove")
        spinNota.pack(anchor="w")

    def botoesAdicionar(self):
        frameBotoesAdicionar = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        frameBotoesAdicionar.pack(anchor="center", pady=(10, 10))

        #trocar hover

        btnVoltar = ctk.CTkButton(frameBotoesAdicionar,
                                  text="Voltar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#9A9A9A",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.showTelamenu)
        btnVoltar.pack(side="left", padx=(0, 10))

        btnLimpar = ctk.CTkButton(frameBotoesAdicionar,
                                  text="Limpar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#9A9A9A",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=lambda: print("Limpar"))
        btnLimpar.pack(side="left", padx=(0, 10))

        btnSalvar = ctk.CTkButton(frameBotoesAdicionar,
                                  text="Salvar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#9A9A9A",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=lambda: print("Salvar"))
        btnSalvar.pack(side="left")

# ---------------Atualizar Título--------------------

    def telaAtualizar(self):
        self.tituloAtualizar()
        self.tipoAtualizar()
        self.selecaoSerieAtualizar()
        self.selecaoTempEpisAtualizar()
        self.statusAtualizar()
        self.notaAtualizar()

        self.botoesAtualizar()

    def tituloAtualizar(self):
        frameTitulo = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")
        frameTitulo.pack(pady=(5, 10), anchor="w")

        label = ctk.CTkLabel(frameTitulo,
                             text="Atualize seu Progresso",
                             font=ctk.CTkFont("Inter", 24, weight="bold"))
        label.pack(anchor="w")

    def tipoAtualizar(self):
        frame_tipo = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")
        frame_tipo.pack(anchor="w", pady=(5, 10))

        label = ctk.CTkLabel(frame_tipo,
                             text="O que deseja atualizar:",
                             font=ctk.CTkFont("Inter", 16))
        label.pack(anchor="w")

        self.tipoAtualizarVar = ctk.StringVar(value="Filme")

        radio_filme = ctk.CTkRadioButton(frame_tipo, text="Filme",
                                         variable=self.tipoAtualizarVar,
                                         value="Filme",
                                         font=ctk.CTkFont("Inter", 15),
                                         radiobutton_width=20,
                                         radiobutton_height=20,
                                         border_width_unchecked=3,
                                         border_width_checked=7,
                                         fg_color="#414141",
                                         hover_color="#6F6F83",
                                         border_color="grey")
        radio_filme.pack(side="left", padx=6)

        radio_serie = ctk.CTkRadioButton(frame_tipo, text="Série",
                                         variable=self.tipoAtualizarVar,
                                         value="Série",
                                         font=ctk.CTkFont("Inter", 15),
                                         radiobutton_width=20,
                                         radiobutton_height=20,
                                         border_width_unchecked=3,
                                         border_width_checked=7,
                                         fg_color="#414141",
                                         hover_color="#6F6F83",
                                         border_color="grey")
        radio_serie.pack(side="left")

    def selecaoSerieAtualizar(self):
        frameSerie = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")
        frameSerie.pack(anchor="w", pady=(5, 10))

        label = ctk.CTkLabel(frameSerie,
                             text="Selecione a série que deseja atualizar:",
                             font=ctk.CTkFont("Inter", 16))
        label.pack(anchor="w")

        self.seriesDisponiveis = ["Dark", "Wandinha", "Black Mirror"]

        self.comboSerie = ctk.CTkOptionMenu(frameSerie,
                                                values=self.seriesDisponiveis,
                                                dropdown_font=ctk.CTkFont("Inter", 12),
                                                font=ctk.CTkFont("Inter", 12, weight="bold"),
                                                fg_color="grey",
                                                button_color="#656565",
                                                button_hover_color="#414141",
                                                dropdown_fg_color="#AFB4BC",
                                                dropdown_hover_color="grey",
                                                dropdown_text_color="black")
        self.comboSerie.pack(side="left")

    def selecaoTempEpisAtualizar(self):
        frameTempEpi = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")
        frameTempEpi.pack(anchor="w", pady=(10, 0))

        labelTemp = ctk.CTkLabel(frameTempEpi,
                                 text="Temporada:",
                                 font=ctk.CTkFont("Inter", 16))
        labelTemp.pack(side="left", padx=(0, 2))

        self.tempAtualizarVar = tk.IntVar(value=1)
        self.qtdTempAtualizar = 3

        spinTemp = tk.Spinbox(frameTempEpi,
                              from_=1,
                              to=self.qtdTempAtualizar,
                              textvariable=self.tempAtualizarVar,
                              width=2,
                              fg="black",
                              bg="#AFB4BC",
                              font=("Inter", 12),
                              justify="center",
                              relief="groove")
        spinTemp.pack(side="left")

        labelEpi = ctk.CTkLabel(frameTempEpi,
                                text="Episódio:",
                                font=ctk.CTkFont("Inter", 16))
        labelEpi.pack(side="left", padx=(10, 2))

        self.epiAtualizarVar = tk.IntVar(value=1)
        self.qtdEpiAtualizar = 12

        spin_epi = tk.Spinbox(frameTempEpi,
                              from_=1,
                              to=self.qtdEpiAtualizar,
                              textvariable=self.epiAtualizarVar,
                              width=2,
                              fg="black",
                              bg="#AFB4BC",
                              font=("Inter", 12),
                              justify="center",
                              relief="groove")
        spin_epi.pack(side="left")

    def notaAtualizar(self):
        frameNota = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")
        frameNota.pack(anchor="w", fill="x", pady=(10, 10))

        labelAvalie = ctk.CTkLabel(frameNota,
                                   text="Avalie esse título:",
                                   font=ctk.CTkFont("Inter", 16),
                                   )
        labelAvalie.pack(anchor="w", side="left", padx=(0, 5))

        self.spinNotaAtulizarVar = tk.IntVar(value=10)

        spinNota = tk.Spinbox(
            frameNota,
            from_=1,
            to=10,
            textvariable=self.spinNotaAtulizarVar,
            width=2,
            fg="black",
            bg="#AFB4BC",
            font=("Inter", 12),
            justify="center",
            relief="groove")
        spinNota.pack(anchor="w")

    def statusAtualizar(self):
        frameStatus = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")
        frameStatus.pack(anchor="w", pady=(10, 10))

        labelStatus = ctk.CTkLabel(frameStatus, text="Status:", font=ctk.CTkFont("Inter", 16))
        labelStatus.pack(anchor="w")

        frameRadioStatus = ctk.CTkFrame(frameStatus, fg_color="transparent")
        frameRadioStatus.pack(anchor="w")

        self.statusAtualizarVar = ctk.StringVar(value="Assistindo")

        radioAssistindo = ctk.CTkRadioButton(frameRadioStatus,
                                              text="Assistindo",
                                              variable=self.statusAtualizarVar,
                                              value="Assistindo",
                                              font=ctk.CTkFont("Inter", 14),
                                              radiobutton_width=20,
                                              radiobutton_height=20,
                                              border_width_unchecked=3,
                                              border_width_checked=7,
                                              fg_color="#414141",
                                              hover_color="#6F6F83",
                                              border_color="grey")
        radioAssistindo.pack(side="left", padx=10)

        radioConcluido = ctk.CTkRadioButton(frameRadioStatus,
                                             text="Concluído",
                                             variable=self.statusAtualizarVar,
                                             value="Concluído",
                                             font=ctk.CTkFont("Inter", 14),
                                             radiobutton_width=20,
                                             radiobutton_height=20,
                                             border_width_unchecked=3,
                                             border_width_checked=7,
                                             fg_color="#414141",
                                             hover_color="#6F6F83",
                                             border_color="grey")
        radioConcluido.pack(side="left")

    def botoesAtualizar(self):
        frameBotoes = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")
        frameBotoes.pack(pady=10)

        btnVoltar = ctk.CTkButton(frameBotoes,
                                  text="Voltar",
                                  width=80,
                                  fg_color="#414141",
                                  hover_color="#9A9A9A",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.showTelamenu)
        btnVoltar.pack(side="left", padx=5)

        btnLimpar = ctk.CTkButton(frameBotoes,
                                  text="Limpar",
                                  width=80,
                                  fg_color="#414141",
                                  hover_color="#9A9A9A",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=lambda: print("Limpar"))
        btnLimpar.pack(side="left", padx=5)

        btnDeletar = ctk.CTkButton(frameBotoes,
                                   text="Deletar",
                                   width=80,
                                   fg_color="#414141",
                                   hover_color="#9A9A9A",
                                   font=ctk.CTkFont("Inter", 16),
                                   command=lambda: print("Deletar"))
        btnDeletar.pack(side="left", padx=5)

        btnAtualizar = ctk.CTkButton(frameBotoes,
                                     text="Atualizar",
                                     width=80,
                                     fg_color="#414141",
                                     hover_color="#9A9A9A",
                                     font=ctk.CTkFont("Inter", 16),
                                     command=lambda: messagebox.showinfo("CineTrack", "O título foi Atualizado."))
        btnAtualizar.pack(side="left", padx=5)

# ---------------Visão Geral--------------------

    def telaGeral(self):
        self.tituloVisaoGeral()
        self.tipoVisaoGeral()
        self.filtrosSecao()
        self.criarTabela()

    def tituloVisaoGeral(self):
        frameTitulo = ctk.CTkFrame(self.frameVisaoGeral, fg_color="transparent")
        frameTitulo.pack(pady=(5, 10), anchor="w")

        labelVisaoGeral = ctk.CTkLabel(frameTitulo,
                             text="Visão Geral",
                             font=ctk.CTkFont("Inter", 24, weight="bold"))
        labelVisaoGeral.pack(anchor="w")

    def tipoVisaoGeral(self):
        frame_tipo = ctk.CTkFrame(self.frameVisaoGeral, fg_color="transparent")
        frame_tipo.pack(anchor="w", pady=(5, 10))

        label = ctk.CTkLabel(frame_tipo,
                             text="O que deseja visualizar:",
                             font=ctk.CTkFont("Inter", 16))
        label.pack(anchor="w")

        self.tipoAtualizarVar = ctk.StringVar(value="Filme")

        radio_filme = ctk.CTkRadioButton(frame_tipo, text="Filme",
                                         variable=self.tipoAtualizarVar,
                                         value="Filme",
                                         font=ctk.CTkFont("Inter", 15),
                                         radiobutton_width=20,
                                         radiobutton_height=20,
                                         border_width_unchecked=3,
                                         border_width_checked=7,
                                         fg_color="#414141",
                                         hover_color="#6F6F83",
                                         border_color="grey")
        radio_filme.pack(side="left", padx=6)

        radio_serie = ctk.CTkRadioButton(frame_tipo, text="Série",
                                         variable=self.tipoAtualizarVar,
                                         value="Série",
                                         font=ctk.CTkFont("Inter", 15),
                                         radiobutton_width=20,
                                         radiobutton_height=20,
                                         border_width_unchecked=3,
                                         border_width_checked=7,
                                         fg_color="#414141",
                                         hover_color="#6F6F83",
                                         border_color="grey")
        radio_serie.pack(side="left")

    def filtrosSecao(self):

        streamings = ["---", "Netflix", "Prime Video", "Max", "Disney +", "Apple TV +", "Globoplay",
                            "Paramount +", "Youtube", "Alugar"]

        genero_values = ["---", "Ação", "Aventura", "Comédia", "Documentário", "Drama", "Terror", "Suspense", "Sci-fi",
                         "Romance", "Musical"]
        status_values = ["---", "Assistindo", "Concluído", "Quero Assistir"]
        ordenar_por_values = ["---", "Nome (A-Z)", "Nome (Z-A)", "Ano (Recente)", "Ano (Antigo)", "Nota (Maior)",
                              "Nota (Menor)"]

        frameFiltros = ctk.CTkFrame(self.frameVisaoGeral, fg_color="transparent")
        frameFiltros.pack(pady=(5, 10))

        frameStreaming = ctk.CTkFrame(frameFiltros, fg_color="transparent")
        frameStreaming.pack(side="left", padx=15)

        frameGenero = ctk.CTkFrame(frameFiltros, fg_color="transparent")
        frameGenero.pack(side="left", padx=15)

        frameStatus = ctk.CTkFrame(frameFiltros, fg_color="transparent")
        frameStatus.pack(side="left", padx=15)

        frameOrdenar = ctk.CTkFrame(frameFiltros, fg_color="transparent")
        frameOrdenar.pack(side="left", padx=15)

        labelStraming = ctk.CTkLabel(frameStreaming,
                                     text="Streaming:",
                                     font=ctk.CTkFont("Inter", 16))
        labelStraming.pack(anchor="w")

        self.comboboxStreamingAdicionar = ctk.CTkOptionMenu(frameStreaming,
                                                            values=streamings,
                                                            dropdown_font=ctk.CTkFont("Inter", 12),
                                                            font=ctk.CTkFont("Inter", 12, weight="bold"),
                                                            fg_color="grey",
                                                            button_color="#656565",
                                                            button_hover_color="#414141",
                                                            dropdown_fg_color="#AFB4BC",
                                                            dropdown_hover_color="grey",
                                                            dropdown_text_color="black"
                                                            )
        self.comboboxStreamingAdicionar.pack()

        labelGenero = ctk.CTkLabel(frameGenero,
                                     text="Genero:",
                                     font=ctk.CTkFont("Inter", 16))
        labelGenero.pack(anchor="w")

        self.comboboxGeneroAtualizar = ctk.CTkOptionMenu(frameGenero,
                                                            values=genero_values,
                                                            dropdown_font=ctk.CTkFont("Inter", 12),
                                                            font=ctk.CTkFont("Inter", 12, weight="bold"),
                                                            fg_color="grey",
                                                            button_color="#656565",
                                                            button_hover_color="#414141",
                                                            dropdown_fg_color="#AFB4BC",
                                                            dropdown_hover_color="grey",
                                                            dropdown_text_color="black")
        self.comboboxGeneroAtualizar.pack()

        labelStatus = ctk.CTkLabel(frameStatus,
                                   text="Status:",
                                   font=ctk.CTkFont("Inter", 16))
        labelStatus.pack(anchor="w")

        self.comboboxStatusAtualizar = ctk.CTkOptionMenu(frameStatus,
                                                         values=status_values,
                                                         dropdown_font=ctk.CTkFont("Inter", 12),
                                                         font=ctk.CTkFont("Inter", 12, weight="bold"),
                                                         fg_color="grey",
                                                         button_color="#656565",
                                                         button_hover_color="#414141",
                                                         dropdown_fg_color="#AFB4BC",
                                                         dropdown_hover_color="grey",
                                                         dropdown_text_color="black")
        self.comboboxStatusAtualizar.pack()

        labelOrdenar = ctk.CTkLabel(frameOrdenar,
                                   text="Ordenar por:",
                                   font=ctk.CTkFont("Inter", 16))
        labelOrdenar.pack(anchor="w")

        self.comboboxStatusAtualizar = ctk.CTkOptionMenu(frameOrdenar,
                                                         values=ordenar_por_values,
                                                         dropdown_font=ctk.CTkFont("Inter", 12),
                                                         font=ctk.CTkFont("Inter", 12, weight="bold"),
                                                         fg_color="grey",
                                                         button_color="#656565",
                                                         button_hover_color="#414141",
                                                         dropdown_fg_color="#AFB4BC",
                                                         dropdown_hover_color="grey",
                                                         dropdown_text_color="black")
        self.comboboxStatusAtualizar.pack()

    def criarTabela(self):
        table_frame = ctk.CTkFrame(self.frameVisaoGeral, fg_color="transparent")
        table_frame.pack(fill="both", expand=False, padx=10, pady=(0, 15))
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)

        style = ttk.Style(table_frame)

        try:
            style.theme_use("clam")
        except tk.TclError:
            style.theme_use("default")

        style.configure("Treeview.Heading",
                        font=('Inter', 12, 'bold'),
                        background="#C4C4C4",
                        foreground="black",
                        borderwidth = 0,
                        relief = "flat")

        style.map("Treeview.Heading",
                  background=[('active', 'grey')])

        style.configure("Treeview",
                        font=('Inter', 9),
                        rowheight=25)

        style.map("Treeview",
                  background=[('selected', 'grey')],
                  foreground=[('selected', 'white')])

        tabela = ttk.Treeview(table_frame, columns=[], show='headings')

        tabela.tag_configure('cinza',
                             background='#EBEBEB',
                             foreground='black')
        tabela.tag_configure('branco',
                             background='white',
                             foreground='black')

        dados = [
            ("Stranger Things", "Suspense", "Concluído", 2016, "100%", 4, 34, 9.4),  # Exemplo original
            ("Good Girls", "Comédia", "Concluído", 2018, "100%", 4, 50, 9.7),  # Exemplo original
            ("Elite", "Drama", "Assistindo", 2018, "84%", 8, 64, "---"),  # Exemplo original
            ("Breaking Bad", "Drama", "Concluído", 2008, "100%", 5, 62, 9.5),
            ("Game of Thrones", "Fantasia", "Concluído", 2011, "100%", 8, 73, 9.2),
            ("The Simpsons", "Animação", "Assistindo", 1989, "92%", 36, 780, 8.7),
            # Estimativa de % e episódios baseada na longevidade
            ("Friends", "Comédia", "Concluído", 1994, "100%", 10, 235, 8.9),
            ("The Office (US)", "Comédia", "Concluído", 2005, "100%", 9, 201, 9.0),
            ("Squid Game", "Suspense", "Assistindo", 2021, "50%", 2, 18, 8.0),  # Estimativa para S2
            ("Wednesday", "Comédia", "Assistindo", 2022, "50%", 2, 16, 8.1),  # Estimativa para S2
            ("Money Heist", "Ação", "Concluído", 2017, "100%", 5, 41, 8.2),
            ("The Witcher", "Fantasia", "Assistindo", 2019, "60%", 5, 40, 8.1),  # Estimativa para temporadas futuras
            ("Black Mirror", "Ficção Científica", "Assistindo", 2011, "85%", 7, 33, 8.7),
            # Estimativa, incluindo especiais e futuras
            ("The Crown", "Drama", "Concluído", 2016, "100%", 6, 60, 8.7),
            ("Peaky Blinders", "Crime", "Concluído", 2013, "100%", 6, 36, 8.8),
            ("Dark", "Mistério", "Concluído", 2017, "100%", 3, 26, 8.7),
            ("The Mandalorian", "Ficção Científica", "Assistindo", 2019, "75%", 4, 32, 8.7),  # Estimativa para S4
            ("Chernobyl", "Drama Histórico", "Concluído", 2019, "100%", 1, 5, 9.4),  # Minissérie
            ("The Queen's Gambit", "Drama", "Concluído", 2020, "100%", 1, 7, 8.5),  # Minissérie
            ("Ted Lasso", "Comédia", "Concluído", 2020, "100%", 3, 34, 8.8),
            ("Severance", "Ficção Científica", "Assistindo", 2022, "50%", 2, 18, 8.7),  # Estimativa para S2
            ("Succession", "Drama", "Concluído", 2018, "100%", 4, 39, 8.9),
            ("The Last of Us", "Ação", "Assistindo", 2023, "50%", 2, 18, 8.8),  # Estimativa para S2
            ("Yellowstone", "Drama", "Assistindo", 2018, "90%", 5, 53, 8.7),  # Episódios e % estimados para final da S5
            ("House of the Dragon", "Fantasia", "Assistindo", 2022, "25%", 4, 40, 8.4),
            # Estimativa para temporadas futuras
            ("The Handmaid's Tale", "Drama", "Assistindo", 2017, "83%", 6, 66, 8.4),  # Estimativa para S6 final
            ("Rick and Morty", "Animação", "Assistindo", 2013, "70%", 10, 81, 9.1),
            # Estimativa para temporadas futuras
            ("Ozark", "Suspense", "Concluído", 2017, "100%", 4, 44, 8.5)
        ]
        cabecalhos = ["Título", "Gênero", "Status", "Ano", "Progresso", "Temps.", "Eps.", "Media Geral"]

        tabela['columns'] = cabecalhos

        for col in cabecalhos:
            tabela.heading(col, text=col)
            if col == "Título":
                tabela.column(col, anchor=tk.W, width=80)
            elif col == "Media Geral":
                tabela.column(col, anchor=tk.CENTER, width=50)
            else:
                tabela.column(col, anchor=tk.CENTER, width=20)

        for i, item in enumerate(dados):
            if i % 2 == 0:
                tabela.insert("", tk.END, values=item, tags=('cinza',))
            else:
                tabela.insert("", tk.END, values=item, tags=('branco',))

        scrollbar = ctk.CTkScrollbar(table_frame, command=tabela.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        tabela.configure(yscrollcommand=scrollbar.set)

        tabela.grid(row=0, column=0, sticky="nsew")

    def create_action_buttons_section(self):
        """Creates the 'Voltar', 'Limpar', 'Filtrar' buttons."""
        buttons_frame = ctk.CTkFrame(self.frameVisaoGeral, fg_color="transparent")
        # Center the frame itself using grid
        buttons_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=(10, 10))

        # Use a sub-frame to group buttons and then center this sub-frame
        # This allows buttons to have their natural width rather than expanding
        inner_buttons_frame = ctk.CTkFrame(buttons_frame, fg_color="transparent")
        inner_buttons_frame.pack(anchor="center")  # Center the inner frame

        # Button styling based on the image (light gray)
        btn_fg_color = "#EAEAEA"
        btn_hover_color = "#D0D0D0"
        btn_text_color = "#333333"  # Dark gray text for better contrast on light button

        btn_voltar = ctk.CTkButton(inner_buttons_frame,
                                   text="Voltar",
                                   font=self.font_button,
                                   width=110,
                                   height=35,
                                   fg_color=btn_fg_color,
                                   hover_color=btn_hover_color,
                                   text_color=btn_text_color,
                                   command=self.action_voltar)  # Placeholder command
        btn_voltar.pack(side="left", padx=(0, 15))

        btn_limpar = ctk.CTkButton(inner_buttons_frame,
                                   text="Limpar",
                                   font=self.font_button,
                                   width=110,
                                   height=35,
                                   fg_color=btn_fg_color,
                                   hover_color=btn_hover_color,
                                   text_color=btn_text_color,
                                   command=self.action_limpar)  # Placeholder command
        btn_limpar.pack(side="left", padx=(0, 15))

        btn_filtrar = ctk.CTkButton(inner_buttons_frame,
                                    text="Filtrar",
                                    font=self.font_button,
                                    width=110,
                                    height=35,
                                    fg_color=btn_fg_color,
                                    hover_color=btn_hover_color,
                                    text_color=btn_text_color,
                                    command=self.action_filtrar)  # Placeholder command
        btn_filtrar.pack(side="left")

if __name__ == "__main__":
    View()




