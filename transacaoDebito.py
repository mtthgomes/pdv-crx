from ctypes import *
import ctypes
import tkinter as tk

class TransacaoDebito(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        print("Carregando dll")
        dll = windll.LoadLibrary(r"C:\ClientLinxTEF\Bin\DPOSDRV.dll")
        print("Dll carregada")

        print("Inicializa DPOS")
        print(dll.InicializaDPOS())
        print('executou a função')


        pValorTransacao = c_buffer(('000000209998').encode('utf-8'))
        pNumeroCupom = c_buffer(7)
        pNumeroControle = c_buffer(7)

        try:
            print("TransacaoCartaoDebito")
            print(dll.TransacaoCartaoDebito(pValorTransacao, pNumeroCupom, pNumeroControle))
            print('executou a função')
        except:
            last_error = ctypes.GetLastError()
            raise ctypes.WinError()
        print('executou a função')