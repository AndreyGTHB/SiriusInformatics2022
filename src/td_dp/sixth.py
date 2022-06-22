L = input()
R = input()

dp = [[0 for _ in range(10)] for _ in range(len(R) + 1)]
dp[1] = [1] * 10

for i in range(2, len(R) + 1):
    for j in range(1, 10):
        dp[i][j] = sum(dp[i - 1][j:])


def nums(n):
    sn = str(n)
    l = len(sn)
    result = 0
    for dps in dp[1:l]:
        result += sum(dps)

    prev = 1
    good = True
    for i in range(l):
        curr = int(sn[i])
        if curr < prev:
            good = False
            break
        for j in range(prev, curr):
            result += dp[l-i][j]
        prev = curr

    if good:
        result += 1

    return result


a = nums(int(R))
b = nums(int(L) - 1)
print((a - b) % 1000000007)
