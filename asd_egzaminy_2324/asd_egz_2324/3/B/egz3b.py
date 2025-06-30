from egz3btesty import runtests


def kunlucky(T, k):
  n = len(T)
  unlucky_values = [0 for _ in range(n+1)]
  
  unlucky_values[0] = k
  arr = [False for _ in range(n+1)]
  
  for i in range(1,n+1):
    if unlucky_values[i-1]<n:
      arr[unlucky_values[i-1]] = True
    else: break
    unlucky_values[i] = unlucky_values[i-1] + (unlucky_values[i-1]%i) + 7
    

  T_arr = [False for _ in range(n)]

  for j in range(n):
    if arr[T[j]]:
      T_arr[j] = True

  left = 0
  right = 0
  count = 0
  last_unlucky_idx = None
  current_unlucky_idx = None
  if T_arr[left]:
    current_unlucky_idx = left
    count+=1
  max_span = 0
  while right < n-1:
    if count <=2:
      right +=1 
      if T_arr[right]: 
        count +=1
        if count == 3:
          max_span = max(max_span,right-left)
          left = last_unlucky_idx+1
          count = 2
        last_unlucky_idx = current_unlucky_idx
        current_unlucky_idx = right
  max_span = max(max_span,right-left+1)
  return max_span



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True )
