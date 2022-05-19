N = int(input())

dp = dict()
dp[1] = 0


def calculator(n):
    if n not in dp:
        m1 = calculator(n-1)
        if n % 2 != 0:
            if n % 3 != 0:
                dp[n] = m1 + 1
            else:
                dp[n] = min(m1, calculator(n//3)) + 1
        else:
            if n % 3 != 0:
                dp[n] = min(m1, calculator(n//2)) + 1
            else:
                dp[n] = min(m1, calculator(n//2), calculator(n//3)) + 1
    return dp[n]


print(calculator(N))
