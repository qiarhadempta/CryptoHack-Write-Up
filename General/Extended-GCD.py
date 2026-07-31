import math

p = 26513
q = 32321

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

gcd, x, y = extended_gcd(p, q)
print(f"GCD: {gcd}, x: {x}, y: {y}")