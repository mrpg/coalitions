from coalitions import coalitions

# see, e.g, https://x.com/MarcusPretzell/status/1893279662756794588

poll = {
    "Union": 0.3006,
    "SPD": 0.1506,
    "Grüne": 0.1319,
    "FDP": 0.0431,
    "Linke": 0.0687,
    "AfD": 0.205,
    "BSW": 0.0444,
}

for p, m in coalitions(poll):
    print(p, m)
