from collections import deque

def BFS(G: list[list[int]],start: int):
    V=len(G)
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]
    d = [float("inf") for _ in range(V)]
    status = deque()

    d[start] = 0
    visited[start] = True
    status.append(start)
    while status:
        u = status.popleft()
        for nb in G[u]:
            if not visited[nb]:
                visited[nb]=True
                parent[nb]=u
                d[nb] = d[u]+1
                status.append(nb)
    
    return d, visited, parent


graph = [[1,2],[0,2,3,5],[0,1,6,4],[1,5,6],[2,5,8],[1,3,4],[3,2,7],[6,8],[4,7]]

print(BFS(graph,0))