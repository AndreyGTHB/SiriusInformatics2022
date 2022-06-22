ins = input().split(' ')
N = int(ins[0])
M = int(ins[1])
cost = []
for i in range(N):
    ins = input().split(' ')
    cost.append([int(num) for num in ins])

dp = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][1] = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i-1][j-1]

path = []
i = N
j = M
while i > 1 or j > 1:
    if dp[i-1][j] > dp[i][j-1]:
        path.insert(0, 'D')
        i -= 1
    else:
        path.insert(0, 'R')
        j -= 1

print(dp[N][M])
print(*path)
