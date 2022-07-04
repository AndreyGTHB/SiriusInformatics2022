from effective_sorting_4.merge_sorting import merge_sorted
from quadratic_sorting_3.bubble_sorting import bubble_sort
from random import randint
from time import time

start_time = time()
a = [randint(1, 12345) for _ in range(1000)]

# Checking a time needed to generate a list
first_point = time()
print(f"First control point: {first_point - start_time}")

merge_sorted(a)

# Checking a time needed to sort the list
second_point = time()
print(f"Second control point: {second_point - first_point}")

print(f"Work time: {second_point - start_time}.")
