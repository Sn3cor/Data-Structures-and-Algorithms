from zad9testy import runtests

def trip(M):
  n = len(M)
  m = len(M[0])
  dp = [[0 for _ in range(m)] for _ in range(n)]

  def trippin(G,i,j,prev):
    
    if i < 0 or j<0 or i>=n or j >= m or G[i][j] <= prev:
      return 0
    if dp[i][j]!=0:
      return dp[i][j]
    up= 1+trippin(G,i-1,j,G[i][j])
    down = 1+trippin(G,i+1,j,G[i][j])
    right = 1+trippin(G,i,j+1,G[i][j])
    left = 1+trippin(G,i,j-1,G[i][j])

    dp[i][j] = max(up,down,right,left)
    return dp[i][j]
  
  maxi = 0
  for i in range(n):
    for j in range(m):
      dp[i][j] = trippin(M,i,j,-1)
      maxi = max(maxi,dp[i][j])

  return maxi

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
