def partition(A,p,r):
    x=A[r][0]
    i=p-1

    for j in range(p,r):
        if A[j][0]>=x:
            i+=1
            A[j],A[i]=A[i],A[j]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quick_select(A,p,r,k): #k is an index that we want to select after sorting
    q = partition(A,p,r)
    if k == q:
        return A[k]
    elif k < q:
        return quick_select(A,p,q-1,k)
    else:
        return quick_select(A,q+1,r,k)
    
#T=[1,2,3,4,5,6,7,8]
finish_times = [[14, 0], [13, 1], [12, 2], [7, 3], [16, 4], [10, 5], [11, 6], [6, 7]]
select = quick_select(finish_times,0,len(finish_times)-1,0)
print(select)
