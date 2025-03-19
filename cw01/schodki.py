def binary_search(T,x):
    pass #zwraca pozycje schodka do którego dochodzi czlowiek

def suma_wys(schodki,ludzie):
    n = len(schodki)
    m=len(ludzie)
    Tab_max = [0 for _ in range(n+1)]
    Tab_max[0]=schodki[0]
    for i in range(n):
        Tab_max=max(Tab_max[i-1],schodki[i])
    s=0
    for i in range(m):
        id_max=binary_search(Tab_max,ludzie[i])
        s+=id_max
    return s

'''
O(s(n)+m*log(n))
'''