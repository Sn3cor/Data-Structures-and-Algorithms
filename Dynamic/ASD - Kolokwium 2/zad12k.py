from zad12ktesty import runtests 

'''
f(i,k) - 

'''

def autostrada( T, k ):
    n = len(T)
    prefix = [0] * (n+1)
    for i in range(1,n+1): prefix[i] = prefix[i-1]+T[i-1]

    def suma(i,j):
        return prefix[j+1] - prefix[i]

    dp = [[None for _ in range(k+1)] for _ in range(n)]

    def F(i,k):
        if k==1: return suma(0,i)
        if dp[i][k] != None: return dp[i][k]
        best = float("+inf")
        for j in range(0,i):
            best = min(best,max(suma(j+1,i),F(j,k-1)))

        dp[i][k] = best
        return best

    #Tutaj proszę wpisać własną implementację
    return F(len(T)-1,k)

runtests ( autostrada,all_tests=False )