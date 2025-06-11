from zad8testy import runtests
from collections import deque
import heapq

def plan(T):
    n = len(T)
    m = len(T[0])

    visited = [[False for _ in range(m)] for _ in range(n)]
    stops = 1
    tank = 0
    
    def bfs(i,j):
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        nonlocal T, visited
        _sum = T[i][j]
        visited[i][j] = True
        status = deque()
        status.append((i,j))

        while status:
            u,v = status.popleft()
            for ru,rv in directions:
                nu,nv = u+ru, v+rv
                if 0<=nu<n and 0<= nv<m and not visited[nu][nv] and T[nu][nv] >0 :
                    visited[nu][nv] = True
                    _sum += T[nu][nv]
                    status.append((nu,nv))

        return _sum
    
    maxheap = [-bfs(0,0)]
    pos = 0
    tank = -heapq.heappop(maxheap)

    while pos < m-1:
        if tank > 0:
            tank-=1
            pos+=1
            if T[0][pos] > 0 and not visited[0][pos]:
                heapq.heappush(maxheap, -bfs(0,pos))
        else:
            if maxheap:
                stops+=1
                tank+= -heapq.heappop(maxheap)
    
    return stops

#(O(n*m + mlogk))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

