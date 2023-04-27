# ------------------------ # 
# Strategy Pattern 
# ------------------------ # 


# ------------------------ # 
# StorePrice strategies  
class StorePrice: 

    def __init__(self): 
        return 

class StorePrice_1(StorePrice): 
    
    def StorePrice(self, d): 
        # set new price 
        d.price = d.temp_p
        print('Price set at:', d.price)

# ------------------------ # 
# ZeroCF strategies 
# ------------------------ # 
class ZeroCF: 

    def __init__(self): 
        return 

class ZeroCF_1(ZeroCF): 
    
    def ZeroCF(self, d): 
        # reset funds 
        d.cf = 0 
        print('Funds zeroed out')

# ------------------------ # 
# IncreaseCF strategies 
# ------------------------ # 
class IncreaseCF: 

    def __init__(self): 
        return 

class IncreaseCF_1(IncreaseCF): 
    
    def IncreaseCF(self, d): 
        # increase funds 
        d.cf += d.temp_v 
        print('Funds increased to:', d.cf)

# ------------------------ # 
# ReturnCoins strategies 
# ------------------------ # 
class ReturnCoins(): 

    def __init__(self): 
        return 

class ReturnCoins_1(ReturnCoins): 
    
    def ReturnCoins(self, d):
        # return coins  
        print('Returning', d.temp_v, 'coin(s)') 
        d.temp_v = 0 

        
# ------------------------ # 
# ReturnFunds strategies 
# ------------------------ # 
class ReturnFunds(): 

    def __init__(self): 
        return 

class ReturnFunds_1(ReturnFunds): 
    
    def ReturnFunds(self, d):
        # return funds  
        print('Returning', d.cf, 'coin(s)') 
        d.cf = 0 

# ------------------------ # 
# DiseposeDrink strategies 
# ------------------------ # 
class DisposeDrink(): 

    def __init__(self): 
        return 

class DisposeTeaLatte(DisposeDrink): 
    
    def DisposeDrink(self, d: int): 
        # dispose tea 
        if d == 1: 
            print('Cup of tea disposed')
        # dispose latte 
        elif d == 2: 
            print('Cup of latte disposed')

class DisposeCoffee(DisposeDrink): 
    
    def DisposeDrink(self, d: int): 
        # dispose coffee
        if d == 1: 
            print('Cup of coffee disposed')

# ------------------------ # 
# DisposeAdditive strategies 
# ------------------------ # 
class DisposeAdditive(): 

    def __init__(self): 
        return 

class DisposeSugar(DisposeAdditive): 
    
    def DisposeAdditive(self, A):
        # dispose sugar 
        if A[1]: 
            print('Sugar disposed')

class DisposeCreamSugar(DisposeAdditive): 
    
    def DisposeAdditive(self, A): 
        # dispose cream 
        if A[1]: 
            print('Cream disposed')
        # dispose sugar 
        if A[2]: 
            print('Sugar disposed') 