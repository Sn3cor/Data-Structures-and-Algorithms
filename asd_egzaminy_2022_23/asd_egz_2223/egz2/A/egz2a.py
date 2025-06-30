from egz2atesty import runtests

class IntervalAdder:
  def __init__(self,n):
    self.p = 1

    while self.p<n:
      self.p*=2

    self.T=[0 for _ in range(2*self.p-1)]

  def parent(self, i):
    return (i-1)//2
  
  def left(self,i):
    return 2*i+1
  
  def right(self,i):
    return 2*i+2
  
  def get(self,i):
    return self.T[i + self.p-1]
  
  def set(self,i,value):
    k = i + self.p-1
    diff = value-self.T[k]

    while k>=0:
      self.T[k] +=diff
      k=self.parent(k)
  
  def sum_helper(self,k,lo,hi,i,j):
    if i==lo and j==hi:
      return self.T[k]

    mid = (hi-lo)//2
    if i > lo + mid:
      return self.sum_helper(self.right(k),lo+mid+1,hi,i,j)
    elif j<= lo + mid:
      return self.sum_helper(self.left(k),lo,lo+mid,i,j)
    else:
      res1 = self.sum_helper(self.right(k),lo+mid+1,hi,lo+mid+1,j)
      res2 = self.sum_helper(self.left(k),lo,lo+mid,i,lo+mid)
      return res1 + res2
    
  def sum(self,i,j):
    return self.sum_helper(0,self.p-1,2*self.p-2,i+self.p-1,j+self.p-1)


def dominance(P):
  n = len(P)
  P.sort()
  ia = IntervalAdder(n+1)
  x_count = [0 for _ in range(n+1)]
  for x,_ in P:
    x_count[x] += 1
  max_dominance = 0
  for x, y in P:
    ia.set(y,ia.get(y)+1)
    max_dominance = max(max_dominance,ia.sum(0,y-1)-x_count[x]+1)
  return max_dominance
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
