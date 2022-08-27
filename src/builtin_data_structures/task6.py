n = int(input())
electors = dict()
first_round = dict()
for _ in range(n):
    s, e = input().split()
    electors[s] = int(e)
    first_round[s] = dict()
m = int(input())
second_round = dict()
for _ in range(m):
    state, candidate = input().split()
    first_round[state][candidate] = first_round[state].get(candidate, 0) + 1
    second_round[candidate] = 0

for state in first_round:
    state_votes = first_round[state]
    candidate = None
    for c in state_votes:
        if (candidate is None or
                state_votes[c] > state_votes[candidate] or
                (state_votes[c] == state_votes[candidate] and c < candidate)):
            candidate = c
    second_round[candidate] = second_round.get(candidate, 0) + electors[state]
for candidate, votes in sorted(second_round.items(), key=lambda x: (x[1], x[0]), reverse=True):
    print(candidate, votes)
