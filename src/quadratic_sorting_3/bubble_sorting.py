# first_in = input()
second_in = input().split(' ')
if second_in[-1] == '':
    del second_in[-1]

numbers = [int(num) for num in second_in]
n = len(numbers)  # int(first_in)


def bubble_sort(nums):
    l = len(nums)
    count = 0
    for i in range(l):
        ordered = True
        for j in range(l - i - 1):
            if nums[j] > nums[j + 1]:
                count += 1
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                ordered = False
        if ordered:
            break
    print(count)


bubble_sort(numbers)
print(*numbers)

