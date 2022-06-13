# N = int(input())
#
# coords = input()
# coords = [int(c) for c in coords.split(' ')]
# coords.sort()
#
# dp = [-1 for _ in range(N+1)]
# dp[1] = 0
# dp[2] = coords[1] - coords[0]
# dp[3] = coords[2] - coords[0]
#
# for i in range(2, N+1):
#     if dp[i] == -1:
#         dp[i] = min(dp[i-2], dp[i-1]) + coords[i-1] - coords[i-2]
#
# print(dp[N])

N = int(input())
coords = [int(i) for i in input().split()]
coords.sort()
dp = [-1 for _ in range(N)]
dp[1] = coords[1] - coords[0]
if N > 2:
    dp[2] = coords[2] - coords[0]
    for i in range(3, N):
        dp[i] = min(dp[i - 2], dp[i - 1]) + coords[i] - coords[i - 1]
print(dp[N - 1])
