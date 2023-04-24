class op: 

    def __init__(self, af): 
        # get pointer to data 
        self.d = af.d 
        # get pointers to action objects
        self.p1 = af.getStorePrice() 
        self.p2 = af.getZeroCF() 
        self.p3 = af.getIncreaseCF() 
        self.p4 = af.getReturnCoins() 
        self.p5 = af.getDisposeDrink() 
        self.p6 = af.getDisposeAdditive() 

    # def __init__(self): 
    #     self.d = None 
    #     self.p1 = None 
    #     self.p2 = None 
    #     self.p3 = None 
    #     self.p4 = None 
    #     self.p5 = None 
    #     self.p6 = None 

    def Initialize(self, af): 
        # get pointer to data 
        self.d = af.d 
        # get pointers to action objects
        self.p1 = af.getStorePrice() 
        self.p2 = af.getZeroCF() 
        self.p3 = af.getIncreaseCF() 
        self.p4 = af.getReturnCoins()
        self.p5 = af.getDisposeDrink() 
        self.p6 = af.getDisposeAdditive() 

    def StorePrice(self): 
        self.p1.StorePrice(self.d)  

    def ZeroCF(self): 
        self.p2.ZeroCF(self.d) 

    def IncreaseCF(self): 
        self.p3.IncreaseCF(self.d) 

    def ReturnCoins(self): 
        self.p4.ReturnCoins(self.d) 

    def DisposeDrink(self, d): 
        self.p5.DisposeDrink(d)

    def DisposeAdditive(self, A):
        self.p6.DisposeAdditive(A)  
