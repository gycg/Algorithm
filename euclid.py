def euclid(a, b):
	if b == 0:
		return a
	else:
		return euclid(b, a % b)

a = 30
b = 21
print euclid(a, b)
