n, m = map(int, input().split())
heights = list(map(int, input().split()))
left = []
right = []
for _ in range(m):
    inp = input().split()
    left.append(int(inp[0]))
    right.append(int(inp[1]))


dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i-1]
    if heights[i-1] > heights[i-2]:
        dp[i] += 1

for j in range(m):
    r = right[j]
    l = left[j]
    print(dp[r] - dp[l])
