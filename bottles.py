numbersOfBottles = range(0,100)

for number in numbersOfBottles[::-1]:
	if number > 0:
		print "{0} bottles of beer on the wall, {0} bottles of beer! \n\tIf one of those bottles should happen to fall, {1} bottles of beer on the wall! \n".format(str(number), str(number-1))
	elif number == 0:
		print "No bottles of beer on the wall, no bottles of beer! Go on a beer run."
