N = int(input())


def next_ticket(n):
    if n == 119:
        return "full"
    if n > 116:
        return "21" + "DE"[(n+1) % 118]
    if n < 3:
        return '1' + "DEF"[n]

    nt = n - 2
    q = nt // 6
    r = nt % 6
    if r == 0:
        return str(q + 1) + 'F'
    return str(q + 2) + "ABCDEF"[r-1]


print(next_ticket(N))
