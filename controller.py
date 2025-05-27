


class Controller():
    def __init__(self, view):


        # Armazena uma ref. de view
        self.view = view

    def somou(self):
        # Processa o click
        self.clicks += 1
        # Retorna o dado p/ quem solicitou (controller)
        return self.clicks