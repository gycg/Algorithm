def bubble_sort(A):
    for i in xrange(len(A)-1):
        for j in xrange(len(A)-1, i, -1):
            k = j-1
            if A[j] < A[k]:
                A[j-1], A[j] = A[j], A[j-1]

A = [8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(A)
print A
