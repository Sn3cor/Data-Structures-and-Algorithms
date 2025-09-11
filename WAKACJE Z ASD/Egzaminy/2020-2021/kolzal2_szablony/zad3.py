from zad3testy import runtests
import heapq
def paths(G, s, t):
    V = len(G)
    dist = [(float("inf"), float("inf")) for _ in range(V)]  # (dystans, liczba krawędzi)
    dist[s] = (0, 0)

    pq = [(0, s, 0)]  # (dystans, wierzchołek, liczba krawędzi)

    while pq:
        curr_dist, u, count = heapq.heappop(pq)
        if curr_dist > dist[u][0]:
            continue
        for v, w in G[u]:
            new_dist = curr_dist + w
            if new_dist < dist[v][0]:
                dist[v] = (new_dist, count + 1)
                heapq.heappush(pq, (new_dist, v, count + 1))

    return dist[t][1]
    
runtests( paths )


