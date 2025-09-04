from egzP8atesty import runtests 
from collections import deque
def reklamy ( T, S, o ):
    def is_disconnected(x1,y1,x2,y2):
        if x2>y1 or x1 > y2:
            return True
        return False
    C = [(T[i][0],T[i][1],S[i]) for i in range(len(T))]
    C.sort(key = lambda x: x[2], reverse=True)
    kolejeczka = deque()
    curr_profit = 0
    profit = 0
    for i in range(len(C)):
        if not kolejeczka:
            kolejeczka.append(C[i])
            curr_profit += C[i][2]
            profit = max(profit,curr_profit)

        else:
            if len(kolejeczka) == 1:
                last = kolejeczka[0]
                if is_disconnected(last[0],last[1],C[i][0],C[i][1]):
                    kolejeczka.append(C[i])
                    curr_profit += C[i][2]
                    profit = max(profit,curr_profit)

            elif len(kolejeczka) == 2:
                last = kolejeczka[0]
                kolejeczka.popleft()
                curr_profit -= last[2]
    
    return profit

runtests ( reklamy, all_tests=True )