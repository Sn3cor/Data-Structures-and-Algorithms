def _2sum(T,x): #zlozonosc s(n)+n, gdzie s(n) zlozonosc sortowania
    #T jest posortowane
    l,r=0,len(T)
    while l<=r:
        if T[l]+T[r]==x:
            return T[l],T[r]
        elif T[l]+T[r]>x:
            r-=1
        else:
            l+=1
    return None

'''
3sum -> robimy 2sum dla kazdel liczby -> O(n^2)


Znalezc prostą ktora przechodzi przez 3 punkty na plaszczyznie docelowo n^2 zlozonosc
'''