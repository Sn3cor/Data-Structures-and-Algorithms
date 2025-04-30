'''
Jak znaleźć cykl o minimalnej wadze w grafie skierowanum z dodatnimi wagami
'''

def floydzik(G):
    V = len(G)
    D = G[:][:]
    for k in range(V):
        for x in range(V):
            for y in range(V):
                if D[x][k] and D[k][y]:
                    D[x][y]=min(D[x][y],D[k][y]+D[x][k])

    mini = float("inf")
    for x in range(V):
        for y in range(x+1,V):
            if D[x][y] and D[y][x]:
                if D[x][y]+D[y][x]<mini:
                    mini = D[x][y]+D[y][x]
    
'''
Dijkstra dla kazdego wierzcholka
for v in V:
    Dijkstra(G,v)
    for (u,v) in E:
        (u+v)+path(v,u)
'''
