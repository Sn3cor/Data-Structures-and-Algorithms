from zad3testy import runtests
from collections import deque
def longer( G, s, t ):
    def bfs_with_count(G,s):
        distance = [None for _ in range(len(G))]
        count = [0 for _ in range(len(G))]
        distance[s] = 0
        count[s] = 1
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for nb in G[u]:
                if distance[nb] is None:
                    distance[nb] = distance[u]+1
                    count[nb] = count[u]
                    queue.append(nb)
                elif distance[nb] == distance[u] + 1:
                    count[nb] += count[u]
        return distance,count
    
    dist_s, count_s = bfs_with_count(G,s)
    dist_t, count_t = bfs_with_count(G,t)

    if dist_s[t] is None: return None

    total_paths = count_s[t]
    for u in range(len(G)):
        for v in G[u]:
            if u<v:
                if dist_s[u] + dist_t[v]+1 == dist_s[t]:
                    if count_s[u] * count_t[v] == total_paths:
                        return (u,v)
                if dist_s[v] + dist_t[u]+1 == dist_s[t]:
                    if count_s[v] * count_t[u] == total_paths:
                        return (v,u)
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
