from zad2testy import runtests


def breaking(G):
    n = len(G)
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j]:
                graph[i].append(j)

    low = [-1] * n
    disc = [-1] * n
    visited = [False] * n
    parent = [None] * n
    time = 0
    art = [[] for _ in range(n)]

    def DFS_vis(G,u):
        nonlocal time
        children = 0
        time +=1
        low[u] = disc[u] = time
        visited[u] = True

        for v in graph[u]:
            if not visited[v]:
                children+=1
                parent[v] = u
                DFS_vis(G,v)
                low[u] = min(low[u],low[v])

                if parent[u] is not None and low[v] >= disc[u]:
                    art[u].append(v)

            elif v != parent[u]:
                low[u] = min(low[u],disc[v])

        
        if parent[u] is None and children >= 2:
            art[u] = graph[u][:]
    
    for u in range(n):
        if not visited[u]:
            DFS_vis(graph,u)

    res = 0
    idx = None
    for i in range(n):
        if res < len(art[i]):
            res = len(art[i])
            idx = i
    
    # tu prosze wpisac wlasna implementacje
    return idx


runtests( breaking )