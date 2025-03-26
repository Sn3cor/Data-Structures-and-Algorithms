#Jakub Krupa
#Najpierw normalizuje tablicę, zamieniając odwrócene stringi. Następnie sortuje tablicę za pomocą heap sort i zliczam ile stringow pod rząd było takich samych
from zad1testy import runtests

def heapify(arr,n,i):
    l=2*i+1
    r=2*i
    max_int=i
    if l<n and arr[l]>arr[max_int]:
        max_int=l
    if r<n and arr[r]>arr[max_int]:
        max_int=r
    if max_int!=i:
        arr[i],arr[max_int]=arr[max_int],arr[i]
        heapify(arr,n,max_int)

def build_heap(arr,n):
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)

def heap_sort(arr):
    n=len(arr)
    build_heap(arr,n)

    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)

def normalize(T):
    for i in range(len(T)):
        if T[i] > T[i][::-1]:
            T[i] = T[i][::-1]

    return T      


def strong_string(T):
    normalized = normalize(T)
    heap_sort(normalized)
    maxi_power=1
    current_power=1
    for i in range(len(T)-1):
        if normalized[i]==normalized[i+1]:
            current_power+=1
        else:
            maxi_power = max(maxi_power,current_power)
            current_power=1
    return maxi_power

# Odkomentuj by uruchomic duze testy
runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
#runtests( strong_string, all_tests=False )
