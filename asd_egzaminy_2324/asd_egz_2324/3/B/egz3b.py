from egz3btesty import runtests


def kunlucky(T, k):
  n = len(T)
  x = [0 for _ in range(n+1)]

  x[0] = k
  arr = [False for _ in range(n+1)]
  arr[x[0]] = True
  for i in range(1,n+1):
    x[i] = x[i-1] + (x[i-1]%i) + 7
    if x[i]<n:
      arr[x[i]] = True
    else: break

  T_arr = [False for _ in range(n)]

  for j in range(n):
    if arr[T[j]]:
      T_arr[j] = True

  left = 0
  right = 0
  count = 1 if T_arr[left] else 0
  while right < n-1:
    if count <=2:
      right +=1 
      if T_arr[right]: count +=1
    else:
      if T_arr[left]: count -=1
      left+=1

  return right -left +1



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True )
