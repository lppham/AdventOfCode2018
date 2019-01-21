# COMPLETE
import numpy as numpy
sNum = 5034

def get_power_level(x, y): # P1 is y,x
	rackID = (x + 1) + 10
	return ((((rackID * (y + 1)) + sNum) * rackID) / 100 % 10) - 5

fuel_grid = np.fromfunction(power, (300, 300))

(max_x, max_y) = (-1, -1)
max_power = -1

for x in range(300 - 3):
	for y in range(300 - 3):
		power = 0
		for dy in range(3):
			for dx in range(3):
				power += fuel_grid[y + dy][x + dx]

			if power > max_power:
				max_power = power
				max_x, max_y = x, y

print max_x, max_y, max_power

# Part 2
max_size = -1
max_power = -1

fuel_grid = np.asarray(fuel_grid)
for w in range(3, 300):
	sizes = sum(fuel_grid[x:x-w+1 or None, y:y-w+1 or None] for x in range(w) for y in range(w))
	power = int(sizes.max())

	if power > max_power:
		max_power = power
		pos = np.where(sizes == power)
		max_x, max_y, max_size = pos[0][0] + 1, pos[1][0] + 1, w

print max_x, max_y, max_size, max_power