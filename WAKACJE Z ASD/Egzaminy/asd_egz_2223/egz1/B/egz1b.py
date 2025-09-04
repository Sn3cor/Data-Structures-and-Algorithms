from egz1btesty import runtests
'''
f(i,b) - minimalny koszt znalezienia sie na planecie i mając b ton paliwa
'''
def planets( D, C, T, E ):
    dp = [[float("+inf") for _ in range(E+1)] for _ in range(len(D))]
    n = len(D)
    dp[0][0] = 0
    if T[0][0] != 0:
        dest = T[0][0]
        cost = T[0][1]
        dp[dest][0] = cost
    for b in range(1,E+1):
        dp[0][b] = dp[0][b-1] + C[0]

    for i in range(1,n):
        dist = D[i] - D[i-1]
        for b in range(E+1):
            if dp[i-1][b] == float("+inf"):
                continue
            if b-dist>=0:
                dp[i][b-dist] = min(dp[i-1][b],dp[i][b-dist])
                if b-dist == 0 and T[i]!=i:
                    dest,cost = T[i]
                    dp[dest][0] = min(dp[dest][0],dp[i][0] + cost)

        for b in range(1,E+1):
            dp[i][b] = min(dp[i][b],dp[i][b-1] + C[i]) 

    return min(dp[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
