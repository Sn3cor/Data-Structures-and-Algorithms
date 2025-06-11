from zad8ktesty import runtests 

#f(i,j) - minimalna liczba zmian w napisie s tak zeby powstal napis t
#f(i,j) = {
#           f(i-1,j-1) gdy s[i] = j[i]
#           min(f(i-1,j-1,f(i-1,j),f(i,j-1)) + 1 gdy róznie
#           }
#
#f(0,j) = f(0,j-1) gdy rozne lub j dla rownych
#f(i,0) = f(i-1,0) gdy rozne lub i dla rownych

def napraw ( s, t ):
    dp = [[None for _ in range(len(s))] for _ in range(len(t))]
    dp[0][0] = 1 if s[0]!=t[0] else 0
    for j in range(1,len(s)):
        dp[0][j] = dp[0][j-1] + 1 if t[0]!=s[j] else j
        
    for i in range(1,len(t)):
        dp[i][0] = dp[i-1][0] + 1 if t[i]!=s[0] else i

    for i in range(1,len(t)):
        for j in range(1,len(s)):
            if t[i] == s[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1

      
    return dp[-1][-1] 

runtests ( napraw )