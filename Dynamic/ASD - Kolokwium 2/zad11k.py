from zad11ktesty import runtests

def kontenerowiec(T):
    
    def rek(i,p1,p2):
        nonlocal T
        n= len(T)
        if i==n-1:
            return abs(p1-p2)
        return min(rek(i+1,p1+T[i],p2),rek(i+1,p1,p2+T[i]))
    

    return rek(0,0,0)

runtests ( kontenerowiec )
    