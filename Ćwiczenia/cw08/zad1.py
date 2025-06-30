'''
Suma podzbiorów

f(i,s) = jesteśmy w stanie stworzyć sumę uzywając elementów do i-tego włącznie

'''


def suma(A,T):
    n = len(A)
    DP = [[False for _ in range(T+1)] for _ in range(n)]
    for i in range(n):
        DP[i][0] = True

    if A[0]<=T: DP[0][A[0]] = True
    for i in range(1,n):
        for s in range(T+1):
            if DP[i-1][s]:
                DP[i][s] = True
            if s>A[i] and DP[i-1][s-A[i]]:
                DP[i][s] = True
            
    return DP[n-1][T]