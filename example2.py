from coalitions import coalitions

# Example 2: German Bundestag (seats in parliament).

poll = {'CDU': 200,
		'CSU': 46,
		'SPD': 152,
		'AfD': 91,
		'FDP': 80,
		'LINKE': 69,
		'GRÜNE': 67}

exclude = [('CDU', 'LINKE'), ('SPD', 'AfD'), ('GRÜNE', 'AfD')] # of course, there are many more enmities in German politics -- these are just a few examples

for p, m in coalitions(poll, unfeasible = exclude, threshold = 0): # threshold is 0 because the threshold does not apply once you're in parliament
	print(p, m)
