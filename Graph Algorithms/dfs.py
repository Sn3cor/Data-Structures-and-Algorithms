def DFS(G: list[list[int]]):
    time = 0
    def DFSVisit(G,start):
        nonlocal time,visited,parent
        visited[start]=True
        time += 1
        for nb in G[start]:
            if not visited[nb]:
                parent[nb]=start
                DFSVisit(G,nb)
        time += 1
    V=len(G)
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]
    for vert in range(V):
        if not visited[vert]:
            DFSVisit(G,vert)

    return parent,visited

graph = [[1,2],[0,2,3,5],[0,1,6,4],[1,5,6],[2,5,8],[1,3,4],[3,2,7],[6,8],[4,7]]
print(DFS(graph))