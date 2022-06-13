from random import randint


N = int(input())
n = int(input())
m = int(input())

with open("generated_numbers.txt", 'w') as file:
    for i in range(N):
        file.write(' '.join([str(randint(1, m)) for _ in range(n)]) + '\n')
