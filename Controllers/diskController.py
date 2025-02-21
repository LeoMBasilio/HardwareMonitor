from models.disksModel import DISKMODEL
import psutil

class DISKController:
    def __init__(self):
        self.disk = DISKMODEL()
        self.disk.set_read(psutil.disk_io_counters().read_bytes)
        self.disk.set_write(psutil.disk_io_counters().write_bytes)
        self.disk.set_readTime(psutil.disk_io_counters().read_time)
        self.disk.set_writeTime(psutil.disk_io_counters().write_time)
        self.disk.set_used(psutil.disk_usage('/').used)
        self.disk.set_total(psutil.disk_usage('/').total)
        self.disk.set_percent(psutil.disk_usage('/').percent)
        self.disk.set_free(psutil.disk_usage('/').free)

    def getDisk(self):
        return self.disk
    
    def __str__(self):
        return str(self.disk)