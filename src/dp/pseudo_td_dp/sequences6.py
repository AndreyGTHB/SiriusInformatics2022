N = int(input())

dp = [[-1, -1, -1] for _ in range(N+1)]
dp[1] = [0, 1, 1]


for i in range(2, N+1):
    if -1 in dp[i]:
        dp[i][0] = dp[i-1][1]
        dp[i][1] = dp[i-1][2]
        dp[i][2] = sum(dp[i-1])


print(sum(dp[N]))
