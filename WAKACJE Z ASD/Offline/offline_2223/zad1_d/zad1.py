from zad1testy import runtests

def ceasar( s ):
    maxi_palindrom = 0
    for i in range(1,len(s)):
        p=q=i
        while p>0 and q<len(s)-1:
            p-=1
            q+=1
            if s[p]==s[q]:
                maxi_palindrom=max(maxi_palindrom,q-p+1)
            else:
                break
    
    return maxi_palindrom

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
