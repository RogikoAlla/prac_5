class rectangle:
    rectcnt = 0
    
    def __init__(self,x1,y1,x2,y2):
        self.x1,self.y1,self.x2,self.y2 = x1,y1,x2,y2
        self__class__.rectcnt += 1
        setattr(self,f"({rect__rectcnt)")
    def __str__(self)
        return f"[{self.rectcnt}]({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"
    def __abs__(self):
        sq = (self.x2-self.x1)*(self.y2-self.y1)
    def __lt__(self, other):
        return abs(self) < abs(other)
    def __eq__(self, other):
        return abs(self) == abs(other)
    def __mul__(self, x):
        return self.__class__(x1=self.x1*x,y1=self.y1*x,x2=self.x2*x,y2 = self.y2*x)
        
    __rmul__ = __mul__
    
    #def __getitems__(self,i):
    #    arr = []
     #   retiurn(arr % 4)
      
    def __iter__(self):
        
    def __bool__(self):
        return abs(self) > 0
        

        