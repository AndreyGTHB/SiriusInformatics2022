n = int(input())
carriages = [int(el) for el in input().split()]
carriages.reverse()

result = []
stack = []
i = 1
lead = 0
withdraw = 0
while carriages or stack:
    if not stack or (carriages and carriages[-1] < stack[-1]):
        if withdraw:
            result.append('2 ' + str(withdraw))
            withdraw = 0
        stack.append(carriages.pop())
        lead += 1
    elif stack[-1] == i:
        if lead:
            result.append('1 ' + str(lead))
            lead = 0
        stack.pop()
        i += 1
        withdraw += 1
    else:
        print(0)
        exit()
if lead:
    result.append('1 ' + str(lead))
elif withdraw:
    result.append('2 ' + str(withdraw))
print(*result, sep='\n')
