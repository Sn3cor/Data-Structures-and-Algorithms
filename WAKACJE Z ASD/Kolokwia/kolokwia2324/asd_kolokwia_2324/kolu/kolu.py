from kolutesty import runtests

def projects(n, L):
  def DFS_visit(G,u):
    visited[u] = True
    max_depth_from[u] = 1
    for v in G[u]:
      if not visited[v]:
        max_depth_from[u] =  max(max_depth_from[u],1+DFS_visit(G,v))
      else:
        max_depth_from[u] = max(max_depth_from[u],max_depth_from[v]+1)
    
    return max_depth_from[u]
    
  graph = [[] for _ in range(n)]
  for p,q in L:
    graph[q].append(p)

  visited = [False for _ in range(n)]
  max_depth_from = [float("-inf") for _ in range(n)]
  for u in range(n):
    if not visited[u]:
      max_depth_from[u] = DFS_visit(graph,u)

  return max(max_depth_from)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )
