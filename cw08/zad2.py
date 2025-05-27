'''
Najdłuzszy wspólny podciąg
'''

def lcs(A,B):
    n,m = len(A), len(B)
    DP = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n-1,-1,-1):
        for j in range(m-1.-1,-1):
            if A[i] == B[j]:
                DP[i][j] = DP[i+1][j+1]+1
            else:
                DP[i][j] = max(DP[i+1][j],DP[i][j+1])
    return DP[0][0]