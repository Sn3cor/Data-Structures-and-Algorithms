def euler_cycle(G,s):
    def euler_visit(G,u):
        nonlocal V,euler
        while index[u]<V:
            v = index[u]
            index[u]=v+1
            #nwm czy dobrze
            if G[u][v]>0:
                G[u][v],G[v][u]=0,0
                euler_visit(G,v)
                euler.append(u)



    V = len(G)
    index = [0 for _ in range(V)]
    euler = []
    for i in range(V):
        if sum(G[i])%2 != 0:
            return None
    
    euler.append(s)
    euler_visit(G,s)
    return euler
