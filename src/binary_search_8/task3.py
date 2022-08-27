n, k = [int(el) for el in input().rstrip().split()]
a = [int(el) for el in input().rstrip().split()]
b = [int(el) for el in input().rstrip().split()]

for x in b:
    l = -1
    r = n
    if n == 1:
        print(a[0])
        continue
    while r - l > 1:
        m = (l + r) // 2
        if a[m] < x:
            l = m
        else:
            r = m
    if r < n and abs(a[r] - x) < abs(a[l] - x):
        print(a[r])
    else:
        print(a[l])
