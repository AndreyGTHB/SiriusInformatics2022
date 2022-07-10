from merge_sorting import msorted

n = int(input())
lst = [int(num) for num in input().split(' ')]

print(*msorted(lst))
