import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class CineTrackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cine Track")
        self.menu()


        container = ttk.Frame(self.root, padding=20)
        container.pack(expand=True, fill="both", padx=40, pady=30)



        # Botões
        ttk.Button(container, text="Adicionar Novo Título", bootstyle="secondary", width=30).pack(pady=10)
        ttk.Button(container, text="Atualize seu Progresso", bootstyle="secondary", width=30).pack(pady=10)
        ttk.Button(container, text="Visão Geral", bootstyle="secondary", width=30).pack(pady=10)

        # Citação
        ttk.Label(container, text='"Your imagination can create a reality."', font=("Segoe UI", 10, "italic")).pack(pady=(40, 0))
        ttk.Label(container, text="James Cameron", font=("Segoe UI", 9, "italic")).pack()

    def menu(self):
        self.root.geometry("400x450")
        self.titulo()


    def titulo(self):
        container = tk.Frame(self.root)
        container.pack()

        labelBemvindo = ttk.Label(container, text="Bem vindo ao", font=("Segoe UI", 18), foreground="#888",)
        labelBemvindo.pack(anchor='w')

        labelCineTrack = ttk.Label(container, text="CineTrack", font=("Helvetica", 34, "bold"))
        labelCineTrack.pack(anchor='w')

    class View():
        def __init__(self):
            self.root = tk.Tk()

            # Instancia o controller e envia uma referência de view para o controller
            self.controller = Controller(self)

            # Desenha a interface.
            self.desenha()

            self.root.bind('<Escape>', self.exit)
            self.root.mainloop()

        def desenha(self):
            frame = ttk.Frame(self.root, padding=10)
            frame.pack()

            btn_get = ttk.Button(frame,
                                 text='Somar',
                                 width=20,
                                 bootstyle="success",
                                 command=self.mais)
            btn_get.pack(pady=5)

            btn_sub = ttk.Button(frame,
                                 text='Subtrair',
                                 width=20,
                                 command=self.menos)
            btn_sub.pack(pady=5)

            self.label_name = ttk.Label(frame, width=20, text='')
            self.label_name.pack(pady=10)

if __name__ == "__main__":
    root = ttk.Window(themename="flatly")  # Tema limpo e claro
    app = CineTrackApp(root)
    root.mainloop()
