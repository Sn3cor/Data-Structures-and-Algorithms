from egz1Btesty import runtests
from collections import deque
def critical(V, E):
    graph = [[float("+inf") for _ in range(V)] for _ in range(V)]
    for u,v in E:
        graph[u][v] = 1
        
    for k in range(V):
        for u in range(V):
            for v in range(V):
                if graph[u][k] != float("+inf") and graph[k][v] != float("+inf"):
                    graph[u][v] = graph[u][k]+graph[k][v]
    ans = 0
    for u in range(V):
        for v in range(V):
            if graph[u][v] == 1:
                ans +=1
    print(graph)
    return ans


#Wzorcówka
def critical2(V,E):
    adj = [[] for _ in range(V)]
    for u,v in E:
        adj[u].append(v)

    reachability = [[False for _ in range(V)] for _ in range(V)]
    

    for start in range(V):
        visited = [False for _ in range(V)]
        visited[start] = True
        queue = deque()
        queue.append(start)
        reachability[start][start] = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    reachability[start][v] = True
                    visited[v] = True
                    queue.append(v)

    ans = 0
    for u,v in E:
        is_critical = True
        for w in range(V):
            if w == u or w == v:
                continue

            if reachability[u][w] and reachability[w][v]:
                is_critical = False
                break

        if is_critical:
            ans += 1
        
    return ans
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical2, all_tests = True)
