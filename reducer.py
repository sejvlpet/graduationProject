def reduceSpells(spells, playground):
	"""
	Function takes moves (spells) and the size of playground and reduces it to 1D array, which includes all necessarily numbers.
	"""
	numbers = []
	for spell in spells:
		numbers += [spell[0], spell[1]]
	numbers += [playground[0], playground[1]]
	return greatestDivider(numbers)


def greatestDivider(numbers):
	"""
	Function takes numbers and finds their greatest common divider.
	"""
	divider = 1
	smallest = min(numbers) 
	res = smallest
	dividers = [1]
	while divider < res:
		divider += 1
		if not testDivider(res, numbers):
			while smallest % divider != 0:
				divider += 1
			res = smallest / divider
			dividers += [divider]
		else:
			return res
	for divider in reversed(dividers):
		if testDivider(divider, numbers):
			return divider			


def testDivider(res, numbers):
	"""
	Tests if divider (res) is divider of all numbers.
	"""
	for number in numbers:
		if number % res != 0:
			return False
	return True


def filterSpells(spells, playground):
	"""
	Spells with move bigger than playground could cause problems and are useless, we have to filter them out.
	This is what this function does.
	"""
	i = 0
	while i < len(spells):
		if spells[i][0] >= playground[0] or spells[i][1] >= playground[1]:
			del spells[i]
			i -= 1
		i += 1