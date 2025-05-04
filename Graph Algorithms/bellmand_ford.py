#Works for directed graphs

def get_edges(G): #for directed graph
    E = []
    for i in range(len(G)):
        for u,weight in G[i]:
            E.append((i,u,weight))
    return E


def bellman_ford(G,s):
    #initialization
    V = len(G)
    distances = [float("inf") for _ in range(V)]
    parent = [None for _ in range(V)]
    distances[s] = 0

    E = get_edges(G)
    #relax all edges

    for i in range(V-1):
        for u,v,weight in E:
            if distances[v]> distances[u]+weight:
                distances[v] = distances[u]+weight
                parent[v] = u

    for u,v,weight in E:
        if distances[v]< distances[u]+weight:
                return None
        
    return distances,parent