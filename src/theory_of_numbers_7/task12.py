n = int(input())

decomp = dict()
for i in range(2, n + 1):
    x = i
    d = 2
    while d * d <= x:
        if x % d == 0:
            if d not in decomp.keys():
                decomp[d] = 0
            while x % d == 0:
                decomp[d] += 1
                x //= d
        d += 1
    if x > 1:
        if x not in decomp.keys():
            decomp[x] = 0
        decomp[x] += 1

result = 1
for exp in decomp.values():
    result *= exp + 1
print(result)
