from egz2btesty import runtests
from queue import PriorityQueue
from collections import deque
def tory_amos( E, A, B ):

  def edges_to_list(E):
    max_vertice = max([max(u,v) for u,v,_,_ in E])
    list = [[] for _ in range(max_vertice + 1)]
    for u,v,cost,type in E:
      list[u].append((v,cost,type))
      list[v].append((u,cost,type))

    return list

  def bfs(G,s):
    n = len(G)
    #          linia I      linia P
    times = [[float("inf"),float("inf")] for _ in range(n)]
    times[s][0] = times[s][0] = 0
    queue = deque()
    for v,cost,type in G[s]:
      type_num = 0 if type == "I" else 1
      queue.append((cost,v,cost,type_num)) # cost, vertice , distance so far, type number

    while queue:
      current_cost, u, dist_travelled, current_type_num = queue.popleft()
      if times[u][current_type_num] < current_cost: continue
      if dist_travelled>0:
        queue.append((current_cost,u,dist_travelled-1,current_type_num))
      elif dist_travelled == 0:
        for v,cost,type in G[u]:
          type_num = 0 if type == "I" else 1
          if current_type_num == type_num:
            extra = 5 if current_type_num == 0 else 10
            if times[v][type_num] > current_cost + cost + extra:
              times[v][type_num] = current_cost + cost + extra
              queue.append((times[v][type_num],v,cost,type_num))
          else:
            if times[v][type_num] > current_cost + cost + 20:
              times[v][type_num] = current_cost + cost + 20
              queue.append((times[v][type_num],v,cost,type_num))
    return times


  def dijkstra(G, s):
    n = len(G)
    #          linia I      linia P
    times = [[float("inf"),float("inf")] for _ in range(n)]
    times[s][0] = times[s][1] = 0
    pq = PriorityQueue()
    # pq.put((0,s,None))
    for v,cost,type in G[A]:
      pq.put((cost,v,type))

    while not pq.empty():
      current_time, u, current_type = pq.get()
      current_type_num = 0 if current_type == "I" else 1
      if current_time > times[u][current_type_num]:
        continue
      for v, cost, type in G[u]:
        type_num = 0 if type == "I" else 1
        # if current_type is None:
        #   if current_time + cost < times[v][type_num]:
        #     times[v][type_num] = current_time + cost
        #     pq.put((times[v],v,type))
        # else:
        if current_type == type:
          extra = 5 if current_type == "I" else 10
          if current_time + cost + extra < times[v][type_num]:
            times[v][type_num] = current_time + cost + extra
            pq.put((times[v][type_num],v,type))
        else:  
          if current_time + cost + 20 < times[v][type_num]:
            times[v][type_num] = current_time + cost + 20
            pq.put((times[v][type_num],v,type))

    return times
  
  result = bfs(edges_to_list(E),A)
  # tu prosze wpisac wlasna implementacje
  return min(result[B])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
