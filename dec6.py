# COMPLETE
import re
from collections import defaultdict

coords = []

with open('input/dec6') as dec6:
	for line in dec6:
		coords.append(map(int, line.split(',')))

# Create a bounding box
bounding = 10000 / len(coords)

min_x = min(x[0] for x in coords) - bounding - 1
max_x = max(x[0] for x in coords) + bounding + 1
min_y = min(x[1] for x in coords) - bounding - 1
max_y = max(x[1] for x in coords) + bounding + 1

def touch_bounds(x, y):
	if x <= min_x or x >= max_x or y <= min_y or y >= max_y:
		return True
	return False

grid = {}
valid = {}
for x,y in coords:
	valid[(x,y)] = 0 


part2 = []

for x in xrange(min_x, max_x + 1):
	for y in xrange(min_y, max_y + 1):
		# find closest pt
		min_dist = max_x + 1
		# Part 2
		total_dist = 0
		####

		for cx, cy in coords:
			manhattan = abs(cx - x) + abs(cy - y)
			total_dist += manhattan
			if manhattan < min_dist:
				min_dist = manhattan
				grid[(x,y)] = (cx, cy)
			elif manhattan == min_dist:
				grid[(x,y)] = None

		# Part 2
		if total_dist < 10000:
			part2.append((x,y))
		####

		# Either add to the area by 1 or if it's infinite, set to -1
		if grid[(x,y)] and valid[grid[(x,y)]] != -1:
			if touch_bounds(x, y):
				valid[grid[(x,y)]] = -1
			else:
				valid[grid[(x,y)]] += 1

r_lookup = {}
for key in valid:
	if valid[key] != -1:
		r_lookup[valid[key]] = key

print r_lookup[max(r_lookup.keys())]

# Part 2 Answer
print len(part2)