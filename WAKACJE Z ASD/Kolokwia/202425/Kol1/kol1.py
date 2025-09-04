from kol1testy import runtests
# Jakub Krupa


def partition(A,l,r):
    x = A[r]
    i=l-1
    for j in range(l,r):
        if A[j]<x:
            i+=1
            A[j],A[i] = A[i],A[j]
    
    A[i+1],A[r] = A[r], A[i+1]
    return i+1

def quicksort(arr,l,r):
    if l<r:
        q=partition(arr,l,r)
        quicksort(arr,l,q-1)
        quicksort(arr,q+1,r)

def quickselect(A,l,r,k):
    q = partition(A,l,r)
    if q == k:
        return A[q]
    elif q > k:
        return quickselect(A,l,q-1,k)
    else:
        return quickselect(A,q+1,r,k)
        
def bucketsort(arr,m):
    buckets = [[] for _ in range(m)]
    for num in arr:
        bi = int(num)
        buckets[bi].append(num)

    for bucket in buckets:
        if bucket:
          quicksort(bucket,0,len(bucket)-1)

    idx = 0
    for bucket in buckets:
        for num in bucket:
            arr[idx] = num
            idx+=1

    return arr
def ogrodzenie(M, D, T):
    
    N = len(T)//2
    middle = quickselect(T,0,len(T)-1,N-1)
    first = bucketsort(T[:N],M) 
    second = bucketsort(T[N:],M)
    ans = first+second
  
    count = 0
    for i in range(len(ans)-1):
        j=i+1
        if ans[j]-ans[i] >= D:
            count+=1

    return count

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = True )
