import win32print
import win32api
import tkinter as tk
from PIL import Image, ImageTk

class PaymentOptionsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        # Configuração do grid para centralizar os elementos
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Redimensionando o logo
        logo = tk.PhotoImage(file="logo.png")
        logo = logo.subsample(2, 2)  # Reduz o tamanho da imagem pela metade

        # Frame superior para o logotipo
        logo_frame = tk.Frame(self, bg="white")
        logo_frame.grid(row=0, column=0, pady=(20, 20), sticky="n")

        # Adicionando o logotipo
        logo_label = tk.Label(logo_frame, image=logo, bg="white")
        logo_label.image = logo  # Manter referência da imagem
        logo_label.pack(anchor="center")

        # Frame que conterá os cartões de pagamento
        options_frame = tk.Frame(self, bg="white")
        options_frame.grid(row=1, column=0, sticky="n")

        # Criar os três cartões lado a lado
        self.create_payment_card(options_frame, "Cartão de Crédito", self.imprimir_cartao_credito)
        self.create_payment_card(options_frame, "Cartão de Débito", self.imprimir_cartao_debito)
        self.create_payment_card(options_frame, "Pix", self.imprimir_pix)

    def create_payment_card(self, parent, title, command):
        card_frame = tk.Frame(parent, bg="white", highlightbackground="#CCCCCC", highlightthickness=2, padx=20, pady=20)
        card_frame.pack(side="left", padx=20, pady=10)

        title_label = tk.Label(card_frame, text=title, font=("Helvetica", 16, "bold"), bg="white")
        title_label.pack(anchor="center")

        # Adiciona um botão de ação em cada cartão
        action_button = tk.Button(card_frame, text="Selecionar", command=command, bg="green", fg="white", font=("Helvetica", 12, "bold"))
        action_button.pack(pady=10)

    # Funções para imprimir os diferentes métodos de pagamento
    def imprimir_cartao_credito(self):
        self.imprimir_nota_fiscal("Cartão de Crédito")

    def imprimir_cartao_debito(self):
        self.imprimir_nota_fiscal("Cartão de Débito")

    def imprimir_pix(self):
        self.imprimir_nota_fiscal("Pix")

    # Função que realiza a impressão
    def imprimir_nota_fiscal(self, metodo_pagamento):
        try:
            # Exemplo de nota fiscal com separação e espaçamento adicional no final
            nota_fiscal = f"""
            
                        NOTA FISCAL
                        
                        
            Produto       Quantidade   Preço
            Produto 1          2       R$ 50,00
            Produto 2          1       R$ 100,00

            Total: R$ 150,00
            Método de Pagamento: {metodo_pagamento}
            
            
            Obrigado por sua compra!







            """  # Adicionando três linhas em branco no final para ajustar o tamanho

            # Obtém o nome da impressora padrão
            nome_impressora = win32print.GetDefaultPrinter()
            print(f"Imprimindo em: {nome_impressora}")

            # Envia a nota fiscal para a impressora térmica
            hPrinter = win32print.OpenPrinter(nome_impressora)
            try:
                hJob = win32print.StartDocPrinter(hPrinter, 1, ("Nota Fiscal", None, "RAW"))
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, nota_fiscal.encode('utf-8'))
                win32print.EndPagePrinter(hPrinter)
                win32print.EndDocPrinter(hPrinter)
                print("Nota fiscal impressa com sucesso!")
            finally:
                win32print.ClosePrinter(hPrinter)
        except Exception as e:
            print(f"Erro ao imprimir: {str(e)}")
