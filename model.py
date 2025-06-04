import mysql.connector

conexao = mysql.connector.connect(
    host="cinetrackbd.cj60kgg0m4yf.us-east-2.rds.amazonaws.com",
    user="admin",
    passwd="AdminCineTrack",
    database="CineTrack")

cursor = conexao.cursor()

comando2 = 'desc generos'
cursor.execute(comando2)
resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()


class Model():
    def __init__(self):
       pass

