def rabin_karp_matcher(T, P, d, q):
	n = len(T)
	m = len(P)
	h = d**(m-1) % q
	p = 0
	t = 0
	for i in range(m):
		p = (d*p + int(P[i])) % q
		t = (d*t + int(T[i])) % q
	for s in range(n-m+1):
		if p == t:
			if P == T[s:s+m]:
				print "Pattern occurs with shift %d" % (s)
		if s < n-m:
			t = (d*(t-int(T[s])*h) + int(T[s+m])) % q

T = "2359023141526739921"
P = "31415"
d = 10
q = 13
rabin_karp_matcher(T, P, d, q)
