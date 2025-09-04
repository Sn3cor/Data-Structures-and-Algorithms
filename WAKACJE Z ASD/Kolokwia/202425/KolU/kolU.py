from kolUtesty import runtests
class IntervalAdder:
    def __init__(self,n):
        self.p = 1
        while self.p < n:
            self.p*=2

        self.T = [0 for _ in range(2*self.p-1)]

    def parent(self,i):
        return (i-1)//2
    
    def left(self,i):
        return 2*i + 1
    
    def right(self,i):
        return 2*i+2
    
    def get(self,i):
        return self.T[i+self.p-1]
    
    def update(self,i,value):
        k = self.p + i -1
        diff = value - self.T[k]
        while k >0:
            self.T[k] += diff
            k = self.parent(k)
            

    def sum_helper(self,k,lo,hi,i,j):
        if i == lo and j == hi:
            return self.T[k]
        
        mid = (hi-lo)//2

        if i > lo + mid :
            return self.sum_helper(self.right(k),lo+mid+1,hi,i,j)
        elif j <= lo + mid:
            return self.sum_helper(self.left(k),lo,lo+mid,i,j)
        else:
            left = self.sum_helper(self.left(k),lo,lo+mid,i,lo+mid)
            right = self.sum_helper(self.right(k),lo+mid+1,hi,lo+mid+1,j)
            return left+right
        
    def sum(self,i,j):
        if i > j:
            return 0
        return self.sum_helper(0,self.p-1,2*self.p-2,i+self.p-1,j+self.p-1)
    
def kawa(T,k):
    ia = IntervalAdder(k+1)
    ans = 0
    for i in range(len(T)-1,-1,-1):
        ans += ia.sum(0,T[i]-1)
        ia.update(T[i],ia.get(T[i])+1)


    return ans
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kawa, all_tests = True )
