import mysql.connector
import re

class BancoDados:
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.passwd = "7654321"
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

    def check(self, tipo, nome, ano, epi, temp):
        if not nome or not nome.strip():
            raise ValueError("Erro no campo Título: \nO nome não pode ser vazio ou conter apenas espaços.")

        ano_limpo = ano.strip()
        if not ano_limpo.isdigit():
            raise ValueError("Erro no campo Ano: \nO ano deve conter somente números.")
        if len(ano_limpo) != 4:
            raise ValueError("Erro no campo Ano: \nO ano deve ter exatamente 4 dígitos.")


        if tipo == "Série":
            temp_limpo = temp.strip()
            if not temp_limpo:
                raise ValueError("Erro no campo Temporadas: \nPreencha a quantidade de temporadas.")
            if not temp_limpo.isdigit():
                raise ValueError("Erro no campo Temporadas: \nA temporada deve conter somente números.")

            epi_limpo = epi.strip()
            if not epi_limpo:
                raise ValueError("Erro no campo Episódio: \nPreencha a quantidade de episódios.")
            if not epi_limpo.isdigit():
                raise ValueError("Erro no campo Episódio: \nO episódio deve conter somente números.")

    def alterar_nota(self, nota, status):
        nota_final = None
        if status == 'Concluído':
            if nota and nota.strip():
                try:
                    nota_final = float(nota)
                except ValueError:
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
        total_temporadas = 0
        episodios_por_temporada = 0

        if temp and temp.strip():
            try:
                total_temporadas = int(temp)
            except ValueError:
                return None

        if epi and epi.strip():
            try:
                episodios_por_temporada = int(epi)
            except ValueError:
                return None

        if tipo != 'Série':
            return None

        try:
            query_titulo = """
                INSERT INTO titulos (tipo, nome, genero, ano, streaming, status, nota) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            dados_titulo = (tipo, nome, genero, ano, streaming, status, nota)
            self.cursor.execute(query_titulo, dados_titulo)

            id_titulo_novo = self.cursor.lastrowid
            if not id_titulo_novo:
                return None

            query_serie = """
                INSERT INTO series (id_serie, total_temporadas, episodios_por_temporada) 
                VALUES (%s, %s, %s)
            """
            dados_serie = (id_titulo_novo, total_temporadas, episodios_por_temporada)
            self.cursor.execute(query_serie, dados_serie)

            for num_temporada in range(1, total_temporadas + 1):
                query_temporada = """
                    INSERT INTO temporadas (id_serie, numero_temporada) 
                    VALUES (%s, %s)
                """
                self.cursor.execute(query_temporada, (id_titulo_novo, num_temporada))

                id_temporada_nova = self.cursor.lastrowid
                if not id_temporada_nova:
                    return None

                for num_episodio in range(1, episodios_por_temporada + 1):
                    query_episodio = """
                        INSERT INTO episodios (id_temporada, numero_do_episodio_temporada, nota_episodio) 
                        VALUES (%s, %s, NULL)
                    """
                    self.cursor.execute(query_episodio, (id_temporada_nova, num_episodio))

            self.conexao.commit()
            return id_titulo_novo

        except mysql.connector.Error as err:
            self.conexao.rollback()
            return None

    def selecionar_filmes(self):
        try:

            query = "SELECT nome FROM titulos WHERE tipo = 'Filme'"


            self.cursor.execute(query)


            resultados_dict = self.cursor.fetchall()

            nomes_filmes = [item['nome'] for item in resultados_dict]

            print(f"Sucesso: {len(nomes_filmes)} filmes encontrados.")
            return nomes_filmes

        except mysql.connector.Error as err:
            return []

    def selecionar_series(self):
        titulos = ["teste", "oi"]
        epi = 2
        temp = 3
        return titulos, epi, temp

