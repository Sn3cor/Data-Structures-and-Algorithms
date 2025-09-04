from egz1Atesty import runtests

def battle(P,K,R):
    # tu prosze wpisac wlasna implementacje
    n = len(K)
    m = len(P)
    field = [None for _ in range(4*n+4*m+1)]
    for i in range(m):
        field[P[i]] = ('p',P[i],0) #rodzaj,pozycja,zasieg(tylko dla katapult)

    for i in range(n):
        field[K[i]] = ('k',K[i],R[i])

    cat_stack = []
    
    count = 0
    for i in range(len(field)):
        if field[i] == None:
            continue
        if field[i][0] == 'k':
            cat_stack.append(field[i])
        elif field[i][0] == 'p':
            if not cat_stack:
                continue
            _,position,cat_range = cat_stack[-1]
            distance = i-position
            while distance > cat_range:
                cat_stack.pop()
                if not cat_stack:
                    break
                _,position,cat_range = cat_stack[-1]
                distance = i-position
                
            if cat_stack:
                count+=1
                cat_stack.pop()

    return count

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( battle, all_tests=True )
