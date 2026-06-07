e = 65537
p = 17
q = 23
n = p * q
m = 12

c = pow(m, e, n)
print(c)
