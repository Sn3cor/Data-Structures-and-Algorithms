from zadtesty import runtests
import heapq
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
  #time = [[float("inf") for _ in range(V)] for _ in range(17)] 
  time = []
  for i in range(V):
    time.append( [float("+inf") for i in range(17)])
  #status = [0 for _ in range(V)]
  #visited = [False for _ in range(V)]
  queue = [(s,0,0)]

  time[s][0] = 0
 

  while queue:
    u, curr_time, status = heapq.heappop(queue)
    
    #if u == t: return curr_time

    for v, v_time in G[u]:
      #print(time[v])
      if time[v][status] > v_time + curr_time+8 and status + v_time > 16:
        time[v][v_time] = v_time + curr_time+8
        _status = v_time
        heapq.heappush(queue,(v,time[v][_status],_status))

      if time[v][status] > v_time + curr_time and status + v_time <= 16:
        time[v][status+v_time] = v_time + curr_time
        _status = status+ v_time
        heapq.heappush(queue,(v,time[v][_status],_status))
  return min(time[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
