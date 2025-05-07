from zadtesty import runtests
import heapq
from collections import deque
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

  time = []
  for _ in range(V):
    time.append( [float("+inf") for _ in range(17)])
  queue = [(s,0,0)]

  time[s][0] = 0
 

  while queue:
    u, curr_time, status = heapq.heappop(queue)

    for v, w in G[u]:

      if status + w <= 16:
        if time[v][status + w] > curr_time + w:
          time[v][status + w] = curr_time + w
          heapq.heappush(queue,(v, time[v][status+w], status + w))

      else: 
        if time[v][w] > curr_time + w + 8:
          time[v][w] = curr_time + w + 8
          heapq.heappush(queue,(v, time[v][w], w))

  return min(time[t])


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

  
#   visited = [[False for _ in range(V)] for _ in range(17)]
#   queue = deque()

#   for i in range(17):
#     visited[s][i] = True

#   for v, weight in G[s]:
#     queue.append(queue,(v,weight,1,weight-1))



#   while queue:
#     u, curr_time, status, remain = heapq.heappop(queue)
#     if visited[u][status]: continue

#     if remain == 0:
#       visited[u] = True
#       for v,weight in G[u]:
#         if 
#         queue.append(queue,(v,status + weight,status+weight,weight-1))
#     else: 


#   return min(time[t])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
