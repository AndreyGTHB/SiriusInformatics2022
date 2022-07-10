def msort(lst):
    n = len(lst)
    if n == 1:
        return
    center = n // 2
    a = lst[:center]
    b = lst[center:]
    msort(a)
    msort(b)
    res = merge(a, b)
    for i in range(n):
        lst[i] = res[i]


def merge(a, b):
    la = len(a)
    lb = len(b)
    i = 0
    j = 0
    result = []
    while i < la and j < lb:
        if int(a[i] + b[j]) < int(b[j] + a[i]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


n = int(input())
parts = []
for _ in range(n):
    parts.append(input().rstrip())

max_length = len(max(parts, key=lambda it: len(it)))
msort(parts)
print(*parts[::-1], sep='')
