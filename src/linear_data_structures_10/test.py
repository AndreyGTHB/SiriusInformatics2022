

def insert_to_middle(q, el):
    s1, s2 = q
    s3 = []
    queue_size = size(q)
    if queue_size == 0:
        s2.append(el)
        return
    m = ceil(queue_size / 2)
    for _ in range(queue_size):
        if not s1:
            flip(q)
        s3.append(s1.pop())
        m -= 1
        if m == 0:
            s3.append(el)
    q[1].extend(s3)



