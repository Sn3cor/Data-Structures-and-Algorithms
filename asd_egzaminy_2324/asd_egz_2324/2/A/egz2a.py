from egz2atesty import runtests

#F(i,j) - rozwiązuje ten sam problem w [i,j]
#F(i,j) = min(n in {i,j-1}, F(i,n-1) + F(n+1,j-1) + 1 + abs(T[n]-T[j]) )
#F(i,i) = +inf
#F(i,i+1) = abs(T[i] - T[i+1])+1
#F(i,i+2) = +inf
#
def wired( T ):

  F = [[None for i in range(len(T))] for j in range(len(T))]

  def rek(i,j):
    nonlocal T,F
    if F[i][j] != None:
      return F[i][j]
    
    elif i == j or i+2 == j:
      return float("+inf")
    
    elif i+1 == j:
      return abs(T[i+1] - T[i]) + 1
    
    elif j<i :
      return 0
    
    current = float("+inf")

    for n in range(i,j,2):
      current = min(current, rek(i,n-1) + rek(n+1,j-1) + 1 + abs(T[n]-T[j]))

    F[i][j] = current
    return current
  # tu prosze wpisac wlasna implementacje
  out = rek(0,len(T)-1)
  return out

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = True )
