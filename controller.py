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
            print("Validação falhou. Mostrando erro na view.")
            self.view.showVerificaoErro(str(e))
        else:
            notaNova = self.model.alterar_nota(nota, status)
            novo_id = self.model.salvar_bd(tipo, nome, genero, ano, streaming, status, notaNova, epi, temp)

            if novo_id is not None:
                print(f"Controller: Model confirmou a inserção com o ID: {novo_id}.")
                self.view.showVerificaoSucesso("Título salvo com sucesso!")
            else:
                print("Controller: Model informou uma falha na inserção.")
                self.view.showVerificaoErro("Não foi possível salvar o título.")

    def selecionar_titulos(self, tipo):
        try:
            if tipo == 'Filme':
                titulos = self.model.selecionar_filmes()
                return titulos
            else:
                titulos = self.model.selecionar_series()
                return titulos

        except Exception as e:
            self.view.showVerificaoErro(f"Erro ao selecionar títulos: {e}")
            return []

    def obter_epitemp_serie(self, titulo):
        print(f"Controller: Buscando detalhes para a série '{titulo}'...")
        detalhes = self.model.buscar_detalhes_serie(titulo)
        return detalhes

    def atualizar_dados(self, tipo, nome, status, nota, epi, temp):
        try:
            notaNova = self.model.alterar_nota(nota, status)
            novo_atual = self.model.atualizar_bd(tipo, nome, status, notaNova, epi, temp)
        except ValueError as e:
            print("Atualização falhou. Mostrando erro na view.")
            self.view.showVerificaoErro(str(e))

            if novo_atual is not None:
                print(f"Controller: Model confirmou a inserção com o ID: {novo_id}.")
                self.view.showVerificaoSucesso("Título atualizado com sucesso!")
            else:
                print("Controller: Model informou uma falha na inserção.")
                self.view.showVerificaoErro("Não foi possível atualizar o título.")
