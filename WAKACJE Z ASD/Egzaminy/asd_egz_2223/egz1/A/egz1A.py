from egz1Atesty import runtests
import heapq

def gold(G,V,s,t,r):
  # tu prosze wpisac wlasna implementacje
  def dijkstra(G,s,wanted,r):
    n = len(G)
    distances = [float("+inf") for _ in range(n)]
    pq = []
    distances[s] = 0
    heapq.heappush(pq,(0,s))

    while pq:
      current_dist, u = heapq.heappop(pq)
      if current_dist > distances[u]:
        continue

      for v,w in G[u]:
        if wanted:
          w = w * 2 + r
        if distances[v] > current_dist + w:
          distances[v] = current_dist + w
          heapq.heappush(pq,(distances[v], v))

    return distances
  
  distance_form_s = dijkstra(G,s,False,r)
  distance_form_t = dijkstra(G,t,True,r)

  ans = distance_form_s[t]
  for castle in range(len(V)):
    if distance_form_s[castle]!=float("+inf") and distance_form_t!= float("+inf"): 
      ans = min(ans,distance_form_s[castle] + distance_form_t[castle]  - V[castle])
  return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
