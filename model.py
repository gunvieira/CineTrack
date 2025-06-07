import mysql.connector
import re

class BancoDados:
    def __init__(self):
        self.host = "cinetrackbd.cj60kgg0m4yf.us-east-2.rds.amazonaws.com"
        self.user = "admin"
        self.passwd = "AdminCineTrack"
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