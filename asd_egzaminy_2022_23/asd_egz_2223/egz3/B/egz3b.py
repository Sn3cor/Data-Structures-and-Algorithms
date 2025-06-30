from egz3btesty import runtests

# class SegmentTree:
#   def __init__(self,n):
#     self.p = 1

#     while self.p<n:
#       self.p*=2

#     self.T=[0 for _ in range(2*self.p-1)]

#   def parent(self, i):
#     return (i-1)//2
  
#   def left(self,i):
#     return 2*i+1
  
#   def right(self,i):
#     return 2*i+2
  
#   def get(self,i):
#     return self.T[i + self.p-1]
  
#   def set(self,i,value):
#     k = i + self.p-1
#     diff = value-self.T[k]

#     while k>=0:
#       self.T[k] +=diff
#       k=self.parent(k)
  
#   def query_helper(self,k,lo,hi,i,j):


#     if i==lo and j==hi:
#       return self.T[k]

#     mid = (hi-lo)//2
#     if i > lo + mid:
#       return self.sum_helper(self.right(k),lo+mid+1,hi,i,j)
#     elif j<= lo + mid:
#       return self.sum_helper(self.left(k),lo,lo+mid,i,j)
#     else:
#       res1 = self.sum_helper(self.right(k),lo+mid+1,hi,lo+mid+1,j)
#       res2 = self.sum_helper(self.left(k),lo,lo+mid,i,lo+mid)
#       return res1 + res2
    
#   def query(self,i,j):


# Rozwiązanie o(n^2)
def uncool( P ):
  def contained_or_disjoined(a1,b1,a2,b2):
    #Zawieranie się
    if (a1 <= a2 and b1 >= b2) or (a2 <= a1 and b2 >= b1):
      return True
    #Rozłączność
    if b1 < a2 or b2 < a1:
      return True
    return False
  
  for i in range(len(P)):
    a1,b1, = P[i]
    for j in range(i+1,len(P)):
      if i!=j:
        a2,b2 = P[j]
        if not contained_or_disjoined(a1,b1,a2,b2):
          return i,j

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = False )
