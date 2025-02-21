from datetime import datetime
class USERMODEL:
    def __init__(self):
        self.name = None
        self.terminal = None
        self.host = None
        self.started = None
        self.pid = None

    def set_name(self, name):
        self.name = name
    
    def set_terminal(self, terminal):
        self.terminal = terminal
    
    def set_host(self, host):
        self.host = host

    def set_started(self, started):
        self.started = datetime.fromtimestamp(started)

    def set_pid(self, pid):
        self.pid = pid

    def get_name(self):
        return self.name

    def get_terminal(self):
        return self.terminal

    def get_host(self):
        return self.host
    
    def get_started(self):
        return self.started

    def get_pid(self):
        return self.pid
    
    def get_dict(self):
        return {
            'name': self.name,
            'terminal': self.terminal,
            'host': self.host,
            'started': self.started,
            'pid': self.pid
        }
    
    def __str__(self):
        return str(self.get_dict())