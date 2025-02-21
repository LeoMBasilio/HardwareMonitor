from models.memoryModel import MESMORYMODEL
import psutil

class MEMORYController():
    def __init__(self):
        self.memory = MESMORYMODEL()
        self.memory.set_total(psutil.virtual_memory().total)
        self.memory.set_used(psutil.virtual_memory().used)
        self.memory.set_percent(psutil.virtual_memory().percent)

    def getMemory(self):
        return self.memory

    def __str__(self):
        return str(self.getMemory())