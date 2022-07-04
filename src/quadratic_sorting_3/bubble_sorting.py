def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        ordered = True
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                ordered = False
        if ordered:
            break
