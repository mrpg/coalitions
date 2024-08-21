import itertools


def powerset(iterable):
    # source: https://docs.python.org/3/library/itertools.html#itertools-recipes

    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)
    )


def coalitions(
    parties, *, unfeasible=[], remove_extraneous=True, majority=0.5, threshold=0.05
):
    """Calculate and yield feasible coalitions.

    Parameters:
            parties (dict): A dict containing party names as values and some performance measure (such as percentages or seats in parliament) as the corresponding values. The values must be numeric.
            unfeasible (list): A list of tuples containing enmities between two parties. No coalition is considered feasible if it contains both parties of any tuple in this list.
            remove_extraneous (bool): Must all parties in a coalition be strictly necessary? If True, no coalitions that contain more parties than strictly required to exceed the majority are returned.
            majority (float): What percentage of the sum of performance measures (sum(parties.values())) constitues a majority?
            threshold (float): Exclude parties that have less than threshold*100% of the sum of performance measures (sum(parties.values())). Mostly relevant for German elections ("Fünfprozenthürde"). Should be set to 0 if the performance measure is seats in parliament and not poll results.

    Yields:
            (coalition, majority): A tuple with a feasible coalition and corresponding majority.
    """

    while True:
        sum_parties = sum(parties.values())
        parties = {
            party: percent / sum_parties for party, percent in parties.items()
        }  # normalize values

        if all(
            x[1] >= threshold for x in parties.items()
        ):  # are all parties above the threshold?
            break
        else:
            parties = {
                a: b for a, b in parties.items() if b >= threshold
            }  # remove small parties and, in the next step, renormalize parties by redistributing the (eliminated) percentages of small parties to larger ones

    for coalition in powerset(parties):  # iterate over powerset of parties
        if not coalition == ():  # ignore empty set
            if all(
                not (u[0] in coalition and u[1] in coalition) for u in unfeasible
            ):  # ignore coalitions with enmities
                if (
                    maj := sum(y for x, y in parties.items() if x in coalition)
                ) > majority:  # ignore coalitions that have no majority
                    if remove_extraneous:
                        if all(
                            maj - y <= majority
                            for x, y in parties.items()
                            if x in coalition
                        ):  # check whether all parties in the coalition are strictly necessary
                            yield coalition, maj
                    else:
                        yield coalition, maj
