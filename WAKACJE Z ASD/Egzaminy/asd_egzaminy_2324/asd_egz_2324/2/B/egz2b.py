from egz2btesty import runtests
from collections import deque
def tory_amos( E, A, B ):
  V = max([max(u,v) for u,v,_,__ in E])+1
  graph = [[] for _ in range(V)]
  for u,v,w,type in E:
    num_type = 0 if type == 'I' else 1
    graph[u].append((v,w,num_type))
    graph[v].append((u,w,num_type))

  
  distance = [[float("+inf"),float("+inf")] for _ in range(V)]
  distance[A][0] = 0
  distance[A][1] = 0
  queue = deque()

  for v,w,num_type in graph[A]:
    queue.append((v,w,w,num_type)) #vertice, current_weight, status/distance to verice(decrements every step), type of connecntion

  while queue:
    u,current_dist,status,num_type = queue.popleft()
    if current_dist > distance[u][num_type]:
      continue
    if status > 0:
      queue.append((u,current_dist,status-1,num_type))
    else:
      for v,w,next_type in graph[u]:
        if num_type!=next_type:
          if current_dist + w + 20 < distance[v][next_type]:
            distance[v][next_type] = current_dist + w +20
            queue.append((v,distance[v][next_type],w,next_type))
        elif num_type==0:
          if current_dist + w + 5 < distance[v][next_type]:
            distance[v][next_type] = current_dist + w +5
            queue.append((v,distance[v][next_type],w,next_type))
        elif num_type==1:
          if current_dist + w + 10 < distance[v][next_type]:
            distance[v][next_type] = current_dist + w + 10
            queue.append((v,distance[v][next_type],w,next_type))
    
  return min(distance[B])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
