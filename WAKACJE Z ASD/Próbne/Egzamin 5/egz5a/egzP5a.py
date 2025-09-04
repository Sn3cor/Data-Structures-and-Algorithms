from egzP5atesty import runtests 

def inwestor ( T ):
    n = len(T)
    stack = []
    max_area = 0
    for i in range(n):
        if not stack:
            stack.append((T[i],i))
            continue
        elif stack[-1][0] < T[i]:
            stack.append((T[i],i))
            continue

        else:
            while stack and stack[-1][0] >= T[i]:
                popped = stack.pop()
                width = i if not stack else i-1-stack[-1][1]
                max_area = max(max_area,width*popped[0])
            stack.append((T[i],i))

    while stack:
        popped = stack.pop()
        width = n if not stack else n-1-stack[-1][1]
        max_area = max(max_area,width*popped[0])

    return max_area

runtests ( inwestor, all_tests=True )