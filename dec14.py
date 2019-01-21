# COMPLETE (No input)
recipes = "37"

e1 = 0
e2 = 1
i = 327901 #input

while True:
	added = int(recipes[e1]) + int(recipes[e2])
	left = (added / 10) % 10
	right = added % 10

	if left != 0:
		recipes += str(left)

	recipes += str(right)

	e1 = (e1 + int(recipes[e1]) + 1) % len(recipes)
	e2 = (e2 + int(recipes[e2]) + 1) % len(recipes)


	#Part 2
	if left == 0 and right == 1:
		if recipes[-6:] == str(i):
			print len(recipes) - 6
			print "lr"
			exit()
	elif left == 1:
		if recipes[-7:-1] == str(i):
			print len(recipes) - 7
			print "l"
			exit()


#Part 1
print recipes[i:i+10]