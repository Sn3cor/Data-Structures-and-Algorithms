from egz3atesty import runtests

# Rozwiązanie o(nlogn)
def snow2(T,I):
    arr = []
    for a,b in I:
        arr.append((a,0))
        arr.append((b,1))
    arr.sort()
    curr = 0
    maxi = 0
    
    for _,t in arr:
        if t == 0: curr +=1
        else: curr -=1
        maxi = max(curr,maxi)
    return maxi

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow2, all_tests = True )
