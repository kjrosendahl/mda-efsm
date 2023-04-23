from actions import StorePrice, StorePrice_1, ZeroCF, ZeroCF_1, IncreaseCF, IncreaseCF_1, ReturnCoins, ReturnCoins_1, DisposeDrink, DisposeCoffee, DisposeTeaLatte, DisposeAdditives, DisposeCreamSugar, DisposeSugar
from data import data, DS1, DS2

class abs_fact: 
    
    def __init__(self): 
        self.d = data() 
        self.StorePrice = StorePrice() 
        self.ZeroCF = ZeroCF() 
        self.IncreaseCF = IncreaseCF() 
        self.ReturnCoins = ReturnCoins() 
        self.DisposeDrink = DisposeDrink() 
        self.DisposeAdditive = DisposeAdditives() 

    def getStorePrice(self): 
        return self.StorePrice 

    def getZeroCF(self): 
        return self.ZeroCF 
    
    def getIncreaseCF(self): 
        return self.IncreaseCF 
    
    def getReturnCoins(self): 
        return self.ReturnCoins
    
    def getDisposeDrink(self): 
        return self.DisposeDrink

    def getDisposeAdditive(self): 
        return self.DisposeAdditive

class CF1(abs_fact): 

    def __init__(self):
        # get DS for VM1  
        self.d = DS1() 
        # get strategies for VM1 
        self.StorePrice = StorePrice_1() 
        self.ZeroCF = ZeroCF_1() 
        self.IncreaseCF = IncreaseCF_1() 
        self.ReturnCoins = ReturnCoins_1() 
        self.DisposeDrink = DisposeTeaLatte() 
        self.DisposeAdditive = DisposeSugar() 

class CF2(abs_fact):

    def __init__(self): 
        # get DS for VM2 
        self.d = DS2() 
        # get strategies for VM2
        self.StorePrice = StorePrice_1() 
        self.ZeroCF = ZeroCF_1() 
        self.IncreaseCF = IncreaseCF_1() 
        self.ReturnCoins = ReturnCoins_1() 
        self.DisposeDrink = DisposeCoffee() 
        self.DisposeAdditive = DisposeCreamSugar() 
    