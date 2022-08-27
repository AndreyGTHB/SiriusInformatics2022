from bisect import bisect_left, bisect_right


n = int(input())
lst = sorted([int(input()) for _ in range(n)])

result = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        max_length = lst[i] + lst[j]
        ub = bisect_left(lst, max_length)
        result += (ub - j - 1)
if result < 0:
    result = 0
print(result)
