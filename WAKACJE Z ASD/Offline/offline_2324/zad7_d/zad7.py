from zad7testy import runtests

def maze( L ):
    n = len(L)
    dp = [[float('-inf') for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        if L[i][0] != '#':
            dp[i][0] = i
        else: break

    for j in range(1,n):
        last = float("-inf")
        for i in range(n):
            if L[i][j]!= '#':
                dp[i][j] = max(max(dp[i][j-1]+1,last+1),dp[i][j])
                last = max(dp[i][j-1]+1,last+1)
            else: 
                last =float('-inf')
        last = float("-inf")
        for i in range(n-1,-1,-1):
            if L[i][j]!= '#':
                dp[i][j] = max(max(dp[i][j-1]+1,last+1),dp[i][j])
                last = max(dp[i][j-1]+1,last+1)
            else: 
                last = float('-inf')

    return dp[-1][-1] if dp[-1][-1] != float("-inf") else -1
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
