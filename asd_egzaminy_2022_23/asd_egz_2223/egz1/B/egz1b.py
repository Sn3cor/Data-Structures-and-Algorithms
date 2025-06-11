from egz1btesty import runtests
'''
f(i,b) - minimalny koszt znalezienia sie na planecie i mając b ton paliwa
'''
def planets( D, C, T, E ):

    dp = [[float("inf") for _ in range(E+1)] for _ in range(len(D))]
    dp[0][0] = 0

    for e in range(1,E+1):
        dp[0][e] = e*C[0]

    T_new = [[] for _ in range(len(D))]

    for i in range(len(T)):
        if T[i][0] != i:
            T_new[T[i][0]].append((i,T[i][1]))

    for i in range(1,len(D)):
        distance = D[i]-D[i-1]
        for e in range(E-distance+1):
            dp[i][e] = dp[i-1][e+distance]
            if e == 0 and T_new[i]:
                for s,c in T_new[i]:
                    dp[i][0] = min(dp[i][0], dp[s][0] + c)

        for e in range(1,E+1):
            dp[i][e] = min(dp[i][e-1] + C[i],dp[i][e])
            
    return min(dp[len(D)-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
