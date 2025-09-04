from egzP3btesty import runtests 
from queue import PriorityQueue

class UnionFind:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self,x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        rootX, rootY = self.find(x),self.find(y)
        if rootX!=rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] +=1

def lufthansa ( G ):
    edges = []
    V = len(G)
    for u in range(V):
        for v,w in G[u]:
            if u < v:
                edges.append((u,v,w))

    edges.sort(key=lambda x: x[2], reverse = True)
    notused = []
    uf = UnionFind(V)
    ans = 0
    print(edges)
    for u,v,w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u,v)
        else:
            notused.append((u,v,w))
            ans += w
    
    notused.sort(key=lambda x: x[2], reverse = True)
    ans -= notused[0][2]
    
    
    return ans

runtests ( lufthansa, all_tests=True )