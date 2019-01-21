# COMPLETE
SOURCE = (500, 0)

def add_tuple(t1, t2):
	return (t1[0] + t2[0], t1[1] + t2[1])



def print_buckets(clay, moving, resting, top_left, bottom_right):
	def to_char(tile):
		if tile == SOURCE:
			return "+"
		elif tile in clay:
			return "#"
		elif tile in moving & resting:
			return "@"
		elif tile in resting:
			return "~"
		elif tile in moving:
			return "|"
		else:
			return "."

	print "\n".join(''.join(to_char((x,y)) for x in range(top_left[0], bottom_right[0] + 1)) for y in range(top_left[1], bottom_right[1] + 1))

def run():
	clay = set()

	with open('input/dec17') as dec17:
		for line in dec17:
			# there's no sscanf in python :/
			# Put all the digits of a number next to each other, then put spaces between the numbers
			# Split based on the spaces we put on the numbers then make them into a list of ints
			nums = list(map(int, ''.join(char if char.isdigit() else ' ' for char in line).split()))

			if line[0] == "x":
				for y in range(nums[1], nums[2] + 1): # nums[1]...nums[2]
					clay.add((nums[0], y))
			elif line[0] == "y":
				for x in range(nums[1], nums[2] + 1):
					clay.add((x, nums[0]))

	min_y, max_y = min(pt[1] for pt in clay), max(pt[1] for pt in clay)

	print min_y, max_y
	moving, resting, to_fall, to_spread = [set() for _ in range(4)]

	to_fall.add(SOURCE)
	while to_fall or to_spread:
		while to_fall:
			pos = fall(to_fall.pop(), max_y, clay, moving)
			if pos:
				to_spread.add(pos)

		while to_spread:
			ts = to_spread.pop()
			l, r = spread(ts, clay, moving, resting)
			if not l and not r:
				to_spread.add(add_tuple(ts, (0, -1)))
			else:
				if r:
					to_fall.add(r)
				if l:
					to_fall.add(l)

	min_x, max_x = min(pt[0] for pt in clay) - 10, max(pt[0] for pt in clay) + 10


	print "Part 1: ", len([pt for pt in (moving | resting) if pt[1] >= min_y and pt[1] <= max_y])
	print "Part 2: ", len([pt for pt in resting if pt[1] >= min_y and pt[1] <= max_y])



def fall(pos, y, clay, moving):
	while pos[1] < y:
		dpos = add_tuple(pos, (0, 1))
		if dpos not in clay:
			moving.add(dpos)
			pos = dpos
		else:
			return pos # it hit clay so it needs to spread
	return None

def spread(pos, clay, moving, resting):
	updates = set()

	def helper(direction):
		curr = pos

		while curr not in clay: # while it has not hit a wall
			updates.add(curr)

			# see if it can go down
			dpos = add_tuple(curr, (0,1))
			if dpos not in clay and dpos not in resting:
				return curr

			curr = add_tuple(curr, direction)
		return None

	l = helper((-1, 0))
	r = helper((1, 0))

	if not l and not r:
		resting.update(updates)
	else:
		moving.update(updates)

	return l, r

# Prints the buckets
def print_buckets(clay, moving, resting, top_left, bottom_right):
	def to_char(tile):
		if tile == SOURCE:
			return "+"
		elif tile in clay:
			return "#"
		elif tile in moving & resting:
			return "@"
		elif tile in resting:
			return "~"
		elif tile in moving:
			return "|"
		else:
			return "."

	print "\n".join(''.join(to_char((x,y)) for x in range(top_left[0], bottom_right[0] + 1)) for y in range(top_left[1], bottom_right[1] + 1))

run()