import win32serviceutil
import win32service
import win32event
import servicemanager
import time
import os

class HelloWorldService(win32serviceutil.ServiceFramework):
    _svc_name_ = "HelloWorldService"
    _svc_display_name_ = "Hello World Python Service"
    _svc_description_ = "A demo service that writes 'Hello, World!' to a log file every 5 seconds"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.running = False
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        servicemanager.LogInfoMsg("HelloWorldService is starting...")
        self.main()

    def main(self):
        log_file = "C:\\hello_service.log"
        while self.running:
            with open(log_file, "a") as f:
                f.write("Hello, World!\n")
            time.sleep(5)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(HelloWorldService)
