def cleaned(lst):
    result = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i-1] != lst[i]:
            result.append(lst[i])
    return result


n = int(input())
lst1 = [int(el) for el in input().rstrip().split()]
m = int(input())
lst2 = [int(el) for el in input().rstrip().split()]

lst1 = cleaned(sorted(lst1))
lst2 = cleaned(sorted(lst2))
if lst1 == lst2:
    print("YES")
else:
    print("NO")

