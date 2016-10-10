from numpy import matrix
from numpy import zeros
def matrix_multiply(A, B):
    Arow = A.shape[0]
    Acol = A.shape[1]
    Brow = B.shape[0]
    Bcol = B.shape[1]
    if Acol != Brow:
        print "incompatible dimensions"
    else:
        C = zeros(shape=(Arow, Bcol))
        for i in xrange(Arow):
            for j in xrange(Bcol):
                C[i, j] = 0
                for k in xrange(Acol):
                    C[i, j] = C[i, j] + A[i, k] * B[k, j]
        return C

A = matrix('1 0 0; 0 1 0; 0 0 1; 1 2 3')
B = matrix('0 0 1 1; 0 1 0 2; 1 0 0 3')
print matrix_multiply(A, B)


