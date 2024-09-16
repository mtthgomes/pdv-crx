import tkinter as tk
from PIL import Image, ImageTk
import qrcode

class MembershipPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        # Configuração do grid para centralizar o QR code e logo
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

        # Gerar o QR code com um valor fixo
        self.generate_qr_code("chave_pix_fixa")

    def generate_qr_code(self, value):
        # Gerando o QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(value)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img = qr_img.resize((300, 300), Image.LANCZOS)  # Usando LANCZOS em vez de ANTIALIAS
        qr_photo = ImageTk.PhotoImage(qr_img)

        # Label para exibir o QR code
        qr_label = tk.Label(self, image=qr_photo, bg="white")
        qr_label.image = qr_photo  # Manter referência da imagem
        qr_label.grid(row=1, column=0, sticky="n")
