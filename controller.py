from model import Model

class Controller:
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



    def salvar_novo_filme(self, tipo, nome, genero, ano, streaming, status, nota):

        tipo_filme = tipo
        nome_filme = nome
        genero_filme = genero
        ano_filme = ano
        streaming_filme = streaming
        status_filme = status
        nota_filme = nota

        try:

            if nome_filme == "":
                raise ValueError("\nPreencha o nome do título")

        except ValueError as e:
            self.view.showVerificaoErro(f"Erro no campo Título: {e}")
            return

        try:
            ano_limpo = ano_filme.strip()

            if any(x.isdigit() == False for x in ano_limpo):
                raise ValueError("\nO ano deve conter somente números.")

            if len(ano_limpo) != 4:
                raise ValueError("\nO ano deve ter exatamente 4 dígitos.")

            ano_int = int(ano_limpo)

        except ValueError as e:
            self.view.showVerificaoErro(f"Erro no campo Ano: {e}")
            return

        nota_final = None
        if nota_filme.strip():
            nota_final = float(nota_filme)

        if status_filme != 'Concluído':
            nota_final = None


        novo_id = self.model.salvar_bd_filme(
            tipo_filme,
            nome_filme,
            genero_filme,
            ano_filme,
            streaming_filme,
            status_filme,
            nota_filme
        )

        if novo_id is not None:
            print(f"Controller: Model confirmou a inserção com o ID: {novo_id}.")
            if self.view:
                self.view.showVerificaoSucesso("Título salvo com sucesso!")
        else:
            print("Controller: Model informou uma falha na inserção.")
            if self.view:
                self.view.showVerificaoErro("Não foi possível salvar o título.")
