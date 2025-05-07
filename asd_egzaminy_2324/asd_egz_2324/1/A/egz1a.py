from egz1atesty import runtests
from queue import PriorityQueue
from math import floor
def armstrong( B, G, s, t):
  def create_list(G):
    max_vertice = max([max(u,v) for u,v,_ in G])
    L = [[] for _ in range(max_vertice+1)]
    for u,v,w in G:
      L[u].append((v,w))
      L[v].append((u,w))

    return L

  def dijkstra(L,s):
    V = len(L)
    distance = [float("+inf") for _ in range(V)]
    distance[s]=0
    queue = PriorityQueue()
    queue.put((0,s))

    while not queue.empty():
      current_weight, u = queue.get()

      if distance[u] < current_weight:
        continue

      for nb,weight in L[u]:
        if distance[nb]> current_weight + weight:
          distance[nb] = current_weight + weight
          queue.put((distance[nb],nb))
    
    return distance
  
  L = create_list(G)
  dist_from_s = dijkstra(L,s)
  dist_from_t = dijkstra(L,t)

  shortest = dist_from_s[t]

  for v,p,q in B:
    if dist_from_s[v]!=float("+inf") and dist_from_t[v]!=float("+inf"):
      path_to_bike = dist_from_s[v]
      path_from_bike = floor(dist_from_t[v]*(p/q))
      total = path_to_bike + path_from_bike
      shortest = min(total,shortest)
  return shortest

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
