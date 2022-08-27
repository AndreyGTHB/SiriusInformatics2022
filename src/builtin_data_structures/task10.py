# n = int(input())
# x_coords = set()
# y_coords = set()
# for i in range(n):
#     x, y = input().split()
#     x_coords.add(int(x))
#     y_coords.add(int(y))
# x_coords.remove(min(x_coords))
# y_coords.remove(min(y_coords))
# lines_x = []
# lines_y = []
# count = 0
# for x in x_coords:
#     lines_x.append(x)
#     count += 1
# for y in y_coords:
#     if count == n - 1:
#         break
#     lines_y.append(y)
#     count += 1
#
# print(count)
# for line_x in lines_x:
#     print('x', line_x)
# for line_y in lines_y:
#     print('y', line_y)

n = int(input())
points = list()
x_coords = set()
y_coords = set()
for i in range(n):
    xx, yy = map(int, input().split())
    points.append([xx, yy])
points.sort()
for i in range(n - 1):
    if points[i + 1][0] == points[i][0] and points[i + 1][1] > points[i][1]:
        y_coords.add(points[i][1] + 1)
    else:
        x_coords.add(points[i][0] + 1)
print(len(x_coords) + len(y_coords))
for x in x_coords:
    print('x', x)
for y in y_coords:
    print('y', y)
