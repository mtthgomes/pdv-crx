import tkinter as tk
from tkinter import PhotoImage

class PaymentPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        # Configuração do grid para centralizar os elementos
        self.grid_rowconfigure(0, weight=1)  # Linha superior
        self.grid_rowconfigure(1, weight=1)  # Linha central (conteúdo)
        self.grid_rowconfigure(2, weight=1)  # Linha inferior
        self.grid_columnconfigure(0, weight=1)

        # Redimensionando o logo
        logo = tk.PhotoImage(file="images/logo.png")
        logo = logo.subsample(2, 2)  # Reduz o tamanho da imagem pela metade

        # Frame superior para o logotipo
        logo_frame = tk.Frame(self, bg="white")
        logo_frame.grid(row=0, column=0, pady=(20, 20), sticky="n")

        # Adicionando o logotipo
        logo_label = tk.Label(logo_frame, image=logo, bg="white")
        logo_label.image = logo  # Manter referência da imagem
        logo_label.pack(anchor="center")

        # Frame para os blocos de pagamento
        payment_frame = tk.Frame(self, bg="white")
        payment_frame.grid(row=1, column=0, sticky="n")

        # Função que será chamada ao clicar em um dos blocos
        def on_block_click(option):
            if option == "Pagamento Único":
                controller.show_frame("PaymentOptionsPage")  # Navegar para a página de opções de pagamento
            elif option == "Assinatura Mensal":
                controller.show_frame("MembershipPage")  # Navegar para a página de QR code

        # Bloco "Pagamento Único" (colocar a imagem)
        one_time_image = tk.PhotoImage(file="images/one-time.png")  # Insira o caminho correto para a imagem
        one_time_label = tk.Label(payment_frame, image=one_time_image, bg="white")
        one_time_label.image = one_time_image  # Manter referência da imagem
        one_time_label.pack(pady=(0, 20))
        one_time_label.bind("<Button-1>", lambda e: on_block_click("Pagamento Único"))

        # Bloco "Assinatura Mensal" (colocar a imagem)
        membership_image = tk.PhotoImage(file="images/membership.png")  # Insira o caminho correto para a imagem
        membership_label = tk.Label(payment_frame, image=membership_image, bg="white")
        membership_label.image = membership_image  # Manter referência da imagem
        membership_label.pack(pady=(0, 20))
        membership_label.bind("<Button-1>", lambda e: on_block_click("Assinatura Mensal"))