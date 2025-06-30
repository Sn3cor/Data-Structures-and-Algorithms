'''
Czarny las

f(i) = maksymalna suma kosztów do i-tego drzewa nie biorąc dwóch drzew pod rząd

f(i) = max(f(i-1),F(i-2)+T[i])
'''


def blackForest(T):
    n=len(T)
    F = [0 for _ in range(n)]
    F[0]=T[0] 
    F[1] = max(F[0],T[1])
    
    for i in range(2,len(T)):
        F[i] = max(F[i-1],F[i-2]+T[i])

    return F[-1]


print(blackForest([1, 0, 8, 0, 3, 0, 4, 0, 5, 0, 2]))