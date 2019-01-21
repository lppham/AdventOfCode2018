# COMPLETE

import re

def extract(s):
	pattern = re.compile(r"""\#*(?P<number>.*?)							#number
						     \s\@\s*(?P<xcoord>.*?),(?P<ycoord>.*?):	#coordinates
						     \s*(?P<width>\d{1,4})x(?P<height>\d{1,4})$ #length
						     """, re.VERBOSE)
	match = pattern.match(s)

	number = int(match.group("number"))
	xcoord = int(match.group("xcoord"))
	ycoord = int(match.group("ycoord"))
	width = int(match.group("width"))
	height = int(match.group("height"))

	return (number, xcoord, ycoord, width, height)


# Part 1
count = 0 
sheet = [[0 for _ in range(1000)] for _ in range(1000)] # bound is 1000 as described by problem
# If we wanted to save a little more space, we could use a dictionary with coordinates as a tuple as the key

with open('input/dec3') as dec3:
	for line in dec3:
		(number, xcoord, ycoord, width, height) = extract(line)

		for i in xrange(xcoord, xcoord + width):
			for j in xrange(ycoord, ycoord + height):
				sheet[i][j] += 1

for row in sheet:
	for item in row:
		count += 1 if item > 1 else 0

print count


# Part 2

count = 0 
sheet = [[0 for _ in range(1000)] for _ in range(1000)] # bound is 1000 as described by problem
# If we wanted to save a little more space, we could use a dictionary with coordinates as a tuple as the key

used = [[0 for _ in range(1000)] for _ in range(1000)]


ans = set()
with open('input/dec3') as dec3:
	for line in dec3:
		(number, xcoord, ycoord, width, height) = extract(line)

		for i in xrange(xcoord, xcoord + width):
			for j in xrange(ycoord, ycoord + height):
				sheet[i][j] += 1
				if sheet[i][j] > 1: # if theres an intersection, remove the current one in it and don't yourself
					try:
						ans.remove(used[i][j])
					except:
						continue
				else: # add yourself as a possible candidate
					ans.add(number) 

print ans