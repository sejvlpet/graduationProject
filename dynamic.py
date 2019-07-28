import reducer
# reducer is useful for a couple of optimilazations in the very start of game


def main(playground, spells):
	"""
	Function takes parametrs, which we've read from standard input and tries to simplify them.
	After simplification, this function'll call another function for game solving and pass those
	parametrs to it. From that function it gets result and returns it back as an integer.
	"""
	# filter out spells, would lead to direct loose
	reducer.filterSpells(spells, playground)
	# we'll find their greatest common divider of numbers in game
	divider = reducer.reduceSpells(spells, playground)

	if divider != 1:
		# if divider doesn't equal to 1, it gotta be bigger so we'll use it to reduce numbers 
		for spell in spells:
			spell[0] = int(spell[0] / divider)
			spell[1] = int(spell[1] / divider)
		playground[0] = int(playground[0] / divider)
		playground[1] = int(playground[1] / divider)

	# for continuous result saving, we'll be using resultMap
	resultMap = [[2 for j in range(playground[1])] for i in range(playground[0])]
	# calling function, which counts our result with previously counted parametrs
	result = createMap(0, 0, [0, 0], spells, resultMap, playground)

	return 1 if result else 0


def createMap(x, y, spell, spells, resultMap, playground):
	"""
	Recursive function to find result of game. Whenever is result found, we save it in resultMap.
	Later on, when we reach such position again, we simply return that result. This way it is much
	more effective.
	x - current coordinate on x axis
	y - current coordinate on y axis
	playground - size of playground
	spells - all moves from assignment
	resultMap - 2d array, where we continously save results
	"""
	
	# move in spell's direction
	x += spell[0]
	y += spell[1]
	if x >= playground[0] or y >= playground[1]: 
		# once we step out, we know that spell used on previous position had sent player to loss
		# we'll return True because winning positions leads only to loosing, which are taggerd as False
		# and since this move led to direct loss, that move couldn't be wining
		return True
	if resultMap[x][y] == 2:
		# we'll work with unvisited positions only
		isWinning = 0
		# by default, we'll asume that we stand on loosing positions 
		# (that means, that player can move only to such positions, that he'll have to step out in the end)
		for spell in spells:
			# try all the spells from this tested position
			if not createMap(x, y, spell, spells, resultMap, playground):
				# if this recursice function returns False, it means that it can reach some loosing position
				isWinning = 1
				# posibility of reaching at least one loosing position means standing on the winning one
				break
		resultMap[x][y] = isWinning
	return resultMap[x][y]


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

