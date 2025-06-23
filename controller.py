from model import Model

class Controller:
    def __init__(self, cursor, conexao):
        self.model = Model(cursor, conexao)
        self.view = None

    def set_view(self, view):
        self.view = view

    def tela_menu(self):
        self.view.showTelamenu()

    def tela_visaoGeral(self):
        self.view.showTelaVisaoGeral()

    def tela_tipo_status_adicionar(self, tipo, status):
        if tipo == 'Filme':
            if status == 'Concluído':
                self.view.showTelaAdicionarFilmeConcluido()
            else:
                self.view.showTelaAdicionarFilme()

        if tipo == 'Série':
            if status == 'Concluído':
                self.view.showTelaAdicionarSerieConcluido()
            else:
                self.view.showTelaAdicionarSerie()

    def tela_tipo_status_atualizar(self, tipo, status):
        if tipo == 'Filme':
            if status == 'Concluído':
               self.view.showTelaAtualizarFilmeConcluido()
            else:
               self.view.showTelaAtualizarFilme()

        if tipo == 'Série':
            if status == 'Concluído':
              self.view.showTelaAtualizarSerieConcluido()
            else:
              self.view.showTelaAtualizarSerie()

    def buscar_todos_os_generos(self):
        try:
            generos = self.model.selecionar_generos()
            return generos
        except Exception as err:
            self.view.showVerificaoErro(f"Erro no Controller: {err}")

    def buscar_todos_os_streamings(self):
        try:
            streamings = self.model.selecionar_streamings()
            return streamings
        except Exception as err:
            self.view.showVerificaoErro(f"Erro no Controller: {err}")

    def verificar_salvar(self, tipo, nome, genero, ano, streaming, status, nota, epi, temp):
        try:
            self.model.check(tipo, nome, ano, epi, temp)
        except ValueError as e:
            self.view.showVerificaoErro(str(e))
        else:
            notaNova = self.model.alterar_nota(nota, status)
            novo_id = self.model.salvar_bd(tipo, nome, genero, ano, streaming, status, notaNova, epi, temp)

            if novo_id is not None:
                self.view.showVerificaoSucesso("Título salvo com sucesso!")
            else:
                self.view.showVerificaoErro("Não foi possível salvar o título.")

    def selecionar_titulos(self, tipo):
        try:
            if tipo == 'Filme':
                titulos = self.model.selecionar_filmes()
                return titulos
            else:
                titulos = self.model.selecionar_series()
                return titulos

        except ValueError as e:
            self.view.showVerificaoErro(f"Erro ao selecionar títulos: {e}")
            return []

    def obter_epitemp_serie(self, titulo):
        detalhes = self.model.buscar_detalhes_serie(titulo)
        return detalhes

    def atualizar_dados(self, tipo, nome, status, nota, epi, temp):
        try:
            nota_episodio = None
            nota_final = None

            if status == 'Assistindo' and tipo == 'Série':
                nota_episodio = nota
            elif status == 'Concluído':
                nota_final = self.model.alterar_nota(nota, status)

            novo_atual = self.model.atualizar_bd(
                tipo=tipo,
                nome=nome,
                status=status,
                nota_final=nota_final,
                nota_episodio=nota_episodio,
                epi=epi,
                temp=temp
            )

            if novo_atual:
                self.view.showVerificaoSucesso("Título atualizado com sucesso!")
            else:
                self.view.showVerificaoErro("Não foi possível atualizar o título.")

        except ValueError as e:
            self.view.showVerificaoErro(str(e))


        self.model.adicionar_media_nota_episodios(nome)

    def deletar_dados(self, nome):
        try:
            sucesso = self.model.deletar_titulo_por_nome(nome)

            if sucesso:
                self.view.showVerificaoSucesso(f"O título '{nome}' e todos os seus dados foram deletados com sucesso.")
            else:
                self.view.showVerificaoErro(f"Erro: Título '{nome}' não foi encontrado na base de dados.")

        except Exception as e:
            self.view.showVerificaoErro(f"Ocorreu um erro inesperado ao deletar o título: {e}")

    def buscar_titulos_com_filtros(self, tipo, genero=None, status=None, streaming=None, ordenar_por=None):
        try:
            if tipo == 'Filme':
                resultados = self.model.selecionar_filmes_com_filtros(
                    genero=genero,
                    status=status,
                    streaming=streaming,
                    ordenar_por=ordenar_por
                )

                return resultados

            elif tipo == 'Série':
                resultados = self.model.selecionar_series_com_filtros(
                    genero=genero,
                    status=status,
                    streaming=streaming,
                    ordenar_por=ordenar_por
                )

                return resultados

            else:
                self.view.mostrar_erro(f"Tipo de busca inválido")
                return []

        except Exception as e:
            self.view.mostrar_erro(f"Ocorreu um erro durante a busca: {e}")
            return []

    def obter_cabecalhos(self, tipo):
        return self.model.obter_cabecalhos(tipo)

    def limpar_campos_adicionar(self):
        self.view.limpa_tela_adicionar()

    def limpar_campos_atualizar(self):
        self.view.limpa_tela_atualizar()

    def limpar_campos_geral(self):
        self.view.limpa_tela_geral()



