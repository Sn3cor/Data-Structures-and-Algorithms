def DFS(G):
    def DFSVisit(G,vertex):
        nonlocal visited, time, finish_times
        visited[vertex] = True
        time +=1
        for nb in G[vertex]:
            if not visited[nb]:
                DFSVisit(G,nb)

        time += 1
        finish_times[vertex] = time


    V = len(G)
    time = 0
    finish_times = [0 for _ in range(V)]
    visited = [False for _ in range(V)]

    for vertex in range(V):
        if not visited[vertex]:
            DFSVisit(G,vertex)

    return finish_times

def SCC(G):
    V=len(G)
    finish_times= DFS(G)
    sorted_vertices = sorted(range(V),key = lambda x: finish_times[x],reverse=True)

    GT = [[] for _ in range(V)]
    for vertex in range(V):
        for nb in G[vertex]:
            GT[nb].append(vertex)
    print(GT)
    gt_visited = [False for _ in range(V)]
    components = []
    
    def DFSVisit_T(GT,vertex,component):
        nonlocal gt_visited
        gt_visited[vertex] = True
        component.append(vertex)
        for nb in GT[vertex]:
            if not gt_visited[nb]:
                DFSVisit_T(GT,nb,component)

    for vertex in sorted_vertices:
        if not gt_visited[vertex]:
            component = []
            DFSVisit_T(GT,vertex,component)
            components.append(component)

    print(gt_visited,components)


graph = [[1],[2,4],[3,6],[2,7],[0,5],[6],[5,7],[7]]
#print(DFS(graph))
SCC(graph)