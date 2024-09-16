import win32serviceutil
import win32service
import win32event
import servicemanager
from impressao import imprimir_texto

class PrinterService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PrinterService"
    _svc_display_name_ = "Python Printer Service"
    _svc_description_ = "Serviço para imprimir na impressora térmica"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, "")
        )
        self.run()

    def run(self):
        # Aqui você pode incluir a chamada da função de impressão
        while True:
            # Substitua por lógica que captura uma requisição, evento ou arquivo a ser impresso
            imprimir_texto("Teste de impressão contínua")
            win32event.WaitForSingleObject(self.hWaitStop, 5000)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PrinterService)
