from egz1atesty import runtests
import heapq
from math import floor
def armstrong( B, G, s, t):
  V = max([max(u,v) for u,v,_ in G]) + 1
  graph = [[] for _ in range(V)]
  for u,v,w in G:
    graph[u].append((v,w))
    graph[v].append((u,w))

  def dijkstra(G,s):
    distances = [float("inf") for _ in range(len(G))]
    distances[s] = 0
    pq = []
    heapq.heappush(pq,(0,s))

    while pq:
      current_dist, u = heapq.heappop(pq)
      for v,w in G[u]:
        if current_dist + w < distances[v]:
          distances[v] = current_dist + w
          heapq.heappush(pq,(distances[v],v))

    return distances
  
  distance_from_s = dijkstra(graph,s)
  distance_from_t = dijkstra(graph,t)
  ans = distance_from_s[t]
  for bike,p,q in B:
    if distance_from_s[bike] != float("inf") and distance_from_t[bike] !=float("inf"):
      ans = min(ans, distance_from_s[bike] + floor(distance_from_t[bike]*p/q))
  return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
