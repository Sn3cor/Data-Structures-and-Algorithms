from zad7ktesty import runtests 
from collections import deque
def ogrodnik (T, D, Z, l):
    m = len(T)
    n = len(T[0])
    korzenie =[]
    visited = [[False for _ in range(n)] for _ in range(m)]

    def BFS(s_x,s_y):
        nonlocal visited, T, korzenie
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        _sum = T[s_x][s_y]
        visited[s_x][s_y] = True
        queue = deque()
        queue.append((s_x,s_y))

        while queue:
            i,j = queue.popleft()
            for ri,rj in directions:
                ni,nj = ri+i, rj+j
                if 0<=ni<m and 0<=nj<n and not visited[ni][nj] and T[ni][nj]>0:
                    visited[ni][nj] = True
                    _sum += T[ni][nj]
                    queue.append((ni,nj))

        return _sum
    
    def Knapsack(W,P,L):
        n = len(W)
        dp = [[0 for _ in range(L+1)] for _ in range(n+1)]
        for l in range(W[0],L+1):
            dp[0][l] = P[0]

        for l in range(L+1):
            for i in range(1,n):
                dp[i][l] = dp[i-1][l]
                if l-W[i]>=0:
                    dp[i][l] = max(dp[i][l], dp[i-1][l-W[i]]+P[i])

        return dp[n-1][L]

    for i in range(len(D)):
        korzenie.append(BFS(0,D[i]))

    
    return Knapsack(korzenie, Z, l)

runtests( ogrodnik, all_tests=True )
