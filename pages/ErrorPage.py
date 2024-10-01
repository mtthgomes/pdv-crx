import tkinter as tk
from utils.printer_utils import Imprimir_comprovante

class ErrorPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        # Variável para armazenar o número do comprovante
        self.numero_comprovante = None

        # Configuração do grid para centralizar os elementos
        self.grid_rowconfigure(0, weight=1)  # Espaço acima do botão
        self.grid_rowconfigure(1, weight=1)  # Área onde a imagem está
        self.grid_rowconfigure(2, weight=1)  # Área onde o botão está
        self.grid_rowconfigure(3, weight=1)  # Espaço abaixo do botão
        self.grid_columnconfigure(0, weight=1)

        # Redimensionando o logo
        logo = tk.PhotoImage(file="images/logo.png")
        logo = logo.subsample(2, 2)  # Reduz o tamanho da imagem pela metade

        # Frame para o logotipo
        logo_frame = tk.Frame(self, bg="white")
        logo_frame.grid(row=0, column=0, pady=(20, 20), sticky="n")

        # Adicionando o logotipo
        logo_label = tk.Label(logo_frame, image=logo, bg="white")
        logo_label.image = logo  # Isso é necessário para manter a referência da imagem
        logo_label.pack(anchor="center")

        # Imagem de sucesso no centro
        success_img = tk.PhotoImage(file="images/error.png")
        success_label = tk.Label(self, image=success_img, bg="white")
        success_label.image = success_img  # Manter referência da imagem
        success_label.grid(row=1, column=0, pady=(10, 20), sticky="n")

        # Frame para o botão
        button_frame = tk.Frame(self, bg="white")
        button_frame.grid(row=2, column=0, pady=(10, 20), sticky="nsew")

        # Criando o botão customizado para reimprimir o comprovante
        self.create_custom_button(button_frame, "Finalizar Compra", self.controller.reiniciar_aplicacao)

    def create_custom_button(self, parent, text, command):
        # Função chamada ao clicar no botão
        def on_button_click(event):
            command()

        # Criando um Canvas para o botão customizado
        canvas = tk.Canvas(parent, width=450, height=70, bg="white", highlightthickness=0)
        canvas.pack(expand=True)

        # Desenhando o botão com bordas arredondadas
        button_rect = canvas.create_rectangle(10, 10, 440, 60, fill="#FF0000", outline="#FF0000", width=0)
        button_text = canvas.create_text(225, 35, text=text, fill="white", font=("Helvetica", 16))

        # Vinculando o clique do mouse ao botão
        canvas.tag_bind(button_rect, "<Button-1>", on_button_click)
        canvas.tag_bind(button_text, "<Button-1>", on_button_click)