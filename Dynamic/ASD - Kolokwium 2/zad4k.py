from zad4ktesty import runtests

def falisz ( T ):
    

    def rek(T,i,j):
        n = len(T)
        if i==n-1 and j == n-1:
            return T[n-1][n-1]
        elif i+1<n and j +1< n:
            return min(T[i][j] + rek(T,i+1,j), T[i][j] + rek(T,i,j+1))
        elif i+1>=n:
            return min(T[i][j] + float("inf"), T[i][j] + rek(T,i,j+1))
        elif j+1>=n:
            return min(T[i][j] + rek(T,i+1,j), T[i][j] + float("inf"))
    return rek(T,0,0)


def falisz(T):
    n = len(T)
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]

    dp[n-1][n-1] = 0

    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i+1>=n and j+1>=n:
                continue
            elif i+1>=n and j+1<n:
                dp[i][j] = T[i][j] + min(float("inf"),dp[i][j+1])
            elif i+1<n and j+1>=n:
                dp[i][j] = T[i][j] + min(float("inf"),dp[i+1][j])
            else:
                dp[i][j] = T[i][j] + min(dp[i+1][j],dp[i][j+1])

    return dp[0][0]

runtests ( falisz )
