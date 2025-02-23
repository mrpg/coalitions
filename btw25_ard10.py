from coalitions import coalitions

# 10 Uhr Trend der ARD am Wahltag

poll = {
    "Union": 0.3126,
    "SPD": 0.1472,
    "Grüne": 0.1395,
    "FDP": 0.0492,
    "Linke": 0.0734,
    "AfD": 0.2263,
    "BSW": 0.0323,
}

poll[None] = 1 - sum(poll.values())

for p, m in coalitions(poll, no_threshold=None):
    print(p, m)
