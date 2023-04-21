from collections import defaultdict

class mda_efsm: 
    
    def __init__(self): 
        self.LS = [0,0,0,0]
        self.S = self.LS[0]
        return

    def change_state(self, ID): 
        self.S = self.LS[ID] 
    
class states: 

    def __init__(self, m): 
        self.d = mda_data()
        self.m = m 
        # add OP pointer 
        self.p = 1 

    def create(self): 
        return 

    def insert_cups(self, n: int): 
        return 
    
    def coin(self, f: int): 
        return 
    
    def card(self): 
        return 
    
    def cancel(self): 
        return 
    
    def set_price(self): 
        return 
    
    def dispose_drink(self, d: int): 
        return 

    def additive(self, a: int): 
        return 

    
class start(states): 

    def create(self): 
        self.p.create()  

class no_cups(states): 

    def insert_cups(self, n: int): 
        self.p.insert_cups(n)  
    
    def coin(self, f: int): 
        self.p.coin(f)

class idle(states): 

    def insert_cups(self, n: int): 
        self.p.insert_cups(n) 
    
    def coin(self, f: int): 
        self.p.coin(f)  
    
    def card(self): 
        self.p.card()  

    def set_price(self): 
        self.p.set_price()  

class ready(states): 

    def coin(self, f: int): 
        self.p.coin(f)  
    
    def cancel(self): 
        self.p.cancel() 

    def dispose_drink(self, d: int): 
        self.p.dispose_drink(d) 

    def additive(self, a: int): 
        self.p.dispose_drink(a)  
    
class mda_data: 
    
    def __init__(self): 
        self.cups == 0 
        self.A = defaultdict(int) 
