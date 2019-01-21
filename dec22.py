# Complete
depth = 8787
target = (10, 725)

erosion_levels = {}

for x in xrange(target[0] + 1):
	for y in xrange(target[1] + 1):
		if (x,y) == (0,0) or (x,y) == target:
			geo_idx = 0
		elif y == 0:
			geo_idx = x * 16807
		elif x == 0:
			geo_idx = y * 48271
		else:
			geo_idx =  erosion_levels[(x-1, y)] * erosion_levels[(x, y-1)]

		erosion_levels[(x,y)] = (geo_idx + depth) % 20183


print "Part 1: ", sum(val % 3 for val in erosion_levels.values())

def erosion(x, y):
	if (x,y) in erosion_levels:
		return erosion_levels[(x,y)]

	if y == 0:
		geo_idx = x * 16807
	elif x == 0:
		geo_idx = y * 16807
	else:
		geo_idx = erosion(x-1, y) * erosion(x, y-1)

	erosion_levels[(x,y)] = (geo_idx + depth) % 20183

	return erosion_levels[(x,y)]

# Making extra, just in case
for x in xrange(target[0] + 1, target[0] + 1000):
	for y in xrange(target[1] +1, target[0] + 1000):
		erosion(x, y)

import heapq

# 0 Rocky
# 1 Wet
# 2 Narrow

# 0 Neither
# 1 Torch
# 2 Climbing


tool = 1
paths = [(0, 0, 0, tool)] # time, x, y, tool
dp = {} # Best path


while paths:
	time, x, y, tool = heapq.heappop(paths)
	curr_best = (x, y, terrain)

	# Check if you already have a more optimal path
	if curr_best in dp and dp[curr_best] <= time:
		continue

	dp[curr_best] = time

	# If we are at the target and we have the torch
	if curr_best == (target[0], target[1], 1):
		print "Part 2: ", time
		break

	# Switch to the other tool
	# i != tool -- can't be current tool
	# i != terrain -- can't be the banned tool
	for i in xrange(3):
		if i != tool and i != erosion(x,y) % 3:
			heapq.heappush(paths, (time + 7, x, y, i))

	# Check neighbors
	for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
		if x + dx < 0 or y + dy < 0:
			continue
		if erosion(x+dx, y+dy) % 3 == tool:
			# Can't move there, have to switch tools
			continue

		heapq.heappush(paths, (time + 1, x+dx, y+dy, terrain))
