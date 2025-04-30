'''
Wypisanie najkrótszej ścieki
'''

from zad1 import dijkstra

#dist,par = dijkstra(G,s)

def shortest_path(parent,s,t):
    path=[]
    while t!=s:
        path.append(t)
        t = parent[t]
    path.append(s)
    return path[::-1]