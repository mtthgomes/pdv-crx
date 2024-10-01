from ctypes import *

class LinxTEFIntegration:
    def __init__(self):
        # Carregar a DLL da Linx TEF
        self.dll = windll.LoadLibrary(r"C:\ClientLinxTEF\Bin\DPOSDRV.dll")

        # Registra os callbacks
        self.registrar_callbacks()

    def registrar_callbacks(self):
        """Registrar callbacks na DLL para integração sem telas."""
        @CFUNCTYPE(None, c_char_p)
        def display_terminal(mensagem):
            print(f"Display: {mensagem.decode('utf-8')}")

        @CFUNCTYPE(None, c_char_p)
        def display_erro(mensagem):
            print(f"Erro: {mensagem.decode('utf-8')}")

        self.dll.RegPDVDisplayTerminal(display_terminal)
        self.dll.RegPDVDisplayErro(display_erro)