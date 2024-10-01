import tkinter as tk
from pages.start_page import StartPage
from pages.payment_page import PaymentPage
from pages.membership_page import MembershipPage
from pages.payment_options_page import PaymentOptionsPage
from pages.transacaoDebito import TransacaoDebito
from pages.transacaoCredit import TransacaoCredit
from pages.transacaoPix import TransacaoPix
from pages.SuccessPage import SuccessPage
from pages.ErrorPage import ErrorPage

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRX Automation")
        self.attributes('-fullscreen', True)
        self.configure(bg="white")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Dicionário para armazenar as páginas criadas

        # Apenas instanciamos a página inicial aqui
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        if page_name not in self.frames:
            if page_name == "StartPage":
                frame = StartPage(parent=self.container, controller=self)
            elif page_name == "PaymentPage":
                frame = PaymentPage(parent=self.container, controller=self)
            elif page_name == "MembershipPage":
                frame = MembershipPage(parent=self.container, controller=self)
            elif page_name == "PaymentOptionsPage":
                frame = PaymentOptionsPage(parent=self.container, controller=self)
            elif page_name == "TransacaoDebito":
                frame = TransacaoDebito(parent=self.container, controller=self)
            elif page_name == "TransacaoCredit":
                frame = TransacaoCredit(parent=self.container, controller=self)
            elif page_name == "TransacaoPix":
                frame = TransacaoPix(parent=self.container, controller=self)
            elif page_name == "SuccessPage":
                frame = SuccessPage(parent=self.container, controller=self)
            elif page_name == "ErrorPage":
                frame = ErrorPage(parent=self.container, controller=self)
            else:
                raise ValueError(f"Página '{page_name}' não encontrada.")

            # Adiciona a página ao dicionário de frames
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Levanta a página solicitada
        frame = self.frames[page_name]
        frame.tkraise()

    def get_page(self, page_name):
        """Retorna a instância de uma página pelo nome"""
        if page_name not in self.frames:
            self.show_frame(page_name)  # Cria a página se ela ainda não existir
        return self.frames.get(page_name)


    def reiniciar_aplicacao(self):
        # Destruir todos os frames existentes
        for frame in self.frames.values():
            if isinstance(frame, tk.Frame):  # Verificar se é um frame Tkinter antes de destruir
                frame.destroy()

        # Limpar o dicionário de frames
        self.frames.clear()

        # Mostrar a página inicial
        self.show_frame("StartPage")

if __name__ == "__main__":
    app = Application()
    app.mainloop()