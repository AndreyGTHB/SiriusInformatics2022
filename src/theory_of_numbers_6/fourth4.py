a, b, d = (int(el) for el in input().rstrip().split())

average = (a + b) / 2
if average.is_integer():
    average = int(average)
    print(average, min(average % d, d - average % d))
else:
    x = int(average + 0.5)
    y = int(average - 0.5)
    distance_x = min(x % d, d - x % d)
    distance_y = min(y % d, d - y % d)
    if distance_x < distance_y:
        print(x, distance_x)
    else:
        print(y, distance_y)
