def merge_sort(T,l,r):
    if l>=r:
        return
    q = (l+r)//2
    merge_sort(T,l,q)
    merge_sort(T,q+1,r)
    merge(T,l,q,r)

def merge(T,l,q,r):
    Nl = q-l+1
    Nr = r-q
    left = [0 for _ in range(Nl)]
    right = [0 for _ in range(Nr)]
    for i in range(0,Nl):
        left[i]=T[l+i]
    for j in range(0,Nr):
        right[j]=T[q+1+j]
    i=0
    j=0
    k=l

    while i<Nl and j<Nr:
        if left[i]<= right[j]:
            T[k]=left[i]
            i+=1
        else:
            T[k]=right[j]
            j+=1
        k+=1
    
    while i < Nl:
        T[k]=left[i]
        i+=1
        k+=1
    
    while j < Nr:
        T[k]=right[j]
        j+=1
        k+=1

T=[1,54,2,4,13,76,5,75,45,5,3]
merge_sort(T,0,len(T)-1)
print(T)