import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk

from controller import Controller


class View:

    # atualizar nome de funçoes tudo minusculo com _

    def __init__(self):
        ctk.set_appearance_mode("Light")  # Opções: "Dark", "Light", "System"
        ctk.set_default_color_theme("blue")  # Você pode mudar o tema aqui
        self.root = ctk.CTk()

        self.controller = Controller(self)


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
        self.frameAdicionar.grid(row=0, column=0, sticky="nswe", padx=20, pady=10)
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

    #---------tela Adicionar------------------

    def showTelaAdicionarSerieConcluido(self):

        self.frameAdicionar.tkraise()
        self.frameTempEpi.pack(anchor="w", fill="x", pady=(10, 10), after=self.frameStremingAno)
        self.frameNota.pack(anchor="w", fill="x", pady=(5, 10), after=self.frameStatus)
        self.root.geometry("450x490")

    def showTelaAdicionarFilme(self):
        self.frameAdicionar.tkraise()
        self.frameTempEpi.forget()
        self.frameNota.forget()
        self.root.geometry("450x400")

    def showTelaAdicionarFilmeConcluido(self):
        self.frameAdicionar.tkraise()
        self.frameTempEpi.forget()
        self.frameNota.pack(anchor="w", fill="x", pady=(5, 10), after=self.frameStatus)
        self.root.geometry("450x440")

    def showTelaAdicionarSerie(self):
        self.frameAdicionar.tkraise()
        self.frameNota.forget()
        self.frameTempEpi.pack(anchor="w", fill="x", pady=(10, 10), after=self.frameStremingAno)
        self.root.geometry("450x440")

    # ---------tela Atualizar------------------

    def showTelaAtualizarFilme(self):
        self.frameAtualizar.tkraise()
        self.frameNotaAtualizar.forget()
        self.frameTempEpiAtualizar.forget()

        self.root.geometry("400x330")

    def showTelaAtualizarFilmeConcluido(self):
        self.frameAtualizar.tkraise()
        self.frameTempEpiAtualizar.forget()
        self.frameNotaAtualizar.pack(anchor="w", fill="x", pady=(10, 10), after=self.frameStatusAtualizar)

        self.root.geometry("400x380")

    def showTelaAtualizarSerie(self):
        self.frameAtualizar.tkraise()
        self.frameNotaAtualizar.forget()
        self.frameTempEpiAtualizar.pack(anchor="w", pady=(10, 0), after=self.frameSerieAtualizarCombo)

        self.root.geometry("400x370")

    def showTelaAtualizarSerieConcluido(self):
        self.frameAtualizar.tkraise()
        self.frameTempEpiAtualizar.pack(anchor="w", pady=(10, 0), after=self.frameSerieAtualizarCombo)
        self.frameNotaAtualizar.pack(anchor="w", fill="x", pady=(10, 10), after=self.frameStatusAtualizar)

        self.root.geometry("400x415")

    # ---------tela visão geral------------------

    def showTelaVisaoGeral(self):

        self.frameVisaoGeral.tkraise()
        self.root.geometry("965x570")


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
                                      command=self.showTelaAdicionarFilme)
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
                                      command=self.showTelaAtualizarFilme)
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
                                        value="Filme",
                                        command=self.mudar_tipo_status_tela_adicionar)
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
                                        value="Série",
                                        command=self.mudar_tipo_status_tela_adicionar)
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

        self.frameStremingAno = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        self.frameStremingAno.pack(anchor="w", fill="x", pady=(5,10))

        frameStreaming = ctk.CTkFrame(self.frameStremingAno, fg_color="transparent")
        frameStreaming.pack(anchor="w", side="left")

        frameAno = ctk.CTkFrame(self.frameStremingAno, fg_color="transparent")
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
        self.frameTempEpi = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        self.frameTempEpi

        frameTemp = ctk.CTkFrame(self.frameTempEpi, fg_color="transparent")
        frameTemp.pack(side="left")

        frameEpi = ctk.CTkFrame(self.frameTempEpi, fg_color="transparent")
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
        self.frameStatus = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        self.frameStatus.pack(anchor="w", fill="x", pady=(0, 10))

        labelStatus = ctk.CTkLabel(self.frameStatus,
                                   text="Status",
                                   font=ctk.CTkFont("Inter", 16))
        labelStatus.pack(anchor="w")

        self.statusAdicionarVar = ctk.StringVar(value="")

        radioQuero = ctk.CTkRadioButton(self.frameStatus,
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
                                      value="Quero Assistir",
                                      command=self.mudar_tipo_status_tela_adicionar)
        radioQuero.pack(side="left", padx=(0,20))

        radioAssis = ctk.CTkRadioButton(self.frameStatus,
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
                                      value="Assistindo",
                                      command=self.mudar_tipo_status_tela_adicionar)
        radioAssis.pack(side="left", padx=(0,20))

        radioConc = ctk.CTkRadioButton(self.frameStatus,
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
                                     value="Concluído",
                                     command=self.mudar_tipo_status_tela_adicionar)
        radioConc.pack(side="left")

    def spinAdicionar(self):
        self.frameNota = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")


        labelAvalie = ctk.CTkLabel(self.frameNota,
                                  text="Avalie esse título:",
                                  font=ctk.CTkFont("Inter", 16),
                                  )
        labelAvalie.pack(anchor="w", side="left", padx=(0, 5))

        self.spinNotaAdicionarVar = tk.IntVar(value=10)

        spinNota = tk.Spinbox(self.frameNota,
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
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.showTelamenu)
        btnVoltar.pack(side="left", padx=(0, 10))

        btnLimpar = ctk.CTkButton(frameBotoesAdicionar,
                                  text="Limpar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=lambda: print("Salvar"))
        btnLimpar.pack(side="left", padx=(0, 10))

        btnSalvar = ctk.CTkButton(frameBotoesAdicionar,
                                  text="Salvar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
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

        self.tipoAtualizarVariavel = ctk.StringVar(value="Filme")

        radio_filme = ctk.CTkRadioButton(frame_tipo,
                                         text="Filme",
                                         variable=self.tipoAtualizarVariavel,
                                         value="Filme",
                                         font=ctk.CTkFont("Inter", 15),
                                         radiobutton_width=20,
                                         radiobutton_height=20,
                                         border_width_unchecked=3,
                                         border_width_checked=7,
                                         fg_color="#414141",
                                         hover_color="#6F6F83",
                                         border_color="grey",
                                         command=self.mudar_tipo_status_tela_atualizar)
        radio_filme.pack(side="left", padx=6)

        radio_serie = ctk.CTkRadioButton(frame_tipo,
                                         text="Série",
                                         variable=self.tipoAtualizarVariavel,
                                         value="Série",
                                         font=ctk.CTkFont("Inter", 15),
                                         radiobutton_width=20,
                                         radiobutton_height=20,
                                         border_width_unchecked=3,
                                         border_width_checked=7,
                                         fg_color="#414141",
                                         hover_color="#6F6F83",
                                         border_color="grey",
                                         command=self.mudar_tipo_status_tela_atualizar)
        radio_serie.pack(side="left")

    def selecaoSerieAtualizar(self):
        self.frameSerieAtualizarCombo = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")
        self.frameSerieAtualizarCombo.pack(anchor="w", pady=(5, 10))

        label = ctk.CTkLabel(self.frameSerieAtualizarCombo,
                             text="Selecione a série que deseja atualizar:",
                             font=ctk.CTkFont("Inter", 16))
        label.pack(anchor="w")

        self.seriesDisponiveis = ["Dark", "Wandinha", "Black Mirror"]

        self.comboSerie = ctk.CTkOptionMenu(self.frameSerieAtualizarCombo,
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
        self.frameTempEpiAtualizar = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")


        labelTemp = ctk.CTkLabel(self.frameTempEpiAtualizar,
                                 text="Temporada:",
                                 font=ctk.CTkFont("Inter", 16))
        labelTemp.pack(side="left", padx=(0, 2))

        self.tempAtualizarVar = tk.IntVar(value=1)
        self.qtdTempAtualizar = 3

        spinTemp = tk.Spinbox(self.frameTempEpiAtualizar,
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

        labelEpi = ctk.CTkLabel(self.frameTempEpiAtualizar,
                                text="Episódio:",
                                font=ctk.CTkFont("Inter", 16))
        labelEpi.pack(side="left", padx=(10, 2))

        self.epiAtualizarVar = tk.IntVar(value=1)
        self.qtdEpiAtualizar = 12

        spin_epi = tk.Spinbox(self.frameTempEpiAtualizar,
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
        self.frameNotaAtualizar = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")


        labelAvalie = ctk.CTkLabel(self.frameNotaAtualizar,
                                   text="Avalie esse título:",
                                   font=ctk.CTkFont("Inter", 16),
                                   )
        labelAvalie.pack(anchor="w", side="left", padx=(0, 5))

        self.spinNotaAtulizarVar = tk.IntVar(value=10)

        spinNota = tk.Spinbox(
            self.frameNotaAtualizar,
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
        self.frameStatusAtualizar = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")
        self.frameStatusAtualizar.pack(anchor="w", pady=(10, 10))

        labelStatus = ctk.CTkLabel(self.frameStatusAtualizar, text="Status:", font=ctk.CTkFont("Inter", 16))
        labelStatus.pack(anchor="w")

        frameRadioStatus = ctk.CTkFrame(self.frameStatusAtualizar, fg_color="transparent")
        frameRadioStatus.pack(anchor="w")

        self.statusAtualizarVariavel = ctk.StringVar(value="Assistindo")

        radioAssistindo = ctk.CTkRadioButton(frameRadioStatus,
                                              text="Assistindo",
                                              variable=self.statusAtualizarVariavel,
                                              value="Assistindo",
                                              font=ctk.CTkFont("Inter", 14),
                                              radiobutton_width=20,
                                              radiobutton_height=20,
                                              border_width_unchecked=3,
                                              border_width_checked=7,
                                              fg_color="#414141",
                                              hover_color="#6F6F83",
                                              border_color="grey",
                                              command=self.mudar_tipo_status_tela_atualizar)
        radioAssistindo.pack(side="left", padx=10)

        radioConcluido = ctk.CTkRadioButton(frameRadioStatus,
                                             text="Concluído",
                                             variable=self.statusAtualizarVariavel,
                                             value="Concluído",
                                             font=ctk.CTkFont("Inter", 14),
                                             radiobutton_width=20,
                                             radiobutton_height=20,
                                             border_width_unchecked=3,
                                             border_width_checked=7,
                                             fg_color="#414141",
                                             hover_color="#6F6F83",
                                             border_color="grey",
                                            command=self.mudar_tipo_status_tela_atualizar)
        radioConcluido.pack(side="left")

    def botoesAtualizar(self):
        frameBotoes = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")
        frameBotoes.pack(pady=10)

        btnVoltar = ctk.CTkButton(frameBotoes,
                                  text="Voltar",
                                  width=80,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.showTelamenu)
        btnVoltar.pack(side="left", padx=5)

        btnLimpar = ctk.CTkButton(frameBotoes,
                                  text="Limpar",
                                  width=80,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=lambda: print("Limpar"))
        btnLimpar.pack(side="left", padx=5)

        btnDeletar = ctk.CTkButton(frameBotoes,
                                   text="Deletar",
                                   width=80,
                                   fg_color="#414141",
                                   hover_color="#5B5B5B",
                                   font=ctk.CTkFont("Inter", 16),
                                   command=lambda: print("Deletar"))
        btnDeletar.pack(side="left", padx=5)

        btnAtualizar = ctk.CTkButton(frameBotoes,
                                     text="Atualizar",
                                     width=80,
                                     fg_color="#414141",
                                     hover_color="#5B5B5B",
                                     font=ctk.CTkFont("Inter", 16),
                                     command=lambda: messagebox.showinfo("CineTrack", "O título foi Atualizado."))
        btnAtualizar.pack(side="left", padx=5)

# ---------------Visão Geral--------------------

    def telaGeral(self):
        self.tituloVisaoGeral()
        self.tipoVisaoGeral()
        self.filtrosSecao()
        self.criarTabela()
        self.botoesVisaoGeral()

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

        streamings = ["", "Netflix", "Prime Video", "Max", "Disney +", "Apple TV +", "Globoplay",
                            "Paramount +", "Youtube", "Alugar"]

        genero_values = ["", "Ação", "Aventura", "Comédia", "Documentário", "Drama", "Terror", "Suspense", "Sci-fi",
                         "Romance", "Musical"]
        status_values = ["", "Assistindo", "Concluído", "Quero Assistir"]
        ordenar_por_values = ["", "Nome (A-Z)", "Nome (Z-A)", "Ano (Recente)", "Ano (Antigo)", "Nota (Maior)",
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
        table_frame.pack(fill="both", expand=False, padx=10, pady=(5, 15))
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
            ('Stranger Things', 'Netflix', 'Suspense', 'Concluído', 2016, '100%', 4, 34, 9.4),
            ('Good Girls', 'Netflix', 'Comédia', 'Concluído', 2018, '100%', 4, 50, 9.7),
            ('Elite', 'Netflix', 'Drama', 'Assistindo', 2018, '84%', 8, 64, '---'),
            ('Breaking Bad', 'Netflix', 'Drama', 'Concluído', 2008, '100%', 5, 62, 9.5),
            ('Game of Thrones', 'Max', 'Fantasia', 'Concluído', 2011, '100%', 8, 73, 9.2),
            ('The Simpsons', 'Disney+', 'Animação', 'Assistindo', 1989, '92%', 36, 780, 8.7),
            ('Friends', 'Max', 'Comédia', 'Concluído', 1994, '100%', 10, 235, 8.9),
            ('The Office (US)', 'Prime Video', 'Comédia', 'Concluído', 2005, '100%', 9, 201, 9.0),
            ('Squid Game', 'Netflix', 'Suspense', 'Assistindo', 2021, '50%', 2, 18, 8.0),
            ('Wednesday', 'Netflix', 'Comédia', 'Assistindo', 2022, '50%', 2, 16, 8.1),
            ('Money Heist', 'Netflix', 'Ação', 'Concluído', 2017, '100%', 5, 41, 8.2),
            ('The Witcher', 'Netflix', 'Fantasia', 'Assistindo', 2019, '60%', 5, 40, 8.1),
            ('Black Mirror', 'Netflix', 'Ficção Científica', 'Assistindo', 2011, '85%', 7, 33, 8.7),
            ('The Crown', 'Netflix', 'Drama', 'Concluído', 2016, '100%', 6, 60, 8.7),
            ('Peaky Blinders', 'Netflix', 'Crime', 'Concluído', 2013, '100%', 6, 36, 8.8),
            ('Dark', 'Netflix', 'Mistério', 'Concluído', 2017, '100%', 3, 26, 8.7),
            ('The Mandalorian', 'Disney+', 'Ficção Científica', 'Assistindo', 2019, '75%', 4, 32, 8.7),
            ('Chernobyl', 'Max', 'Drama Histórico', 'Concluído', 2019, '100%', 1, 5, 9.4),
            ('The Queen\'s Gambit', 'Netflix', 'Drama', 'Concluído', 2020, '100%', 1, 7, 8.5),
            ('Ted Lasso', 'Apple TV+', 'Comédia', 'Concluído', 2020, '100%', 3, 34, 8.8),
            ('Severance', 'Apple TV+', 'Ficção Científica', 'Assistindo', 2022, '50%', 2, 18, 8.7),
            ('Succession', 'Max', 'Drama', 'Concluído', 2018, '100%', 4, 39, 8.9),
            ('The Last of Us', 'Max', 'Ação', 'Assistindo', 2023, '50%', 2, 18, 8.8),
            ('Yellowstone', 'Paramount+', 'Drama', 'Assistindo', 2018, '90%', 5, 53, 8.7),
            ('House of the Dragon', 'Max', 'Fantasia', 'Assistindo', 2022, '25%', 4, 40, 8.4),
            ('The Handmaid\'s Tale', 'Star+', 'Drama', 'Assistindo', 2017, '83%', 6, 66, 8.4),
            ('Rick and Morty', 'Max', 'Animação', 'Assistindo', 2013, '70%', 10, 81, 9.1),
            ('Ozark', 'Netflix', 'Suspense', 'Concluído', 2017, '100%', 4, 44, 8.5),
        ]
        cabecalhos = ["Título", "Streaming", "Gênero", "Status", "Ano", "Progresso", "Temps.", "Eps.", "Media Geral"]

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

    def botoesVisaoGeral(self):
        frameBotoesAtualizar = ctk.CTkFrame(self.frameVisaoGeral, fg_color="transparent")
        frameBotoesAtualizar.pack(anchor="center", pady=(10, 10))

        # trocar hover

        btnVoltar = ctk.CTkButton(frameBotoesAtualizar,
                                  text="Voltar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.showTelamenu)
        btnVoltar.pack(side="left", padx=(0, 10))

        btnLimpar = ctk.CTkButton(frameBotoesAtualizar,
                                  text="Limpar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=lambda: print("Limpar"))
        btnLimpar.pack(side="left", padx=(0, 10))

        btnSalvar = ctk.CTkButton(frameBotoesAtualizar,
                                  text="Filtrar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=lambda: print("Filtrar"))
        btnSalvar.pack(side="left")

# ---------------Funçoes--------------------

    def mudar_tipo_status_tela_adicionar(self):
        tipo = self.tipoAdicionarVar.get()
        status = self.statusAdicionarVar.get()
        self.controller.tela_tipo_status_adicionar(tipo, status)

    def mudar_tipo_status_tela_atualizar(self):
        tipo = self.tipoAtualizarVariavel.get()
        status = self.statusAtualizarVariavel.get()
        self.controller.tela_tipo_status_atualizar(tipo, status)




if __name__ == "__main__":
    View()




