def msorted(lst):
    n = len(lst)
    if n == 1:
        return lst
    center = n // 2
    a = msorted(lst[:center])
    b = msorted(lst[center:])
    return merge(a, b)


def msort(lst):
    n = len(lst)
    if n == 1:
        return
    center = n // 2
    a = lst[:center]
    b = lst[center:]
    msort(a)
    msort(b)
    res = merge(a, b)
    for i in range(n):
        lst[i] = res[i]


def merge(a, b):
    la = len(a)
    lb = len(b)
    i = 0
    j = 0
    result = []
    while i < la and j < lb:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
