from numpy import matrix
from numpy import zeros
def squre_matrix_multiply(A, B):
    n = A.shape[0]
    C = zeros(shape=(n,n))
    for i in xrange(n):
        for j in xrange(n):
            C[i, j] = 0
            for k in xrange(n):
                C[i, j] = C[i, j] + A[i, k] * B[k, j]
    return C

A = matrix('1 0 0; 0 1 0; 0 0 1')
B = matrix('0 0 1; 0 1 0; 1 0 0')
print squre_matrix_multiply(A, B)
