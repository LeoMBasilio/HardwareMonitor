from models.networkModel import NETWORKMODEL
import psutil

class NETWORKCONTROLLER:
    def __init__(self):
       self.network = NETWORKMODEL()
       self.network.set_recv(psutil.net_io_counters().bytes_recv)
       self.network.set_send(psutil.net_io_counters().bytes_sent)
       self.network.set_packets_recv(psutil.net_io_counters().packets_recv)
       self.network.set_packets_sent(psutil.net_io_counters().packets_sent)
       self.network.set_dropin(psutil.net_io_counters().dropin)
       self.network.set_dropout(psutil.net_io_counters().dropout)
       self.network.set_speed(psutil.net_if_stats())

    def getNetwork(self):
        return self.network


