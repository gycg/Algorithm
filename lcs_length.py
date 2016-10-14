def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0 for x in xrange(n)] for y in xrange(m)]
    c = [[0 for x in xrange(n+1)] for y in xrange(m+1)]
#    for i in xrange(m+1):
#        c[i][0] = 0
#    for j in xrange(n+1):
#        c[0][j] = 0
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = "lu"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = "u"
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = "l"
    return c, b

def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i-1][j-1] == "lu":
        print_lcs(b, X, i-1, j-1)
        print X[i-1]
    elif b[i-1][j-1] == "u":
        print_lcs(b, X, i-1, j)
    else:
        print_lcs(b, X, i, j-1)

X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']
(c, b) = lcs_length(X, Y) 
print_lcs(b, X, len(X), len(Y))
