first_in = input().split()
n = int(first_in[0])
k = int(first_in[1])

nums = [i + 1 for i in range(n)]

i = n - 2
while k != 0:
    if i < 0 or nums[i+1] < nums[i]:
        i = n - 2
    else:
        nums[i+1], nums[i] = nums[i], nums[i+1]
        i -= 1
        k -= 1

print(*nums)
