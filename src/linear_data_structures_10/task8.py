INF = 20000


def __flip(q, mq):
    s1, s2 = q
    ms1, ms2 = mq
    for _ in range(len(s2)):
        el = s2.pop()
        s1.append(el)
        ms2.pop()
        ms1.append(el if not ms1 or el < ms1[-1] else ms1[-1])


def push(q, mq, el):
    s1, s2 = q
    ms1, ms2 = mq
    s2.append(el)
    ms2.append(el if not ms2 or el < ms2[-1] else ms2[-1])


def pop(q, mq):
    s1, s2 = q
    ms1, ms2 = mq
    if not s1:
        __flip(q, mq)
    ms1.pop()
    return s1.pop()


def first(q, mq):
    s1, s2 = q
    if not s1:
        __flip(q, mq)
    return s1[-1]


def size(q):
    s1, s2 = q
    return len(s1) + len(s2)


def get_min(mq):
    ms1, ms2 = mq
    if not ms1:
        if not ms2:
            return INF
        ms1 = [INF]
    if not ms2:
        ms2 = [INF]
    return min(ms1[-1], ms2[-1])


n = int(input())
requests = (int(input()) for _ in range(n))

result = []
queue = ([], [])
mqueue = ([], [])
combined = (queue, mqueue)
for req in requests:
    if req == 0:
        if not size(queue):
            result.append(-1)
        else:
            result.append(get_min(mqueue))
            pop(*combined)
        continue
    push(*combined, req)
print(*result, sep='\n')
