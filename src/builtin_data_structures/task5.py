n = int(input())

clients = dict()
output = []
for _ in range(n):
    req = input().split()
    cmd = req[0]
    args = req[1:]

    if cmd == "DEPOSIT":
        clients[args[0]] = clients.get(args[0], 0) + int(args[1])
    if cmd == "WITHDRAW":
        clients[args[0]] = clients.get(args[0], 0) - int(args[1])
    if cmd == "BALANCE":
        output.append(clients.get(args[0], "ERROR"))
    if cmd == "TRANSFER":
        clients[args[0]] = clients.get(args[0], 0) - int(args[2])
        clients[args[1]] = clients.get(args[1], 0) + int(args[2])
    if cmd == "INCOME":
        for name in clients:
            if clients[name] > 0:
                clients[name] += (clients[name] * int(args[0])) // 100
print(*output, sep='\n')
