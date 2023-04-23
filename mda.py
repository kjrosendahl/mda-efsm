from collections import defaultdict
from op import op 

class mda_efsm: 
    
    def __init__(self): 

        # initialize list of states 
        self.LS = [start(self), no_cups(self), idle(self), ready(self)]
        # initialize pointer to start state 
        self.S = self.LS[0]

        # initialize cups and additive list 
        self.cups = 0 
        self.A = None 

        print('MDA-EFSM created with', self.cups, 'cups')
        
    def change_state(self, ID): 
        old = self.S 
        self.S = self.LS[ID] 
        new = self.S 
        print('Transition from state ', old, ' to state ', new)
    
    def create(self): 
        self.S.create() 

    def insert_cups(self, n: int): 
        self.S.insert_cups(n) 
    
    def coin(self, f: int): 
        self.S.coin(f)  
    
    def card(self): 
        self.S.card()  
    
    def cancel(self): 
        self.S.cancel()  
    
    def set_price(self): 
        self.S.set_price()  
    
    def dispose_drink(self, d: int): 
        self.S.dispose_drink(d) 

    def additive(self, a: int): 
        self.S.additive(a) 
    
class states(): 

    def __init__(self, m):

        # set MDA-EFSM pointer for state 
        self.m = m 
        # add OP pointer 
        self.p = op() 

    # abstract methods 
    def create(self): 
        pass 

    def insert_cups(self, n: int): 
        pass 
    
    def coin(self, f: int): 
        pass 
    
    def card(self): 
        pass 
    
    def cancel(self): 
        pass 
    
    def set_price(self): 
        pass 
    
    def dispose_drink(self, d: int): 
        pass 

    def additive(self, a: int): 
        pass 

class start(states): 

    def create(self): 
        self.p.StorePrice() 
        # transition to no_cups state 
        self.m.change_state(1)

class no_cups(states): 

    def insert_cups(self, n: int): 
        print('Inserting', n, 'cups')
        # increase cups 
        self.m.cups += n
        print('Total cups:', self.m.cups)
        # transition to idle state  
        self.m.change_state(2)
        
    def coin(self): 
        self.p.ReturnCoins() 

class idle(states): 

    def insert_cups(self, n: int): 
        print('inserting ', n, 'cups')
        # increase cups 
        self.m.cups += n 
        print('Total cups:', self.m.cups)
    
    def coin(self, f: int): 
        self.p.IncreaseCF() 
        # if enough funds: 
        if f == 1: 
            # transition to ready state 
            self.m.change_state(3)
            # reset additives list 
            self.m.A = defaultdict(int)
    
    def card(self): 
        self.p.ZeroCF()
        # transition to ready state 
        self.m.change_state(3) 
        # reset additives list 
        self.m.A = defaultdict(int)

    def set_price(self): 
        self.p.StorePrice() 

class ready(states): 

    def coin(self, f: int): 
        self.p.ReturnCoins() 
    
    def cancel(self): 
        self.p.ReturnCoins() 
        self.p.ZeroCF() 
        # transition back to idle state 
        self.m.change_state(2)

    def dispose_drink(self, d: int): 
        self.p.DisposeDrink(d)
        self.p.DisposeAdditive(self.m.A)
        self.m.cups -= 1 
        # if out of cups 
        if self.m.cups == 0: 
            # transition to no_cups state 
            self.m.change_state(1)
        else: 
            self.p.ZeroCF() 
            # transition to idle state 
            self.m.change_state(2)

    def additive(self, a: int): 
        # swap additive in additive list (T->F or F->T)
        self.m.A[a] =  not self.m.A[a]
