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
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Redimensionando o logo
        logo = tk.PhotoImage(file="images/logo.png")
        logo = logo.subsample(2, 2)

        logo_frame = tk.Frame(self, bg="white")
        logo_frame.grid(row=0, column=0, pady=(20, 20), sticky="n")

        logo_label = tk.Label(logo_frame, image=logo, bg="white")
        logo_label.image = logo
        logo_label.pack(anchor="center")

        # Frame para os cartões de pagamento
        options_frame = tk.Frame(self, bg="white")
        options_frame.grid(row=1, column=0, sticky="n")

        # Adiciona os cartões (imagens clicáveis) para Pix, Cartão de Débito, Cartão de Crédito
        self.create_payment_card(options_frame, "images/Pix.png", self.imprimir_pix)
        self.create_payment_card(options_frame, "images/debit.png", self.imprimir_cartao_debito)
        self.create_payment_card(options_frame, "images/credit.png", self.imprimir_cartao_credito)

    def create_payment_card(self, parent, image_path, command):
        card_frame = tk.Frame(parent, bg="white")
        card_frame.pack(pady=10)

        image = Image.open(image_path)
        image = image.resize((300, 150), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(card_frame, image=photo, bg="white")
        image_label.image = photo
        image_label.pack(anchor="center")

        # Adiciona funcionalidade de clique na imagem
        image_label.bind("<Button-1>", lambda e: command())

    # Funções para redirecionamento
    def imprimir_cartao_credito(self):
        self.controller.show_frame("TransacaoCredit")

    def imprimir_cartao_debito(self):
        self.controller.show_frame("TransacaoDebito")

    def imprimir_pix(self):
        self.controller.show_frame("TransacaoPix")

# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1080x1920")
    root.title("Payment Options Page")
    
    def mock_show_frame(page):
        print(f"Navigate to {page}")
    
    controller = type("MockController", (), {"show_frame": mock_show_frame})()
    
    page = PaymentOptionsPage(root, controller)
    page.pack(fill="both", expand=True)
    
    root.mainloop()