def insertion_sort(T):
    N = len(T)
    for i in range(1,N):
        key = T[i]
        j=i-1
        while j>0 and T[j]>key:
            T[j+1]=T[j]
            j-=1
        T[j+1]=key
    return T
