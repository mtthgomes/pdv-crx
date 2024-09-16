import tkinter as tk
from start_page import StartPage
from payment_page import PaymentPage
from membership_page import MembershipPage
from payment_options_page import PaymentOptionsPage
from transacaoDebito import TransacaoDebito
from transacaoCredit import TransacaoCredit
from transacaoPix import TransacaoQrCode

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

        self.frames = {}

        for F in (StartPage, PaymentPage, MembershipPage, PaymentOptionsPage, TransacaoDebito):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("TransacaoDebito")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
