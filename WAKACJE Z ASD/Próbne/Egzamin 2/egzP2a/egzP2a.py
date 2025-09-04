from egzP2atesty import runtests 
from collections import deque
import random
def partition(arr,l,r):
    rand = random.randint(l,r)
    arr[rand],arr[r] = arr[r],arr[rand]
    pivot = arr[r][1]
    i=l-1

    for j in range(l,r):
        if arr[j][1] <= pivot:
            i+=1
            arr[j],arr[i] = arr[i],arr[j]

    arr[i+1],arr[r] = arr[r],arr[i+1]
    return i+1

def quickselect(arr,l,r,k):
    while l <= r:
        q = partition(arr,l,r)
        if q == k:
            break
        elif k<q:
            r = q-1
        else:
            l = q+1
    return

def zdjecie(T, m, k):
    
    queues = [None for _ in range(m)]
    start = 0

    for i in range(m):
        size = k + i
        if i < m-1:
            quickselect(T,start,len(T) - 1,start + size -1)
            queues[i] = deque(T[start:start+size])
        else:
            queues[i] = deque(T[start::])
        start += size
    
    ans = []
    i = m-1
    while queues[m-1]:
        if i < 0:
            i = m-1
        if queues[i]:
            person = queues[i].popleft()
            ans.append(person)
            i-=1
        else:
            i-=1

    for i in range(len(T)):
        T[i] = ans[i]
    return None


runtests ( zdjecie, all_tests=True )