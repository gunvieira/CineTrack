
from model import BancoDados
from controller import Controller
from view import View


def main():
    # Iniciar e conectar o banco de dados
    db = BancoDados()
    db.connect()

    # Cria o Controller, passando os recursos do banco
    main_controller = Controller(db.cursor, db.connection)

    # Cria a View, passando o Controller para ela
    main_view = View(main_controller)

    # Conecta a View ao Controller
    main_controller.set_view(main_view)

    main_view.root.mainloop()

    # Fechar a conexão com o banco de dados ao sair
    db.close()


if __name__ == "__main__":
    main()