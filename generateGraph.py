import random
"""This script generates random test sets for testing of algorithms"""


def createPlayground(maxX, maxY):
	"""
	IN range defined on standard input, this function generates playground size.
	"""
	return [random.randrange(1, maxX, 1), random.randrange(1, maxY, 1)]


def createSpells(count, maxX, maxY):
	"""
	This function generates spells.
	"""
	spells = []
	for i in range(random.randrange(1, count, 1)):
		spells += [[random.randrange(0, maxX, 1), random.randrange(1, maxY, 1)]]
	return spells

# read input
countOfGames = int(input())
maxX =  int(input())
maxY = int(input())
maxCountOfSpells = int(input())
maxXForSpells = int(input())
maxYForSpells = int(input())
# print all needed things to standard output
print(countOfGames)

# from input, generate our test sets
for i in range(countOfGames):
	playground = createPlayground(maxX, maxY)
	spells = createSpells(maxCountOfSpells, maxXForSpells, maxYForSpells)
	# print all needed things to standard output
	print(playground[0], playground[1], len(spells))
	for spell in spells:
		# print all needed things to standard output
		print(spell[0], spell[1])
