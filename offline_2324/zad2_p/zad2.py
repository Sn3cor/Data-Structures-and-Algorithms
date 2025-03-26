from zad2testy import runtests
#Algorytm iteruje po tablicy T i wykonuje w kadym mozliwym okienku o dlugosci p quick_select. 
#W ten sposób wyszukujemy k-ty największy element w oknie. 
#Następnie sumujemy wybrane elementy
#Złozonosc obliczeniowa O(p*(n-p+1))
#Złozonosc pamięciowa O(p)
def partition(T,p,r):
    x=T[r]
    i=p-1

    for j in range(p,r):
        if T[j]<=x:
            i+=1
            T[j],T[i]=T[i],T[j]
    T[i+1],T[r]=T[r],T[i+1]
    return i+1
    
def quick_select(T,p,r,k):
    q=partition(T,p,r)
    if k==q: return T[q]
    elif k<q: return quick_select(T,p,q-1,k)
    else: return quick_select(T,q+1,r,k)

def ksum(T, k, p):
    sum = 0
    n=len(T)
    for i in range(n-p+1):
        el = quick_select(T[i:i+p],0,p-1,p-k)
        sum+=el
    return sum



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
