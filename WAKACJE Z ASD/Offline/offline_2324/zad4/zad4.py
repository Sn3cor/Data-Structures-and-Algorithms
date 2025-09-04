from zad4testy import runtests

def Flight(L, x, y, t):
    def list_from_edges(L):
        max_vert = max(max(u, v) for u, v, w in L)
        G = [[] for _ in range(max_vert + 1)]
        for u, v, w in L:
            G[u].append((v, w))
            G[v].append((u, w)) 
        return G

    G = list_from_edges(L)
    V = len(G)

    # Zbierz wszystkie unikalne pułapy
    all_altitudes = []
    for u in range(V):
        for _, w in G[u]:
            all_altitudes.append(w)
    all_altitudes.sort()
    unique_altitudes = []
    prev = None
    for a in all_altitudes:
        if a != prev:
            unique_altitudes.append(a)
            prev = a

    # Spróbuj każdego pułapu jako stałego pułapu przelotu
    for p in unique_altitudes:
        visited = [False for _ in range(V)]
        parent = [None for _ in range(V)]
        queue = [x]
        visited[x] = True

        while queue:
            u = queue.pop(0)
            if u == y:
                return True
            for v, w in G[u]:
                if not visited[v] and abs(p - w) <= t:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)

    return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
