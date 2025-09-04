from egzP4atesty import runtests 

def bisect_left(arr,x,l,r):
    while l < r:
        mid = l + (r-l)//2
        if x > arr[mid]:
            l = mid + 1
        else:
            r = mid

    return l

def mosty ( T ):

    T.sort(key = lambda x: x[0])
    ans = []

    ans.append(T[0][1])

    for i in range(1,len(T)):

        if T[i][1] > ans[-1]:
            ans.append(T[i][1])

        else:
            idx = bisect_left(ans,T[i][1],0,len(ans)-1)
            ans[idx] = T[i][1]

    return len(ans)



runtests ( mosty, all_tests=True )