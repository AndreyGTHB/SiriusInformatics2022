N = int(input())
nums = []
for el in input().split(' '):
    nums.append(int(el))

dp = [None] * (N + 1)
dp[0] = 0
dp[1] = nums[0]


def stairs(n):
    if dp[n] is None:
        dp[n] = max(stairs(n-2), stairs(n-1)) + nums[n-1]
    return dp[n]


print(stairs(N))
