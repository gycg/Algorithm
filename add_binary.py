def add_binary(a, b):
    c = [0]*(len(a)+1)
    carry = 0
    for i in xrange(len(a)):
        c[i] = (a[i] + b[i] + carry) % 2
        carry = (a[i] + b[i] + carry) /2
    c[i+1] = carry
    return c

a = [1, 1, 1]
b = [1, 1, 1]
print add_binary(a, b)
