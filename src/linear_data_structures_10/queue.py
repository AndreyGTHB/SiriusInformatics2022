def flip(q):
    s1, s2 = q
    for _ in range(len(s2)):
        s1.append(s2.pop())


def push(q: (list, list), el):
    s1, s2 = q
    s2.append(el)


def pop(q: (list, list)):
    s1, s2 = q
    if not s1:
        flip(q)
    return s1.pop()


def first(q: (list, list)):
    s1, s2 = q
    if not s1:
        flip(q)
    return s1[-1]


def size(q: (list, list)):
    s1, s2 = q
    return len(s1) + len(s2)


def clear(q: (list, list)):
    q = ([], [])
