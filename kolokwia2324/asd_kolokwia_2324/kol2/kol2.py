from kol2testy import runtests

# wersja z dijkstra
# from queue import PriorityQueue
# def warrior( G, s, t):
  
#   def edges_to_list(E):
#     max_vertex = max([max(u,v) for u,v,_ in E])
#     G = [[] for _ in range(max_vertex+1)]

#     for u,v,w in E:
#       G[u].append((v,w))
#       G[v].append((u,w))

#     return G

#   G = edges_to_list(G)
#   V = len(G)
#   time = [[float("inf") for _ in range(17)] for _ in range(V)]
#   time[s][0] = 0
#   pq = PriorityQueue()
#   pq.put((0,s,0))

#   while not pq.empty():
#     curr_dist, u, status = pq.get()

#     for v,w in G[u]:
#       if status + w <=16:
#         if time[v][status+w] > curr_dist + w:
#           time[v][status+w] = curr_dist + w
#           pq.put((time[v][status + w], v, status + w))
#       else:
#         if time[v][w] > curr_dist + w + 8:
#           time[v][w] = curr_dist + w + 8
#           pq.put((time[v][w], v, w))
#   return min(time[t])

from collections import deque

def warrior(G,s,t):
  def edges_to_list(E):
    max_vertex = max([max(u,v) for u,v,_ in E])
    G = [[] for _ in range(max_vertex+1)]
    for u,v,w in E:
      G[u].append((v,w))
      G[v].append((u,w))

    return G

  #BFS
  G = edges_to_list(G)
  V = len(G)
  time = [[float("inf") for _ in range(17)] for _ in range(V)]
  time[s][0] = 0
  queue = deque([(s,0,0,0)]) #vertex/edge_value/curr_time/status

  while queue:
    u, edge_value, curr_time,status = queue.popleft()

    if edge_value > 0: queue.append((u,edge_value-1,curr_time,status))
    else:
      for v, w in G[u]:
        if w + status <= 16:
          if time[v][status + w] > curr_time + w:
            time[v][status + w] = curr_time + w
            queue.append((v,w,time[v][status+w],status+w))
        else:
          if time[v][w] > curr_time + w + 8:
            time[v][w] = curr_time +w +8
            queue.append((v,w,time[v][w],w))
  return min(time[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
