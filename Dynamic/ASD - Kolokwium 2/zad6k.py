from zad6ktesty import runtests 
#f(i)
def haslo ( S ):
    F = [None for _ in range(len(S)+1)]
    def rek(i):
        nonlocal S
        if i == 0:
            return 1
        if F[i] != None:
            return F[i]
        if S[i-1] == '0':
            return 0
        
        result = rek(i-1)

        if i >=2:
            two_d = int(S[i-2:i])
            if 10<= two_d <=26:
                result += rek(i-2)
        F[i] = result
        return result
    return rek(len(S))

runtests ( haslo )