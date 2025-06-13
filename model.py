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

    import mysql.connector

    # Supondo que 'self' seja uma classe que já tem 'conexao' e 'cursor'
    # Exemplo:
    # class DatabaseManager:
    #     def __init__(self, config):
    #         self.conexao = mysql.connector.connect(**config)
    #         self.cursor = self.conexao.cursor()
    #
    #     def salvar_bd_serie(self, ...):
    #         # código abaixo

    def salvar_bd_serie(self, tipo, nome, genero, ano, streaming, status, nota, temp, epi):
        """
        Salva uma nova série e todas as suas temporadas e episódios no banco de dados
        dentro de uma única transação.

        Args:
            self: A instância da classe com a conexão do banco de dados.
            tipo (str): O tipo de título, deve ser 'Série'.
            nome (str): O nome da série.
            genero (str): O gênero da série.
            ano (int): O ano de lançamento.
            streaming (str): O serviço de streaming.
            status (str): O status (Ex: 'Assistindo').
            nota (int or None): A nota geral da série.
            total_temporadas (int): O número total de temporadas a serem criadas.
            episodios_por_temporada (int): O número de episódios para cada temporada.

        Returns:
            int or None: O ID do título da série recém-criada em caso de sucesso,
                         ou None em caso de falha.

        """

        if temp and temp.strip():
            try:
                total_temporadas = int(temp)
            except ValueError:
                print("Numero de temporadas erradas")

        if epi and epi.strip():
            try:
                 episodios_por_temporada = int(epi)
            except ValueError:
                print("Numero de episodeos errado")


        # Garante que o tipo seja sempre 'Série' para esta função
        if tipo != 'Série':
            print(f"Erro de lógica: A função salvar_bd_serie só aceita o tipo 'Série'.")
            return None

        try:
            # --- 1. Inserir na tabela principal 'titulos' ---
            query_titulo = """
                INSERT INTO titulos (tipo, nome, genero, ano, streaming, status, nota) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            dados_titulo = (tipo, nome, genero, ano, streaming, status, nota)
            self.cursor.execute(query_titulo, dados_titulo)

            # Pega o ID do título que acabamos de inserir. É crucial para as outras tabelas.
            id_titulo_novo = self.cursor.lastrowid
            if not id_titulo_novo:
                raise mysql.connector.Error("Não foi possível obter o ID do novo título.")

            # --- 2. Inserir na tabela 'series' usando o ID obtido ---
            query_serie = """
                INSERT INTO series (id_serie, total_temporadas, episodios_por_temporada) 
                VALUES (%s, %s, %s)
            """
            dados_serie = (id_titulo_novo, total_temporadas, episodios_por_temporada)
            self.cursor.execute(query_serie, dados_serie)

            # --- 3. Inserir todas as temporadas e seus respectivos episódios em um loop ---
            for num_temporada in range(1, total_temporadas + 1):
                # Insere a temporada
                query_temporada = """
                    INSERT INTO temporadas (id_serie, numero_temporada) 
                    VALUES (%s, %s)
                """
                self.cursor.execute(query_temporada, (id_titulo_novo, num_temporada))

                # Pega o ID da temporada que acabamos de inserir
                id_temporada_nova = self.cursor.lastrowid
                if not id_temporada_nova:
                    raise mysql.connector.Error(f"Não foi possível obter o ID da temporada {num_temporada}.")

                # Para cada temporada, insere todos os episódios
                for num_episodio in range(1, episodios_por_temporada + 1):
                    query_episodio = """
                        INSERT INTO episodios (id_temporada, numero_do_episodio_temporada, nota_episodio) 
                        VALUES (%s, %s, NULL)
                    """
                    # A nota do episódio começa como NULL
                    self.cursor.execute(query_episodio, (id_temporada_nova, num_episodio))

            # --- 4. Finalizar a transação ---
            # Se tudo ocorreu bem, salva todas as alterações no banco de dados
            self.conexao.commit()
            print(f"Sucesso: Série '{nome}' e suas {total_temporadas} temporadas foram inseridas no banco de dados.")

            return id_titulo_novo

        except mysql.connector.Error as err:
            # Se qualquer uma das operações acima falhar, desfaz tudo
            print(f"Falha ao inserir a série '{nome}': {err}")
            self.conexao.rollback()
            return None

