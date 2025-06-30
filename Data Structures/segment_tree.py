class IntervalAdder:
    def __init__(self,n):
        self.p = 1
        while self.p<n: 
            self.p*=2 

        self.T=[0 for _ in range(2*self.p - 1)]


    def parent(self,i):
        return (i-1)//2
    
    def left(self,i):
        return 2*i + 1
    
    def right(self,i):
        return 2*i+2
    
    def get(self,i):
        return self.T[i + self.p-1]
    
    def set(self,i,value):
        k = i + self.p - 1

        diff = value - self.T[k]

        while k >=0:
            self.T[k] += diff
            k = self.parent(k)

    def sum_helper(self,k,lo,hi,i,j):
        if i==lo and j == hi:
            return self.T[k]
        
        r = (hi-lo)//2

        if i > lo + r:
            return self.sum_helper(self.right(k),lo+r+1,hi,i,j)
        elif j<= lo+r:
            return self.sum_helper(self.left(k),lo,lo+r,i,j)
        else:
            res1 = self.sum_helper(self.left(k),lo,lo+r,i,lo+r)
            res2 = self.sum_helper(self.right(k),lo+r+1,hi,lo+r+1,j)
            return res1+res2


    def sum(self,i,j):
        if i > j:
            return 0
        
        return self.sum_helper(0,self.p-1,2*self.p-2,i + self.p-1,j+self.p-1)
    


ia = IntervalAdder(8)
ia.set(0,5)
ia.set(1,2)
ia.set(2,5)
ia.set(3,2)
ia.set(4,5)
ia.set(5,2)
ia.set(6,5)
ia.set(7,2)

print(ia.sum(0,3))