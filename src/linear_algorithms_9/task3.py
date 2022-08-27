n, x = [int(el) for el in input().rstrip().split()]
p_prices = [int(el) for el in input().rstrip().split()]
s_prices = [int(el) for el in input().rstrip().split()]

if n == 1:
    print(x, "-1 -1", sep='\n')
    exit()

imin = 0
p_day = 0
s_day = 1
for k in range(2, n):
    if p_prices[k-1] < p_prices[imin]:
        imin = k - 1
    best_profit = (s_prices[s_day] - p_prices[p_day]) * (x // p_prices[p_day])
    curr_profit = (s_prices[k] - p_prices[imin]) * (x // p_prices[imin])
    if curr_profit > best_profit:
        s_day = k
        p_day = imin

diff = s_prices[s_day] - p_prices[p_day]
if diff <= 0:
    print(x, "-1 -1", sep='\n')
else:
    shares_count = x // p_prices[p_day]
    summary = x + diff * shares_count
    print(summary)
    print(p_day + 1, s_day + 1)
