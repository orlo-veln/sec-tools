scores = {}

for team in ['Liverpool', 'Liverpool', 'Chelsea', 'Liverpool']:
	if team in scores:
		scores[team] = scores[team] + 1
	else:
		scores[team] = 1

print (scores)

