import math

def insertion_sort(A, p, r):
    for j in xrange(p+1, r+1):
        key = A[j]
        i = j-1
        while i >= p and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
            A[i+1] = key

def merge(A, p, q, r):
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
            
def merge_sort(A, p, r):
    if p < r:
        q = (p+r)/2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    
def mixed_sort(A, p, r):
    if r - p < 2:
        insertion_sort(A, p, r)
    else:
        #q = int((p+r)/2)
        #mixed_sort(A, p, q)
        #mixed_sort(A, q + 1, r)
        #merge(A, p, q, r)
        merge_sort(A, p, r)

A = [8, 7, 6, 5, 4, 3, 2, 1]
mixed_sort(A, 0, 7)
print A
