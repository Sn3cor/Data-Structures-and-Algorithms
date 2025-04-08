class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def print(self):
        while self:
            print(f"{self.value} -> ",end="")
            self = self.next
        print("")
        pass

def topology_sort(G):
    list = Node()
    def DFSVisit(G,start):
        nonlocal visited,parent,list
        visited[start] = True
        for nb in G[start]:
            if not visited[nb]:
                parent[nb]=start
                DFSVisit(G,nb)

        tmp = list.next
        list.next = Node(start)
        list.next.next = tmp

    V = len(G)
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]
    for vertex in range(V):
        if not visited[vertex]:
            DFSVisit(G,vertex)

    return list.next

#Example from Cormen's Introduction to Algorithms
graph =[
    [3,4],      #0 - Undershirt
    [4],        #1 - Socks
    [],         #2 - Watch
    [6,4],        #3 - Pants
    [],         #4 - Shoes
    [6,7],      #5 - Shirt
    [8],        #6 - Belt
    [8],        #7 - Tie
    []          #8 - Jacket
]

result = topology_sort(graph)
result.print()