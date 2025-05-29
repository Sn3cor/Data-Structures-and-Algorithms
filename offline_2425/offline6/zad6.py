from zad6testy import runtests
'''
f(i,j) = minimalna suma odległości biurowców z pocycji X[0],...,X[i] do przydzielonych im działek, 
przy załozeniu ze biurowiec z pozycji X[i] ma przydzieloną działkę z pozycji Y[j]

f(i,j) = min()

f(0,j) = abs(X[0]-Y[j])
'''
def parking(X,Y):
  X.sort()
  Y.sort()
  m,n = len(Y), len(X)
  F = [[float("inf") for _ in range(m)] for _ in range(n)]

  F[0][0] = abs(X[0]-Y[0])
  for j in range(1,m):
    F[0][j] = min(F[0][j-1], abs(X[0]-Y[j]))

  for i in range(1,n):
    for j in range(i,m):
      F[i][j] = min(F[i][j-1] ,F[i-1][j-1]+abs(X[i]-Y[j]))

  return F[n-1][m-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = False )
