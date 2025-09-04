from egzP1btesty import runtests 
import heapq
def turysta( G, D, L ):
    n= max([max(u,v) for u,v,_ in G]) + 1
    graph = [[] for _ in range(n)]
    for u,v,w in G:
        graph[u].append((v,w))
        graph[v].append((u,w))

    distances = [[float("inf") for _ in range(5)] for _ in range(n)]
    distances[D][0] = 0
    pq = []
    heapq.heappush(pq,(0,D,0))

    while pq:
        curr_dist, u, status = heapq.heappop(pq)
        if curr_dist > distances[u][status]:
            continue
        for v,w in graph[u]:
            if status + 1 > 4:
                continue

            if curr_dist + w  < distances[v][status+1]:
                distances[v][status+1] = curr_dist + w
                heapq.heappush(pq,(distances[v][status+1], v, status+1))

    return distances[L][4]

runtests ( turysta )