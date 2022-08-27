def gdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gdc(a, b)


a, b = (int(el) for el in input().split())
print(lcm(a, b))
