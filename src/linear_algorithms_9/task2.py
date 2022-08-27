n, K = [int(el) for el in input().split()]
lst = [int(el) for el in input().split()]
K += 1


i = 0
j = K
imax = 0
for k in range(j + 1, n):
    if lst[k - K] > lst[imax]:
        imax = k - K
    if lst[imax] + lst[k] > lst[i] + lst[j]:
        i = imax
        j = k

print(i + 1, j + 1)
