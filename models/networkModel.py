class NETWORKMODEL:
    def __init__(self):
        self.send = None
        self.recv = None
        self.packets_sent = None
        self.packets_recv = None
        self.dropin = None
        self.dropout = None
        self.speed = None


    def set_send(self, send):
        self.send = send
    
    def set_recv(self, recv):
        self.recv = recv

    def set_packets_sent(self, packets_sent):
        self.packets_sent = packets_sent

    def set_packets_recv(self, packets_recv):
        self.packets_recv = packets_recv

    def set_dropin(self, dropin):
        self.dropin = dropin

    def set_dropout(self, dropout):
        self.dropout = dropout

    def set_speed(self, speed):
        self.speed = self.speed_spareted(speed)

    def get_send(self):
        return self.send

    def get_recv(self):
        return self.recv

    def get_packets_sent(self):
        return self.packets_sent

    def get_packets_recv(self):
        return self.packets_recv

    def get_dropin(self):
        return self.dropin

    def get_dropout(self):
        return self.dropout

    def get_speed(self):
        return self.speed
    
    def speed_spareted(self, speed):
        if speed['Ethernet'].isup == True:
            return speed['Ethernet'].speed
        elif speed['Ethernet 2'].isup == True:
            return speed['Ethernet 2'].speed
        elif speed['Ethernet 3'].isup == True:
            return speed['Ethernet 3'].speed
        elif speed['Wireless'].isup == True:
            return speed['Wireless'].speed

    def get_dict(self):
        return {
            'send': self.send,
            'recv': self.recv,
            'packets_sent': self.packets_sent,
            'packets_recv': self.packets_recv,
            'dropin': self.dropin,
            'dropout': self.dropout,
            'speed': self.speed,
        }
    
    def __str__(self):
        return str(self.get_dict())
    
