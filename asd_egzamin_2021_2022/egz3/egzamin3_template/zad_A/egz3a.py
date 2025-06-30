from egz3atesty import runtests

# Rozwiązanie o(nlogn)
def snow2(T,I):
    arr = []
    for a,b in I:
        arr.append((a,0))
        arr.append((b,1))
    count = 0
    maxi = 0
    arr.sort()
    
    for _,t in arr:
        if t == 0: count+=1
        else: count-=1
        maxi = max(count,maxi)

    return maxi

# Rozwiązanie o(n^2)
def snow( T, I ):
    stan = [0 for _ in range(T)]

    for start,end in I:
        for j in range(start,end+1):
            stan[j]+=1
    
    return max(stan)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow2, all_tests = True )
