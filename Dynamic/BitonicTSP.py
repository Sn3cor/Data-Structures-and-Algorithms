'''
Bitoniczny Problem Komiwojazera

Miasta to punkty w przestrzeni R^2
Odległości są zadane euklidesowo
Najpierw poruszamy się "z lewa na prawo"
a potem "z prawa na lewo"

I Podejście z wykładu - rekurencja ze memoizacją

1. Funkcja

f(i,j) - minimalna suma kosztów ścieek z miasta x_0 do miasta x_i oraz z x_0 do x_j,
         które są rozłączne uzywają wszystkich miast x_0,...,x_j.

2. Zapis rekurencyjny

a) i<j-1

f(i,j) = f(i,j-1) + d(x_j-1, x_j)

b) i=j-1

f(i,j) = min{ f(k,j-1) + d(x_k,x_j) | i<=k<j-1 }

3. Implementacja
'''
from random import randint
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def BitonicTSP(A,D):

    n = len(A)
    F = [[float("+inf")]*n for i in range(n)]
    F[0][1] = D[0][1]

    def tspf(i,j,F,D):
        if F[i][j] != float("+inf"): return F[i][j]
        if i==j-1:
            best = float("+inf")
            for k in range(j-1):
                best = min(best, tspf(k,j-1,F,D) + D[k][j])
            F[j-1][j] = best # F[i][j] = best

        else:
            F[i][j] = tspf(i,j-1,F,D) + D[j-1][j]

        return F[i][j]
    
    for j in range(2, n):
        for i in range(j):
            tspf(i, j, F, D)

    best = float("+inf")
    for i in range(n-1):
        best = min(best, F[i][n-1] + D[i][n-1])
    F[n-1][n-1] = best

    return F[n-1][n-1]

def distance(x_1,y_1,x_2,y_2):
    return ((x_2-x_1)**2 + (y_2-y_1)**2)**(1/2)

'''
II Podejście iteracyjne

Implementacja
'''

def BitonicTSP_iter(A,D):
    n = len(A)
    F = [[0] * n for i in range(n)]
    F[0][1] = D[0][1]

    for j in range(2,n):

        # W tej pętli cały czas jest spełniony warunek i<j-1
        # dlatego realizujemy działanie z podpunktu a)
        for i in range(j-1):
            F[i][j] = F[i][j-1] + D[j-1][j]
        
        # Po wyjściu z pętli i=j-1
        # dlatego rozpoczynamy działanie z podpunktu b)
        F[j-1][j] = F[0][j-1] + D[0][j] # incjalizacja dla k=0

        for k in range(1,j-1): 
            # Optymalizujemy ściezkę, szukając takiej kombinacji z dostępnych miast,
            # aby znaleźć takie ściezki zeby suma ich długości była minimalna 
            F[j-1][j] = min(F[j-1][j], F[k][j-1] + D[k][j])

    F[n-1][n-1] = F[n-2][n-1] + D[n-2][n-1] # Dodajemy ostatni krok do zamknięcia ścieki

    return F[n-1][n-1] # Zwracamy wynik




###################################
#### TESTOWANIE
###################################


A = [Point(0,0) for _ in range(7)]

# for i in range(len(A)):
#     A[i].x = randint(0,10)
#     A[i].y = randint(0,10)

A = [
    Point(0, 0),
    Point(1, 3),
    Point(2, 1),
    Point(3, 4),
    Point(4, 0),
    Point(5, 2)
]

A = sorted(A, key=lambda k: k.x)

D = [[distance(A[i].x,A[i].y,A[j].x,A[j].y) for j in range(len(A))] for i in range(len(A))]

print(BitonicTSP_iter(A,D))
