from kol1atesty import runtests
from collections import defaultdict
def g(T):
    def normalise(string):
        return string if string < string[::-1] else string[::-1]
    
    def hash(string):
        n = len(string)
        p=31
        m = int(1e9 + 7)

        hashVal = 0
        pPower = 1

        for i in range(n):
            hashVal = (hashVal + (ord(string[i]) - ord('a') + 1) * pPower) % m
            pPower = (pPower * p)

        return hashVal

    hashmap = defaultdict(lambda: 0)
    res = 0
    for i in range(len(T)):
        T[i] = normalise(T[i])
        key = hash(T[i])
        hashmap[key] += 1
        res = max(res,hashmap[key])

    return res


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
