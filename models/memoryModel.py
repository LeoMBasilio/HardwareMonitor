class MESMORYMODEL:
    def __init__(self):
        self.total = None 
        self.used = None 
        self.percent = None 

    def set_total(self, total):
        self.total = total
    
    def set_used(self, used):
        self.used = used

    def set_percent(self, percent):
        self.percent = percent
    
    def get_total(self):
        return self.total
    
    def get_used(self):
        return self.used
    
    def get_percent(self):
        return self.percent
    
    def get_dict(self):
        return {
            'total': self.total,
            'used': self.used,
            'percent': self.percent
        }
    
    def __str__(self):
        return str(self.get_dict())