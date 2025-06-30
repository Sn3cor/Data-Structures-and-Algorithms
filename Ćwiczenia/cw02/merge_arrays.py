#Given two sorted arrays of integers return one merged array

def merge(arr1:list[int] ,arr2: list[int])-> list[int]:
    n,m = len(arr1),len(arr2)
    if n>1:
        merge(arr1[:n//2],arr1[n//2:])
    if m>1:
        merge(arr2[:m//2],arr2[m//2:])
    
    result = [0 for _ in range(n+m)]
    i=j=k=0

    while i<n and j<m:
        if arr1[i] <= arr2[j]:
            result[k]=arr1[i]
            i+=1
        else:
            result[k]=arr2[j]
            j+=1
        k+=1

    while i<n:
        result[k]=arr1[i]
        i+=1
        k+=1
    
    while j<m:
        result[k]=arr2[j]
        j+=1
        k+=1
    
    return result

arr1=[1,12,23,45,123]
arr2=[3,15,17,30,41]
print(merge(arr1,arr2))