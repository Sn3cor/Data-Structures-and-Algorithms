'''
Algorytm Kruskla i union
'''

class Node:
    def __init__(self,value):
        self.parent = self
        self.value = value
        self.rank = 0

def find(x):
    y=x
    while x.parent!=x:
        x = x.parent
    y.parent = x
    return x

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y: return
    if x.rang<y.rang:
        x.parent = y
    else:
        y.parent = x
        if x.rang==y.rang:
            y.rang+=1

def kruskal(E,n):#Zakładamy ze mamy liste krawedzi
    N = [Node(v) for v in range(n)]
    T=[]
    E.sort(key=lambda x:x[2])
    for e in E:
        if find(N[e[0]])!=find(N[e[1]]):
            union(N[e[0]],N[e[1]])
            T.append(e)

    return T

#O(ElogV)