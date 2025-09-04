from zad6testy import runtests
import heapq

def jumper( G, s, w ):
    V = len(G)
    graph = [[] for _ in range(V)]
    for i in range(V):
        for j in range(i,V):
            if G[i][j] == 0:
                continue
            graph[i].append((j,G[i][j]))
            graph[j].append((i,G[i][j]))


    distances = [[float("+inf"),float("+inf")] for _ in range(V)]
    distances[s][1] = 0
    pqueue = []
    heapq.heappush(pqueue,(0,s,1)) #dist, vertice, can jump

    while pqueue:
        curr_dist,u,can_jump = heapq.heappop(pqueue)

        if curr_dist > distances[u][can_jump]:
            continue
        for v,weight in graph[u]:

            if can_jump:
                for x,next_weight in graph[v]: #Moemy skoczyć i skaczemy
                    if distances[x][0] > curr_dist+max(weight,next_weight):
                        distances[x][0] = curr_dist+max(weight,next_weight)
                        heapq.heappush(pqueue,(distances[x][0],x,0))

                if curr_dist + weight < distances[v][1]: # Mozemy skoczyć ale idziemy normalnie
                    distances[v][1] = curr_dist + weight
                    heapq.heappush(pqueue,(distances[v][1],v,1))
                
            else:
                if curr_dist + weight < distances[v][1]: # Niemozemy skoczyć, więc idziemy normalnie
                    distances[v][1] = curr_dist + weight
                    heapq.heappush(pqueue,(distances[v][1],v,1))

    # tu prosze wpisac wlasna implementacje
    return min(distances[w])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )