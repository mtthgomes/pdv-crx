from ctypes import *
import ctypes
from pages.TransacaoBase import TransacaoBase
import os
import win32print
from utils.printer_utils import Imprimir_comprovante

class TransacaoPix(TransacaoBase):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.iniciar_transacao()

    def iniciar_transacao(self):
        # Parâmetros para transação de qr
        pValorTransacao = c_buffer(('000000002998').encode('utf-8'))
        pNumeroCupom = c_buffer(('123456').encode('utf-8'))
        pNumeroControle = c_buffer(7)
        pReservado = c_buffer(b'0' * 256)

        try:
            resultado_transacao = self.dll.TransacaoQRCode(
                pValorTransacao,
                pNumeroCupom,
                pNumeroControle,
                pReservado
            )

            if resultado_transacao == 0:
                numero_controle = pNumeroControle.value.decode('utf-8')
                confirma = self.confirmar_transacao(numero_controle)
                if confirma == 0:
                    comprovante_normal = f"C:\\ClientLinxTEF\\Cupons\\{numero_controle}.001"
                    Imprimir_comprovante(comprovante_normal)
                self.finalizar_transacao()
                success_page = self.controller.get_page("SuccessPage")
                success_page.set_numero_comprovante(numero_controle)
                self.controller.show_frame("SuccessPage")
            else:
                print(f"Erro na transação de QrCode. Código de erro: {resultado_transacao}")
                self.controller.show_frame("ErrorPage")

        except Exception as e:
            print(f"Erro ao realizar a transação: {e}")
            self.controller.show_frame("ErrorPage")