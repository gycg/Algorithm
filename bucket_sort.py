def insertion_sort(A):
    for j in xrange(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A

def bucket_sort(A):
    n = len(A)
    B = [[] for x in range(len(A))]
    for i in xrange(n):
        B[int(n*A[i])].append(A[i])
    out = []
    for buck in B:
        out += insertion_sort(buck)
    return out
        

A = [.31, .41, .59, .26, .41, .58]
print bucket_sort(A)
