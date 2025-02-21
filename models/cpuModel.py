class  CPUMODEL:
    def __init__(self):
        self.percent = None
        self.core = None
        self.frequency = None
    
    def set_percent(self, percent):
        self.percent = percent
    
    def set_core(self, core):
        self.core = core
    
    def set_frequency(self, frequency):
        self.frequency = frequency

    def get_percent(self):
        return self.percent

    def get_core(self):
        return self.core
    
    def get_frequency(self):
        return self.frequency
    
    def get_dict(self):
        return {
            'percent': self.percent,
            'core': self.core,
            'frequency': self.frequency
        }    
    
    def __str__(self):
        return str(self.get_dict())