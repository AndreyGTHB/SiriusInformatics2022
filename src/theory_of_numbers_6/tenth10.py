def factorization(n: int):
    result = dict()
    multiple = 2
    number = n
    while multiple * multiple <= number:
        if number % multiple:
            multiple += 1 if multiple == 2 else 2
        else:
            number //= multiple
            if multiple not in result.keys():
                result[multiple] = 0
            result[multiple] += 1
    if number > 1:
        if number not in result.keys():
            result[number] = 0
        result[number] += 1
    return result


a = int(input())

multipliers = factorization(a)
result = 1
for m in multipliers:
    result *= m
max_degree = max(multipliers.values()) if multipliers else 1
if max_degree > result:
    result *= 2
print(result)
