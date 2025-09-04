from egzP8btesty import runtests

def robot( G, P ):
    n = len(G)
    graph = [[float("+inf") for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v,w in G[u]:
            graph[u][v] = w
            graph[v][u] = w

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if graph[u][k]!=float("+inf") and graph[k][v]!=float("+inf"):
                    graph[u][v] = min(graph[u][v],graph[u][k]+graph[k][v])    

    ans = 0
    for i in range(1,len(P)):
        start = P[i-1]
        finish = P[i]
        ans += graph[start][finish]
    return ans

    
runtests(robot, all_tests = True)
