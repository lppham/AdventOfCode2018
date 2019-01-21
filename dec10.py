import re
from collections import defaultdict
coords = []
with open('input/dec10') as dec10:

	for line in dec10:
		parsed = [int(i) for i in re.findall(r'-?\d+', line)]
		coords.append(parsed)

i = 0
while True:
	x_i = [x + i*vx for x, _, vx, _ in coords]
	y_i = [y + i*vy for _, y, _, vy in coords]
	max_x = max(x_i)
	min_x = min(x_i)
	max_y = max(y_i)
	min_y = min(y_i)

	isolated = False
	lookup = defaultdict(bool)

	for j in range(len(coords)):
		lookup[(x_i[j], y_i[j])] = True
	for j in range(len(coords)):
		if not any((x_i[j] + dx, y_i[j] + dy) in lookup for dx in range(-1,2) for dy in range(-1,2) if (dx,dy) != (0,0)): # dont want themselves
			isolated = True
			break

	if not isolated:
		for y in range(min_y, max_y + 1):
			s = ""
			for x in range(min_x, max_x + 1):
				s += "#" if lookup[(x,y)] else "."
			print s
		print i
		break

	i += 1
