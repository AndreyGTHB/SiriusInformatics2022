N = int(input())

dp = [[1] * (N + i if i < N else 3 * N - i - 2) for i in range(2 * N - 1)]

for i in range(1, 2 * N - 1):
    for j in range(len(dp[i])):
        dp[i][j] = 0
        first = j == 0
        last = j == len(dp[i]) - 1
        if not first:
            dp[i][j] += dp[i][j-1]
        if len(dp[i]) > len(dp[i-1]):
            if not first:
                dp[i][j] += dp[i-1][j-1]
            if not last:
                dp[i][j] += dp[i-1][j]
        else:
            dp[i][j] += dp[i-1][j] + dp[i-1][j+1]

print(dp[2*N-2][N-1])
