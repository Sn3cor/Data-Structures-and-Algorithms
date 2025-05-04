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

            