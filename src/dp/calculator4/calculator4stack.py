N = int(input())


dp = dict()
dp[1] = 0


class Stack:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.__data = data.copy()

    def put(self, el):
        self.__data.append(el)

    def pop(self):
        return self.__data.pop()

    def get(self):
        return self.__data[-1]


def calculator(n):
    s = Stack([n])
    while n not in dp:
        curr = s.get()
        if curr in dp:
            s.pop()
            continue

        subtasks = [curr-1, curr/2, curr/3]
        if subtasks[2] % 1 != 0:
            subtasks.pop(2)
        if subtasks[1] % 1 != 0:
            subtasks.pop(1)

        all_subtasks_decided = True
        solutions = []
        for st in subtasks:
            subtask = int(st)
            if subtask in dp:
                solutions.append(dp[subtask])
            else:
                all_subtasks_decided = False
                s.put(subtask)
        if all_subtasks_decided:
            dp[curr] = min(solutions) + 1
            s.pop()

    return dp[n]


print(calculator(N))
