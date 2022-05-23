from dp.calculator4 import calculator
import time


N = int(input())

start_time = time.time()
result = calculator(N)
work_time = time.time() - start_time

print(result)
print("--- %s seconds ---" % work_time)
