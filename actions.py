class StorePrice: 

    def __init__(self): 
        return 

class StorePrice_1(StorePrice): 
    
    def StorePrice(self, d): 
        d.price = d.temp_p
        print('Price set at:', d.price)

class ZeroCF: 

    def __init__(self): 
        return 

class ZeroCF_1(ZeroCF): 
    
    def ZeroCF(self, d): 
        d.cf = 0 
        print('Funds zeroed out')

class IncreaseCF: 

    def __init__(self): 
        return 

class IncreaseCF_1(IncreaseCF): 
    
    def IncreaseCF(self, d): 
        d.cf += d.temp_v 
        print('Funds increased to:', d.cf)

class ReturnCoins(): 

    def __init__(self): 
        return 

class ReturnCoins_1(ReturnCoins): 
    
    def ReturnCoins(self, d): 
        print('Returning', d.temp_v, 'coin(s)') 
        d.temp_v = 0 

class DisposeDrink(): 

    def __init__(self): 
        return 

class DisposeTeaLatte(DisposeDrink): 
    
    def DisposeDrink(self, d: int): 
        if d == 1: 
            print('Cup of tea disposed')
        elif d == 2: 
            print('Cup of latte disposed')

class DisposeCoffee(DisposeDrink): 
    
    def DisposeDrink(self, d: int): 
        if d == 1: 
            print('Cup of coffee disposed')

class DisposeAdditive(): 

    def __init__(self): 
        return 

class DisposeSugar(DisposeAdditive): 
    
    def DisposeAdditive(self, A): 
        if A[1]: 
            print('Sugar disposed')

class DisposeCreamSugar(DisposeAdditive): 
    
    def DisposeAdditive(self, A): 
        if A[1]: 
            print('Cream disposed')
        if A[2]: 
            print('Sugar disposed') 