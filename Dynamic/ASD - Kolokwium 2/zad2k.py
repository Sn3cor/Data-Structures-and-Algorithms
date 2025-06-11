from zad2ktesty import runtests
'''
f(a,b)
f(a,a) = true
f(a+1,b) t[a]==t[b] - True else False

f
'''
def palindrom( S ):
    n = len(S)
    dp = [[None for _ in range(n)] for _ in range(n)]
    def rek(i,j):
        nonlocal dp, S
        if dp[i][j] != None: return dp[i][j]
        if i==j:
            dp[i][j] = True
        elif i+1 == j:
            dp[i][j] =( S[i]==S[j])
        else:
            if S[i] != S[j]:
                dp[i][j] = False
            else:
                dp[i][j] = rek(i + 1, j - 1)
        return dp[i][j]
    

    for i in range(n):
        for j in range(i, n):
            rek(i, j)
    
    pali = ""
    maxi=0
    for a in range(n):
        for b in range(a+1,n):
            if dp[a][b] and b-a+1>maxi:
                maxi = b-a+1
                pali = S[a:b+1]
                
    return pali

runtests ( palindrom )