n = int(input())
lst = list(map(int, input().split()))


s = [-1] * 3
e = [-1] * 3
p = 0
max_length = 0
_max = -1
m = 0
for i in range(n):
    if s[m] < 0:
        s[m] = i
    p += lst[i]
    m = p % 3
    if s[m] >=0:
        e[m] = i
        if i - s[m] + 1 > max_length:
            max_length = i - s[m] + 1
            _max = m
if _max >=0:
    print(s[_max] + 1, e[_max] + 1)
else:
    print(_max)
