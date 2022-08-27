n = int(input())
lst = [int(input()) for _ in range(n)]


dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i-1] + lst[i-1]

imin = 1
ibest = 1
jbest = 1
for j in range(2, n + 1):
    if dp[j-1] <= dp[imin-1]:
        imin = j
    if dp[j] - dp[imin-1] > dp[jbest] - dp[ibest-1]:
        jbest = j
        ibest = imin

print(ibest, jbest)
