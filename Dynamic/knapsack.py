'''
Knapsack Problem (Problem Pleckaowy)

I={0,...,n-1} - item numbers
w: I->N - item weights
p: I->N - item prices
B - max weight of the knapsack

Problem: Find a subset of I that has maximal price and weight less or equal to B

1. Function

f(i,b) = max sum of item prices, which weight <= b

2. Recursive equation

f(i,b) max(f(i-1,b),f(i-1,b-w(i))+p(i))
f(0,b) = p(0) if w(0)<=b
f(0,b) = 0    if w(0)>b

3. Implementation
'''

def knapsack(W,P,B):
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n)]
    for b in range(W[0],B+1):
        F[0][b] = P[0]
    for b in range(B+1):
        for i in range(1,n):
            F[i][b] = F[i-1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b],F[i-1][b-W[i]]+P[i])
    return F[n-1][B]

W = [4, 2, 6, 3, 7, 1, 8, 5, 9, 3]   # Wagi
P = [50, 40, 70, 30, 80, 20, 90, 60, 100, 25]  # Wartości
B = 25  # Pojemność plecaka

wynik = knapsack(W, P, B)
print("Maksymalna wartość:", wynik)