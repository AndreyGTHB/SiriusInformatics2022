N = int(input())

dp = [-1 for _ in range(N+1)]
dp[1] = 0


def calculator(n):
    for i in range(2, N+1):
        m = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(m, dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(m, dp[i // 3] + 1)
    return dp[N]


print(calculator(N))
