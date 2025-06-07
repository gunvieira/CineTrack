
from model import BancoDados
from controller import Controller
from view import View


def main():
    # 1. Iniciar e conectar o banco de dados
    db = BancoDados()
    db.connect()

    # 2. Criar o Controller, passando os recursos do banco
    main_controller = Controller(db.cursor, db.connection)

    # 3. Criar a View, passando o Controller para ela
    main_view = View(main_controller)

    # 4. Conectar a View ao Controller
    main_controller.set_view(main_view)

    main_view.root.mainloop()

    # 5. Fechar a conexão com o banco de dados ao sair
    db.close()


if __name__ == "__main__":
    main()