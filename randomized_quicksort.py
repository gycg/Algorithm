def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in xrange(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def randomized_partition(A, p, r):
    from random import randrange
    i = randrange(p, r+1, 1)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1)
        randomized_quicksort(A, q+1, r)

A = [2, 8, 7, 1, 3, 5, 6, 4]
randomized_quicksort(A, 0, 7)
print A
