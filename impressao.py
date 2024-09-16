import win32print
import win32api

def imprimir_texto(texto):
    # Obtém o nome da impressora padrão
    nome_impressora = win32print.GetDefaultPrinter()
    print(f"Imprimindo em: {nome_impressora}")
    
    # Envia o texto para a impressora
    hPrinter = win32print.OpenPrinter(nome_impressora)
    try:
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("Texto a ser impresso", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)
        win32print.WritePrinter(hPrinter, texto.encode('utf-8'))
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)

if __name__ == "__main__":
    # Chama a função de impressão com o texto que você deseja imprimir
    imprimir_texto("Olá, isso é um teste de impressão!\nObrigado por utilizar nosso serviço.")
