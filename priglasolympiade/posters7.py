def main():
    n = int(input())
    a = int(input())
    b = int(input())

    print(n // a + n // b - n // (a * b))


if __name__ == "__main__":
    main()
