def naive_string_matcher(T, P):
	n = len(T)
	m = len(P)
	for s in xrange(n-m):
		if P == T[s:s+m]:
			print "Pattern occurs with shift %d" % (s)

T = "asdfgh"
P = "asd"
naive_string_matcher(T, P)
