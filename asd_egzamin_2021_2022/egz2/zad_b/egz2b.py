from egz2btesty import runtests

def magic( C ):
    n = len(C)
    dp = [0 for _ in range(n)] # Maksymalna ilość sztabek posiadana w i-tej komnacie (???)
    available = [False for _ in range(n)]
    available[0] = True
    for i in range(n):
        bars = C[i][0]
        for j in range(1,4):
            req, dest = C[i][j]
            if dest == -1 or dest < i or not available[i]:
                continue
            
            if req>=bars:
                if req - bars <= dp[i]:
                    available[dest] = True
                    dp[dest] = max(dp[dest],dp[i]-(req-bars))
            elif bars-req<=10:
                    available[dest] = True
                    dp[dest] = max(dp[dest],dp[i]+(bars-req))
        
    return dp[-1] if available[-1] else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
