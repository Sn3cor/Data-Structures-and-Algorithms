def solve_hamilton(G):
    V=len(G)
    order=[0 for _ in range(V)]
    for i in range(V):
        for u in G[i]:
            order[u]+=1
    
    index=1
    for i in range(V):
        if order[i]==u:
            index = i
        if order[i]==0 and index:
            return False