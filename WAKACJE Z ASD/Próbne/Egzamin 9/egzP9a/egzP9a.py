from egzP9atesty import runtests

def ASD(T, p, Q, n):
    def parent(i):
        return (i-1)//2
    def left(i):
        return 2*i+1
    def right(i):
        return 2*i+2
    
    def update(T,idx,value):
        T.set(idx, T.get(idx) + value)

    def getsum(T,k,i,j,klo,khi):
        pass
    ans = 0
    for el in Q:
        if el[0] == 0:
            index = el[1]
            value = el[2]
            
            update(T,index,value)
        else:
            a,b = el[1],el[2]
            output += getsum(T,a,b)
    #Tutaj proszę wpisać własną implementację
    return 0


#Podpowiedź. Format zadania jest dość nietypowy (także ze względu na sposób działania testów),
#w takiej formie żadne zadanie raczej nie powinno się pojawić na egzaminie. Zadanie ma na celu
#sprawdzenie zrozumienia struktury #### Drzewa Przedziałowego ####

runtests(ASD, all_tests = False)

