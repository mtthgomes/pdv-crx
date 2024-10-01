from integration.linx_tef_integration import LinxTEFIntegration
from ctypes import *
import ctypes
from pages.TransacaoBase import TransacaoBase

class TransacaoDebito(TransacaoBase):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.iniciar_transacao()

    def iniciar_transacao(self):
        # Parâmetros para transação de débito
        pValorTransacao = c_buffer(('000000209998').encode('utf-8'))
        pNumeroCupom = c_buffer(('123456').encode('utf-8'))
        pNumeroControle = c_buffer(7)
        pTipoOperacao = c_buffer(('AV').encode('utf-8'))
        pNumeroParcelas = c_buffer(('00').encode('utf-8'))
        pSequenciaParcela = c_buffer(('01').encode('utf-8'))
        pDataDebito = c_buffer(('01012024').encode('utf-8'))
        pValorParcela = c_buffer(('000000209998').encode('utf-8'))
        pValorTaxaServico = c_buffer(('000000000000').encode('utf-8'))
        pPermiteAlteracao = c_buffer(('N').encode('utf-8'))
        pReservado = c_buffer(b'0' * 148)

        try:
            resultado_transacao = self.dll.TransacaoCartaoDebitoCompleta(
                pValorTransacao, pNumeroCupom, pNumeroControle, 
                pTipoOperacao, pNumeroParcelas, pSequenciaParcela, 
                pDataDebito, pValorParcela, pValorTaxaServico, 
                pPermiteAlteracao, pReservado
            )

            if resultado_transacao == 0:
                numero_controle = pNumeroControle.value.decode('utf-8')
                print("Transação de débito aprovada! NSU:", numero_controle)

                # Redireciona para página de sucesso
                self.controller.show_frame("SuccessPage")
            else:
                print(f"Erro na transação de débito. Código de erro: {resultado_transacao}")
                # Redireciona para página de erro
                self.controller.show_frame("ErrorPage")

        except Exception as e:
            print(f"Erro ao realizar a transação: {e}")
            self.controller.show_frame("ErrorPage")