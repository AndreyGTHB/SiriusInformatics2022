stack1 = []
stack2 = []


def push(el):
    if len(stack1) == 0 and len(stack2) != 0:
        for _ in range(len(stack2)):
            stack1.append(stack2.pop())
    stack1.append(el)


def pop():
    if len(stack2) == 0:
        if len(stack1) == 0:
            return "error"
        for _ in range(len(stack1)):
            stack2.append(stack1.pop())
    return stack2.pop()


def front():
    if len(stack1) == 0:
        if len(stack2) == 0:
            return "error"
        return stack2[-1]
    return stack1[0]


def size():
    return max(len(stack1), len(stack2))


def clear():
    global stack1
    global stack2
    stack1 = []
    stack2 = []
    return "ok"


command_dict = {
    "pop": pop,
    "front": front,
    "size": size,
    "clear": clear
}
protocol = []
while True:
    cmd = input().split()
    if cmd[0] == "push":
        push(int(cmd[1]))
        protocol.append("ok")
        continue
    if cmd[0] == "exit":
        protocol.append("bye")
        break
    protocol.append(command_dict[cmd[0]]())
print(*protocol, sep='\n')
