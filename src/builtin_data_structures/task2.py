string = input()
string_set = set()
result = ''
for char in string:
    if char not in string_set:
        result += char
        string_set.add(char)
print(result)
