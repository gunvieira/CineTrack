import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk


class View:

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
        self.root.geometry("600x815")


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
        self.create_table_section()





    def create_title_section(self):
        """Creates the main title 'Visão Geral'."""
        title_label = ctk.CTkLabel(self.frameVisaoGeral,
                                   text="Visão Geral",
                                   font=self.font_title,
                                   anchor="w")
        title_label.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 15))

    def create_type_selection_section(self):
        """Creates the 'O que deseja visualizar:' section with radio buttons."""
        frame_type_selection = ctk.CTkFrame(self.frameVisaoGeral, fg_color="transparent")
        frame_type_selection.grid(row=1, column=0, sticky="w", padx=10, pady=(0, 15))

        label_type = ctk.CTkLabel(frame_type_selection,
                                  text="O que deseja visualizar:",
                                  font=self.font_subtitle)
        label_type.pack(side="left", padx=(0, 10))

        self.tipo_visualizar_var = ctk.StringVar(value="Série")  # Default selection based on image

        radio_filme = ctk.CTkRadioButton(frame_type_selection,
                                         text="Filme",
                                         font=self.font_radio_text,
                                         variable=self.tipo_visualizar_var,
                                         value="Filme")
        radio_filme.pack(side="left", padx=(0, 10))

        radio_serie = ctk.CTkRadioButton(frame_type_selection,
                                         text="Série",
                                         font=self.font_radio_text,
                                         variable=self.tipo_visualizar_var,
                                         value="Série")
        radio_serie.pack(side="left")

    def create_filters_section(self):
        """Creates the filter dropdowns: Streaming, Gênero, Status, Ordenar por."""
        filters_main_frame = ctk.CTkFrame(self.frameVisaoGeral, fg_color="transparent")
        filters_main_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 20))

        # Configure columns to distribute space. We have 4 filters.
        filters_main_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # --- Placeholder values for dropdowns (add more as needed) ---
        streaming_values = ["---", "Netflix", "Prime Video", "Max", "Disney +", "Apple TV +", "Globoplay",
                            "Paramount +", "Youtube", "Alugar"]
        genero_values = ["---", "Ação", "Aventura", "Comédia", "Documentário", "Drama", "Terror", "Suspense", "Sci-fi",
                         "Romance", "Musical"]
        status_values = ["---", "Assistindo", "Concluído", "Quero Assistir"]
        ordenar_por_values = ["---", "Nome (A-Z)", "Nome (Z-A)", "Ano (Recente)", "Ano (Antigo)", "Nota (Maior)",
                              "Nota (Menor)"]

        # --- Filter 1: Streaming ---
        frame_streaming = ctk.CTkFrame(filters_main_frame, fg_color="transparent")
        frame_streaming.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        label_streaming = ctk.CTkLabel(frame_streaming, text="Streaming:", font=self.font_filter_label, anchor="w")
        label_streaming.pack(fill="x", pady=(0, 2))
        self.combo_streaming = ctk.CTkOptionMenu(frame_streaming,
                                                 values=streaming_values,
                                                 font=self.font_filter_option,
                                                 dropdown_font=self.font_filter_option)
        self.combo_streaming.pack(fill="x")

        # --- Filter 2: Gênero ---
        frame_genero = ctk.CTkFrame(filters_main_frame, fg_color="transparent")
        frame_genero.grid(row=0, column=1, sticky="ew", padx=10)
        label_genero = ctk.CTkLabel(frame_genero, text="Gênero:", font=self.font_filter_label, anchor="w")
        label_genero.pack(fill="x", pady=(0, 2))
        self.combo_genero = ctk.CTkOptionMenu(frame_genero,
                                              values=genero_values,
                                              font=self.font_filter_option,
                                              dropdown_font=self.font_filter_option)
        self.combo_genero.pack(fill="x")

        # --- Filter 3: Status ---
        frame_status = ctk.CTkFrame(filters_main_frame, fg_color="transparent")
        frame_status.grid(row=0, column=2, sticky="ew", padx=10)
        label_status = ctk.CTkLabel(frame_status, text="Status:", font=self.font_filter_label, anchor="w")
        label_status.pack(fill="x", pady=(0, 2))
        self.combo_status = ctk.CTkOptionMenu(frame_status,
                                              values=status_values,
                                              font=self.font_filter_option,
                                              dropdown_font=self.font_filter_option)
        self.combo_status.pack(fill="x")

        # --- Filter 4: Ordenar por ---
        frame_ordenar = ctk.CTkFrame(filters_main_frame, fg_color="transparent")
        frame_ordenar.grid(row=0, column=3, sticky="ew", padx=(10, 0))
        label_ordenar = ctk.CTkLabel(frame_ordenar, text="Ordenar por:", font=self.font_filter_label, anchor="w")
        label_ordenar.pack(fill="x", pady=(0, 2))
        self.combo_ordenar = ctk.CTkOptionMenu(frame_ordenar,
                                               values=ordenar_por_values,
                                               font=self.font_filter_option,
                                               dropdown_font=self.font_filter_option)
        self.combo_ordenar.pack(fill="x")

    def create_table_section(self):
        # --- Font definitions (using Inter as in the original code) ---
        self.font_title = ctk.CTkFont("Inter", 30, weight="bold")
        self.font_subtitle = ctk.CTkFont("Inter", 16)
        self.font_radio_text = ctk.CTkFont("Inter", 14)
        self.font_filter_label = ctk.CTkFont("Inter", 14)
        self.font_filter_option = ctk.CTkFont("Inter", 12)
        self.font_button = ctk.CTkFont("Inter", 15, weight="bold")
        self.font_table_header = ctk.CTkFont("Inter", 11, weight="bold")
        self.font_table_row = ctk.CTkFont("Inter", 10)


        """Creates the table/Treeview to display data."""
        table_frame = ctk.CTkFrame(self.frameVisaoGeral, fg_color="transparent")
        table_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 15))
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)

        # --- Style for Treeview (to match CustomTkinter look and feel) ---
        # The Treeview header background in the image is a light purplish-gray.
        # Treeview item rows are white.
        style = ttk.Style()
        # Note: theme_use might affect other ttk widgets if you have them.
        # 'clam' is often a good base for custom styling.
        try:
            style.theme_use("clam")
        except tk.TclError:
            # Fallback if 'clam' is not available on all systems
            style.theme_use("default")

        style.configure("Treeview.Heading",
                        font=self.font_table_header,
                        background="#E8E8F0",  # Light purplish-gray for header
                        foreground="black",
                        relief="flat",
                        padding=(5, 5))
        style.map("Treeview.Heading",
                  relief=[('active', 'groove'), ('!active', 'flat')])

        style.configure("Treeview",
                        font=self.font_table_row,
                        background="white",  # Background of the tree itself
                        fieldbackground="white",  # Background of the fields
                        foreground="black",
                        rowheight=25,  # Adjust row height
                        relief="solid",  # Border around the treeview
                        borderwidth=1,
                        )
        # Remove border from items, use a light gray for selected item
        style.map('Treeview',
                  background=[('selected', '#D0D0D5')],
                  foreground=[('selected', 'black')],
                  borderwidth=[('focus', 0), ('!focus', 0)])

        columns = ("titulo", "genero", "status", "ano", "progresso", "temporadas", "episodios", "media_notas")

        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", style="Treeview")

        # --- Define headings ---
        self.tree.heading("titulo", text="Título", anchor=tk.W)
        self.tree.heading("genero", text="Gênero", anchor=tk.W)
        self.tree.heading("status", text="Status", anchor=tk.W)
        self.tree.heading("ano", text="Ano", anchor=tk.CENTER)
        self.tree.heading("progresso", text="Progresso", anchor=tk.CENTER)
        self.tree.heading("temporadas", text="Temporadas", anchor=tk.CENTER)
        self.tree.heading("episodios", text="Episódios", anchor=tk.CENTER)
        self.tree.heading("media_notas", text="Media das Notas", anchor=tk.CENTER)

        # --- Define column widths (adjust as needed) ---
        self.tree.column("titulo", width=200, minwidth=150, stretch=tk.YES, anchor=tk.W)
        self.tree.column("genero", width=50, minwidth=50, stretch=tk.YES, anchor=tk.W)
        self.tree.column("status", width=70, minwidth=70, stretch=tk.YES, anchor=tk.W)
        self.tree.column("ano", width=60, minwidth=50, stretch=tk.NO, anchor=tk.CENTER)
        self.tree.column("progresso", width=80, minwidth=70, stretch=tk.NO, anchor=tk.CENTER)
        self.tree.column("temporadas", width=80, minwidth=70, stretch=tk.NO, anchor=tk.CENTER)
        self.tree.column("episodios", width=70, minwidth=60, stretch=tk.NO, anchor=tk.CENTER)
        self.tree.column("media_notas", width=100, minwidth=90, stretch=tk.NO, anchor=tk.CENTER)

        self.tree.grid(row=0, column=0, sticky="nsew")

        # --- Add a scrollbar ---
        scrollbar = ctk.CTkScrollbar(table_frame, command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # --- Add sample data (as shown in the image) ---
        sample_data = [
            ("Stranger Thing", "Suspense", "Concluido", "2016", "100%", "4", "34", "9.4"),
            ("Good Girls", "Comédia", "Concluido", "2018", "100%", "4", "50", "9.7"),
            ("Elite", "Drama", "Assistindo", "2018", "84%", "8", "64", "---"),
            ("Homem Aranha Longe de casa","")
        ]

        for item in sample_data:
            self.tree.insert("", tk.END, values=item)

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




