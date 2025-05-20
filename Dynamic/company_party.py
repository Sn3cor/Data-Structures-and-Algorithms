'''
We need to find the set of employees who have the highest sum of party rate,
but any boss cant meet his subordinates directly

1. Functions definition

f(v) - value of the best party from tree T(v)
g(v) - value of the best party in T(v) without the boss (v) / without the root

2. Recursive formula

f(v) = max(fun(v) + sum(g(u)), g(v))
g(v) = sum(f(u))

where:
    - fun(x) is a value of party rate for x,
    - "u" are children of "v"

3. Implementation
'''

class Emp:
    def __init__(self, fun):
        self.emp=[]
        self.fun = fun
        self.f = -1
        self.g = -1


def f(v):
    if v.f != -1: return v.f
    f1 = v.fun
    for u in v.emp:
        f1+=g(u)
    
    f2 = g(v)
    v.f = max(f1,f2)
    return v.f

def g(v):
    if v.g != -1: return v.g
    v.g = 0
    for u in v.emp:
        v.g+=f(u)
    return v.g
