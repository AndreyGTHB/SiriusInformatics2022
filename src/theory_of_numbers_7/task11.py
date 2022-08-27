def solution(n):
    deuces_count = 0
    while n % 2 == 0:
        deuces_count += 1
        n //= 2
    if deuces_count == 1:
        print("prime")
        return

    decomp = [2] * deuces_count
    other = 1
    prime = n
    d = 3
    while d * d <= n:
        if n % d == 0:
            prime = d
            other = n // d
            break
        d += 2
    if other == 1:
        decomp[0] *= prime
        print("single")
        print(*decomp)
        return
    decomp1 = [2] * deuces_count
    decomp[0] *= other * prime
    decomp1[0] *= other
    decomp1[1] *= prime
    print("many")
    print(*decomp)
    print(*decomp1)


n = int(input())
solution(n)

