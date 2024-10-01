import win32print

def Imprimir_comprovante(caminho_comprovante):
    nome_impressora = win32print.GetDefaultPrinter()
    hPrinter = win32print.OpenPrinter(nome_impressora)
    
    try:
        with open(caminho_comprovante, 'r') as file:
            comprovante = file.read()

            comprovante += "\n\n\n\n\n\n\n\n"

            hJob = win32print.StartDocPrinter(hPrinter, 1, ("Nota Fiscal", None, "RAW"))
            win32print.StartPagePrinter(hPrinter)
            win32print.WritePrinter(hPrinter, comprovante.encode('utf-8'))
            win32print.EndPagePrinter(hPrinter)
            win32print.EndDocPrinter(hPrinter)

    except Exception as e:
        print(f"Erro ao imprimir comprovante: {e}")
    finally:
        win32print.ClosePrinter(hPrinter)