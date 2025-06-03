from model import Model

class Controller():
    def __init__(self, view):
        self.model = Model()
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