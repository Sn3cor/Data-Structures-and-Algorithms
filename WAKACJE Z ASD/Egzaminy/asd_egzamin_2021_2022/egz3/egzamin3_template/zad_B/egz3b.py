from egz3btesty import runtests

def maze( L ):
    n = len(L)
    dp = [[float("-inf") for _ in range(n)]for _ in range(n)]
    dp[0][0] = 0

    
    for j in range(1,n):
        if L[j][0]!= "#":
            dp[j][0] = dp[j-1][0]+1

    for i in range(1,n):
        last_val = float("-inf")
        for j in range(n):
            if L[j][i] != "#":
                dp[j][i] = max(max(dp[j][i-1]+1,last_val+1), dp[j][i])
                last_val = max(dp[j][i-1]+1,last_val+1)
            else:
                last_val = float("-inf")

        last_val = float("-inf")
        for j in range(n-1,-1,-1):
            if L[j][i] != "#":
                dp[j][i] = max(max(dp[j][i-1]+1,last_val+1), dp[j][i])
                last_val = max(dp[j][i-1]+1,last_val+1)
            else:
                last_val = float("-inf")

    return dp[n-1][n-1] if dp[-1][-1] != float("-inf") else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
