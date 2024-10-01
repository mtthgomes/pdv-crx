from ctypes import *

class TransacaoBase:
    def __init__(self):
        print("Carregando dll")
        self.dll = windll.LoadLibrary(r"C:\ClientLinxTEF\Bin\DPOSDRV.dll")
        print("DLL carregada")

        # Inicializar DPOS
        print("Inicializa DPOS")
        resultado_inicializa = self.dll.InicializaDPOS()
        print(f"Resultado InicializaDPOS: {resultado_inicializa}")
        pReservadoAutomacao = c_buffer(('CRX AUTOMATION').encode('utf-8'))
        pReservadoVersion = c_buffer(('1.0').encode('utf-8'))
        pReservadoIdentifica = c_buffer(('010').encode('utf-8'))
        
        self.dll.IdentificacaoAutomacaoComercial(pReservadoAutomacao, pReservadoVersion, pReservadoIdentifica)
        
        self.dll.ConfiguraModoDesfazimento(1)

    def confirmar_transacao(self, pNumeroControle):
        # Confirma a transação
        pControleNumero = c_buffer((pNumeroControle).encode('utf-8'))  
        confirma = self.dll.ConfirmaCartao(pControleNumero)
        return confirma

    def finalizar_transacao(self):
        # Finaliza a transação
        try:
            resultado_finaliza = self.dll.FinalizaTransacao()
            print(f"Transação finalizada com sucesso, resultado: {resultado_finaliza}")
        except Exception as e:
            print(f"Erro ao finalizar a transação: {e}")