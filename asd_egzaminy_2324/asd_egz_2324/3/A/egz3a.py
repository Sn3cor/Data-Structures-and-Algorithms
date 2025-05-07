from egz3atesty import runtests
from collections import deque


def mykoryza( G,T,d ):
  V = len(G)
  owner = [None for _ in range(V)]
  time = [float("inf") for _ in range(V)] # czas przejecia drzewa
  queue = deque()
  for grzyb in range(len(T)):
    owner[T[grzyb]] = grzyb
    time[T[grzyb]] = 0
    queue.append((T[grzyb],grzyb,0)) #drzewo przejete przez grzyba/ id grzyba / czas

  while queue:
    tree, grzyb, curr_time = queue.popleft()
    for nb in G[tree]:
      if time[nb] > curr_time+1:
        owner[nb] = grzyb
        time[nb] = curr_time+1
        queue.append((nb,grzyb,curr_time+1))
      elif time[nb]==curr_time+1 and grzyb<owner[nb]:
        owner[nb] = grzyb
        queue.append((nb,grzyb,curr_time+1))
  return owner.count(d)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )
