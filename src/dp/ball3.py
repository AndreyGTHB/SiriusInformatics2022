N = int(input())

if N < 2:
    dp = [-1, -1, -1]
else:
    dp = [-1] * (N+1)
dp[0] = dp[1] = 1
dp[2] = 2


def ball_options(n):
    if dp[n] == -1:
        dp[n] = ball_options(n-3) + ball_options(n-2) + ball_options(n-1)
    return dp[n]


print(ball_options(N))
