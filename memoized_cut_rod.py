def memoized_cut_rod(p, n):
    r = [0]*(n+1)
    for i in xrange(n+1):
        r[i] = float("-inf")
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float("-inf")
        for i in xrange(n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-i-1, r))
    r[n] = q
    return q

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 8
print memoized_cut_rod(p, n)

