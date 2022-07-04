def merge_sorted(lst):
    n = len(lst)
    if n == 1:
        return lst
    center = n // 2
    a = merge_sorted(lst[:center])
    b = merge_sorted(lst[center:])
    return merge(a, b)


def merge(a, b):
    la = len(a)
    lb = len(b)
    i = 0
    j = 0
    result = []
    while i < la or j < lb:
        if j == lb or (i < la and a[i] < b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result
