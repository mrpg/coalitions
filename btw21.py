from coalitions import coalitions

# see, e.g, https://www.wahlrecht.de/umfragen/index.htm

poll = {'Union': 0.241,
    'SPD': 0.205,
    'Grüne': 0.18,
    'FDP': 0.121,
    'Linke': 0.068,
    'AfD': 0.108}

for p, m in coalitions(poll):
    print(p, m)
