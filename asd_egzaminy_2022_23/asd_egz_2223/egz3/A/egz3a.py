from egz3atesty import runtests
from queue import PriorityQueue
from collections import deque
def goodknight( G, s, t ):

  def matrix_to_list(M):
    n = len(M)
    list = [[] for _ in range(n)]
    for i in range(n):
      for j in range(n):
        if M[i][j] > 0:
          list[i].append((j,M[i][j]))
         

    return list
    
  def dijkstra(G,s,t):
    n = len(G)
    time = [[float("+inf") for _ in range(17)] for _ in range(n)]
    pq = PriorityQueue()
    time[s][0] = 0
    pq.put((0,0,s)) # time travelled overall / status(0-16) / vertex

    while not pq.empty():
      time_travelled, status, u = pq.get()
      if time_travelled > time[u][status]:
        continue
      for v, cost in G[u]:
        if status + cost <= 16:
          if time_travelled + cost < time[v][status+cost]:
            time[v][status+cost] = time_travelled + cost
            pq.put((time[v][status+cost],status+cost,v))
        else:
          if time_travelled + cost + 8 < time[v][cost]:
            time[v][cost] = time_travelled+cost+8
            pq.put((time[v][cost],cost,v))

    return min(time[t])
  
  def bfs(G,s,t):
    n = len(G)
    times = [[float("inf") for _ in range(17)] for _ in range(n)]
    times[s][0] = 0
    queue = deque()
  
    queue.append((s,0,0,0)) #vertex, time travelled so far, status, time to next vertex

    while queue:
      u, time_travelled, status, time_to_next =queue.popleft()
      if time_to_next >0:
        queue.append((u,time_travelled,status,time_to_next-1))
      elif time_to_next == 0:
        for v, cost in G[u]:
          if status + cost <=16:
            if time_travelled + cost< times[v][status+cost]:
              times[v][status+cost] = time_travelled+cost
              queue.append((v,times[v][status+cost],status+cost,cost))
          else:
            if time_travelled +cost + 8< times[v][cost]:
              times[v][cost] = time_travelled+cost + 8
              queue.append((v,times[v][cost],cost,cost))

    return min(times[t])


  return bfs(matrix_to_list(G),s,t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = False )
