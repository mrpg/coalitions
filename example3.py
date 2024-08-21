import random
from coalitions import coalitions

# Example 3: Find coalitions among 25 parties.

random.seed(123)

poll = {
    "A": 2,
    "B": 2,
    "C": 2,
    "D": 2,
    "E": 2,
    "F": 3,
    "G": 3,
    "H": 3,
    "I": 3,
    "J": 3,
    "K": 3,
    "L": 4,
    "M": 4,
    "N": 4,
    "O": 4,
    "P": 4,
    "Q": 5,
    "R": 5,
    "S": 5,
    "T": 5,
    "U": 6,
    "V": 6,
    "W": 6,
    "X": 7,
    "Y": 7,
}

excluded = []

for party in poll.keys():  # generate a few enmities... ;-)
    for enemy in random.sample(poll.keys(), 2):
        if not enemy == party:
            excluded.append((party, enemy))

for p, m in coalitions(
    poll, unfeasible=excluded, threshold=0
):  # no threshold in this election system
    print(p, m)

# note: this takes approximately 1 minute to run
