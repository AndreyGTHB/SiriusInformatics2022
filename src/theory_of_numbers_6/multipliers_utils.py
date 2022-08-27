from math import sqrt


def gcd(a, b):
    """
    Finding the greatest common divisor of two numbers.
    :param a: first number
    :param b: second number
    :return: GCD(a, b)
    """
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Finding the lowest common multiple of two numbers.
    :param a: a first number
    :param b: a second number
    :return: LCM(a, b)
    """
    return a * b / gcd(a, b)


def gcd_ext(a, b) -> (int, int, int):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = gcd_ext(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return d, x, y


def factor(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        result.append(n)
    return result

