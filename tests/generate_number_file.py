from random import randint


N = int(input("Strings:"))
n = int(input("Columns:"))
m = int(input("Max:"))

with open("generated_numbers.txt", 'w') as file:
    for i in range(N):
        file.write(' '.join([str(randint(1, m)) for _ in range(n)]) + '\n')
