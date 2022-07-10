x = int(input())

result = 0
i = 1
j = 1
while x > 0:
    a = i**2
    b = j**3
    if a == b:
        i += 1
        continue
    if a < b:
        result = a
        i += 1
    else:
        result = b
        j += 1
    x -= 1

print(result)
