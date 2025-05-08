from zadtesty import runtests
import heapq
from collections import deque

# wersja z dijkstra
# def goodknight( G, s, t ):

#   def create_list(G):
#     L = [[] for _ in range(len(G))]
#     for u in range(len(G)):
#       for v in range(len(G)):
#         if G[u][v] != -1:
#           L[u].append((v,G[u][v]))

#     return L
  
#   G = create_list(G)
#   V = len(G)

#   time = []
#   for _ in range(V):
#     time.append( [float("+inf") for _ in range(17)])
#   queue = [(s,0,0)]

#   time[s][0] = 0
 

#   while queue:
#     u, curr_time, status = heapq.heappop(queue)

#     for v, w in G[u]:

#       if status + w <= 16:
#         if time[v][status + w] > curr_time + w:
#           time[v][status + w] = curr_time + w
#           heapq.heappush(queue,(v, time[v][status+w], status + w))

#       else: 
#         if time[v][w] > curr_time + w + 8:
#           time[v][w] = curr_time + w + 8
#           heapq.heappush(queue,(v, time[v][w], w))

#   return min(time[t])

#wersja z "bfs"
def goodknight( G, s, t ):

  def create_list(G):
    L = [[] for _ in range(len(G))]
    for u in range(len(G)):
      for v in range(len(G)):
        if G[u][v] != -1:
          L[u].append((v,G[u][v]))

    return L
  
  G = create_list(G)
  V = len(G)
  visited = [[float("inf") for _ in range(17)] for _ in range(V)]
  visited[s][0] = 0
  queue = deque([(s,0,0,0)]) #vertex, edge_value, curr_time, status

  while queue:
    u, edge_value, curr_time, status = queue.popleft()

    if edge_value>0: queue.append((u,edge_value-1,curr_time,status))
    else:
      for v,w in G[u]:
        if status + w <= 16:
          if visited[v][status + w] > curr_time + w:
            visited[v][status + w] = curr_time + w
            queue.append((v,w,visited[v][status+w],status + w))

        else:
          if visited[v][w] > curr_time + w + 8:
            visited[v][w] = curr_time + w + 8
            queue.append((v,w,visited[v][w],w))
  return min(visited[t])
        



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
