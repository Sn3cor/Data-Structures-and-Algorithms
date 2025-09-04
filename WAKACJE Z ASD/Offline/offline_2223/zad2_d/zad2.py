from zad2testy import runtests

def merge(T,l,q,r):
    left = T[l:q+1]
    right = T[q+1:r+1]
    i=j=0
    k=l
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            T[k]=left[i]
            i+=1
        else:
            T[k]=right[j]
            j+=1
        k+=1

    while i<len(left):
        T[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        T[k]=right[j]
        j+=1
        k+=1

def merge_sort(T,l,r):
    if l>=r:
        return 
    q=(l+r)//2
    merge_sort(T,l,q)
    merge_sort(T,q+1,r)
    merge(T,l,q,r)

def snow( S ):
    merge_sort(S,0,len(S)-1)

    days=0
    total=0

    for i in range(len(S)-1,-1,-1):
        if S[i]-days<0:
            break
        
        total+=S[i]-days
        days+=1
    return total

S = [1, 7, 3, 4, 1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
