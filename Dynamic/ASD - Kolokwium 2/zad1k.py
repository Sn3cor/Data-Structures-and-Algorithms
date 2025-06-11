from zad1ktesty import runtests
'''
f(i,j) -  podciąg od i do j zawierający największą róznicę 0 i 1

f(i,j) = dp[a][b-1]-1 or dp[a][b-1]+1
'''
def roznica( S ):
    n = len(S)
    dp = [[0 for _ in range(n)]for _ in range(n)]

    for a in range(n):
        dp[a][a] = 1 if S[a] == '0' else -1
        for b in range(a+1,n):
            dp[a][b] = (dp[a][b-1] -1) if S[b]=='1' else (dp[a][b-1]+1)

    maxi = -1
    for a in range(n):
        for b in range(a+1,n):
            maxi = max(maxi,dp[a][b])

    return maxi
runtests ( roznica )