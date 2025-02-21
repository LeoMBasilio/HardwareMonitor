from models.userModel import USERMODEL
import psutil

class USERCONTROLLER:
    def __init__(self):
        self.user = USERMODEL()
        self.user.set_name(psutil.users()[0].name)
        self.user.set_host(psutil.users()[0].host)
        self.user.set_pid(psutil.users()[0].pid)
        self.user.set_started(psutil.users()[0].started)

    def getUser(self):
        return self.user