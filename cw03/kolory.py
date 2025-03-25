#tablica kolorow oznaczonych cyframi; znalezc najmniejszy przedzial tak zeby kazdy kolor byl w nim zawarty
#trzymamy liczniki i jak wszystkie kolory są to skracamy gąsienice a następnie odpowiednio rozszerzamy tak aby znowu miec kolory
#O(n+k)
def min_colors(T,k):
    counters=[0 for _ in range(k+1)]
    mini_size = float("inf")
    start = 0
    end=0
    l=0
    r=len(T)-1
    i=0
    j=0
    while j < len(T):
        counters[T[j]]+=1
        flag=True
        for n in range(1,len(counters)):
            if counters[n]<1:
                j+=1
                flag=False
                break
        if flag:
            if j-i+1<mini_size:
                start=i
                end=j
                mini_size = j-i+1
            counters[T[i]]-=1
            i+=1

    return start,end,mini_size

T=[1,2,4,1,2,4,3,2,2,1,1,2,1]
print(min_colors(T,4))

        
        
