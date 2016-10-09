def bottom_up_cut_rod(p, n):
    r = [0]*(n+1)
    r[0] = 0
    for j in xrange(1, n+1):
        q = float("-inf")
        for i in xrange(1, j+1):
            q = max(q, p[i-1] + r[j-i-1])
        r[j-1] = q
    return r[n-1]

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 8
print bottom_up_cut_rod(p, n)

