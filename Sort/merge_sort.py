inversions=0
def merge_sort(T,l,r):
    if l>=r:
        return
    q = (l+r)//2
    merge_sort(T,l,q)
    merge_sort(T,q+1,r)
    merge(T,l,q,r)

def merge(T,l,q,r):
    global inversions
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
            inversions += i
        k+=1
    
    while i < Nl:
        T[k]=left[i]
        i+=1
        k+=1
    
    while j < Nr:
        T[k]=right[j]
        j+=1
        k+=1
        inversions+=1

def local_inversions(nums):
    count=0
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]: count+=1
    return count

T1=[1,2,0]
T=[1,20,6,4,5]
print(local_inversions(T1))
merge_sort(T1,0,len(T1)-1)
print(T1)
print(inversions)
