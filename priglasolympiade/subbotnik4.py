def inconv(l):
    return max(l) - min(l)


heights = []
with open("s.txt") as f:
    for line in f:
        heights.append(int(line))
heights.sort()

# 1
diff = inconv(heights)
print(f"1: {diff}")

# 2
a = heights[:50]
b = heights[50:]
print(f"2: {max(inconv(a), inconv(b))}")

# 3
brigades = [heights[i*10:(i+1)*10] for i in range(10)]
max_inc = 0
for brigade in brigades:
    inc = inconv(brigade)
    if inc > max_inc:
        max_inc = inc
print(f"3: {max_inc}")

# 4
min_inc = inconv(heights)
for i in range(91):
    inc = heights[i+9] - heights[i]
    if inc < min_inc:
        min_inc = inc
print(f"4: {min_inc}")
