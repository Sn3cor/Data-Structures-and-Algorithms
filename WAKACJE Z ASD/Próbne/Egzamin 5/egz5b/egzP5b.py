from egzP5btesty import runtests 

def koleje ( B ):
    new_B = set(B)
    n = max([max(u,v) for u,v in B]) + 1
    graph = [[] for _ in range(n)]
    for u,v in new_B:
        graph[u].append(v)
        graph[v].append(u)

    time = 0
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    low = [float("inf") for _ in range(n)]
    discovery = [0 for _ in range(n)]
    points = [False for _ in range(n)]

    def DFS_visit(G,u):
        nonlocal time
        visited[u] = True
        time += 1
        low[u] = discovery[u] = time
        children = 0
        for v in G[u]:
            if not visited[v]:
                children+=1
                parent[v] = u
                DFS_visit(G,v)
                low[u] = min(low[u],low[v])

                if parent[u] is not None and low[v] >= discovery[u]:
                    points[u] = True

            elif v != parent[u]:
                low[u] = min(low[u],discovery[v])

        if parent[u] is None and children >= 2:
            points[u] = True
        

    for v in range(n):
        if not visited[v]:
            DFS_visit(graph,v)

    # print(points)
    return points.count(True)

runtests ( koleje, all_tests=True )