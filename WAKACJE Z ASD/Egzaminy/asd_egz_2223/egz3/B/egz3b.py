from egz3btesty import runtests


# Rozwiązanie o(n^2)
def uncool( P ):
  def contained_or_disjoined(a1,b1,a2,b2):
    #Zawieranie się
    if (a1 <= a2 and b1 >= b2) or (a2 <= a1 and b2 >= b1):
      return True
    #Rozłączność
    if b1 < a2 or b2 < a1:
      return True
    return False
  
  for i in range(len(P)):
    a1,b1, = P[i]
    for j in range(i+1,len(P)):
      if i!=j:
        a2,b2 = P[j]
        if not contained_or_disjoined(a1,b1,a2,b2):
          return i,j

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = False )
