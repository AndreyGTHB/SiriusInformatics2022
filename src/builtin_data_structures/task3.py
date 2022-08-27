input()
a = set(input().split())
input()
b = set(input().split())

diff = a ^ b
print(len(diff))
if diff:
    print(*sorted(diff, key=int))
