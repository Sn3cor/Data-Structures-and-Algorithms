#Sprawdzić czy graf jest dwudzielny repr macierzowa

def is_bipartite(G):
    V=len(G)
    color = [None for _ in range(V)]
    Q = [0]
    ptr=0
    color[0]=False
    while ptr < len(Q):
        p=Q[ptr]
        ptr+=1
        for i in range(V):
            if G[p][i] == 1:
                if color[i] == None:
                    color[i]=not color[p]
                if color[i]==color[p]:
                    return False
    return True
