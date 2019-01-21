# COMPLETE

import re
from collections import defaultdict

def dist((x0, y0, z0), (x1, y1, z1)):
	return abs(x0 - x1) + abs(y0 - y1) + abs(z0 - z1)

nanobots = []


with open('dec23') as dec23:
	for line in dec23:
		m = map(int, re.findall(r'-?\d+', line))
		nanobots.append([(m[0], m[1], m[2]), m[3]])

nano_iter = range(len(nanobots))
in_range = defaultdict(int)

r_longest = 0
idx_longest = 0

for i in nano_iter:
	pos, r  = nanobots[i]

	if r > r_longest:
		r_longest = r
		idx_longest = i

		for j in nano_iter:
			posj, _ = nanobots[j]
			if dist(pos, posj) <= r:
				in_range[i] += 1

print "Part 1: ", in_range[idx_longest]

from z3 import *

def z3_abs(x):
	return If(x >= 0, x, -x)

(x,y,z) = (Int('x'), Int('y'), Int('z'))


in_ranges = [Int('in_range_' + str(i)) for i in range(len(nanobots))]

range_count = Int('sum')

optimizer = Optimize()

for i in range(len(nanobots)):
	(xp, yp, zp), rp = nanobots[i]
	optimizer.add(in_ranges[i] 
		== If(z3_abs(x - xp) + z3_abs(y - yp) + z3_abs(z - zp) 
		<= rp, 1, 0))
optimizer.add(range_count == sum(in_ranges))

dist_from_zero = Int('dist')
optimizer.add(dist_from_zero == z3_abs(x) + z3_abs(y) + z3_abs(z))

max_rng_ct = optimizer.maximize(range_count)
min_zero_dist = optimizer.minimize(dist_from_zero)

print optimizer.check()
print "Part 2: ", optimizer.lower(min_zero_dist), optimizer.upper(min_zero_dist)
