class DISKMODEL:
    def __init__(self):
        self.read = None
        self.write = None
        self.readTime = None
        self.writeTime = None
        self.used = None
        self.total = None
        self.percent = None
        self.free = None

    def set_read(self, read):
        self.read = read
    
    def set_write(self, write):
        self.write = write
    
    def set_readTime(self, readTime):
        self.readTime = readTime
    
    def set_writeTime(self, writeTime):
        self.writeTime = writeTime

    def set_used(self, used):
        self.used = used

    def set_total(self, total):
        self.total = total

    def set_percent(self, percent):
        self.percent = percent

    def set_free(self, free):
        self.free = free
    
    def get_read(self):
        return self.read
    
    def get_write(self):
        return self.write
    
    def get_readTime(self):
        return self.readTime
    
    def get_writeTime(self):
        return self.writeTime
    
    def get_used(self):
        return self.used

    def get_total(self):
        return self.total

    def get_percent(self):
        return self.percent

    def get_free(self): 
        return self.free
    
    def get_dict(self):
        return {
            'read': self.read,
            'write': self.write,
            'readTime': self.readTime,
            'writeTime': self.writeTime,
            'used': self.used,
            'total': self.total,
            'percent': self.percent,
            'free': self.free
        }
    
    def __str__(self):
        return str(self.get_dict())