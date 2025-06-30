'''
Pokrycie przedziałami
'''


T = [0, .25, .5, 1.51, 1.8, 2.6, 2.61]

def pokrycie(T):
    if not T: return 0
    count=1
    length=1
    for i in range(1,len(T)):
        if T[i]-T[i-1]<=length:
            length -= T[i]-T[i-1]
        else:
            count+=1
            length = 1

    return count


print(pokrycie(T))
