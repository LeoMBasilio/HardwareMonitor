from models.cpuModel import CPUMODEL
import psutil

class CPUController:

    def __init__(self):
        self.cpu = CPUMODEL()
        self.cpu.set_percent(psutil.cpu_percent(interval=1))
        self.cpu.set_core(psutil.cpu_count(logical=True))
        self.cpu.set_frequency(psutil.cpu_freq().current)

    def get_cpu(self):
        return self.cpu
    
    def __str__(self):
        return str(self.cpu)