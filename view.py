import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk

class View:
    def __init__(self, controller):
        self.controller = controller

        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")
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
        self.frameAdicionar.grid(row=0, column=0, sticky="nswe", padx=20, pady=10)
        self.frameAtualizar.grid(row=0, column=0, sticky="nswe", padx=20, pady=10)
        self.frameVisaoGeral.grid(row=0, column=0, sticky="nswe", padx=20, pady=10)

        self.telaMenu()
        self.telaAdicionar()
        self.telaAtualizar()
        self.telaGeral()

        self.showTelamenu()

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
        self.carregar_dados_atualizacao()

    def showTelaAtualizarFilmeConcluido(self):
        self.carregar_dados_atualizacao()
        self.frameAtualizar.tkraise()
        self.frameTempEpiAtualizar.forget()
        self.frameNotaAtualizar.pack(anchor="w", fill="x", pady=(10, 10), after=self.frameStatusAtualizar)

        self.root.geometry("400x380")

    def showTelaAtualizarSerie(self):
        self.frameAtualizar.tkraise()

        self.frameTempEpiAtualizar.pack(anchor="w", pady=(10, 0), after=self.frameSerieAtualizarCombo)
        self.frameNotaAtualizar.pack(anchor="w", fill="x", pady=(10, 10), after=self.frameStatusAtualizar)

        self.root.geometry("400x415")
        self.carregar_dados_atualizacao()

    def showTelaAtualizarSerieConcluido(self):
        self.carregar_dados_atualizacao()
        self.frameAtualizar.tkraise()
        self.frameNotaAtualizar.forget()
        self.frameTempEpiAtualizar.pack(anchor="w", pady=(10, 0), after=self.frameSerieAtualizarCombo)

        self.root.geometry("400x370")

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
                                      command=self.chamarAdicionar)
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
                                      command=self.chamarAtualizar)
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
                                      command=self.chamarVisaoGeral)
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
        generos = self.controller.buscar_todos_os_generos()

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
        streamings = self.controller.buscar_todos_os_streamings()

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
                                           dropdown_text_color="black",
                                           width=130,
                                           height=30)
        self.comboboxStreamingAdicionar.pack()

    def tempEpiAdicionar(self):
        self.frameTempEpi = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")


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

        self.statusAdicionarVar = ctk.StringVar(value="Quero Assistir")

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

        self.spinNotaAdicionar = tk.Spinbox(self.frameNota,
                        from_=1,
                        to=10,
                        textvariable=self.spinNotaAdicionarVar,
                        width=2,
                        fg="black",
                        bg="#AFB4BC",
                        font=("Inter", 12),
                        justify="center",
                        relief="groove")
        self.spinNotaAdicionar.pack(anchor="w")

    def botoesAdicionar(self):
        frameBotoesAdicionar = ctk.CTkFrame(self.frameAdicionar, fg_color="transparent")
        frameBotoesAdicionar.pack(anchor="center", pady=(10, 10))

        btnVoltar = ctk.CTkButton(frameBotoesAdicionar,
                                  text="Voltar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.chamarMenu)
        btnVoltar.pack(side="left", padx=(0, 10))

        btnLimpar = ctk.CTkButton(frameBotoesAdicionar,
                                  text="Limpar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.limpar_adicionar)
        btnLimpar.pack(side="left", padx=(0, 10))

        btnSalvar = ctk.CTkButton(frameBotoesAdicionar,
                                  text="Salvar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.cadastro_novo_titulo)
        btnSalvar.pack(side="left")

# ---------------Atualizar Título--------------------

    def telaAtualizar(self):
        self.tituloAtualizar()
        self.tipoAtualizar()
        self.carregar_dados_atualizacao()
        self.selecaoTituloAtualizar()
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

    def selecaoTituloAtualizar(self):
        self.frameSerieAtualizarCombo = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")
        self.frameSerieAtualizarCombo.pack(anchor="w", pady=(5, 10))

        label = ctk.CTkLabel(self.frameSerieAtualizarCombo,
                             text="Selecione a série que deseja atualizar:",
                             font=ctk.CTkFont("Inter", 16))
        label.pack(anchor="w")



        self.comboSerie = ctk.CTkOptionMenu(self.frameSerieAtualizarCombo,
                                                values=["Carregando..."],
                                                command=self.atualizar_temp_epi,
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


        self.spinTemp = tk.Spinbox(self.frameTempEpiAtualizar,
                              from_=1,
                              to=1,
                              textvariable=self.tempAtualizarVar,
                              width=2,
                              fg="black",
                              bg="#AFB4BC",
                              font=("Inter", 12),
                              justify="center",
                              relief="groove")
        self.spinTemp.pack(side="left")

        labelEpi = ctk.CTkLabel(self.frameTempEpiAtualizar,
                                text="Episódio:",
                                font=ctk.CTkFont("Inter", 16))
        labelEpi.pack(side="left", padx=(10, 2))

        self.epiAtualizarVar = tk.IntVar(value=1)


        self.spin_epi = tk.Spinbox(self.frameTempEpiAtualizar,
                              from_=1,
                              to=1,
                              textvariable=self.epiAtualizarVar,
                              width=2,
                              fg="black",
                              bg="#AFB4BC",
                              font=("Inter", 12),
                              justify="center",
                              relief="groove")
        self.spin_epi.pack(side="left")

    def notaAtualizar(self):
        self.frameNotaAtualizar = ctk.CTkFrame(self.frameAtualizar, fg_color="transparent")


        labelAvalie = ctk.CTkLabel(self.frameNotaAtualizar,
                                   text="Avalie esse título:",
                                   font=ctk.CTkFont("Inter", 16),
                                   )
        labelAvalie.pack(anchor="w", side="left", padx=(0, 5))

        self.spinNotaAtulizarVar = tk.IntVar(value=10)

        self.spinNotaAtualizar = tk.Spinbox(
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
        self.spinNotaAtualizar.pack(anchor="w")

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
                                  command=self.chamarMenu)
        btnVoltar.pack(side="left", padx=5)

        btnLimpar = ctk.CTkButton(frameBotoes,
                                  text="Limpar",
                                  width=80,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.limpar_atualizar)
        btnLimpar.pack(side="left", padx=5)

        btnDeletar = ctk.CTkButton(frameBotoes,
                                   text="Deletar",
                                   width=80,
                                   fg_color="#414141",
                                   hover_color="#5B5B5B",
                                   font=ctk.CTkFont("Inter", 16),
                                   command=self.excluir_titulo)
        btnDeletar.pack(side="left", padx=5)

        btnAtualizar = ctk.CTkButton(frameBotoes,
                                     text="Atualizar",
                                     width=80,
                                     fg_color="#414141",
                                     hover_color="#5B5B5B",
                                     font=ctk.CTkFont("Inter", 16),
                                     command=self.atualizar_titulo)
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

        self.tipoVisaoGeralradio = ctk.StringVar(value="Filme")

        radio_filme = ctk.CTkRadioButton(frame_tipo, text="Filme",
                                         variable=self.tipoVisaoGeralradio,
                                         value="Filme",
                                         font=ctk.CTkFont("Inter", 15),
                                         radiobutton_width=20,
                                         radiobutton_height=20,
                                         border_width_unchecked=3,
                                         border_width_checked=7,
                                         fg_color="#414141",
                                         hover_color="#6F6F83",
                                         border_color="grey",
                                         command=self.aplicar_filtros_e_atualizar_tabela)
        radio_filme.pack(side="left", padx=6)

        radio_serie = ctk.CTkRadioButton(frame_tipo, text="Série",
                                         variable=self.tipoVisaoGeralradio,
                                         value="Série",
                                         font=ctk.CTkFont("Inter", 15),
                                         radiobutton_width=20,
                                         radiobutton_height=20,
                                         border_width_unchecked=3,
                                         border_width_checked=7,
                                         fg_color="#414141",
                                         hover_color="#6F6F83",
                                         border_color="grey",
                                         command=self.aplicar_filtros_e_atualizar_tabela)
        radio_serie.pack(side="left")

    def filtrosSecao(self):
        streamings = [""] + self.controller.buscar_todos_os_streamings()
        genero_values = [""] + self.controller.buscar_todos_os_generos()
        status_values = ["", "Assistindo", "Concluído", "Quero Assistir"]
        ordenar_por_values = ["", "Título", "Ano", "Nota"]

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

        self.comboboxStreamingFiltro = ctk.CTkOptionMenu(frameStreaming,
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
        self.comboboxStreamingFiltro.pack()

        labelGenero = ctk.CTkLabel(frameGenero,
                                     text="Genero:",
                                     font=ctk.CTkFont("Inter", 16))
        labelGenero.pack(anchor="w")

        self.comboboxGeneroFiltro = ctk.CTkOptionMenu(frameGenero,
                                                            values=genero_values,
                                                            dropdown_font=ctk.CTkFont("Inter", 12),
                                                            font=ctk.CTkFont("Inter", 12, weight="bold"),
                                                            fg_color="grey",
                                                            button_color="#656565",
                                                            button_hover_color="#414141",
                                                            dropdown_fg_color="#AFB4BC",
                                                            dropdown_hover_color="grey",
                                                            dropdown_text_color="black")
        self.comboboxGeneroFiltro.pack()

        labelStatus = ctk.CTkLabel(frameStatus,
                                   text="Status:",
                                   font=ctk.CTkFont("Inter", 16))
        labelStatus.pack(anchor="w")

        self.comboboxStatusFiltro = ctk.CTkOptionMenu(frameStatus,
                                                         values=status_values,
                                                         dropdown_font=ctk.CTkFont("Inter", 12),
                                                         font=ctk.CTkFont("Inter", 12, weight="bold"),
                                                         fg_color="grey",
                                                         button_color="#656565",
                                                         button_hover_color="#414141",
                                                         dropdown_fg_color="#AFB4BC",
                                                         dropdown_hover_color="grey",
                                                         dropdown_text_color="black")
        self.comboboxStatusFiltro.pack()

        labelOrdenar = ctk.CTkLabel(frameOrdenar,
                                   text="Ordenar por:",
                                   font=ctk.CTkFont("Inter", 16))
        labelOrdenar.pack(anchor="w")

        self.comboboxOrdenarFiltro = ctk.CTkOptionMenu(frameOrdenar,
                                                         values=ordenar_por_values,
                                                         dropdown_font=ctk.CTkFont("Inter", 12),
                                                         font=ctk.CTkFont("Inter", 12, weight="bold"),
                                                         fg_color="grey",
                                                         button_color="#656565",
                                                         button_hover_color="#414141",
                                                         dropdown_fg_color="#AFB4BC",
                                                         dropdown_hover_color="grey",
                                                         dropdown_text_color="black")
        self.comboboxOrdenarFiltro.pack()

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
                        borderwidth=0,
                        relief="flat")

        style.map("Treeview.Heading",
                  background=[('active', 'grey')])

        style.configure("Treeview",
                        font=('Inter', 9),
                        rowheight=25)

        style.map("Treeview",
                  background=[('selected', 'grey')],
                  foreground=[('selected', 'white')])

        self.tabela = ttk.Treeview(table_frame, columns=[], show='headings')

        self.tabela.tag_configure('cinza',
                             background='#EBEBEB',
                             foreground='black')
        self.tabela.tag_configure('branco',
                             background='white',
                             foreground='black')

        dados = []
        cabecalhos = []

        self.tabela['columns'] = cabecalhos

        for col in cabecalhos:
            self.tabela.heading(col, text=col)
            if col == "Título":
                self.tabela.column(col, anchor=tk.W, width=80)
            elif col == "Media Geral":
                self.tabela.column(col, anchor=tk.CENTER, width=50)
            else:
                self.tabela.column(col, anchor=tk.CENTER, width=20)

        for i, item in enumerate(dados):
            if i % 2 == 0:
                self.tabela.insert("", tk.END, values=item, tags=('cinza',))
            else:
                self.tabela.insert("", tk.END, values=item, tags=('branco',))

        scrollbar = ctk.CTkScrollbar(table_frame, command=self.tabela.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.tabela.configure(yscrollcommand=scrollbar.set)

        self.tabela.grid(row=0, column=0, sticky="nsew")
        self.aplicar_filtros_e_atualizar_tabela()

    def botoesVisaoGeral(self):
        frameBotoesAtualizar = ctk.CTkFrame(self.frameVisaoGeral, fg_color="transparent")
        frameBotoesAtualizar.pack(anchor="center", pady=(10, 10))

        btnVoltar = ctk.CTkButton(frameBotoesAtualizar,
                                  text="Voltar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.chamarMenu)
        btnVoltar.pack(side="left", padx=(0, 10))

        btnLimpar = ctk.CTkButton(frameBotoesAtualizar,
                                  text="Limpar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.limpar_geral)
        btnLimpar.pack(side="left", padx=(0, 10))

        btnSalvar = ctk.CTkButton(frameBotoesAtualizar,
                                  text="Filtrar",
                                  width=120,
                                  fg_color="#414141",
                                  hover_color="#5B5B5B",
                                  font=ctk.CTkFont("Inter", 16),
                                  command=self.aplicar_filtros_e_atualizar_tabela)
        btnSalvar.pack(side="left")

# ---------------Funçoes--------------------
    def chamarMenu(self):
        self.controller.tela_menu()

    def chamarAdicionar(self):
        tipo = "Filme"
        status = "Quero Assistir"
        self.limpar_adicionar()
        self.controller.tela_tipo_status_adicionar(tipo, status)

    def chamarAtualizar(self):
        tipo = "Filme"
        status = "Concluído"
        self.limpar_atualizar()
        self.controller.tela_tipo_status_atualizar(tipo, status)

    def chamarVisaoGeral(self):
        self.limpar_geral()
        self.controller.tela_visaoGeral()
        self.aplicar_filtros_e_atualizar_tabela()

    def mudar_tipo_status_tela_adicionar(self):
        tipo = self.tipoAdicionarVar.get()
        status = self.statusAdicionarVar.get()
        self.controller.tela_tipo_status_adicionar(tipo, status)

    def mudar_tipo_status_tela_atualizar(self):
        tipo = self.tipoAtualizarVariavel.get()
        status = self.statusAtualizarVariavel.get()
        self.controller.tela_tipo_status_atualizar(tipo, status)

    def cadastro_novo_titulo(self):
        tipo = self.tipoAdicionarVar.get()
        nome = self.entryNome.get()
        genero = self.comboboxGeneroAdicionar.get()
        ano = self.entryAno.get()
        streaming = self.comboboxStreamingAdicionar.get()
        status = self.statusAdicionarVar.get()
        nota = self.spinNotaAdicionar.get()
        epi = self.entryEpiAdicionar.get()
        temp = self.entryTempAdicionar.get()

        self.controller.verificar_salvar(tipo, nome, genero, ano, streaming, status, nota, epi, temp)
        self.limpar_adicionar()

    def limpar_adicionar(self):
        self.controller.limpar_campos_adicionar()

    def limpa_tela_adicionar(self):
        self.tipoAdicionarVar.set('Filme')
        self.entryNome.delete(0, 100)
        self.comboboxGeneroAdicionar.set('')
        self.entryAno.delete(0, 10)
        self.comboboxStreamingAdicionar.set('')
        self.statusAdicionarVar.set('Quero Assistir')
        self.spinNotaAdicionarVar.set(10)
        self.entryEpiAdicionar.delete(0, 10)
        self.entryTempAdicionar.delete(0, 10)
        self.mudar_tipo_status_tela_adicionar()

    def showVerificaoErro(self, mensagem):
        messagebox.showwarning('CineTrack', mensagem)

    def showVerificaoSucesso(self, mensagem):
        messagebox.showinfo('CineTrack', mensagem)

    def carregar_dados_atualizacao(self):
        tipo = self.tipoAtualizarVariavel.get()
        titulos = [""] + self.controller.selecionar_titulos(tipo)

        self.todosTitulos = titulos

        #verifica se o campo comboSerie foi carregado
        if hasattr(self, 'comboSerie'):
            valor_selecionado_antes = self.comboSerie.get()
            self.comboSerie.configure(values=self.todosTitulos)

            if valor_selecionado_antes in self.todosTitulos:
                self.comboSerie.set(valor_selecionado_antes)
            else:
                self.comboSerie.set(self.todosTitulos[0])

    def atualizar_temp_epi(self, titulo_selecionado):
        qtd_temp, qtd_epi = self.controller.obter_epitemp_serie(titulo_selecionado)

        self.spinTemp.config(to=qtd_temp or 1)
        self.spin_epi.config(to=qtd_epi or 1)

        self.tempAtualizarVar.set(1)
        self.epiAtualizarVar.set(1)

    def atualizar_titulo(self):
        tipo = self.tipoAtualizarVariavel.get()
        nome = self.comboSerie.get()
        status = self.statusAtualizarVariavel.get()
        nota = self.spinNotaAtulizarVar.get()
        epi = self.epiAtualizarVar.get()
        temp = self.tempAtualizarVar.get()

        self.controller.atualizar_dados(tipo, nome, status, nota, epi, temp)
        self.limpar_atualizar()

    def limpar_atualizar(self):
        self.controller.limpar_campos_atualizar()

    def limpa_tela_atualizar(self):
        self.tipoAtualizarVariavel.set('Filme')
        self.comboSerie.set('')
        self.statusAtualizarVariavel.set('Concluído')
        self.spinNotaAtulizarVar.set(10)
        self.mudar_tipo_status_tela_atualizar()

    def excluir_titulo(self):
        nome = self.comboSerie.get()
        self.controller.deletar_dados(nome)
        self.limpar_atualizar()

    def aplicar_filtros_e_atualizar_tabela(self):
        tipo = self.tipoVisaoGeralradio.get()
        genero = self.comboboxGeneroFiltro.get()
        status = self.comboboxStatusFiltro.get()
        streaming = self.comboboxStreamingFiltro.get()
        ordenar_por = self.comboboxOrdenarFiltro.get()

        dados = self.controller.buscar_titulos_com_filtros(tipo, genero, status, streaming, ordenar_por)
        self.atualizar_tabela_completa(dados)

    def atualizar_tabela_completa(self, dados):
        tipo = self.tipoVisaoGeralradio.get()

        self.tabela.delete(*self.tabela.get_children())  #remove todas as linhas de dados
        self.tabela['columns'] = ()  #remove a configuração das colunas

        cabecalhos = self.controller.obter_cabecalhos(tipo)
        self.tabela['columns'] = cabecalhos

        # configura cabeçalhos
        for col in cabecalhos:
            self.tabela.heading(col, text=col)
            if col == "Título":
                self.tabela.column(col, anchor=tk.W, width=80)
            elif col == "Media Geral":
                self.tabela.column(col, anchor=tk.CENTER, width=50)
            else:
                self.tabela.column(col, anchor=tk.CENTER, width=20)

        # insere os novos dados na tabela
        for i, item in enumerate(dados):
            if i % 2 == 0:
                self.tabela.insert("", tk.END, values=item, tags=('cinza',))
            else:
                self.tabela.insert("", tk.END, values=item, tags=('branco',))

    def limpar_geral(self):
        self.controller.limpar_campos_geral()

    def limpa_tela_geral(self):
        self.comboboxGeneroFiltro.set('')
        self.comboboxStatusFiltro.set('')
        self.comboboxStreamingFiltro.set('')
        self.comboboxOrdenarFiltro.set('')













