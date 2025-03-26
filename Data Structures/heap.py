'''

Max Heap

'''

def max_heapify(arr,n,i):
    right = 2*i
    left = 2*i+1
    max_int = i
    if left<n and arr[max_int]<arr[left]:
        max_int = left
    if right<n and arr[max_int]<arr[right]:
        max_int = right
    if max_int!=i:
        arr[i],arr[max_int]=arr[max_int],arr[i]
        max_heapify(arr,n,max_int)

def build_max_heap(arr,n):
    for i in range(n//2,-1,-1):
        max_heapify(arr,n,i)
    

def max_insert(arr,x):
    arr.append(x)
    i = len(arr)-1
    while i > 0 and arr[i]>arr[(i-1)//2]:
        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
        i=(i-1)//2

def extract_max(arr):
    if len(arr) == 0:
        return 0
    max_value = arr[0]
    arr[0]=arr[-1]
    arr.pop()

    max_heapify(arr,len(arr),0)
    return max_value
    

heap = [1,4,2,5,6,7,10]

# def heap_sort(arr):
#     n = len(arr)
#     build_max_heap(arr,n)

#     for i in range(n-1,0,-1):
#         arr[0],arr[i]=arr[i],arr[0]
#         max_heapify(arr,i,0)

build_max_heap(heap,len(heap))
print(heap)
max_insert(heap,9)
print(heap)
print(extract_max(heap))
print(heap)
print("-"*20)
'''

Min Heap

'''

def min_heapify(arr,n,i):
    left = 2*i
    right = 2*i+1
    min_int = i

    if left<n and arr[min_int]>arr[left]:
        min_int = left
    if right<n and arr[min_int]>arr[right]:
        min_int = right
    if min_int!=i:
        arr[i],arr[min_int]=arr[min_int],arr[i]
        min_heapify(arr,n,min_int)


def build_min_heap(arr,n):
    for i in range(n//2,-1,-1):
        min_heapify(arr,n,i)

def min_insert(arr,x):
    arr.append(x)
    i=len(arr)-1
    while i > 0 and arr[i]<arr[(i-1)//2]:
        arr[i],arr[(i-1)//2]=arr[(i-1)//2],arr[i]
        i=(i-1)//2

def extract_min(arr):
    if len(arr) == 0:
        return None
    min_value = arr[0]
    arr[0]=arr[-1]
    arr.pop()

    min_heapify(arr,len(arr),0)
    return min_value

heap2 = [1,4,2,5,6,7,10]
build_min_heap(heap2,len(heap2))
print(heap2)
min_insert(heap2,9)
print(heap2)
print(extract_min(heap2))
print(heap2)
