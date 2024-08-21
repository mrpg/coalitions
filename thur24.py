from coalitions import coalitions

# see, e.g, https://de.wikipedia.org/wiki/Landtagswahl_in_Th%C3%BCringen_2024#Umfragen

poll = {
    "Linke": 0.15,
    "AfD": 0.29,
    "CDU": 0.20,
    "SPD": 0.09,
    "Grüne": 0.04,
    "FDP": 0.02,
    "BSW": 0.18,
}

for p, m in coalitions(poll):
    print(p, m)
