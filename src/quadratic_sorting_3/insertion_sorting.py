def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i - 1
        value = nums[i]
        while j >= 0 and value < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = value


a = [2, 6, 1, 7, 6, 8, 10]
insertion_sort(a)
print(a)
