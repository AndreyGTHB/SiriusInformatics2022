from random import randint, choice

l = 1
h = 100000
a = 1
b = 1000000

with open("data.txt", 'w') as file:
    file.writelines([' '.join([choice(['+', '*']) + ' ' + str(randint(a, b)) for _ in range(l)]) + '\n' for _ in range(h)])
