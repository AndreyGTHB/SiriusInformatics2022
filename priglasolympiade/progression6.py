def mod(n):
    if n < 0:
        return -n
    return n


def main():
    a = int(input())
    b = int(input())
    c = int(input())

    x = mod(a - b)
    y = mod(b - c)

    if x == y:
        if a > c:
            print(a + x, 1, sep='\n')
        else:
            print(c + x, 4, sep='\n')
    elif x > y:
        print((a + b) // 2, 2, sep='\n')
    elif x < y:
        print((b + c) // 2, 3, sep='\n')


if __name__ == "__main__":
    main()
