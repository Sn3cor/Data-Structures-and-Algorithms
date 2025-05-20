def fib(n): # nieoptymalne / złozoność wykładnicza
    if n<=1: return 1
    else: return fib(n-1)+fib(n-2)

def fast_fib(n):
    F=[1 for _ in range(n+1)]
    for i in range(2,n+1):
        F[i] = F[i-1]+F[i-2]
    return F[n]

print(fast_fib(5))
