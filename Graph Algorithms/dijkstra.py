import heapq

def dijkstra(G,s,t):
    V = len(G)

    distance = [float("inf") for _ in range(V)]
    parent = [None for _ in range(V)]
    distance[s] = 0
    minheap = [(s,0)]

    while minheap:
        u,curr_distance = heapq.heappop(minheap)
        
        if u == t: break
        for v,v_weight in G[u]:
            if distance[v] > curr_distance + v_weight:
                distance[v] = distance[u] + v_weight
                parent[v] = u
                heapq.heappush(minheap, (v,distance[v]))

    return parent,distance


graph = [
    [(1, 2), (3, 5)],     # 0: A → B (2), D (5)
    [(2, 1), (3, 3)],     # 1: B → C (1), D (3)
    [(4, 2)],             # 2: C → E (2)
    [(2, 1), (4, 2)],     # 3: D → C (1), E (2)
    []                    # 4: E (no outgoing edges)
]

print(dijkstra(graph,0,4))