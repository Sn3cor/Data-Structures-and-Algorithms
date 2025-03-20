def count_sort(A,k): #k = max(A)
    n=len(A)
    counters=[0]*k
    result=[0]*n

    for i in range(n):
        counters[A[i]]+=1
    
    for i in range(1,k):
        counters[i] = counters[i-1]+counters[i]

    for i in range(n-1,-1,-1):
        counters[A[i]]-=1
        result[counters[A[i]]]=A[i]

    for i in range(n):
        A[i] = result[i]