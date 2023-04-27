class data: 
    def __init__(self): 
        return 
    
# data store for VM1 
class DS1(data): 
        
    def __init__(self): 
        self.temp_p = float(0)
        self.temp_v = float(0)
        self.price = float(0)
        self.cf = float(0)

# data store for VM2  
class DS2(data): 
        
    def __init__(self): 
        self.temp_p = float(0) 
        self.temp_v = int(0)
        self.price = float(0)
        self.cf = int(0)

