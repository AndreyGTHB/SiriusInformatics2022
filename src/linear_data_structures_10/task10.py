from math import ceil


n = int(input().rstrip())

queue = []
result = []
for _ in range(n):
    req = input().split()
    if req[0] == '+':
        queue.append(req[1])
    elif req[0] == '*':
        queue.insert(ceil(len(queue) / 2), req[1])
    else:
        result.append(queue[0])
        del queue[0]
print(*result, sep='\n')
