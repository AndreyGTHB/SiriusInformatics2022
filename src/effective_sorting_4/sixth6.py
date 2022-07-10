n = int(input())
lst = [int(el) for el in input().rstrip().split()]

print(*sorted(lst, key=lambda it: sum([int(el) for el in str(it)]), reverse=True))
