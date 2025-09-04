from egzP6atesty import runtests 
 
def partition(A,p,r):
    x=A[r]
    i=p-1

    for j in range(p,r):
        if A[j]>=x:
            i+=1
            A[j],A[i]=A[i],A[j]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quick_select(A,p,r,k):
    q = partition(A,p,r)
    if k == q:
        return A[k]
    elif k < q:
        return quick_select(A,p,q-1,k)
    else:
        return quick_select(A,q+1,r,k)


def google ( H, s ):
    n = len(H)
    values = []

    for i,string in enumerate(H):
        length = len(string)
        power = 0
        for ch in string:
            if 'a'<=ch<='z':
                power +=1

        values.append((length,power,i))

    ans = quick_select(values,0,n-1,s-1)
    return H[ans[2]]


runtests ( google, all_tests=True )