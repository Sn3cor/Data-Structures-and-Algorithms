from egz3atesty import runtests
from collections import deque


def mykoryza( G,T,d ):
  V = len(G)
  owners = [None for _ in range(V)]
  times = [None for _ in range(V)]
  queue = deque()
  for i in range(len(T)):
    times[T[i]] =0
    owners[T[i]] = i
    queue.append((T[i],i,0))

  while queue:
    u,gr,time = queue.popleft()
    
    for v in G[u]:
      if owners[v] is None:
        owners[v] = gr
        times[v] = time + 1
        queue.append((v,gr,time+1))
      else:
        if times[v] == time + 1:
          owners[v] = min(owners[v], gr)

  return owners.count(d)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )
