from kol1btesty import runtests
from collections import defaultdict

def f(T):
    counter = defaultdict(lambda:0)
    res = 0
    for word in T:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch)-ord('a')]+=1
        hash = tuple(freq)
        counter[hash] +=1
        res = max(res,counter[hash])
    # tu prosze wpisac wlasna implementacje
    return res


runtests( f, all_tests=True )
