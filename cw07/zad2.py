'''
Domknięcie przechodnie

graf nad tym samym zbiorem wierzchołków który dla kazdych dwóch wierzchołków, 
który dla kadych dwóch wierzchołków u i v ma krawędź z u do v wtedy i tylko wtedy gdy w G istnieje ścieka z u do v
'''

def floydzik(G):
    V = len(G)
    D = G[:][:]
    for k in range(V):
        for x in range(V):
            for y in range(V):
                if D[x][k] and D[k][y]:
                    D[x][y]=1