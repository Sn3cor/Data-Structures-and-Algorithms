'''
Stacje benzynowe v1

Mamy drogę a->b
Traktor ma spalanie 1l1/km i pojemność baku L
na drodze są nieregularne punkty ze stacjami paliw
na początku ma tez stacje lub pełny bak

Minimalizacja liczby postoji
--------------------------------

'''
T=[0,4,6,9,12]
L=5

def traktor(T,L,b):
    n=len(T)
    f = L
    T.append(b)
    c = 0
    for i in range(n-1):
        if T[i] >=b: break
        if T[i+1]-T[i]<f:
            c+=1
            f=L
        f-= T[i+1] - T[i]
        if f < 0: return -1

    return c



'''
Stacje v2

Dla kazdej stacji podane ceny paliwa

Zaplacić jak najmniej
'''