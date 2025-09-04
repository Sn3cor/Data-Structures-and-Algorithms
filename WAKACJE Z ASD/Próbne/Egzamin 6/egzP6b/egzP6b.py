from egzP6btesty import runtests 
from collections import defaultdict
def jump ( M ):
    moves = {
        "UR": (1,2),
        "RU": (2,1),
        "RD": (2,-1),
        "DR": (1,-2),
        "DL": (-1,-2),
        "LD": (-2,-1),
        "LU": (-2,1),
        "UL": (-1,2)
    }

    lights = defaultdict()
    x,y = 0,0
    lights[(x,y)] = True
    for el in M:
        dx,dy = moves[el]
        x,y = x+dx,y+dy
        if (x,y) in lights:
            lights[(x,y)] = not lights[(x,y)]
        else:
            lights[(x,y)] = 1
    ans = 0
    for key in lights.keys():
        if lights[key]:
            ans +=1
    #tutaj proszę wpisać własną implementację
    return ans
    
runtests(jump, all_tests = True)