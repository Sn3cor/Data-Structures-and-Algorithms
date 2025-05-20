'''
A - array of random numbers

Step 1:
Find a fundtion that helps to solve the problem (not the one that solves it)

f(i) - lenght of the longest incrementing subsequence that ends at A[i]

Step 2:
Find the recursive equation for function f

f(i) = max{ f(j)+1 | j<i and A[j] < A[i] }

Step 3:
Implementation O(n^2)
'''

def LIS(A): 
    n = len(A)
    maxi = 0
    F = [1 for _ in range(n)]
    Parent = [-1 for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                Parent[i] = j

            if F[i] > F[maxi]: maxi = i
    
    return maxi, F, Parent


print(LIS([5,4,1,3,6,8,10,12,11,14,16]))

'''
Implementation O(n logn)
'''

def bet_LIS(A):
    n = len(A)
    ans = []
    ans.append(A[0])
    # ans keeps the elemnets of current longest incrementing subsequence of A
    for i in range(1,n):
        if A[i] > ans[-1]:
            # If current element from input is greater than the last element from our ans array, 
            # that means we found a longer sequence, so we append it to ans.
            ans.append(A[i])

        else:
            # If it isn't greater, then we perform binary search to find the smallest element in ans,
            # that still is greater than or equal to the current number.

            l = 0
            r = len(ans) - 1
            while l < r:
                mid = (l + r)//2
                if ans[mid] < A[i]:
                    l = mid + 1
                else:
                    r = mid
            # And then we replace the found element with our number
            ans[l] = A[i]

    return len(ans)


print(bet_LIS([10,22,9,33,21,50,41,60]))