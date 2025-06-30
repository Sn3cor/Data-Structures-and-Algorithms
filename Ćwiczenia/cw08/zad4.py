'''
maximin

f(i,k)= max{ min(f(j,k-1), sum(j+1,i)) | k<j<i}
f(n,k)
f(_,1) = sum(T)

O(n^3*k)
korzystając z sum prefiksowych O(n^2*k)
'''

def m(T,k):

    n = len(T)
    prefix = [0]*(n+1)

    for i in range(1,n+1): prefix[i]=prefix[i-1]+T[i-1]

    def suma(i,j):
        return prefix[j+1]-prefix[i]
    
    dp = [[None]*(k+1) for _ in range(n)]


    def minimax(i,k):
        if k==1: return suma(0,i)
        if dp[i][k] is not None: return dp[i][k]
        best = 0
        for j in range(k,i):
            best = max(best, min(minimax(j,k-1),suma(j+1,i)))
        dp[i][k] = best
        return best
    
    return minimax(n-1,k)
