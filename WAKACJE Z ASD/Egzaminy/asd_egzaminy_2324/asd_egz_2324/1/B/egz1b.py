from egz1btesty import runtests
#   f(i,k) - maksymalna suma podciągu kończącego się na i-tym elemencie oraz przy wykluczeniu k liczb
#   f(0,0) = T[0]
#   f(0,1) = 0
#   f(0,2..k) = -inf
def kstrong(T,k):
    n= len(T)
    dp = [[None for _ in range(k+1)] for _ in range(n)]
    dp[0][0] = T[0]
    dp[0][1] = 0
    for ki in range(2,k+1):
        dp[0][ki] = float("-inf")

    for i in range(1,n):
        for ki in range(k+1):
            if ki == 0:
                dp[i][ki] = max(dp[i-1][ki] + T[i], T[i])

            else:
                dp[i][ki] = max(dp[i-1][ki]+T[i],dp[i-1][ki-1])
            
    ans = 0
    for i in range(n):
        for ki in range(k+1):
            ans = max(ans,dp[i][ki])
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
