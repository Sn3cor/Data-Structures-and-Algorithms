from zad9testy import runtests
'''
f(i,used) - minimalny koszt dojechania do itego parkingu pod warunkiem zuzycia/niezuzycia ciaglej jazdy, 
f(i,used) = min()

'''
def min_cost( O, C, T, L ):
    O.append(0)
    C.append(0)
    O.append(L)
    C.append(0)

    parkingi = [(O[i],C[i]) for i in range(len(O))]
    parkingi.sort(key=lambda x: x[0])

    dp = [[float('inf') for _ in range(2)] for _ in range(len(parkingi))]
    dp[0][0] = 0

    
    for i in range(len(parkingi)):
        for j in range(i+1,len(parkingi)):
            dist = abs(parkingi[i][0]-parkingi[j][0])
            if dist > 2*T: break
            elif dist <= T:
                dp[j][0] = min(dp[j][0],dp[i][0]+parkingi[i][1])
                dp[j][1] = min(dp[j][1],dp[i][1]+parkingi[i][1])
            elif dist <= 2*T:
                dp[j][1] = min(dp[j][1],dp[i][0]+parkingi[i][1])

        

    # tu prosze wpisac wlasna implementacje
    return min(dp[-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = False )
