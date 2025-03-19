def heapify(arr,n,i):
    l = 2*i+1
    r = 2*i
    max_int=i
    if l<n and arr[l]>arr[max_int]:
        max_int=l
    if r<n and arr[r]>arr[max_int]:
        max_int=r
    if max_int!=i:
        arr[i],arr[max_int]=arr[max_int],arr[i]
        heapify(arr,n,max_int)

def build_max_heap(arr, n):
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)

def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr,n)

    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)


T=[1,3452,43,23,87,44,32,54,36]

heap_sort(T)
print(T)