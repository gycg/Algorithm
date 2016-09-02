def insertion_sort(A):
    for j in xrange(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

A = [31, 41, 59, 26, 41, 58]
insertion_sort(A)
print A
