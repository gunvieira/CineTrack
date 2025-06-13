from model import Model

class Controller:
#-------------------arrumar tk raise--------------------------



    def __init__(self, cursor, conexao):
        self.model = Model(cursor, conexao)
        self.view = None

    def set_view(self, view):
        self.view = view

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
            print(f"Erro no Controller: {err}")

    def buscar_todos_os_streamings(self):
        try:
            streamings = self.model.selecionar_streamings()
            return streamings
        except Exception as err:
            print(f"Erro no Controller: {err}")

    def verificar_salvar(self, tipo, nome, genero, ano, streaming, status, nota, epi, temp):
        try:
            self.model.check(nome, ano, nota, status)
        except ValueError as e:
            print("Validação falhou. Mostrando erro na view.")
            self.view.showVerificaoErro(str(e))
        else:
            notaNova = self.model.alterar_nota(nota, status)
            novo_id = self.model.salvar_bd(tipo, nome, genero, ano, streaming, status, nota, epi, temp)

            if novo_id is not None:
                print(f"Controller: Model confirmou a inserção com o ID: {novo_id}.")
                self.view.showVerificaoSucesso("Título salvo com sucesso!")
            else:
                print("Controller: Model informou uma falha na inserção.")
                self.view.showVerificaoErro("Não foi possível salvar o título.")
