def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)

a, b = (int(el) for el in input().split())
divisor = gcd(a, b)
print(a // divisor, b // divisor)
