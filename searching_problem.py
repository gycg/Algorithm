def search(A, v):
    for i in xrange(len(A)):
        if A[i] == v:
            return i
    return None

A = [1, 2, 3, 4]
v = 5 
print search(A, v)
