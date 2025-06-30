from egz2atesty import runtests

def coal( A, T ):
    # tu prosze wpisac wlasna implementacje
    magazyny = [0 for _ in range(len(A))]
    gdzie = [-1 for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A)):
            if magazyny[j]+A[i] <= T:
                magazyny[j] += A[i]
                gdzie[i] = j
                break

    return gdzie[-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = False )
