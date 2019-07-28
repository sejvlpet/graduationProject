def main(playground, spells):
	"""
	This function just takes assignment and passes it to recursive function which counts result.
	This result is then returned as an integer.
	"""
	return 1 if solving(0, 0, playground, spells, False) else 0

def solving(x, y, playground, spells, player):
	"""
	Recursive function to find result of game.
	x - current coordinate on x axis
	y - current coordinate on y axis
	playground - size of playground
	spells - all moves from assignment
	player - boolean, whose value describes who's on the move
	"""
	if (x >= playground[0] or y >= playground[1]):	
		return not player
	for spell in spells:
		if solving(x + spell[0], y + spell[1], playground, spells, not player):
			final = True
			if player:
				for spell1 in spells:
					if not solving(x + spell1[0], y + spell1[1], playground, spells, not player):
						final = False
						break
			return final
	return False

# There's reading of game assignment from standard input.
# Comment it, if you want to import this script to another one and define assignment there.


countOfGames = int(input())
for j in range(countOfGames):
	spells = []
	firstLine = input().split()
	playground = [int(firstLine[0]), int(firstLine[1])]
	for i in range(int(firstLine[2])):
		strSpells = input().split()
		spells += [[int(strSpells[0]), int(strSpells[1])]]
	# call main function with just read assignment
	print(main(playground, spells))

