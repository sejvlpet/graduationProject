import reducer
# reducer is useful for a couple of optimilazations in the very start of game


def getLimits(spells, limits):
	"""
	Function takes spells and limits as parametrs. Spells are all posiblle
	moves taken from assignment, limits is there for all previously found limits.
	Function is recursive, in one call it always finds maximally pair of moves. It calls itself
	until all moves are somehow classified.
	Goal of this function is to find all moves, which are unique in the sence, that on certain
	positions they're the only which can be played.
	"""
	# copy spells, so there wont be any problem with overwriting
	spells = spells[:]
	# we'll be always limited by moving right or down
	down = spells[0]
	right = spells[0]
	for spell in spells:
		if spell[0] < down[0] or (spell[0] == down[0] and spell[1] < down[1]):
			down = spell
		elif spell[1] < right[1] or (spell[1] == right[1] and spell[0] < right[0]):
			right = spell
	# if moves are tagged, as limits, we'll save them
	limits += [down, right] if down != right else [down]
	i = 0
	while(i < len(spells)):
		# find spells, usable inside of the rectangle created by bigger numbers in our limits 
		# (in case of mimum closer to x-axis, I mean y-number), otherwise we're not into them and we'll remove them
		if (spells[i][1] < down[1] and spells[i][0] < right[0]):
			i += 1
		else:
			del spells[i]
	if(len(spells) > 0):
		# because we need to find all the limits, we'll do it recursively with spells, that weren't removed in previous step
		getLimits(spells, limits)
	return limits



def createLostZone(limits, resultMap, playground):
	"""
	This function is next step after finding limits.
	It takes our previously found limits and decribed limits, resultMap for tagging of fields in lostZone and
	the size of playground.
	From those parametrs, function finds zone where player can only leave the play field.
	"""
	# creates zone, where you cannot play anymore
	x = playground[0] - 1
	y = playground[1] - 1
	lostZone = []
	# going through playground while positions are lost
	while(isLost(limits, [x, y], playground) and y < playground[1]) and y >= 0: 
		while(isLost(limits, [x, y], playground) and x < playground[0]) and x >= 0:
			lostZone += [[x, y]]
			resultMap[x][y] = 0
			x -= 1
		x = playground[0] - 1
		y -= 1
	return lostZone


def isLost(limits, position, playground):
	"""
	This function simply checks whether is possible to play only out of playground and
	return bollean with value according to it.
	Limits - moves, just as limits described above.
	Position - current position.
	Playground - size of playground.
	"""
	for spell in limits:
		# positions after move
		pos = [position[0] + spell[0],  position[1] + spell[1]]
		# test it 
		if inGame(pos, playground):
			return False
	return True


def findMovesFromLostZone(lostZone, spells, resultMap, playground):
	"""
	Function plays back all moves from previously found lost zone,
	so all positions found like this are winning. Function returns those moves.
	lostZone - positions, from where you can only lose
	spells - all moves from assignement
	resultMap - 2D array for result saving
	playground - size of playground
	"""
	moves = []
	for position in lostZone:
		if resultMap[position[0]][position[1]] == 0:
			# test only if position's value in resultMap is really 0
			for spell in spells:
				testedX = position[0] - spell[0]
				testedY = position[1] - spell[1]
				if inGame([testedX, testedY], playground):
					moves += [[testedX, testedY]]
					resultMap[testedX][testedY] = 1
	return moves

def inGame(position, playground):
	"""
	Simply checks whether position lays in playground
	"""
	return position[0] < playground[0] and position[1] < playground[1] and position[0] >= 0 and position[1] >= 0



def findLosingPositions(positionsToBeTested, spells, resultMap, playground):
	"""
	This function takes positions found during game, which ought to be tested. Those positions
	were found by playing back from winning positions. After checking, it saves results to resultMap.
	In the end, function returns all losing positions positions.
	positionsToBeTested - positions to be tested
	spells - all moves from assignment
	resultMap - 2D array for saving results
	playground - size of the playground
	"""
	lostZone = []
	newMoves = []
	i = 0
	# pass all positions
	while i < len(positionsToBeTested):
		x = positionsToBeTested[i][0]
		y = positionsToBeTested[i][1]
		if resultMap[x][y] == 2:
			# test only positions, which haven't been tagged yet
			resultMap[x][y] = 0
			# firstly, lets assume that position is losing
			for spell in spells:
				pos = [x + spell[0], y + spell[1]]
				if inGame(pos, playground) and resultMap[x + spell[0]][y + spell[1]] == 0:
					# if position leads to at least one losing position, it is winning
					resultMap[x][y] = 1
					del positionsToBeTested[i]
					i -= 1
					break
				elif inGame(pos, playground) and resultMap[x + spell[0]][y + spell[1]] == 2:
					# if position leads to at least one unknown, it cannot be yet tagged as losing
					resultMap[x][y] = 2

			if resultMap[x][y] == 0:
				# if none of above is True, position is losing
				lostZone += [[x, y]]
				del positionsToBeTested[i]
				i -= 1
		else:
			# if position already have been tested, remove it from list
			del positionsToBeTested[i]
			i -= 1
		i += 1
	return lostZone



def doMoves(positions, spells, playground, resultMap):
	"""
	This takes some positions and plays all moves back from them. It also checks whether or not
	has such position been already visited, in that case it would be useless.
	positions - positions from which we''ll play moves back
	spells - all moves from assignment
	resultMap - 2d array for saving results
	playground - size of playground
	"""
	newPositions = []
	for pos in positions:
		for spell in spells:
			x = pos[0] - spell[0]
			y = pos[1] - spell[1]
			if inGame([x, y], playground) and resultMap[x][y] == 2:
				newPositions += [[x, y]]
	return newPositions	

def tryDirectWin(spells, resultMap, playground):
	"""
	It's not bad to check, if first positions is winning continuously.
	spells - all moves from assignment
	resultMap - 2d array for saving results
	playground - size of playground
	"""
	for spell in spells:
		if inGame(spell, playground) and resultMap[spell[0]][spell[1]] == 0:
			resultMap[0][0] = 1
			return

def main(playground, spells):
	"""
	Function takes parametrs, which we've read from standard input and tries to simplify them.
	After simplification, it calls above described functions to get result and then returns it back as an integer.
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
	if len(spells) == 0:
		return 0
	# for continuous result saving, we'll be using resultMap
	resultMap = [[2 for j in range(playground[1])] for i in range(playground[0])]
	# find limits
	limits = getLimits(spells, [])
	# find lost zone
	lostZone = createLostZone(limits, resultMap, playground)

	moves = []
	i = 0
	while resultMap[0][0] == 2:
		# play moves back from lost zone
		movesFromLostZone = findMovesFromLostZone(lostZone, spells, resultMap, playground)
		# add moves
		moves += doMoves(movesFromLostZone, spells, playground, resultMap)
		# from moves, create new lostZone
		lostZone = findLosingPositions(moves, spells, resultMap, playground)
		# continuously try if there's direct win
		tryDirectWin(spells, resultMap, playground)
		i += 1

		
	return 1 if resultMap[0][0] else 0



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

