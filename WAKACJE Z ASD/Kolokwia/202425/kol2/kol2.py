from kol2testy import runtests
import heapq

def lets_roll(start_city,flights, resorts):
    V = max([max(u,v) for u,v,_ in flights]) + 1
    graph = [[] for _ in range(V)]
    for u,v,w in flights:
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    visited_resorts = [0 for _ in range(V)]
    for r in resorts:
        visited_resorts[r] = 1
    distances = [float("inf") for _ in range(V)]
    distances[start_city] = 0
    pq = []
    heapq.heappush(pq,(0,start_city))

    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > distances[u]:
            continue
        
        if visited_resorts[u]==2:
                continue
        for v,w in graph[u]:
            
            
            if current_dist + w < distances[v]:
                distances[v] = current_dist + w
                if visited_resorts[v] == 1:
                    visited_resorts[v] = 2
                    

                heapq.heappush(pq,(distances[v],v))
    ans = 0
    for r in resorts:
        ans += 2*distances[r]
    return ans
runtests(lets_roll, all_tests = True)
