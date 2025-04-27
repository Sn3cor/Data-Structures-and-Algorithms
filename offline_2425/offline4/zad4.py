from zad4testy import runtests
import heapq
# Jakub Krupa
def spacetravel( n, E, S, a, b ):
    graph = [[] for _ in range(n)]
    for u,v,weight in E:
        graph[u].append((v,weight))
        graph[v].append((u,weight))

    def dijkstra(G,S,start,end):
        V = len(G)
    
        distance = [float("inf") for _ in range(V)]

        distance[start] = 0
        queue = [(start,0)]

        while queue:
            current_v, curr_dist = heapq.heappop(queue)
            
            if curr_dist>distance[current_v]:
                continue

            for nb, weight in G[current_v]:
                if distance[nb] > curr_dist + weight:
                    distance[nb] = curr_dist + weight
                    heapq.heappush(queue, (nb, distance[nb]))
                    
            if current_v in S:
                for u in S:
                    if u!=current_v and distance[u] > distance[current_v]:
                        distance[u] = distance[current_v]
                        heapq.heappush(queue,(u,distance[u]))

        return distance
        
    distance = dijkstra(graph,S,a,b)

    return distance[b] if distance[b] != float("inf") else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
