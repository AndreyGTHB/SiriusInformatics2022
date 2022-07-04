string = input()

counts = [0] * 10
for ch in string:
    if ch.isdigit():
        counts[int(ch)] += 1

number = ''
for i in range(10):
    number += str(9 - i) * counts[9-i]

print(number)
