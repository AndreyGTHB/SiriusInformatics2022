n, k, m = map(int, input().split())
lst = list(map(int, input().split()))


p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i-1] + lst[i-1]

result = 0
for i in range(n - k):
    if p[i+k+1] - p[i] == m:
        result = i + 1
        break
print(result)
