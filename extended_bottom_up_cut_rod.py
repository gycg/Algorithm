def extended_bottom_up_cut_rod(p, n):
    r = [0]*(n+1)
    s = [0]*(n+1)
    r[0] = 0
    for j in xrange(1, n+1):
        q = float("-inf")
        for i in xrange(1, j+1):
            if q < p[i-1] + r[j-i-1]:
                q = p[i-1] + r[j-i-1]
                s[j] = i
        r[j-1] = q
    return r[n-1], s

def print_cut_rod_solution(p, n):
    (r, s) = extended_bottom_up_cut_rod(p, n)
    while n>0:
        print s[n]
        n = n - s[n]

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 8 
print extended_bottom_up_cut_rod(p, n)
print_cut_rod_solution(p, n)
