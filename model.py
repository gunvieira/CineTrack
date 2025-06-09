import mysql.connector
import re

class BancoDados:
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.passwd = ""
        self.database = "CineTrack"
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host, user=self.user, passwd=self.passwd, database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print("Conexão com o banco de dados aberta.")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao MySQL: {err}")
            self.connection = None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexão com o banco de dados fechada.")

class Model:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def check(self, nome, ano, nota, status):
        try:
            if nome == "":
                raise ValueError("\nPreencha o nome do título")

        except ValueError as e:
            erro1 = f"Erro no campo Título: {e}"
            raise ValueError(erro1)

        try:
            ano_limpo = ano.strip()

            if any(x.isdigit() == False for x in ano_limpo):
                raise ValueError("\nO ano deve conter somente números.")

            if len(ano_limpo) != 4:
                raise ValueError("\nO ano deve ter exatamente 4 dígitos.")

            ano_int = int(ano_limpo)
            print("esta no check")

        except ValueError as e:
            erro = f"Erro no campo Ano: {e}"
            raise ValueError(erro)


    def alterar_nota(self, nota, status):
        nota_final = None
        if nota.strip():
            nota_final = float(nota)

        if status != 'Concluído':
            nota_final = None
            return nota_final

    def selecionar_generos(self):

        try:

            self.cursor.execute("SHOW COLUMNS FROM titulos LIKE 'genero'")

            descricao_da_coluna = self.cursor.fetchone()

            string_com_os_generos = descricao_da_coluna['Type']

            lista_limpa = re.findall(r"'([^']*)'", string_com_os_generos)

            return lista_limpa

        except Exception as err:
            print(f"Erro no Model ao selecionar gêneros: {err}")
            return []

    def selecionar_streamings(self):
        try:

            self.cursor.execute("SHOW COLUMNS FROM titulos LIKE 'streaming'")

            descricao_da_coluna = self.cursor.fetchone()

            string_com_os_generos = descricao_da_coluna['Type']

            lista_limpa = re.findall(r"'([^']*)'", string_com_os_generos)

            return lista_limpa

        except Exception as err:
            print(f"Erro no Model ao selecionar Streamings: {err}")
            return []

    def salvar_bd(self, tipo, nome, genero, ano, streaming, status, nota, epi, temp):
        if tipo == "Filme":
            id = self.salvar_bd_filme(tipo, nome, genero, ano, streaming, status, nota)
        else:
            id = self.salvar_bd_serie(tipo, nome, genero, ano, streaming, status, nota, epi, temp)
        return id


    def salvar_bd_filme(self, tipo, nome, genero, ano, streaming, status, nota):

        try:

            query = """
                    INSERT INTO titulos 
                    (tipo, nome, genero, ano, streaming, status, nota) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

            dados = (tipo, nome, genero, ano, streaming, status, nota)

            self.cursor.execute(query, dados)
            self.conexao.commit()

            print(f"Sucesso: Título '{nome}' inserido no banco de dados.")

            return self.cursor.lastrowid

        except mysql.connector.Error as err:
            print(f"Falha ao inserir título '{nome}': {err}")
            self.conexao.rollback()
            return None

    def salvar_bd_serie(self, tipo, nome, genero, ano, streaming, status, nota, epi, temp):
        pass