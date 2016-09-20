def minimum(A):
    min = A[0]
    for i in xrange(1, len(A)):
        if min > A[i]:
            min = A[i]
    return min

A = [6, 5, 7, 3, 8, 4, 5]
print minimum(A)
