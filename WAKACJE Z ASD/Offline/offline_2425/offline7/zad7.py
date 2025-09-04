from zad7testy import runtests

#dp[i][r] - minimalna liczba drzew do wycięcia aby po rozwazeniu i drzew uzyskac sume modulo 7

def orchard(T, m):
 n = len(T)
 dp = [[float("+inf") for _ in range(m)] for _ in range(n+1)]
 dp[0][0] = 0

 for i in range(1,n+1):
  for r in range(m):
   if dp[i-1][r] != float("+inf"):
    new_r = (r+T[i-1])%m
    dp[i][new_r] = min(dp[i][new_r],dp[i-1][r])
    
    dp[i][r] = min(dp[i][r], dp[i-1][r] + 1)

 return dp[n][0]
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
