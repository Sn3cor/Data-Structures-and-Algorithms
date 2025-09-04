from egz2atesty import runtests

class SegmentTree:
    def __init__(self, n, capacity):
        self.p = 1
        while self.p < n:
            self.p*=2
        self.last_magazine = None
        self.T = [0 for _ in range(2*self.p-1)]

        for i in range(self.p-1,2*self.p-1):
            self.T[i] = capacity

        for i in range(self.p-2,-1,-1):
            self.T[i] = max(self.T[self.right(i)],self.T[self.left(i)])
        

    def left(self,i):
        return 2*i+1
    
    def right(self,i):
        return 2*i+2

    def parent(self,i):
        return (i-1)//2
    
    def get(self,i):
        return self.T[i+self.p-1]
    
    def set(self,i,value):
        k = i + self.p -1 
        self.T[k] = value

        while k > 0:
            k = self.parent(k)
            self.T[k] = max(self.T[self.left(k)],self.T[self.right(k)])

    def find(self,k,value):
        if k>= self.p-1:
            self.set(k-self.p+1, self.get(k-self.p + 1) - value)
            self.last_magazine = k-self.p+1
            return

        if self.T[self.left(k)] >= value:
            self.find(self.left(k),value)

        elif self.T[self.right(k)] >= value:
            self.find(self.right(k),value)


def coal( A, T ):
    st = SegmentTree(len(A), T)
    for el in A:
        st.find(0,el)

    return st.last_magazine

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
