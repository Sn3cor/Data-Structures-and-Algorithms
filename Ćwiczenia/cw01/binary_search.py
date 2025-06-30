#Wyszukiwanie najmniejszego brakującego elementu
def search(T):
    n=len(T)
    l=0
    r=n-1
    while l<r:
        m=(l+r)//2
        if m==T[m]:
            l=m+1
        else:
            r=m
    return l+1

