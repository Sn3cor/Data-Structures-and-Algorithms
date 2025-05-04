def floyd_warshall(G):
    V = len(G)
    for k in range(V):
        for u in range(V):
            for v in range(V):
                if G[u][k]!= float("inf") and G[k][v] != float("inf"):
                    G[u][v] =min(G[u][v], G[u][k] + G[k][v])

    return G