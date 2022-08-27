from collections import deque
d = deque()


def pop_front():
    if len(d) == 0:
        return "error"
    return d.popleft()


def pop_back():
    if len(d) == 0:
        return "error"
    return d.pop()


def front():
    if len(d) == 0:
        return "error"
    return d[0]


def back():
    if len(d) == 0:
        return "error"
    return d[-1]


def size():
    return len(d)


cmd_map = {
    "push_front": d.appendleft,
    "push_back": d.append,
    "pop_front": pop_front,
    "pop_back": pop_back,
    "front": front,
    "back": back,
    "size": size,
    "clear": d.clear,
}

result = []
while True:
    cmd = input().split()
    if cmd[0] == "exit":
        result.append("bye")
        break
    if len(cmd) > 1:
        answer = cmd_map[cmd[0]](int(cmd[1]))
    else:
        answer = cmd_map[cmd[0]]()
    if answer is None:
        answer = "ok"
    result.append(answer)
print(*result, sep="\n")
