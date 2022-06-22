n = int(input())

dp = [[0 for _ in range(10)]]
dp[0][9] = 1

l = 1
while True:
    dp.append([0])
    for j in range(1, 10):
        dp[l].append(sum(dp[l - 1][j:]))
    nums = sum(dp[l])
    if nums >= n:
        break
    n -= nums
    l += 1
dp[0][9] = 0

x = 0
curr = 1
for i in range(l):
    nums = dp[l-i][curr]

    while nums < n:
        curr += 1
        n -= nums
        nums = dp[l - i][curr]
    x = (x * 10 + curr) % 1000000007

print(x)




