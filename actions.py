class StorePrice: 

    def __init__(self): 
        return 

class StorePrice_1(StorePrice): 
    pass 

class ZeroCF: 

    def __init__(self): 
        return 

class ZeroCF_1(ZeroCF): 
    pass 

class IncreaseCF: 

    def __init__(self): 
        return 

class IncreaseCF_1(IncreaseCF): 
    pass 

class ReturnCoins(): 

    def __init__(self): 
        return 

class ReturnCoins_1(ReturnCoins): 
    pass 

class DisposeDrink(): 

    def __init__(self): 
        return 

class DisposeTeaLatte(DisposeDrink): 
    
    def DisposeDrink(d: int): 
        if d == 1: 
            print('Cup of tea disposed.')
        elif d == 2: 
            print('Cup of latte disposed.')

class DisposeCoffee(DisposeDrink): 
    
    def DisposeDrink(d: int): 
        if d == 1: 
            print('Cup of coffee disposed.')

class DisposeAdditives(): 

    def __init__(self): 
        return 

class DisposeSugar(DisposeAdditives): 
    
    def DisposeAdditives(A): 
        if A[1]: 
            print('Sugar disposed.')

class DisposeCreamSugar(DisposeAdditives): 
    
    def DisposeAdditives(A): 
        if A[1]: 
            print('Cream disposed.')
        if A[2]: 
            print('Sugar disposed.') 