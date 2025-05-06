from kol2testy import runtests

class Node:
    def __init__(self,value):
        self.value=value
        self.parent=self
        self.rank=0

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y: return
    if x.rank<y.rank:
        x.parent = y
    else:
        y.parent = x
        if x.rank==y.rank:
            x.rank+=1

def get_edges(G):
    E = []
    for i in range(len(G)):
        for u,weight in G[i]:
            if i<u:
                E.append((i,u,weight))
    return E

def Kruskal(G):
    A=[]
    E = get_edges(G)
    n=len(G)
    E.sort(key=lambda x: x[2])
    Nodes = [Node(v) for v in range(n)]
    for e in E:
        if find(Nodes[e[0]]) != find(Nodes[e[1]]):
            union(Nodes[e[0]],Nodes[e[1]])
            A.append(e)

    return A

def beautree(G):
    pass
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = False )
