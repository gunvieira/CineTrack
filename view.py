import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


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

        self.frameMenu.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)
        self.frameAdicionar.grid(row=0, column=0, sticky="nswe", padx=30, pady=10)
        self.frameAtualizar.grid(row=0, column=0, sticky="nswe", padx=20, pady=10)

        self.telaMenu()
        self.telaAdicionar()
        self.telaAtualizar()

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


if __name__ == "__main__":
    View()




