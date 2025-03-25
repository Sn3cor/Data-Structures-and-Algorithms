def radix_sort(A):
    max_arr = max(A)
    exp = 1 
    while max_arr//exp >=1:
        countingSort(A,exp)
        exp *= 10

def countingSort(arr,exp):
    n = len(arr)
    result = [0]*n
    count = [0]*10
    for i in range(0,n):
        index = arr[i]//exp
        count[index%10]+=1

    for i in range(1,10):
        count[i]+= count[i-1]

    for i in range(n-1,-1,-1):
        index=arr[i]//exp
        result[count[index%10]-1]=arr[i]
        count[index%10]-=1

    for i in range(0,n):
        arr[i]=result[i]

T=[34,24,12,65,23,44,11,2,5,9]
radix_sort(T)
print(T)