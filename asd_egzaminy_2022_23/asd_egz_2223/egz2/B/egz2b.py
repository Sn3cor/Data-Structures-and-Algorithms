from egz2btesty import runtests
'''
F(i,j) - minimalna suma odległości ze wszystkich mozliwych, przy zalozeniu ze wiezowiec X[i] dostaje parking Y[j]
F(0,0) = abs(X[i]-Y[j])

F(0,j) = min(F(0,j-1), abs(X[i]-Y[j]))

Zasada bezpieczeństwa: w zagniezdzonej pętli robimy od i do m

F(i,j) = min (F(i-1,j-1) + abs(X[i]-Y[j]), F(i,j-1))
''' 
def parking(X,Y):
  n = len(X)
  m = len(Y)

  dp = [[float("inf") for _ in range(m)] for _ in range(n)]

  dp[0][0] = abs(X[0]-Y[0])

  for j in range(1,m):
    dp[0][j] = min(dp[0][j-1],abs(X[0]-Y[j]))

  for i in range(1,n):
    for j in range(i,m):
      dp[i][j] = min(dp[i-1][j-1]+abs(X[i]-Y[j]), dp[i][j-1])
  return dp[n-1][m-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
