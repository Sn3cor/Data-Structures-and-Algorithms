from random import random

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while arr[j]>key and j>0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    


def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        bi = int(n*num)
        buckets[bi].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    idx = 0
    for bucket in buckets:
        for num in bucket:
            arr[idx]=num
            idx+=1

arr = [random() for _ in range(10)]
print(arr)
bucket_sort(arr)
print(arr)