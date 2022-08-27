def gcd_ext(a, b) -> (int, int, int):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = gcd_ext(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return d, x, y


a, b, c = (int(el) for el in input().rstrip().split())

d, x0, _ = gcd_ext(a, b)
attitude = c // d
if c % d:
    print(-1)
else:
    x = (x0 * attitude) % (b // d)
    y = (c - a * x) // b
    print(x, y)
