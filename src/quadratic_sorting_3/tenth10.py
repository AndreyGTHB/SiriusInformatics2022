N = int(input())
students = []
for _ in range(N):
    inputs = input().split()
    students.append([int(inputs[0]), int(inputs[1])])

for i in range(1, N):
    number = students[i][0]
    points = students[i][1]
    for j in range(i - 1, -2, -1):
        if j < 0 or students[j][1] > points or (students[j][1] == points and students[j][0] < number):
            students[j+1] = [number, points]
            break
        students[j+1] = [students[j][0], students[j][1]]

for student in students:
    print(*student)
