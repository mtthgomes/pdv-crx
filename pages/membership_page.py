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
        logo = tk.PhotoImage(file="images/logo.png")
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

        # Criar o label do timer
        self.time_remaining = 5 * 60  # 5 minutos em segundos
        self.timer_label = tk.Label(self, text="", font=("Helvetica", 18, "bold"), bg="white")
        self.timer_label.grid(row=2, column=0, pady=10)

        # Adicionar o botão "Cancelar" na parte inferior
        cancel_button = tk.Button(self, text="Cancelar", font=("Helvetica", 14), bg="#FF5555", fg="white", 
                                  command=self.cancel_transaction)
        cancel_button.grid(row=3, column=0, pady=(30, 40))

        # Iniciar o temporizador
        self.update_timer()

    def generate_qr_code(self, value):
        # Gerando o QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=30,
            border=4,
        )
        qr.add_data(value)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img = qr_img.resize((600, 600), Image.LANCZOS)  # Usando LANCZOS em vez de ANTIALIAS
        qr_photo = ImageTk.PhotoImage(qr_img)

        # Label para exibir o QR code
        qr_label = tk.Label(self, image=qr_photo, bg="white")
        qr_label.image = qr_photo  # Manter referência da imagem
        qr_label.grid(row=1, column=0, sticky="n")

    def update_timer(self):
        """Atualiza o temporizador e exibe o tempo restante no formato MM:SS."""
        if self.time_remaining > 0:
            minutes, seconds = divmod(self.time_remaining, 60)
            time_format = f"Tempo restante: {minutes:02}:{seconds:02}"
            self.timer_label.config(text=time_format)
            self.time_remaining -= 1
            self.after(1000, self.update_timer)  # Chama novamente após 1 segundo
        else:
            # Quando o tempo acabar, redirecionar para o app
            self.controller.show_frame("StartPage")  # Redirecionar para a página inicial

    def cancel_transaction(self):
        """Redireciona para a página inicial quando o botão 'Cancelar' é clicado."""
        self.controller.show_frame("StartPage")


# Exemplo de uso dessa classe com tkinter
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1080x1920")
    root.title("Membership Page")
    
    def mock_show_frame(page):
        print(f"Navigate to {page}")
    
    controller = type("MockController", (), {"show_frame": mock_show_frame})()
    
    page = MembershipPage(root, controller)
    page.pack(fill="both", expand=True)
    
    root.mainloop()