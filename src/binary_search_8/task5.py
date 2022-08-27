from bisect import bisect_right


n, k = [int(el) for el in input().split()]
a = [int(el) for el in input().split()]
b = [int(el) for el in input().split()]

for x in b:
    ub = bisect_right(a, x)
    if ub > 0 and a[ub-1] == x:
        print("YES")
    else:
        print("NO")
