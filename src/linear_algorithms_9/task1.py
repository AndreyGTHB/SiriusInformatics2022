n = int(input())
lst = [int(el) for el in input().rstrip().split()]


imin = 0
i = -1
j = -1
max_res = 1
for k in range(1, n):
    if lst[k-1] < lst[imin]:
        imin = k - 1
    if lst[k] / lst[imin] > max_res:
        max_res = lst[k] / lst[imin]
        i = imin
        j = k

print(i + 1, j + 1)
