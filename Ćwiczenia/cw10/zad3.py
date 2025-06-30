'''
Zadanie

Kazde zadanie ma deadline d(ti) oraz wartość/nagrode G(ti)
Wykonanie jednego zadania trwa jedną jednostkę czasu

zadanie o najwyzszej wartości chcemy zrobić jak najpozniej
'''



#Źle
def zadania(T,D,G):
    n = len(T)
    last_deadline = max(D)
    arr = [(D[i],G[i],T[i]) for i in range(n)]

    arr.sort(key= lambda x:x[1],reverse=True)
    timer = 0
    result=[]
    i=0
    while i<n:
        if timer <= arr[i][0]:
            result.append(T[i])
            timer+=1
        i+=1

    return result


T = ["t1", "t2", "t3", "t4", "t5", "t6"]
D = [4, 1, 2, 2, 3, 1]
G = [70, 60, 50, 40, 30, 20]

print(zadania(T,D,G))

'''
zadanie dynamiczne - widać w nich podproblem, który wygląda tak samo i zrobić rekurencje

zadanie zachłanne - wybieramy optymalność lokalną i zmniejszamy problem

'''