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

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q-1, i)
    else:
        return randomized_select(A, q+1, r, i-k)

A = [2, 8, 7, 1, 3, 5, 6, 4]
print randomized_select(A, 0, 7, 5)
