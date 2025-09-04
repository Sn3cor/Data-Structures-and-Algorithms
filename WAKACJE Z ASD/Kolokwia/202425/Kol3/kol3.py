from kol3testy import runtests
#Dynamik
def parkiet(B, C, s):
    n = len(B)
    m = len(B[0])

    dp = [[None for _ in range(m)] for _ in range(n)]
    
    def rek(i,j,s):
        if (i == n-1 or j == m-1) and C[i][j] <= s:
            return 0 
        if dp[i][j] is not None:
            return dp[i][j]

        up = float("+inf")
        left = float("+inf")
        if i+1 <n and C[i][j]-C[i+1][j]<=s:
            up = rek(i+1,j,s)
        if j+1 < m and  C[i][j] - C[i][j+1]<=s:
            left = rek(i,j+1,s)

        dp[i][j] = 1 + min(up,left)
        return dp[i][j]
    
    dp[0][0] = rek(0,0,s)
    return -1 if dp[0][0] == float("+inf") else dp[0][0]

#Wzorcówka
def parkiet2(B,C,s):
    i = 0
    j = 0
    count1 = 0
    n = len(B)
    m = len(B[0])
    while True:
        if i+1 <n and C[i][j] - C[i+1][j] <= s:
            i+=1
            count1+=1

        elif j+1 < m and C[i][j] - C[i][j+1] <= s:
            j+=1
            count1+=1

        if C[i][j] <= s:
            break

        elif i == n-1 and j == m-1 and C[i][j] > s:
            return -1
        
    i = 0
    j = 0
    count2 = 0
    while True:
        if j+1 < m and C[i][j] - C[i][j+1] <= s:
            j+=1
            count2+=1

        elif i+1 <n and C[i][j] - C[i+1][j] <= s:
            i+=1
            count2+=1

        if C[i][j] <= s:
            break
        
        elif i == n-1 and j == m-1 and C[i][j] > s:
            return -1

    return min(count1,count2)
        

runtests(parkiet2, all_tests = True)
