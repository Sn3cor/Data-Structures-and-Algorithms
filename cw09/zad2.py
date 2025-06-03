'''
Ładowanie promu
P-lista długości samochodow
f(i,a,b)=max(f(i-1,a,b),f(i-1,a-P[i],b)+1,f(i-1,a,b-P[i])+1) a-P[i]>=0, b-p[i]>=0
f(0,a,b)=1 dla a>P[0]
'''

def ferry(P,L):
    n=len(P)
    F=[[[0 for _ in range(L+1)] for _ in range(L+1)] for _ in range(n)]

    for a in range(L+1):
        for b in range(L+1):
            if a>=P[0]:
                F[0][a][b] = 1
            if b >=P[0]:
                F[0][a][b] = 1
    
            for i in range(1,n):
                if a-P[i] >= 0:
                    P[i][a][b] = max(P[i-1][a][b],P[i-1][a-P[i]][b]+1)
                if b-P[i] >= 0:
                    P[i][a][b] = max(P[i-1][a][b],P[i-1][a][b-P[i]]+1)

    return F[n-1][L][L]