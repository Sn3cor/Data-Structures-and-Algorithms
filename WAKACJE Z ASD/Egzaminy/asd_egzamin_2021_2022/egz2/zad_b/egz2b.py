from egz2btesty import runtests
#dp[i] - maksymalna ilość sztabek w i-tej komnacie
def magic( C ):
    dp = [float("-inf") for _ in range(len(C))]
    dp[0] = 0
    for i in range(len(C)):
        if dp[i] == float("-inf"):
            continue
        chest = C[i][0]
        for j in range(1,4):
            if C[i][j][1] == -1:
                continue

            need = C[i][j][0]
            dest = C[i][j][1]

            if chest - need <= 10 and chest >= need:
                dp[dest] = max(dp[dest],chest - need + dp[i])
            elif need >= chest:
                if chest + dp[i] >= need:
                    dp[dest] = max(dp[dest],dp[i] - (need - chest))

    return dp[len(C)-1] if dp[len(C)-1] != float("-inf") else -1
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
