n = int(input())
numbers = [int(num) for num in input().split()]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i - 1
        value = nums[i]
        while j >= 0 and value < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = value
        if j + 1 != i:
            print(*nums)


insertion_sort(numbers)
