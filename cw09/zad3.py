'''
Głodna zaba
T - tablica energii

f(i,e) minimalna ilość skoków do końca będąc na polu i mając e energii

f(i,e) = min(f(i+1,e+T[i]-1),...,f(i+e+T[i],0))+1

'''

def zaba(T):
    n = len(T)
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[n-1][i] = 0

    for i in range(n-2,-1,-1):
        for e in range(n-1,-1,-1):
            for j in range(i, min(i+T[i]+e,n)):
                if e-j+i+T[i] <0:
                    continue
                dp[i][e] = min (dp[i][e], dp[j][e-j+i+T[i]]+1)

    return dp[0][0]