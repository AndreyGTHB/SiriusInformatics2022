ins = input().split(' ')
x = int(ins[0]) - 1
y = int(ins[1]) - 1

dp = [[0 for _ in range(10)] for _ in range(8)]
dp[7] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]

i = 6
while i >= y:
    for j in range(1, 9):
        dp[i][j] = dp[i+1][j+1] + dp[i+1][j-1]
        if i == y and j == x + 1:
            break
    i -= 1

print(dp[y][x+1])
