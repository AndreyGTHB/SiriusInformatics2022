def smaller_count(a, x):
    l = -1
    r = len(a)
    while r - l > 1:
        m = (r + l) // 2
        if a[m] <= x:
            l = m
        else:
            r = m
    return r


N = int(input())
lst = sorted((int(el) for el in input().rstrip().split()))
M = int(input())
reqs = [int(el) for el in input().rstrip().split()]

print(*[smaller_count(lst, req) for req in reqs])
