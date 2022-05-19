N = int(input())
dp = [-1] * (N + 1)
dp[0] = 0
dp[1] = 1


def F(n):
    if dp[n] == -1:
        dp[n] = F(n - 2) + F(n - 1)
    return dp[n]


print(F(N))
