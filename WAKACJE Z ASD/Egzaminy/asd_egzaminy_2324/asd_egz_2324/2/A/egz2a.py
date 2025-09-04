from egz2atesty import runtests
#dp[i][j] - minimalny koszt połączenia wejść od i do j
#dp[i][i+2] = +inf bo zostawimy jedeno wejśćie
#dp[i][i+1] = 1+ abs(T[i]-T[i+1])
#dp
def wired(T):
    n = len(T)
    dp = [[None for _ in range(n)] for _ in range(n)]
    
    def helper(i,j):
        if dp[i][j] is not None:
            return dp[i][j]
        elif i == j or i+2 == j:
          return float("+inf")
    
        elif i+1 == j:
          return abs(T[i+1] - T[i]) + 1
    
        elif j<i:
          return 0

        curr = float("+inf")
        for k in range(i,j,2):
            curr = min(curr,helper(i,k-1) + helper(k+1,j-1) + 1 + abs(T[k]-T[j]))
        dp[i][j] = curr
        return dp[i][j]
    
    return helper(0,n-1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = False )
