import itertools


def powerset(iterable):
    # source: https://docs.python.org/3/library/itertools.html#itertools-recipes
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)
    )


def coalitions(
    parties, *, remove_extraneous=True, threshold=0.05, no_threshold=None, majority=0.5
):
    """Calculate and yield feasible parliamentary coalitions.

    This function generates possible coalitions of political parties that could form
    a government based on their parliamentary representation or poll results. It takes
    into account various rules such as minimum thresholds and majority requirements.

    Parameters:
        parties (dict): Dictionary mapping party names (str) to their performance measure
            (numeric). Performance can be either percentage of votes or number of seats.
            Use None as key for "Other" parties which will be excluded from calculations
            after threshold-passers are ascertained.
        remove_extraneous (bool, optional): If True, excludes coalitions that contain more
            parties than necessary to form a majority. Defaults to True.
        threshold (float, optional): Minimum percentage (as decimal) of total performance
            measure required for a party to be included. Used for election thresholds like
            Germany's "Fünfprozenthürde". Set to 0 if working with seat numbers.
            Defaults to 0.05 (5%).
        no_threshold (set/list, optional): Collection of party names exempt from the
            threshold requirement. Useful for exceptions like Germany's
            "Grundmandatsklausel". Defaults to None.
        majority (float, optional): Decimal fraction of total performance measure required
            to form a majority. Defaults to 0.5 (50%).

    Yields:
        tuple: (coalition, total_strength) where:
            - coalition is a tuple of party names forming a valid coalition
            - total_strength is the sum of their performance measures

    Examples:
        >>> parties = {"A": 0.35, "B": 0.25, "C": 0.20, "D": 0.15, None: 0.05}
        >>> list(coalitions(parties))
        [(("A", "B"), 0.60), (("A", "C"), 0.55), (("A", "B", "C"), 0.80), ...]
    """
    # Convert no_threshold to set if provided, empty set if None
    no_threshold = set(no_threshold or [])
    total = sum(parties.values())

    # Apply threshold and create working set of parties
    valid_parties = {
        name: value
        for name, value in parties.items()
        if (value / total >= threshold or name in no_threshold) and name is not None
    }

    # Generate all possible combinations using powerset
    for coalition in powerset(valid_parties.keys()):
        # Skip empty coalitions
        if not coalition:
            continue

        # Calculate coalition strength
        coalition_strength = sum(valid_parties[party] for party in coalition)
        coalition_share = coalition_strength / total

        # Check if coalition reaches majority threshold
        if coalition_share >= majority:
            # If removing extraneous parties is requested
            if remove_extraneous:
                # Check if coalition would still have majority after removing any single party
                is_minimal = all(
                    sum(valid_parties[p] for p in coalition if p != party) / total
                    < majority
                    for party in coalition
                )
                if not is_minimal:
                    continue

            yield (coalition, coalition_strength)
