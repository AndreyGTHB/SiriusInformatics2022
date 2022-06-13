N = int(input())
a = []
b = []
c = []
for i in range(N):
    ins = input().split(' ')
    a.append(int(ins[0]))
    b.append(int(ins[1]))
    c.append(int(ins[2]))

dp = [-1 for _ in range(N)]
dp[0] = a[0]
if N > 1:
    dp[1] = min(dp[0] + a[1], b[0])
if N > 2:
    dp[2] = min(dp[1] + a[2], dp[0] + b[1], c[0])
if N > 3:
    for i in range(3, N):
        dp[i] = min(
            dp[i-1] + a[i],
            dp[i-2] + b[i-1],
            dp[i-3] + c[i-2]
        )

print(dp[N-1])
