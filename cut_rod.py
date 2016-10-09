def cut_rod(p, n):
    if n == 0:
        return 0
    q = float("-inf")
    for i in xrange(n):
        q = max(q, p[i] + cut_rod(p, n-i-1))
    return q

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 8 
print cut_rod(p, n)
