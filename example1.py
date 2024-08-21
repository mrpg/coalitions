from coalitions import coalitions

# Example 1: Find coalitions among eight "ordinary" parties.

poll = {"A": 23, "B": 20, "C": 13, "D": 17, "E": 13, "F": 5, "G": 4, "H": 3}

excluded = [
    ("A", "C"),
    ("B", "E"),
    ("A", "F"),
]  # This means that A and C will never be in a coalition; and B and E, and A and F will also never be in coalitions

for p, m in coalitions(
    poll, unfeasible=excluded
):  # coalitions() is a generator! Note that the default threshold is 5%
    print(p, m)
