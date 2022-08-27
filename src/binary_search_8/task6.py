from bisect import bisect_left, bisect_right


n, k = [int(el) for el in input().split()]
a = [int(el) for el in input().split()]
b = [int(el) for el in input().split()]

for x in b:
    lower = bisect_left(a, x) + 1
    upper = bisect_right(a, x)
    if upper == 0 or a[upper-1] != x:
        print(0)
    else:
        print(lower, upper)
