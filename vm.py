from mda import mda_efsm
from data import DS1, DS2
from absfact import CF1, CF2

class vm1: 
    
    def __init__(self): 
        self.m = mda_efsm() 
        self.d = DS1() 
        self.af = CF1() 

    def create(self, p: int): 
        print('create function called with ', p)
    
    def coin(self, v: float): 
        print('coin function called with ', v)

    def sugar(self): 
        print('sugar called ')

    def tea(self): 
        print('tea called ')
    
    def latte(self): 
        print('latte called ')
    
    def insert_cups(self, n: int): 
        print('insert cups called with ', n, ' cups ')

    def set_price(self, p: float): 
        print('set price called ')

    def cancel(self): 
        print('cancel called ')


class vm2: 
    
    def __init__(self): 
        self.m = mda_efsm() 
        self.d = DS2() 
        self.af = CF2() 

    def CREATE(self, p: float): 
        print('CREATE function called with ', p)
    
    def COIN(self, v: int): 
        print('COIN function called with ', v)

    def CARD(self, x: int): 
        print('CARD called with ', x, 'funds ')

    def SUGAR(self): 
        print('SUGAR called ')

    def CREAM(self): 
        print('CREAM called ')

    def COFFEE(self): 
        print('COFFEE called ')
    
    def InsertCups(self, n: int): 
        print('InsertCups called with ', n, ' cups ')

    def SetPrice(self, p: float): 
        print('SetPrice called ')

    def CANCEL(self): 
        print('CANCEL called ')

        
