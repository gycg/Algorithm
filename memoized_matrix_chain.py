def memoized_matrix_chain(p):
    n = len(p) - 1
    m = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            m[i][j] = float("inf")
    return lookup_chain(m, p, 0, n-1)

def lookup_chain(m, p, i, j):
    if m[i][j] < float("inf"):
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k+1, j) + p[i]*p[k+1]*p[j+1]
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]

p = [30, 35, 15, 5, 10, 20, 25]
print memoized_matrix_chain(p)
