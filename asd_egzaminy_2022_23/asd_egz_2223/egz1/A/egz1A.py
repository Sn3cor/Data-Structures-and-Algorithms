from egz1Atesty import runtests
from queue import PriorityQueue


def gold(G,V,s,t,r):
  # tu prosze wpisac wlasna implementacje
  def dijkstra(G,s,wanted,r):
    cost = [float("inf") for _ in range(len(G))]
    
    cost[s] = 0
    
    pq = PriorityQueue()
    pq.put((0,s))

    while not pq.empty():
      curr_dist,u = pq.get()

      if curr_dist>cost[u]:
        continue

      for v,w in G[u]:
        if wanted:
          w = (2*w)+r
        if cost[v] > curr_dist + w:
          cost[v] = curr_dist + w
          
          pq.put((cost[v],v))

    return cost     
  
  cost_from_s = dijkstra(G,s,False,0)
  cost_from_t = dijkstra(G,t,True,r)

  lowest_cost = cost_from_s[t]

  for v in range(len(V)):
    if cost_from_s[v] == float("inf") or cost_from_t[v] == float("inf"):
            continue
    total = cost_from_s[v]+cost_from_t[v] - V[v]
    lowest_cost = min(lowest_cost, total)

  return lowest_cost

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
