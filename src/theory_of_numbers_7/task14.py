def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


n = int(input())
numbers = [int(el) for el in input().rstrip().split()] + [1]

length = 0
max_length = 0
d = 0
for num in numbers:
    d = gcd(num, d)
    if d > 1:
        length += 1
    else:
        if max_length < length:
            max_length = length
        length = 1
        d = num
print(max_length)
