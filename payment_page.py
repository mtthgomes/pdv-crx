import tkinter as tk

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
        logo = tk.PhotoImage(file="logo.png")
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
            if option == "One-Time Payment":
                controller.show_frame("PaymentOptionsPage")  # Navegar para a página de opções de pagamento
            elif option == "Membership":
                controller.show_frame("MembershipPage")  # Navegar para a página de QR code

        # Bloco "One-Time Payment"
        one_time_frame = tk.Frame(payment_frame, bg="white", highlightbackground="#CCCCCC", highlightthickness=2, padx=20, pady=20)
        one_time_frame.pack(fill="x", padx=100, pady=(0, 20))

        one_time_title = tk.Label(one_time_frame, text="One-Time Payment", font=("Helvetica", 16, "bold"), bg="white")
        one_time_title.pack(anchor="nw", pady=(0, 10))

        one_time_desc = tk.Label(one_time_frame, text="Charge users a one-time payment fee to access the content...", wraplength=800, bg="white")
        one_time_desc.pack(anchor="nw")

        one_time_frame.bind("<Button-1>", lambda e: on_block_click("One-Time Payment"))
        one_time_title.bind("<Button-1>", lambda e: on_block_click("One-Time Payment"))
        one_time_desc.bind("<Button-1>", lambda e: on_block_click("One-Time Payment"))

        # Bloco "Membership" com destaque
        membership_frame = tk.Frame(payment_frame, bg="white", highlightbackground="#FFA500", highlightthickness=4, padx=20, pady=20)
        membership_frame.pack(fill="x", padx=100)

        membership_title = tk.Label(membership_frame, text="Membership", font=("Helvetica", 16, "bold"), fg="#FFA500", bg="white")
        membership_title.pack(anchor="nw", pady=(0, 10))

        membership_desc = tk.Label(membership_frame, text="Charge users a one-time payment fee to access the content...", wraplength=800, bg="white")
        membership_desc.pack(anchor="nw")

        membership_frame.bind("<Button-1>", lambda e: on_block_click("Membership"))
        membership_title.bind("<Button-1>", lambda e: on_block_click("Membership"))
        membership_desc.bind("<Button-1>", lambda e: on_block_click("Membership"))
