def main():
    n = int(input())

    number = 1
    for i in range(n):
        number += int(str(number)[-1])
        print(f"{i+1}: {number}")
    print(f"{n}: {number}")


if __name__ == "__main__":
    main()
