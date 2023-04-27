# ------------------------ # 
# Abstract Factory + Strategy Pattern 
# ------------------------ # 

class op: 

    def __init__(self, af): 
        # get pointer to data 
        self.d = af.d 
        # get pointers to action objects
        self.p1 = af.getStorePrice() 
        self.p2 = af.getZeroCF() 
        self.p3 = af.getIncreaseCF() 
        self.p4 = af.getReturnCoins() 
        self.p5 = af.getReturnFunds() 
        self.p6 = af.getDisposeDrink() 
        self.p7 = af.getDisposeAdditive() 


    # def Initialize(self, af): 
    #     # get pointer to data 
    #     self.d = af.d 
    #     # get pointers to action objects
    #     self.p1 = af.getStorePrice() 
    #     self.p2 = af.getZeroCF() 
    #     self.p3 = af.getIncreaseCF() 
    #     self.p4 = af.getReturnCoins()
    #     self.p5 = af.getDisposeDrink() 
    #     self.p6 = af.getDisposeAdditive() 

    def StorePrice(self): 
        self.p1.StorePrice(self.d)  

    def ZeroCF(self): 
        self.p2.ZeroCF(self.d) 

    def IncreaseCF(self): 
        self.p3.IncreaseCF(self.d) 

    def ReturnCoins(self): 
        self.p4.ReturnCoins(self.d) 

    def ReturnFunds(self): 
        self.p5.ReturnFunds(self.d) 

    def DisposeDrink(self, d): 
        self.p6.DisposeDrink(d)

    def DisposeAdditive(self, A):
        self.p7.DisposeAdditive(A)  
