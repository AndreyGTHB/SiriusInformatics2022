ins = input().split(' ')
N = int(ins[0])
M = int(ins[1])

dp = [[1] * M] * N
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[N-1][M-1])
