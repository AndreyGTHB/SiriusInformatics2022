N = int(input())
s = []
for _ in range(N):
    s.append(int(input()))


def greatest_subset_length(nums):
    result = 0
    for i in range(len(nums)):
        curr = min(nums[i] - 1, len(nums) - i)
        if result < curr:
            result = curr
    return result


print(greatest_subset_length(s))
