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
            if isinstance(nota, str):
                try:
                    temp_nota = float(nota.strip())
                    nota_final = int(temp_nota)
                except ValueError:
                    nota_final = None
            elif isinstance(nota, (int, float)):
                nota_final = int(nota)

        return nota_final

    def selecionar_generos(self):
        try:
            self.cursor.execute("SHOW COLUMNS FROM titulos LIKE 'genero'")

            descricao_da_coluna = self.cursor.fetchone()

            string_com_os_generos = descricao_da_coluna['Type']

            lista_limpa = re.findall(r"'([^']*)'", string_com_os_generos)

            return lista_limpa

        except Exception as err:
            return []

    def selecionar_streamings(self):
        try:
            self.cursor.execute("SHOW COLUMNS FROM titulos LIKE 'streaming'")

            descricao_da_coluna = self.cursor.fetchone()

            string_com_os_generos = descricao_da_coluna['Type']

            lista_limpa = re.findall(r"'([^']*)'", string_com_os_generos)

            return lista_limpa

        except Exception as err:
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

            return self.cursor.lastrowid

        except mysql.connector.Error:
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
            query = "SELECT nome FROM titulos WHERE tipo = 'Filme' and status != 'Concluído'"

            self.cursor.execute(query)

            resultados_dict = self.cursor.fetchall()

            nomes_filmes = [item['nome'] for item in resultados_dict]

            return nomes_filmes

        except mysql.connector.Error as err:
            return []

    def selecionar_series(self):
        try:
            query = "SELECT nome FROM titulos WHERE tipo = 'Série' and status != 'Concluído'"

            self.cursor.execute(query)

            resultados_dict = self.cursor.fetchall()

            nomes_series = [item['nome'] for item in resultados_dict]

            return nomes_series

        except mysql.connector.Error as err:
            return []

    def buscar_detalhes_serie(self, titulo):
        try:
            query = """
                SELECT s.total_temporadas, s.episodios_por_temporada
                FROM series s
                JOIN titulos t ON s.id_serie = t.id_titulo
                WHERE t.nome = %s AND t.tipo = 'Série'
            """

            self.cursor.execute(query, (titulo,))
            resultado = self.cursor.fetchone()

            if resultado:
                total_temporadas = resultado['total_temporadas']
                episodios_por_temporada = resultado['episodios_por_temporada']
                return (total_temporadas, episodios_por_temporada)
            else:
                return (1, 1)

        except (mysql.connector.Error, KeyError) as err:
            return (1, 1)

    def atualizar_bd(self, tipo, nome, status, nota_final, nota_episodio, epi, temp):
        if tipo == "Filme":
            id = self.atualizar_filme(nome, status, nota_final)
        else:
            id = self.atualizar_serie(nome, status, temp, epi, nota_episodio)

        return id

    def atualizar_filme(self, nome_filme, novo_status, nova_nota=None):
        try:
            query = "UPDATE titulos SET status = %s, nota = %s WHERE nome = %s AND tipo = 'Filme'"
            dados = (novo_status, nova_nota, nome_filme)
            self.cursor.execute(query, dados)

            if self.cursor.rowcount == 0:
                self.conexao.rollback()
                return None

            self.conexao.commit()
            return True

        except mysql.connector.Error as err:
            self.conexao.rollback()
            return None

    def atualizar_serie(self, nome_serie, novo_status, numero_temporada=None, numero_episodio=None, nota_episodio=None):
        try:
            query_verifica_serie = "SELECT id_titulo FROM titulos WHERE nome = %s AND tipo = 'Série'"
            self.cursor.execute(query_verifica_serie, (nome_serie,))

            if self.cursor.fetchone() is None:
                return None

            #atualiza status da serie
            query_status = "UPDATE titulos SET status = %s WHERE nome = %s AND tipo = 'Série'"
            self.cursor.execute(query_status, (novo_status, nome_serie))

            if novo_status == 'Assistindo':
                if numero_temporada is None or numero_episodio is None or nota_episodio is None:
                    self.conexao.rollback()
                    return None

                query_verifica_episodio = """
                    SELECT e.id_episodio
                    FROM episodios e
                    JOIN temporadas t ON e.id_temporada = t.id_temporada
                    JOIN series s ON t.id_serie = s.id_serie
                    JOIN titulos ti ON s.id_serie = ti.id_titulo
                    WHERE ti.nome = %s AND t.numero_temporada = %s AND e.numero_do_episodio_temporada = %s
                """
                dados_verificacao = (nome_serie, numero_temporada, numero_episodio)
                self.cursor.execute(query_verifica_episodio, dados_verificacao)

                if self.cursor.fetchone() is None:
                    self.conexao.rollback()
                    return None

                #atualiza nota do episodio
                query_episodio = """
                       UPDATE episodios e
                       JOIN temporadas t ON e.id_temporada = t.id_temporada
                       JOIN series s ON t.id_serie = s.id_serie
                       JOIN titulos ti ON s.id_serie = ti.id_titulo
                       SET e.nota_episodio = %s
                       WHERE ti.nome = %s AND t.numero_temporada = %s AND e.numero_do_episodio_temporada = %s
                   """
                dados_episodio = (nota_episodio, nome_serie, numero_temporada, numero_episodio)
                self.cursor.execute(query_episodio, dados_episodio)

            self.conexao.commit()
            return True

        except mysql.connector.Error as err:
            self.conexao.rollback()
            return None

    def deletar_titulo_por_nome(self, nome):
        try:
            query = "DELETE FROM titulos WHERE nome = %s"
            self.cursor.execute(query, (nome,))

            if self.cursor.rowcount == 0:
                return False

            self.conexao.commit()
            return True

        except Exception as e:
            self.conexao.rollback()
            raise e

    def obter_cabecalhos(self, tipo):
        if tipo == 'Filme':
            return ['Título', 'Streaming', 'Gênero', 'Status', 'Ano', 'Nota']
        elif tipo == 'Série':
            return ['Título', 'Streaming', 'Gênero', 'Status', 'Ano',
                    'Nº Temps', 'Total Eps', 'Nota Geral']
        return []

    def selecionar_filmes_com_filtros(self, genero=None, status=None, streaming=None, ordenar_por=None):
        try:
            query = "SELECT nome, genero, status, ano, nota, streaming FROM titulos WHERE tipo = 'Filme'"
            filtros_valores = []

            if genero:
                query += " AND genero = %s"
                filtros_valores.append(genero)
            if status:
                query += " AND status = %s"
                filtros_valores.append(status)
            if streaming:
                query += " AND streaming = %s"
                filtros_valores.append(streaming)

            if ordenar_por:
                if ordenar_por == 'Título':
                    query += " ORDER BY nome ASC"
                elif ordenar_por == 'Nota':
                    query += " ORDER BY nota DESC"
                elif ordenar_por == 'Ano':
                    query += " ORDER BY ano DESC"

            self.cursor.execute(query, tuple(filtros_valores))
            dados = self.cursor.fetchall()
            return [
                (
                    item['nome'],
                    item['streaming'],
                    item['genero'],
                    item['status'],
                    item['ano'],
                    item['nota'] if item['nota'] is not None else '---',

                )
                for item in dados
            ]

        except Exception as e:
            return []

    def selecionar_series_com_filtros(self, genero=None, status=None, streaming=None, ordenar_por=None):
        try:

            query = """
                  SELECT t.nome, t.genero, t.status, t.ano, t.nota, t.streaming, s.total_temporadas, 
                  (s.total_temporadas * s.episodios_por_temporada) AS total_episodios
                FROM titulos t
                JOIN series s ON t.id_titulo = s.id_serie
                WHERE t.tipo = 'Série'
               """
            filtros_valores = []

            if genero:
                query += " AND t.genero = %s"
                filtros_valores.append(genero)
            if status:
                query += " AND t.status = %s"
                filtros_valores.append(status)
            if streaming:
                query += " AND t.streaming = %s"
                filtros_valores.append(streaming)

            if ordenar_por:
                if ordenar_por == 'Titulo':
                    query += " ORDER BY t.nome ASC"
                elif ordenar_por == 'Nota':
                    query += " ORDER BY t.nota DESC"
                elif ordenar_por == 'Ano':
                    query += " ORDER BY t.ano DESC"

            self.cursor.execute(query, tuple(filtros_valores))
            dados = self.cursor.fetchall()
            return [
                (
                    item['nome'],
                    item['streaming'],
                    item['genero'],
                    item['status'],
                    item['ano'],
                    item['total_temporadas'],
                    item['total_episodios'],
                    item['nota'] if item['nota'] is not None else '---'
                )
                for item in dados
            ]

        except Exception as e:
            return []

    def adicionar_media_nota_episodios(self, nome):
        try:
            self.cursor.execute("""
                SELECT t.id_titulo, t.status 
                FROM titulos t 
                WHERE t.nome = %s AND t.tipo = 'Série'
            """, (nome,))
            resultado = self.cursor.fetchone()

            if not resultado:
                return

            id_serie = resultado['id_titulo']
            status = resultado['status']

            if status != 'Concluído':
                return

            self.cursor.execute("""
                SELECT AVG(e.nota_episodio) AS media_calculada
                FROM episodios e
                JOIN temporadas temp ON e.id_temporada = temp.id_temporada
                WHERE temp.id_serie = %s AND e.nota_episodio IS NOT NULL
            """, (id_serie,))

            media_dict = self.cursor.fetchone()

            if media_dict is None or media_dict['media_calculada'] is None:
                return

            media = media_dict['media_calculada']

            self.cursor.execute("""
                UPDATE titulos 
                SET nota = %s 
                WHERE id_titulo = %s
            """, (round(media), id_serie))

            self.conexao.commit()

        except mysql.connector.Error as err:
            self.conexao.rollback()




