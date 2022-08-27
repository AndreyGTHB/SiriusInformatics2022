n = int(input())
mods = []
nums = []
for i in range(n):
    inp = input().split()
    mods.append(int(inp[0]))
    nums.append(int(inp[1]))

for i in range(n):
    result = pow(nums[i], mods[i] - 2, mods[i])
    print(result)
