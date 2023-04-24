from mda import mda_efsm
from absfact import CF1, CF2

class vm1: 
    
    def __init__(self, af, m): 
        # make concrete factory 
        self.af = af
        self.m = m
        self.d = self.af.d

    def create(self, p: int): 
        self.d.temp_p = p 
        self.m.create() 
    
    def coin(self, v: float): 
        self.d.temp_v = v 
        if self.d.cf + v >= self.d.price: 
            self.m.coin(1)
        else: 
            self.m.coin(0)

    def sugar(self): 
        self.m.additive(1)

    def tea(self): 
        self.m.dispose_drink(1)
    
    def latte(self): 
        self.m.dispose_drink(2)
    
    def insert_cups(self, n: int): 
        self.m.insert_cups(n)

    def set_price(self, p: float): 
        self.d.temp_p = p 
        self.m.set_price()

    def cancel(self): 
        self.m.cancel() 

class vm2: 
    
    def __init__(self, af, m):
        self.af = af
        self.m = m
        self.d = self.af.d

    def CREATE(self, p: float): 
        self.d.temp_p = p 
        self.m.create() 
    
    def COIN(self, v: int): 
        self.d.temp_v = v 
        if self.d.cf + v >= self.d.price: 
            self.m.coin(1)
        else: 
            self.m.coin(0)

    def CARD(self, x: int): 
        if x >= self.d.price: 
            self.m.card() 

    def SUGAR(self): 
        self.m.additive(2)

    def CREAM(self): 
        self.m.additive(1)

    def COFFEE(self): 
        self.m.dispose_drink(1)
    
    def InsertCups(self, n: int): 
        self.m.insert_cups(n)

    def SetPrice(self, p: float): 
        self.d.temp_p = p 
        self.m.set_price() 

    def CANCEL(self): 
        self.m.cancel() 

        
