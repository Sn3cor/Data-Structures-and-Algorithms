from egz1atesty import runtests

def snow( S ):
    S.sort(reverse = True)
    ans = 0
    for i in range(len(S)):
        if S[i] - i >0:
            ans  = ans + S[i] - i

    # tu prosze wpisac wlasna implementacje
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
