a, b = [int(el) for el in input().split()]
n = b - 1

prime = [True] * (n + 1)
prime[0] = prime[1] = False
for i in range(2, n + 1):
    if not prime[i]:
        continue
    for j in range(i * i, n + 1, i):
        prime[j] = False
prime_list = []
for i in range(2, n + 1):
    if prime[i]:
        prime_list.append(i)

n = len(prime_list)
result = []
for i in prime_list:
    for j in prime_list:
        if a <= i + j <= b:
            result.append(i + j)

print(*sorted(list(set(result))), sep='\n')

