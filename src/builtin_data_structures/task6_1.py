from random import choice


def winner_in_state(state_votes: dict):
    winner = choice(list(state_votes))
    winner_votes = state_votes[winner]
    for candidate, candidate_votes in state_votes.items():
        if candidate_votes < winner_votes:
            pass
        elif candidate_votes == winner_votes and candidate > winner:
            pass
        else:
            winner = candidate
            winner_votes = candidate_votes
    return winner


n = int(input())
electors = dict()
first_round = dict()
for i in range(n):
    state, state_electors = input().split()
    electors[state] = int(state_electors)
    first_round[state] = dict()
m = int(input())
results = dict()
for i in range(m):
    state, candidate = input().split()
    state_votes = first_round[state]
    state_votes[candidate] = state_votes.get(candidate, 0) + 1
    results[candidate] = 0
for state in first_round:
    state_winner = winner_in_state(first_round[state])
    results[state_winner] = results.get(state_winner, 0) + electors[state]

sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
for name, votes in sorted_results:
    print(name, votes)
