ins = input().split(' ')
K = int(ins[0])
P = int(ins[1])

dp = [0 for i in range(K+1)]
dp[1] = 0
if K > 1:
    dp[2] = 1

if K > 2:
    for i in range(3, K+1):
        dp[i] = dp[i-1]
        if i % 2 == 0:
            dp[i] += dp[i//2]

print(dp[K] % P)

