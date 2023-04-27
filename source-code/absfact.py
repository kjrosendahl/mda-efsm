# ------------------------ # 
# Abstract Factory Pattern 
# ------------------------ #

from actions import StorePrice_1, StorePrice_2, ZeroCF_1, ZeroCF_2, IncreaseCF_1, ReturnCoins_1, ReturnCoins_2, IncreaseCF_2, ReturnFunds_1, ReturnFunds_2, DisposeCoffee, DisposeTeaLatte, DisposeCreamSugar, DisposeSugar
from data import data, DS1, DS2

class abs_fact: 
    
    def __init__(self): 
        self.d = data() 

    # abstract methods 
    def getStorePrice(self): 
        pass 

    def getZeroCF(self): 
        pass 
    
    def getIncreaseCF(self): 
        pass 
    
    def getReturnCoins(self): 
        pass 
    
    def getDisposeDrink(self): 
        pass 

    def getDisposeAdditive(self): 
        pass 

# Factory for VM1 
class CF1(abs_fact): 

    def __init__(self):
        # make DS for VM1  
        self.d = DS1() 

    def getStorePrice(self): 
        return StorePrice_1()  

    def getZeroCF(self): 
        return ZeroCF_1()  
    
    def getIncreaseCF(self): 
        return IncreaseCF_1()  
    
    def getReturnCoins(self): 
        return ReturnCoins_1() 
    
    def getReturnFunds(self): 
        return ReturnFunds_1() 
    
    def getDisposeDrink(self): 
        return DisposeTeaLatte() 

    def getDisposeAdditive(self): 
        return DisposeSugar()  

# Factory for VM2 
class CF2(abs_fact):

    def __init__(self): 
        # make DS for VM2 
        self.d = DS2() 

    def getStorePrice(self): 
        return StorePrice_2()  

    def getZeroCF(self): 
        return ZeroCF_2()  
    
    def getIncreaseCF(self): 
        return IncreaseCF_2()  
    
    def getReturnCoins(self): 
        return ReturnCoins_2() 
    
    def getReturnFunds(self): 
        return ReturnFunds_2() 
    
    def getDisposeDrink(self): 
        return DisposeCoffee() 

    def getDisposeAdditive(self): 
        return DisposeCreamSugar()  