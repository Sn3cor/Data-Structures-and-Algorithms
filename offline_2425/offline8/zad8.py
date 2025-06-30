from zad8testy import runtests

def partition(A,l,r):
    pivot = A[r]
    i=l-1

    for j in range(l,r):
        if A[j]>=pivot:
            i+=1
            A[j],A[i] = A[i],A[j]

    A[i+1],A[r]=A[r],A[i+1]

    return i+1

# def quickselect(A,l,r,k):
#     q = partition(A,l,r)
#     if q==k:
#         return A[k]
#     elif k<q:
#         return quickselect(A,l,q-1,k)
#     else:
#         return quickselect(A,q+1,r,k)

def quicksort(A,l,r):
    if l<r:
        q=partition(A,l,r)
        quicksort(A,l,q-1)
        quicksort(A,q+1,r)


def ice_cream( T ):
    n = len(T)
    _sum = 0
    quicksort(T,0,len(T)-1)
    for i in range(n):
        if(T[i]-i)<= 0: break
        _sum+= (T[i]-i)
    return _sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
