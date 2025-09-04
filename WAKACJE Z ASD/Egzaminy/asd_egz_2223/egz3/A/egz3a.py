from egz3atesty import runtests

from collections import deque
def goodknight( G, s, t ):
  n = len(G)
  graph = [[] for _ in range(n)]
  for u in range(n):
    for v in range(n):
      if G[u][v] != -1:
        graph[u].append((v,G[u][v]))
        graph[v].append((u,G[u][v]))

  distances = [[float("inf") for _ in range(17)] for _ in range(n)]
  distances[s][0] = 0
  queue = deque()
  queue.append((s,0,0,0)) #vertice,current_dist,hours_travelled,status

  while queue:
    u,current_dist,hours_travelled,status = queue.popleft()
    if current_dist > distances[u][hours_travelled]:
      continue
    if status > 0:
      queue.append((u,current_dist,hours_travelled,status-1))
    else:
      for v,w in graph[u]:
        if hours_travelled + w > 16:
          if current_dist + w + 8 < distances[v][0]:
            distances[v][0] = current_dist + w + 8
            queue.append((v,distances[v][0],0,w))
        else:
          if current_dist + w < distances[v][hours_travelled+w]:
            distances[v][hours_travelled+w] = current_dist + w
            queue.append((v,distances[v][hours_travelled+w],hours_travelled+w,w)) 
    
 
  return min(distances[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
