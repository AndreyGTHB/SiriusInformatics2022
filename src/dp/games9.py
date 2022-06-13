n = int(input())
coords = []
for c in input().split(' '):
    coords.append(int(c))

dp = [-1 for i in range(n+1)]
dp[1] = 0
dp[2] = abs(coords[1] - coords[0])

for i in range(3, n+1):
    dp[i] = min(dp[i-1] + abs(coords[i-1] - coords[i-2]), dp[i-2] + 3 * abs(coords[i-1] - coords[i-3]))

print(dp[n])
