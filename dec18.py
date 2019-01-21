#COMPLETE

from copy import deepcopy
area = [list(line.rstrip('\n')) for line in open('input/dec18')]

def minute(area, new_area):

	def adjacent(i,j):

		adj = [(i + x,j + y) for x in range(-1, 2) for y in range(-1, 2) if (x,y) != (0,0)]
		resources = { "." : 0, "#" : 0, "|" : 0}

		for x, y in adj:
			if x >= 0 and y >= 0 and x < len(area) and y < len(area[0]):
				resources[area[x][y]] += 1

		return resources["."], resources["#"], resources["|"]

	for i in range(len(area)):
		for j in range(len(area[0])):
			op, lumb, tree = adjacent(i,j)

			tile = area[i][j]
			if tile == ".":
				new_area[i][j] = "|" if tree >= 3 else "."
			elif tile == "|":
				new_area[i][j] = "#" if lumb >= 3 else "|"
			elif tile == "#":
				new_area[i][j] = "#" if lumb > 0 and tree > 0 else "."



past_areas = {}


l_size = 1
l_area = ""

secondary = deepcopy(area)
i = 0
while i < 1000000000: # Change this to 10 for Part 1

	test = " ".join(["".join(x) for x in area])
	if test not in past_areas:
		past_areas[test] = i
	else:
		cycle = past_areas[test]
		break

	print i
	i += 1

	# Leave this in for Part 1
	minute(area, secondary)
	area, secondary = secondary, area


# Part 2
# the num we wanna lookup
iter_num = (1000000000 - cycle) % (i - cycle)

for _ in range(iter_num):
	minute(area, secondary)
	area, secondary = secondary, area




# Count the resources at this point			
resources = { "." : 0, "#" : 0, "|" : 0}
for i in range(len(area)):
	for j in range(len(area[0])):
		resources[area[i][j]] += 1


for row in area:
	print "".join(row)


print resources
print resources["#"] * resources["|"]


