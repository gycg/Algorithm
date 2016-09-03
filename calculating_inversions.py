import math
            
def merge_sort(A, p, r):
    inversions = 0
    if p < r:
        q = (p+r)/2
        inversions += merge_sort(A, p, q)
        inversions += merge_sort(A, q+1, r)
        inversions += merge(A, p, q, r)
        return inversions
    else:
        return 0

def merge(A, p, q, r):
    inversions = 0
    L = A[p: q+1]+[float("inf")]
    R = A[q+1:r+1]+[float("inf")]
    i = 0
    j = 0
    for k in xrange(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inversions += len(L) - i - 1
    return inversions

A = [8, 7, 6, 5, 4, 3, 2, 1]
print merge_sort(A, 0, 7)
print A
