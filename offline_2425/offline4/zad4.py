from zad4testy import runtests
import heapq
from queue import PriorityQueue
# Jakub Krupa
# def spacetravel( n, E, S, a, b ):
#     graph = [[] for _ in range(n)]
#     for u,v,weight in E:
#         graph[u].append((v,weight))
#         graph[v].append((u,weight))

#     def dijkstra(G,S,start,end):
#         V = len(G)
    
#         distance = [float("inf") for _ in range(V)]

#         distance[start] = 0
#         queue = [(start,0)]

#         while queue:
#             current_v, curr_dist = heapq.heappop(queue)
            
#             if curr_dist>distance[current_v]:
#                 continue

#             for nb, weight in G[current_v]:
#                 if distance[nb] > curr_dist + weight:
#                     distance[nb] = curr_dist + weight
#                     heapq.heappush(queue, (nb, distance[nb]))
                    
#             if current_v in S:
#                 for u in S:
#                     if u!=current_v and distance[u] > distance[current_v]:
#                         distance[u] = distance[current_v]
#                         heapq.heappush(queue,(u,distance[u]))

#         return distance
        
#     distance = dijkstra(graph,S,a,b)

#     return distance[b] if distance[b] != float("inf") else None

def spacetravel(n,E,S,a,b):
    def dijkstra(G,s):
        distance = [float("inf") for _ in range(len(G)+1)]
        distance[s] = 0
        queue = PriorityQueue()
        queue.put((0,s))

        while not queue.empty():
            curr_dist,u = queue.get()

            if curr_dist>distance[u]: continue

            for v,w in G[u]:
                if distance[v] > curr_dist + w:
                    distance[v] = curr_dist + w
                    queue.put((distance[v],v))

        return distance
    
    G = [[] for _ in range(n+1)]
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))
    
    for v in S:
        G[n].append((v,0))
        G[v].append((n,0))

    dist_from_new = dijkstra(G, n)
    dist_from_a = dijkstra(G,a)
    if dist_from_new[a]!=float("inf") and dist_from_new[b]!=float("inf"):
        return min(dist_from_new[a] + dist_from_new[b], dist_from_a[b])
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
