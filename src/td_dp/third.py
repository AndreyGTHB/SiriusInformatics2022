ins = input().split(' ')
N = int(ins[0])
M = int(ins[1])
cst = []

for i in range(N):
    ins = input().split(' ')
    mapped_numbers = list(map(lambda s: s.strip(), ins))
    filtered = filter(lambda s: s != '', mapped_numbers)

    line = []
    for n in filtered:
        cost = 0
        # try:
        cost = int(n)
        # except:
        #     pass
        line.append(cost)
    cst.append(line)

inf = 0
dp = [[inf for _ in range(M)] for _ in range(N)]
dp[0][0] = cst[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + cst[0][j]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + cst[i][0]
# print(cst)
# print(dp)

if N > 1:
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = cst[i][j] + min(dp[i-1][j], dp[i][j-1])

# print(dp)
print(dp[N-1][M-1])
